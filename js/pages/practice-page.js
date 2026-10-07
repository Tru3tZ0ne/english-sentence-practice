const CLOZE_WORD=/^[A-Za-z0-9]+(?:[’'][A-Za-z0-9]+)*(?:-[A-Za-z0-9]+(?:[’'][A-Za-z0-9]+)*)*$/;

function escapePracticeHtml(value){
  return String(value).replace(/[&<>"']/g,character=>({
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
  })[character]);
}

function normalizeClozeValue(value){
  return String(value).normalize('NFKC').replace(/[’‘]/g,"'").trim().toLocaleLowerCase();
}

function buildCloze(sentence){
  const parts=sentence.match(/[A-Za-z0-9]+(?:[’'][A-Za-z0-9]+)*(?:-[A-Za-z0-9]+(?:[’'][A-Za-z0-9]+)*)*|[^A-Za-z0-9]+/g)||[sentence];
  const wordParts=[];
  parts.forEach((part,index)=>{if(CLOZE_WORD.test(part))wordParts.push(index)});
  let blanks=wordParts.filter((_,wordIndex)=>{
    const edge=wordIndex<2||wordIndex>=wordParts.length-2;
    const middleHint=wordIndex>=2&&wordIndex<wordParts.length-2&&wordIndex%3===2;
    return !edge&&!middleHint;
  });
  if(!blanks.length&&wordParts.length)blanks=[wordParts[Math.floor(wordParts.length/2)]];
  return {parts,blanks};
}

