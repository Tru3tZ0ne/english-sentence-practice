window.WordPage={
  active:false,stage:'libraries',wordlist:null,dayData:null,current:0,revealStates:[],
  escape(value){const node=document.createElement('div');node.textContent=String(value??'');return node.innerHTML},
  setBack(label){document.getElementById('back').querySelector('span').textContent=label},
  showLibraries(){
    this.active=true;this.stage='libraries';this.wordlist=null;this.dayData=null;this.setBack('题库');
    document.getElementById('progress-bar').style.width='0';document.querySelector('footer').textContent='选择一个单词库，再按 Day 学习';
    document.getElementById('view').innerHTML=`<section class="content"><div class="eyebrow">词汇学习 · 每 100 词一个 Day</div><h1 class="page-title">选择单词库</h1>${STATE.wordlists.length?`<div class="cards">${STATE.wordlists.map(item=>`<article class="card wordlist-card"><h2>${this.escape(item.title)}</h2><p>${this.escape(item.description||'')}</p><div class="tags">${(item.tags||[]).map(x=>this.escape(x)).join('　')}</div><div class="meta">${item.word_count.toLocaleString()} 个单词　·　${item.day_count} Days</div><button class="primary" data-wordlist="${this.escape(item.id)}">查看 Days</button></article>`).join('')}</div>`:'<div class="empty">暂无可用单词库。</div>'}</section>`;
    document.querySelectorAll('[data-wordlist]').forEach(button=>button.onclick=()=>this.showDays(button.dataset.wordlist));
  },
  showDays(id){
    const wordlist=STATE.wordlists.find(item=>item.id===id);if(!wordlist)return;
    this.active=true;this.stage='days';this.wordlist=wordlist;this.dayData=null;this.setBack('单词库');document.getElementById('progress-bar').style.width='0';
    document.querySelector('footer').textContent='每个 Day 最多 100 个单词，可按自己的进度选择';
    document.getElementById('view').innerHTML=`<section class="content"><div class="eyebrow">${this.escape(wordlist.title)} · ${wordlist.word_count.toLocaleString()} 词</div><h1 class="page-title">选择学习日</h1><div class="day-grid">${wordlist.days.map(day=>`<button class="day-card" data-day="${day.day}"><strong>Day ${day.day}</strong><span>${day.count} 词</span></button>`).join('')}</div></section>`;
    document.querySelectorAll('[data-day]').forEach(button=>button.onclick=()=>this.openDay(Number(button.dataset.day)));
  },
  async openDay(dayNumber){
    if(!this.wordlist)return;this.active=true;this.stage='day';this.setBack('Days');
    document.getElementById('view').innerHTML='<section class="content empty">正在加载单词…</section>';
    const result=await API.call('get_word_day',this.wordlist.id,dayNumber);
    if(!result.ok){document.getElementById('view').innerHTML=`<section class="content empty">${this.escape(result.error||'单词加载失败')}</section>`;return}
    this.dayData=result;this.current=0;this.revealStates=new Array(result.items.length).fill(0);this.renderDay();
  },
  renderDay(){
    const items=this.dayData.items;document.querySelector('footer').textContent='↑ / ↓：移动当前单词　·　空格或 Enter：显示 4 个释义 / 只留正确释义';
    const dayIndex=this.wordlist.days.find(day=>day.day===this.dayData.day),excelFile=dayIndex?.excel_file||`excel/day ${this.dayData.day}.xlsx`,downloadBase=API.mode==='static'?`wordlists/${this.wordlist.id}/`:`../content/wordlists/${this.wordlist.id}/`;
    document.getElementById('view').innerHTML=`<section class="content word-content"><div class="practice-head"><span>${this.escape(this.wordlist.title)} · Day ${this.dayData.day}</span><span>${items.length} 词</span></div><div class="word-day-tools"><div class="word-help">先回忆中文意思，再点右侧按钮。第一次显示 4 个释义，第二次只保留正确释义。</div><a class="excel-download" href="${downloadBase}${this.escape(excelFile).replace(/ /g,'%20')}" download="day ${this.dayData.day}.xlsx">下载 Day ${this.dayData.day} Excel</a></div><div class="word-rows">${items.map((item,index)=>this.rowMarkup(item,index)).join('')}</div></section>`;
    this.bindRows();this.select(0,false);
  },
  rowMarkup(item,index){
    const state=this.revealStates[index],options=state===1?item.options:(state===2?item.options.filter(option=>option.correct):[]);
    const label=state===0?'显示 4 个释义':state===1?'只看正确释义':'已显示正确释义';
    return `<article class="word-row${index===this.current?' current':''}" data-word-index="${index}"><div class="word-main"><span class="word-number">${index+1}</span><div><strong class="word-text">${this.escape(item.word)}</strong>${item.phonetic?`<span class="phonetic">${this.escape(item.phonetic)}</span>`:''}</div><button class="word-reveal${state===2?' complete':''}" data-reveal="${index}" ${state===2?'disabled':''}>${label}</button></div>${options.length?`<div class="meaning-options ${state===2?'answer-only':''}">${options.map(option=>`<div class="meaning-option${state===2&&option.correct?' correct':''}">${this.escape(option.text)}</div>`).join('')}</div>`:''}</article>`;
  },
  bindRows(){
    document.querySelectorAll('[data-word-index]').forEach(row=>row.onclick=event=>{if(!event.target.closest('[data-reveal]'))this.select(Number(row.dataset.wordIndex),false)});
    document.querySelectorAll('[data-reveal]').forEach(button=>button.onclick=event=>{event.stopPropagation();this.reveal(Number(button.dataset.reveal))});
  },
  replaceRow(index){
    const old=document.querySelector(`[data-word-index="${index}"]`);if(!old)return;
    const holder=document.createElement('div');holder.innerHTML=this.rowMarkup(this.dayData.items[index],index);const fresh=holder.firstElementChild;old.replaceWith(fresh);
    fresh.onclick=event=>{if(!event.target.closest('[data-reveal]'))this.select(index,false)};fresh.querySelector('[data-reveal]')?.addEventListener('click',event=>{event.stopPropagation();this.reveal(index)});
  },
  reveal(index){this.select(index,false);if(this.revealStates[index]<2){this.revealStates[index]++;this.replaceRow(index)}},
  select(index,scroll=true){
    if(!this.dayData)return;this.current=Math.max(0,Math.min(this.dayData.items.length-1,index));
    document.querySelectorAll('.word-row.current').forEach(row=>row.classList.remove('current'));const row=document.querySelector(`[data-word-index="${this.current}"]`);row?.classList.add('current');
    document.getElementById('progress-bar').style.width=`${(this.current+1)/this.dayData.items.length*100}%`;if(scroll)row?.scrollIntoView({behavior:'smooth',block:'center'});
  },
  handleKey(event){
    if(!this.active||this.stage!=='day'||event.ctrlKey||event.altKey||event.metaKey)return false;
    if(event.key==='ArrowUp'){event.preventDefault();this.select(this.current-1);return true}
    if(event.key==='ArrowDown'){event.preventDefault();this.select(this.current+1);return true}
    if(event.key===' '||event.key==='Enter'){event.preventDefault();this.reveal(this.current);return true}
    return false;
  },
  back(){if(this.stage==='day')this.showDays(this.wordlist.id);else if(this.stage==='days')this.showLibraries();else LibraryPage.render()}
};
