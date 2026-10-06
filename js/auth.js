const SITE_LOGIN={
  username:'ielts-learner',
  passwordHash:'45f72587dd17e66c3ad957afa4cabb984dc8804236f1afff1e1de26455423993',
  sessionKey:'english-sentence-practice-auth-v1'
};

const applicationScripts=[
  'js/api.js','js/state.js','js/components/dialog.js','js/pages/library-page.js',
  'js/pages/practice-page.js','js/pages/settings-page.js','js/app.js'
];

function applicationMarkup(){return `<div id="app" class="shell"><header class="topbar"><button id="back" class="icon-btn" title="返回">← <span>题库</span></button><div class="brand">听写练习</div><div class="top-actions"><button id="settings-btn">设置</button><button id="favorites-btn">收藏</button><button id="close-btn" class="close-btn">关闭应用</button></div></header><div class="progress-track"><div id="progress-bar"></div></div><main id="view"></main><footer>Enter 提交/下一题　·　Ctrl + ←/→ 切题　·　Ctrl + D 收藏　·　Ctrl + L 朗读　·　Esc 关闭弹窗</footer></div><div id="toast"></div>`}

async function loadApplication(){
  document.body.innerHTML=applicationMarkup();
  for(const source of applicationScripts){
    await new Promise((resolve,reject)=>{const script=document.createElement('script');script.src=source;script.onload=resolve;script.onerror=()=>reject(new Error(`无法加载 ${source}`));document.body.appendChild(script)});
  }
}

async function sha256(value){
  const bytes=new TextEncoder().encode(value),digest=await crypto.subtle.digest('SHA-256',bytes);
  return Array.from(new Uint8Array(digest),byte=>byte.toString(16).padStart(2,'0')).join('');
}

function renderLogin(){
  document.body.innerHTML=`<main class="login-page"><section class="login-card" aria-labelledby="login-title"><div class="login-mark">EN</div><div class="eyebrow">English Sentence Practice</div><h1 id="login-title">登录学习空间</h1><p>请输入访问账号和密码。</p><form id="login-form"><label for="login-user">账号</label><input id="login-user" name="username" autocomplete="username" required><label for="login-password">密码</label><input id="login-password" name="password" type="password" autocomplete="current-password" required><div id="login-error" class="login-error" role="alert" aria-live="polite"></div><button class="primary login-submit" type="submit">进入题库</button></form></section></main>`;
  const form=document.getElementById('login-form'),button=form.querySelector('button'),error=document.getElementById('login-error');
  form.addEventListener('submit',async event=>{
    event.preventDefault();button.disabled=true;error.textContent='';
    const username=document.getElementById('login-user').value.trim(),password=document.getElementById('login-password').value;
    const valid=username===SITE_LOGIN.username&&await sha256(password)===SITE_LOGIN.passwordHash;
    if(valid){sessionStorage.setItem(SITE_LOGIN.sessionKey,'ok');await loadApplication();return}
    error.textContent='账号或密码不正确。';button.disabled=false;document.getElementById('login-password').select();
  });
  document.getElementById('login-user').focus();
}

async function start(){
  if(location.protocol==='file:'||sessionStorage.getItem(SITE_LOGIN.sessionKey)==='ok')await loadApplication();
  else renderLogin();
}

document.addEventListener('DOMContentLoaded',start);