window.PracticePage={
  async open(lib,mode='continue',kind='all'){
    STATE.currentLibrary=lib;STATE.mode=kind;
    const response=await API.call('get_sequence',lib,kind);
    STATE.sequence=response.items;STATE.index=0;
    if(mode==='continue'&&response.last_item_id){
      const index=STATE.sequence.findIndex(item=>item.id===response.last_item_id);
      if(index>=0)STATE.index=index;
    }
    this.render();
  },

  render(){
    const view=document.getElementById('view');
    if(!STATE.sequence.length){
      view.innerHTML='<section class="content empty">没有符合条件的题目。</section>';
      return;
    }
    const item=STATE.sequence[STATE.index],cloze=buildCloze(item.en),blankSet=new Set(cloze.blanks);
    STATE.submitted=false;STATE.answerShown=false;STATE.cloze=cloze;
    let blankNumber=0;
    const sentence=cloze.parts.map((part,partIndex)=>{
      if(!blankSet.has(partIndex))return escapePracticeHtml(part);
      blankNumber+=1;
      const width=Math.max(3,Math.min(14,part.length));
      return `<input class="cloze-input" data-part-index="${partIndex}" aria-label="第 ${blankNumber} 个空" autocomplete="off" autocapitalize="none" spellcheck="false" size="${width}">`;
    }).join('');
    view.innerHTML=`<section class="content"><div class="practice-head"><span>${escapePracticeHtml(item.library_title)}</span><span>第 ${STATE.index+1} / ${STATE.sequence.length} 题</span></div><div class="practice-card"><div class="zh">${escapePracticeHtml(item.zh)}</div><div class="cloze-instruction">填写下面 ${cloze.blanks.length} 个空格即可，其他内容不用重复输入</div><div id="cloze" class="cloze-sentence">${sentence}</div><div id="result"></div><div class="actions"><div><button id="prev">上一题</button><button id="fav">${item.favorite?'★ 已收藏':'☆ 收藏'}</button><button id="speak">🔊 朗读</button></div><div class="right"><button id="reveal">查看答案</button><button id="submit" class="primary">提交</button></div></div></div></section>`;
    document.getElementById('prev').onclick=()=>this.move(-1);
    document.getElementById('submit').onclick=()=>STATE.submitted?this.move(1):this.submit();
    document.querySelectorAll('.cloze-input').forEach(input=>{
      input.oninput=()=>input.classList.remove('missing');
      input.onkeydown=event=>{
        if(event.key==='Enter'){
          event.preventDefault();
          STATE.submitted?this.move(1):this.submit();
        }
      };
    });
    document.getElementById('fav').onclick=async()=>{
      const response=await API.call('toggle_favorite',item.library_id,item.id);
      if(response.ok){item.favorite=response.favorite;this.render()}
    };
    document.getElementById('reveal').onclick=()=>this.toggleAnswer();
    document.getElementById('speak').onclick=()=>speechSynthesis.speak(Object.assign(new SpeechSynthesisUtterance(item.en),{rate:STATE.settings.speech_rate||1,lang:item.language||'en-US'}));
    document.getElementById('progress-bar').style.width=`${(STATE.index+1)/STATE.sequence.length*100}%`;
    document.querySelector('.cloze-input')?.focus();
  },

  composedAnswer(){
    const values=new Map([...document.querySelectorAll('.cloze-input')].map(input=>[
      Number(input.dataset.partIndex),input.value.trim()
    ]));
    return STATE.cloze.parts.map((part,index)=>values.has(index)?values.get(index):part).join('');
  },

  async submit(){
    const inputs=[...document.querySelectorAll('.cloze-input')];
    const firstEmpty=inputs.find(input=>!input.value.trim());
    if(firstEmpty){
      firstEmpty.classList.add('missing');firstEmpty.focus();
      document.getElementById('result').innerHTML='<div class="result wrong"><strong>请先填完所有空格</strong></div>';
      return;
    }
    inputs.forEach(input=>input.classList.remove('missing'));
    const item=STATE.sequence[STATE.index];
    const response=await API.call('submit_answer',item.library_id,item.id,this.composedAnswer());
    if(response.ok){
      STATE.submitted=true;
      inputs.forEach(input=>{
        const expected=STATE.cloze.parts[Number(input.dataset.partIndex)];
        const fieldCorrect=response.correct||normalizeClozeValue(input.value)===normalizeClozeValue(expected);
        input.classList.add(fieldCorrect?'correct':'incorrect');
        input.readOnly=true;
      });
      document.getElementById('submit').textContent='下一题';
      const reveal=document.getElementById('reveal');reveal.textContent='答案已显示';reveal.disabled=true;
      this.showResult(response.correct,response.standard_answer,response.notes);
      if(STATE.settings.auto_next)setTimeout(()=>this.move(1),650);
    }
  },

  showResult(ok,answer,notes=''){
    STATE.answerShown=true;
    document.getElementById('result').innerHTML=`<div class="result ${ok?'':'wrong'}"><strong>${ok?'✓ 正确':'✕ 再想想'}</strong>${ok?'':`<div>正确答案：<span class="standard">${escapePracticeHtml(answer)}</span></div>`}${notes?`<div class="meta">${escapePracticeHtml(notes)}</div>`:''}</div>`;
  },

  toggleAnswer(){
    const inputs=[...document.querySelectorAll('.cloze-input')],button=document.getElementById('reveal');
    if(!inputs.length)return;
    if(STATE.answerShown&&!STATE.submitted){
      inputs.forEach(input=>{
        input.value=input.dataset.userValue||'';
        input.readOnly=false;input.classList.remove('revealed');
      });
      STATE.answerShown=false;button.textContent='查看答案';
      inputs[0].focus();
      return;
    }
    if(!STATE.answerShown){
      inputs.forEach(input=>{
        input.dataset.userValue=input.value;
        input.value=STATE.cloze.parts[Number(input.dataset.partIndex)];
        input.readOnly=true;input.classList.add('revealed');
      });
      STATE.answerShown=true;button.textContent='隐藏答案';
    }
  },

  move(delta){
    STATE.index=Math.max(0,Math.min(STATE.sequence.length-1,STATE.index+delta));
    API.call('save_position',STATE.currentLibrary,STATE.sequence[STATE.index].id);
    this.render();
  }
};
