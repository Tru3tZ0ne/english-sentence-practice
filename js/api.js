const STATIC_DEFAULTS={theme:'system',font_size:'medium',auto_speak:false,speech_rate:1,ignore_terminal_punctuation:true,auto_next:false};

class StaticApi{
  constructor(){this.storageKey='english-sentence-practice-v1';this.libraries=[];this.byId=new Map();this.wordlists=[];this.wordlistsById=new Map();this.wordDayCache=new Map();this.readings=[];this.readingsById=new Map();this.readingDayCache=new Map();this.state=this.loadState()}
  loadState(){
    try{
      const saved=JSON.parse(localStorage.getItem(this.storageKey)||'{}');
      return {settings:{...STATIC_DEFAULTS,...saved.settings},progress:saved.progress||{},favorites:saved.favorites||{},positions:saved.positions||{}};
    }catch(_){return {settings:{...STATIC_DEFAULTS},progress:{},favorites:{},positions:{}}}
  }
  saveState(){localStorage.setItem(this.storageKey,JSON.stringify(this.state))}
  async initialize(){
    const response=await fetch('library-manifest.json');
    if(!response.ok)throw new Error(`题库清单加载失败：${response.status}`);
    const files=await response.json();
    const results=await Promise.all(files.map(async file=>{
      const result=await fetch(`libraries/${encodeURIComponent(file)}`);
      if(!result.ok)throw new Error(`题库加载失败：${file}`);
      return result.json();
    }));
    this.libraries=results;this.byId=new Map(results.map(lib=>[lib.id,lib]));
    const wordManifestResponse=await fetch('wordlists/manifest.json');
    if(!wordManifestResponse.ok)throw new Error(`单词库清单加载失败：${wordManifestResponse.status}`);
    const wordManifest=await wordManifestResponse.json();
    const indexes=await Promise.all((wordManifest.wordlists||[]).map(async entry=>{
      const response=await fetch(`wordlists/${entry.index}`);
      if(!response.ok)throw new Error(`单词库索引加载失败：${entry.index}`);
      const index=await response.json();index._base=entry.index.replace(/[^/]+$/,'');return index;
    }));
    this.wordlists=indexes;this.wordlistsById=new Map(indexes.map(index=>[index.id,index]));
    const readingManifestResponse=await fetch('readings/manifest.json');
    if(readingManifestResponse.ok){
      const readingManifest=await readingManifestResponse.json();
      const readingIndexes=await Promise.all((readingManifest.collections||[]).map(async entry=>{
        const response=await fetch(`readings/${entry.index}`);
        if(!response.ok)throw new Error(`阅读库索引加载失败：${entry.index}`);
        const index=await response.json();index._base=entry.index.replace(/[^/]+$/,'');return index;
      }));
      this.readings=readingIndexes;this.readingsById=new Map(readingIndexes.map(index=>[index.id,index]));
    }
  }
  itemKey(libraryId,itemId){return `${libraryId}/${itemId}`}
  stats(libraryId){
    const lib=this.byId.get(libraryId),rows=(lib?.items||[]).map(item=>this.state.progress[this.itemKey(libraryId,item.id)]).filter(Boolean);
    const correct=rows.reduce((sum,row)=>sum+(row.correct||0),0),wrong=rows.reduce((sum,row)=>sum+(row.wrong||0),0),total=correct+wrong;
    const favorites=(lib?.items||[]).filter(item=>this.state.favorites[this.itemKey(libraryId,item.id)]).length;
    return {practiced:rows.length,correct,wrong,accuracy:total?Math.round(correct*100/total):0,favorites,last_item_id:this.state.positions[libraryId]||null};
  }
  normalize(value,ignoreTerminal=true){
    let result=(value||'').normalize('NFKC').replace(/[’‘]/g,"'").replace(/[“”]/g,'"').replace(/，/g,',').replace(/。/g,'.').replace(/！/g,'!').replace(/？/g,'?').trim().replace(/\s+/g,' ').toLocaleLowerCase();
    if(ignoreTerminal)result=result.replace(/[.!?]+$/,'').trim();
    return result;
  }
  item(libraryId,itemId){return this.byId.get(libraryId)?.items.find(item=>item.id===itemId)}
  async bootstrap(){
    return {ok:true,version:'web',library_errors:[],wordlist_errors:[],reading_errors:[],settings:{...this.state.settings},libraries:this.libraries.map(lib=>({id:lib.id,title:lib.title,description:lib.description||'',language:lib.language||'en-US',tags:lib.tags||[],item_count:lib.items.length,stats:this.stats(lib.id)})),wordlists:this.wordlists.map(({_base,...index})=>index),readings:this.readings.map(({_base,...index})=>index)};
  }
  async get_word_day(wordlistId,dayNumber){
    const index=this.wordlistsById.get(wordlistId);if(!index)return {ok:false,error:'单词库不存在'};
    const day=index.days.find(item=>item.day===Number(dayNumber));if(!day)return {ok:false,error:`Day ${dayNumber} 不存在`};
    const key=`${wordlistId}/${day.day}`;
    if(!this.wordDayCache.has(key)){
      const response=await fetch(`wordlists/${index._base}${day.file}`);
      if(!response.ok)return {ok:false,error:`Day ${day.day} 加载失败：${response.status}`};
      this.wordDayCache.set(key,await response.json());
    }
    return {ok:true,...this.wordDayCache.get(key)};
  }
  async get_reading_day(collectionId,dayNumber){
    const index=this.readingsById.get(collectionId);if(!index)return {ok:false,error:'阅读库不存在'};
    const day=index.days.find(item=>item.day===Number(dayNumber));if(!day)return {ok:false,error:`Day ${dayNumber} 不存在`};
    const key=`${collectionId}/${day.day}`;
    if(!this.readingDayCache.has(key)){
      const response=await fetch(`readings/${index._base}${day.file}`);
      if(!response.ok)return {ok:false,error:`Day ${day.day} 加载失败：${response.status}`};
      this.readingDayCache.set(key,await response.json());
    }
    return {ok:true,...this.readingDayCache.get(key)};
  }
  async get_sequence(libraryId='',kind='all'){
    let pairs=[];
    if(kind==='all')pairs=(this.byId.get(libraryId)?.items||[]).map(item=>[libraryId,item]);
    else if(kind==='favorites'){
      pairs=Object.entries(this.state.favorites).filter(([,value])=>value).sort((a,b)=>b[1]-a[1]).map(([key])=>{
        const split=key.indexOf('/'),libId=key.slice(0,split),itemId=key.slice(split+1);return [libId,this.item(libId,itemId)];
      }).filter(([,item])=>item);
    }
    const items=pairs.map(([libId,item])=>{const lib=this.byId.get(libId);return {...item,library_id:libId,library_title:lib.title,language:lib.language||'en-US',favorite:Boolean(this.state.favorites[this.itemKey(libId,item.id)])}});
    return {ok:true,items,last_item_id:libraryId?this.state.positions[libraryId]||null:null};
  }
  async submit_answer(libraryId,itemId,userAnswer){
    const item=this.item(libraryId,itemId);if(!item)return {ok:false,error:'题目不存在或题库已更新'};
    const answers=item.answers?.length?item.answers:[item.en],normalized=this.normalize(userAnswer,this.state.settings.ignore_terminal_punctuation);
    const matched=answers.find(answer=>normalized&&normalized===this.normalize(answer,this.state.settings.ignore_terminal_punctuation))||null;
    const key=this.itemKey(libraryId,itemId),row=this.state.progress[key]||{correct:0,wrong:0};
    row[matched?'correct':'wrong']+=1;row.last_answer=userAnswer;row.last_practiced_at=Date.now();this.state.progress[key]=row;this.state.positions[libraryId]=itemId;this.saveState();
    return {ok:true,correct:Boolean(matched),standard_answer:item.en,matched_answer:matched,notes:item.notes||''};
  }
  async save_position(libraryId,itemId){if(this.item(libraryId,itemId)){this.state.positions[libraryId]=itemId;this.saveState()}return {ok:true}}
  async toggle_favorite(libraryId,itemId){
    if(!this.item(libraryId,itemId))return {ok:false,error:'题目不存在'};
    const key=this.itemKey(libraryId,itemId),favorite=!this.state.favorites[key];
    if(favorite)this.state.favorites[key]=Date.now();else delete this.state.favorites[key];this.saveState();return {ok:true,favorite};
  }
  async save_settings(values){
    const settings={...this.state.settings};
    if(['light','dark','system'].includes(values.theme))settings.theme=values.theme;
    if(['small','medium','large'].includes(values.font_size))settings.font_size=values.font_size;
    settings.auto_speak=Boolean(values.auto_speak);settings.auto_next=Boolean(values.auto_next);settings.ignore_terminal_punctuation=Boolean(values.ignore_terminal_punctuation);
    settings.speech_rate=Math.max(.5,Math.min(1.5,Number(values.speech_rate)||1));this.state.settings=settings;this.saveState();return {ok:true,settings:{...settings}};
  }
  async shutdown(){return {ok:true}}
  call(name,...args){if(typeof this[name]!=='function')return Promise.reject(new Error(`未知接口：${name}`));return this[name](...args)}
}

const isStatic=location.protocol!=='file:';
const staticApi=isStatic?new StaticApi():null;
const desktopReady=isStatic?null:(window.pywebview?.api?Promise.resolve():new Promise(resolve=>window.addEventListener('pywebviewready',resolve)));
window.API={
  mode:isStatic?'static':'desktop',
  call(name,...args){return isStatic?staticApi.call(name,...args):window.pywebview.api[name](...args)},
  ready:isStatic?staticApi.initialize():desktopReady
};
