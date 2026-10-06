window.ReadingPage={
  active:false,stage:'libraries',collection:null,dayData:null,current:0,revealedSentences:0,showAnswers:false,
  escape(value){const node=document.createElement('div');node.textContent=String(value??'');return node.innerHTML},
  setBack(label){document.getElementById('back').querySelector('span').textContent=label},
  showLibraries(){
    this.active=true;WordPage.active=false;this.stage='libraries';this.collection=null;this.dayData=null;this.setBack('题库');
    document.getElementById('progress-bar').style.width='0';document.querySelector('footer').textContent='选择阅读库，再进入与单词 Day 对应的阅读训练';
    document.getElementById('view').innerHTML=`<section class="content"><div class="eyebrow">阅读训练 · 在语境中复习当天单词</div><h1 class="page-title">选择阅读库</h1>${STATE.readings.length?`<div class="cards">${STATE.readings.map(item=>`<article class="card reading-library-card"><h2>${this.escape(item.title)}</h2><p>${this.escape(item.description||'')}</p><div class="tags">${(item.tags||[]).map(x=>this.escape(x)).join('　')}</div><div class="meta">${item.article_count} 篇阅读　·　${item.day_count} Days</div><button class="primary" data-reading="${this.escape(item.id)}">查看 Days</button></article>`).join('')}</div>`:'<div class="empty">暂无可用阅读库。</div>'}</section>`;
    document.querySelectorAll('[data-reading]').forEach(button=>button.onclick=()=>this.showDays(button.dataset.reading));
  },
  showDays(id){
    const collection=STATE.readings.find(item=>item.id===id);if(!collection)return;
    this.active=true;WordPage.active=false;this.stage='days';this.collection=collection;this.dayData=null;this.setBack('阅读库');
    document.getElementById('progress-bar').style.width='0';document.querySelector('footer').textContent='每个 Day 有故事、说明文和观点文三种阅读';
    document.getElementById('view').innerHTML=`<section class="content"><div class="eyebrow">${this.escape(collection.title)} · ${collection.article_count} 篇</div><h1 class="page-title">选择阅读日</h1><div class="day-grid">${collection.days.map(day=>`<button class="day-card" data-reading-day="${day.day}"><strong>Day ${day.day}</strong><span>${day.count} 篇阅读</span></button>`).join('')}</div></section>`;
    document.querySelectorAll('[data-reading-day]').forEach(button=>button.onclick=()=>this.openDay(Number(button.dataset.readingDay)));
  },
  async openDay(dayNumber){
    if(!this.collection)return;this.active=true;this.stage='day';this.setBack('Days');
    document.getElementById('view').innerHTML='<section class="content empty">正在加载阅读…</section>';
    const result=await API.call('get_reading_day',this.collection.id,dayNumber);
    if(!result.ok){document.getElementById('view').innerHTML=`<section class="content empty">${this.escape(result.error||'阅读加载失败')}</section>`;return}
    this.dayData=result;this.current=0;this.revealedSentences=0;this.showAnswers=false;this.renderDay();
  },
  typeLabel(type){return {story:'生活与故事',explanatory:'知识说明',opinion:'观点思考'}[type]||type},
  highlighted(text,words){
    let html=this.highlightedInline(text,words);
    return html.split(/\n\s*\n/).map(paragraph=>`<p>${paragraph.replace(/\n/g,'<br>')}</p>`).join('');
  },
  highlightedInline(text,words){
    let html=this.escape(text);const ordered=[...words].sort((a,b)=>b.word.length-a.word.length);
    for(const item of ordered){const escaped=this.escape(item.word).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');html=html.replace(new RegExp(`(^|[^A-Za-z])(${escaped})(?=$|[^A-Za-z])`,'gi'),'$1<mark>$2</mark>')}
    return html;
  },
  renderDay(){
    const articles=this.dayData.articles,article=articles[this.current];
    document.querySelector('footer').textContent='← / →：切换文章　·　T：逐句显示中文　·　Q：显示/隐藏答案';
    document.getElementById('progress-bar').style.width=`${(this.current+1)/articles.length*100}%`;
    const sentences=article.sentences||[{en:article.text,zh:article.translation}];
    document.getElementById('view').innerHTML=`<section class="content reading-content"><div class="practice-head"><span>${this.escape(this.collection.title)} · Day ${this.dayData.day}</span><span>第 ${this.current+1} / ${articles.length} 篇</span></div><div class="article-tabs">${articles.map((item,index)=>`<button data-article="${index}" class="${index===this.current?'active':''}">${this.typeLabel(item.type)}</button>`).join('')}</div><article class="reading-card"><div class="reading-heading"><div><span class="reading-type">${this.typeLabel(article.type)} · ${this.escape(article.difficulty||'CET-4')}</span><h1>${this.escape(article.title)}</h1></div><button id="speak-reading" title="朗读文章">朗读</button></div><div class="reading-text sentence-reading">${sentences.map((sentence,index)=>`<div class="reading-sentence"><p>${this.highlightedInline(sentence.en,article.target_words)}</p>${index<this.revealedSentences?`<p class="sentence-translation">${this.escape(sentence.zh)}</p>`:''}</div>`).join('')}</div><div class="sentence-reveal-bar"><button id="reveal-sentence" class="primary">${this.revealedSentences<sentences.length?`显示第 ${this.revealedSentences+1} 句中文（T）`:'重新隐藏全部中文'}</button><span>已显示 ${this.revealedSentences} / ${sentences.length} 句</span></div><section class="target-panel"><h2>本篇重点词</h2><div class="target-words">${article.target_words.map(item=>`<span><b>${this.escape(item.word)}</b><small>${this.escape(item.meaning)}</small></span>`).join('')}</div></section><div class="reading-actions"><button id="toggle-answers">${this.showAnswers?'隐藏题目答案':'显示题目答案（Q）'}</button></div><section class="questions-panel"><h2>阅读理解</h2>${article.questions.map((question,index)=>`<div class="reading-question"><strong>${index+1}. ${this.escape(question.prompt)}</strong>${this.showAnswers?`<p><span>答案：</span>${this.escape(question.answer)}</p>${question.explanation?`<small>${this.escape(question.explanation)}</small>`:''}`:''}</div>`).join('')}</section></article><div class="article-nav"><button data-move="-1" ${this.current===0?'disabled':''}>← 上一篇</button><button data-move="1" ${this.current===articles.length-1?'disabled':''}>下一篇 →</button></div></section>`;
    document.querySelectorAll('[data-article]').forEach(button=>button.onclick=()=>this.select(Number(button.dataset.article)));
    document.querySelectorAll('[data-move]').forEach(button=>button.onclick=()=>this.select(this.current+Number(button.dataset.move)));
    document.getElementById('reveal-sentence').onclick=()=>this.revealNext();
    document.getElementById('toggle-answers').onclick=()=>{this.showAnswers=!this.showAnswers;this.renderDay()};
    document.getElementById('speak-reading').onclick=()=>{speechSynthesis.cancel();const utterance=new SpeechSynthesisUtterance(article.text);utterance.lang='en-US';utterance.rate=Number(STATE.settings.speech_rate)||1;speechSynthesis.speak(utterance)};
  },
  revealNext(){const count=(this.dayData.articles[this.current].sentences||[]).length;this.revealedSentences=this.revealedSentences>=count?0:this.revealedSentences+1;this.renderDay()},
  select(index){if(!this.dayData)return;this.current=Math.max(0,Math.min(this.dayData.articles.length-1,index));this.revealedSentences=0;this.showAnswers=false;this.renderDay();window.scrollTo({top:0,behavior:'smooth'})},
  handleKey(event){
    if(!this.active||this.stage!=='day'||event.ctrlKey||event.altKey||event.metaKey||['INPUT','TEXTAREA'].includes(event.target.tagName))return false;
    if(event.key==='ArrowLeft'){event.preventDefault();this.select(this.current-1);return true}
    if(event.key==='ArrowRight'){event.preventDefault();this.select(this.current+1);return true}
    if(event.key.toLowerCase()==='t'){event.preventDefault();this.revealNext();return true}
    if(event.key.toLowerCase()==='q'){event.preventDefault();this.showAnswers=!this.showAnswers;this.renderDay();return true}
    return false;
  },
  back(){if(this.stage==='day')this.showDays(this.collection.id);else if(this.stage==='days')this.showLibraries();else LibraryPage.render()}
};
