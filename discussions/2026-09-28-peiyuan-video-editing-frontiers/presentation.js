(() => {
  const slides = [...document.querySelectorAll('.slide')];
  const meta = window.DECK_META;
  const dialogs = [...document.querySelectorAll('dialog')];
  const popover = document.getElementById('termPopover');
  let termAnchor = null, pinned = false, termTimer, suppressFocus = false;
  function closeTerm(restoreFocus = false) {
    clearTimeout(termTimer);
    const previous = termAnchor;
    previous?.setAttribute('aria-expanded','false');
    previous?.removeAttribute('aria-controls');
    termAnchor = null; pinned = false; popover.hidden = true;
    if (restoreFocus && previous) { suppressFocus = true; previous.focus(); suppressFocus = false; }
  }
  function placeTerm() {
    if (!termAnchor || popover.hidden) return;
    popover.style.maxHeight=`${innerHeight-24}px`;
    const r=termAnchor.getBoundingClientRect(), p=popover.getBoundingClientRect(),pad=12;
    let left=r.left < innerWidth/2 ? r.right+18 : r.left-p.width-18;
    let top=Math.max(pad,Math.min(innerHeight-p.height-pad,r.top-30));
    if (left<pad || left+p.width>innerWidth-pad) {
      left=Math.max(pad,Math.min(innerWidth-p.width-pad,r.left));
      const below=innerHeight-r.bottom-2*pad,above=r.top-2*pad;
      if(below>=p.height)top=r.bottom+pad;
      else if(above>=p.height)top=r.top-p.height-pad;
      else if(below>=above){popover.style.maxHeight=`${Math.max(100,below)}px`;top=r.bottom+pad;}
      else{popover.style.maxHeight=`${Math.max(100,above)}px`;top=pad;}
    }
    popover.style.left=`${left}px`;popover.style.top=`${top}px`;
  }
  function pinState(value) {
    pinned=value;popover.classList.toggle('pinned',pinned);
    document.getElementById('pinTerm').textContent=pinned?'Pinned':'Pin';
    document.getElementById('pinTerm').setAttribute('aria-pressed',String(pinned));
    document.getElementById('termMode').textContent=pinned?'PINNED · ESC TO CLOSE':'TECHNICAL NOTE';
  }
  function showTerm(el,force=false) {
    clearTimeout(termTimer);
    if(suppressFocus || (pinned&&!force))return;
    const d=window.DECK_DETAILS[el.dataset.detail];
    if(!d)return;
    termAnchor?.setAttribute('aria-expanded','false');termAnchor?.removeAttribute('aria-controls');
    termAnchor=el;el.setAttribute('aria-expanded','true');el.setAttribute('aria-controls','termPopover');
    document.getElementById('termTitle').innerHTML=d.titleHtml;
    const body=document.getElementById('termBody');body.replaceChildren();
    d.blocks.forEach(b=>{const h=document.createElement('h3'),p=document.createElement('p');h.textContent=b.label;p.innerHTML=b.html;body.append(h,p)});
    const sources=document.createElement('div');sources.className='term-sources';
    d.refs.forEach(r=>{const a=document.createElement('a');a.href=r.url;a.textContent=r.title+' ↗';a.target='_blank';a.rel='noopener noreferrer';sources.append(a)});
    body.append(sources);popover.hidden=false;popover.scrollTop=0;pinState(false);placeTerm();
  }
  function hideTermSoon(){clearTimeout(termTimer);termTimer=setTimeout(()=>{if(!pinned&&!popover.matches(':hover')&&!popover.contains(document.activeElement)&&!termAnchor?.matches(':hover'))closeTerm()},180)}
  document.querySelectorAll('.term-trigger').forEach(el=>{
    el.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse')showTerm(el)});
    el.addEventListener('pointerleave',hideTermSoon);
    el.addEventListener('focus',()=>showTerm(el));el.addEventListener('blur',hideTermSoon);
    el.addEventListener('click',e=>{if(el.tagName==='A')return;e.stopPropagation();if(pinned&&termAnchor===el){closeTerm();return;}showTerm(el,true);pinState(true)});
    el.addEventListener('keydown',e=>{if(e.key==='ArrowDown'){e.preventDefault();showTerm(el,true);pinState(true);document.getElementById('pinTerm').focus()}});
  });
  popover.addEventListener('pointerenter',()=>clearTimeout(termTimer));popover.addEventListener('pointerleave',hideTermSoon);
  popover.addEventListener('focusout',hideTermSoon);
  document.getElementById('pinTerm').onclick=()=>pinState(!pinned);
  document.getElementById('closeTerm').onclick=()=>closeTerm(true);
  document.addEventListener('pointerdown',e=>{if(!popover.contains(e.target)&&!e.target.closest('.term-trigger'))closeTerm()});
  document.querySelectorAll('[data-notes]').forEach(el=>el.onclick=()=>toggle('notes'));
  document.querySelectorAll('[data-image]').forEach(el=>el.onclick=()=>{document.querySelector('#zoom img').src=el.dataset.image;toggle('zoom')});
  let index = Math.max(0, meta.findIndex(s => s.id === location.hash.slice(1)));
  let mediaRequest = 0;
  const videos = () => [...slides[index].querySelectorAll('video')];
  function updatePlaybackControls() {
    const vs=videos(),playing=vs.some(v=>!v.paused&&!v.ended);
    const buttons=[document.getElementById('mediaButton'),...slides[index].querySelectorAll('[data-media-toggle]')];
    buttons.forEach(button=>{
      button.textContent=(playing?'Pause':'Play')+(vs.length>1||button.hasAttribute('data-media-toggle')?' all':'');
      button.setAttribute('aria-pressed',String(playing));
      button.title=playing?'Pause all videos (P)':'Play all videos from the start (P)';
    });
    document.getElementById('mediaButton').hidden=vs.length===0;
  }
  function resize() {
    document.documentElement.style.setProperty('--scale', Math.min(innerWidth / 1280, innerHeight / 720));
    placeTerm();
  }
  function updateNotes() {
    document.getElementById('noteTitle').innerHTML = `${index + 1}. ${meta[index].titleHtml}`;
    document.getElementById('noteBody').innerHTML = window.DECK_NOTES[index];
  }
  function go(n) {
    closeTerm();
    mediaRequest++;
    index = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, i) => { s.classList.toggle('active', i === index); s.inert = i !== index; if (i !== index) s.querySelectorAll('video').forEach(v => v.pause()); });
    history.replaceState(null, '', `#${meta[index].id}`);
    document.getElementById('counter').textContent = `${index + 1} / ${slides.length}`;
    videos().forEach(v=>{v.preload='auto';});
    updatePlaybackControls();
    document.getElementById('prev').disabled = index === 0;
    document.getElementById('next').disabled = index === slides.length - 1;
    updateNotes();
  }
  function toggle(id) { closeTerm(); const d = document.getElementById(id); if (d.open) d.close(); else { dialogs.forEach(x => x.close()); d.showModal(); } }
  async function play() {
    const vs=videos(),request=++mediaRequest;
    if(!vs.length)return;
    if(vs.some(v=>!v.paused))vs.forEach(v=>v.pause());
    else {
      vs.forEach(v=>{v.currentTime=0;});
      const results=await Promise.allSettled(vs.map(v=>v.play()));
      if(request!==mediaRequest)return;
      if(results.some(result=>result.status==='rejected')){
        vs.forEach(v=>v.pause());
        updatePlaybackControls();
        [document.getElementById('mediaButton'),...slides[index].querySelectorAll('[data-media-toggle]')].forEach(button=>{button.title='A video could not play. Check the video controls, then retry.';});
        return;
      }
    }
    updatePlaybackControls();
  }
  document.getElementById('prev').onclick = () => go(index - 1);
  document.getElementById('next').onclick = () => go(index + 1);
  document.getElementById('tocButton').onclick = () => toggle('toc');
  document.getElementById('notesButton').onclick = () => toggle('notes');
  document.getElementById('mediaButton').onclick = play;
  document.querySelectorAll('[data-media-toggle]').forEach(button=>button.onclick=play);
  document.querySelectorAll('video').forEach(video=>['play','pause','ended'].forEach(event=>video.addEventListener(event,()=>{
    if(video.closest('.slide')===slides[index])updatePlaybackControls();
  })));
  document.getElementById('fullButton').onclick = () => document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen();
  document.querySelectorAll('[data-go]').forEach(b => b.onclick = () => { go(Number(b.dataset.go)); document.getElementById('toc').close(); });
  dialogs.forEach(d => { d.querySelector('.close').onclick = () => d.close(); d.addEventListener('click', e => { if (e.target === d) { const r = d.getBoundingClientRect(); if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) d.close(); } }); });
  document.querySelectorAll('.figure').forEach(img => {
    const zoom = () => { document.querySelector('#zoom img').src = img.src; toggle('zoom'); };
    img.onclick = zoom; img.onkeydown = e => { if (e.key === 'Enter') zoom(); };
  });
  addEventListener('keydown', e => {
    if(e.key==='Escape'&&!popover.hidden){e.preventDefault();closeTerm(true);return;}
    if (dialogs.some(d => d.open)) return;
    if (['INPUT','TEXTAREA','SELECT','VIDEO'].includes(document.activeElement?.tagName)||popover.contains(document.activeElement)) return;
    if(document.activeElement?.tagName==='BUTTON'&&e.key===' ')return;
    if (['ArrowRight','PageDown',' '].includes(e.key)) { e.preventDefault(); go(index + 1); }
    if (['ArrowLeft','PageUp'].includes(e.key)) { e.preventDefault(); go(index - 1); }
    if (e.key === 'Home') go(0); if (e.key === 'End') go(slides.length - 1);
    if (e.key.toLowerCase() === 'o') toggle('toc');
    if (e.key.toLowerCase() === 'n') toggle('notes');
    if (e.key.toLowerCase() === 'f') document.getElementById('fullButton').click();
    if (e.key.toLowerCase() === 'p') play();
  });
  let timer;
  addEventListener('pointermove', () => { document.body.classList.add('controls-visible'); clearTimeout(timer); timer = setTimeout(() => document.body.classList.remove('controls-visible'), 1800); });
  addEventListener('resize', resize); addEventListener('hashchange', () => { const i = meta.findIndex(s => s.id === location.hash.slice(1)); if (i >= 0) go(i); });
  // Programmatic navigation also supports repeatable offline review.
  window.goToSlide = go; resize(); go(index);
})();
