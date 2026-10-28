import os, sys
sys.path.insert(0,'tools')
from build import build

HOME_BODY = """<main id="main">
<section class="lede">
  <p class="kicker">Start at the edge, move inward</p>
  <h1>We are all <em>basically sane.</em></h1>
  <p class="sub">Every segment is a door. The outer ring answers the practical questions, the middle ring is about you, and the center is where the work actually happens.</p>
</section>

<div class="stage-wrap">
  <p class="words words-top">Our actual agency and power lies in our ability to choose how we want to relate to ourselves and the world.</p>
  <p class="mid-words mid-top">Contemplative Psychotherapy starts with the premise that we are all basically sane: in other words, we are all basically okay.</p>
  <div class="stage" id="stage">
    <div class="orbit" aria-hidden="true"></div>
    <svg class="rings" id="ringSvg" viewBox="-52 -52 504 504" role="group" aria-label="Ring navigation"></svg>
    <button class="core" id="core" aria-label="About me, Lisa Wallace, the center of the practice">
      <span class="faces">
        <span class="face front">
          <picture>
            <source srcset="assets/img/center-peak.webp" type="image/webp">
            <img class="portrait" src="assets/img/center-peak.jpg" width="640" height="640" alt="">
          </picture>
          <span class="veil"></span>
          <span class="plate"><span class="nm">About Me</span><span class="rl">Lisa Wallace, LPC</span></span>
        </span>
        <span class="face back">
          <span class="q">&ldquo;Help people fall in love with themselves, and, in doing so, fall in love with the world.&rdquo;</span>
          <span class="go">Meet Lisa &rarr;</span>
        </span>
      </span>
    </button>
  </div>
  <p class="mid-words mid-bot">The issue is not us, rather it&rsquo;s because of factors outside of our control (societal expectations and dominant norms, trauma, upbringing, life circumstances) that we might not always believe this.</p>
  <p class="words words-bot">True healing begins when we recognize what is in our control and that starts with the relationship with ourselves.</p>
</div>

<div class="readout" id="readout">
  <div class="ro-idle">
    <p class="center-words">At the center of my practice is my commitment to help people fall in love with themselves, and, in doing so, fall in love with the world. I am qualified to do so only in so far as I have taken this journey myself. I welcome the opportunity to walk with you as you discover who you are and were always meant to be.</p>
    <p class="hint" id="hint">Hover a segment, click to learn more</p>
    <div class="legend">
      <span><i style="background:#5A4C44"></i>01 &middot; The Practical</span>
      <span><i style="background:#C4C2E5"></i>02 &middot; Who This Is For</span>
      <span><i style="background:#CABFB6"></i>The Center &middot; About Me</span>
    </div>
  </div>
  <div class="ro-live">
    <p class="ro-eyebrow" id="roEyebrow"></p>
    <h2 class="ro-title" id="roTitle"></h2>
    <p class="ro-text" id="roText"></p>
    <button class="ro-cta" id="roCta">Learn more &rarr;</button>
  </div>
</div>

<section class="band has-img">
  <picture>
    <source type="image/webp" srcset="assets/img/lake-1000.webp 1000w, assets/img/lake-1600.webp 1600w, assets/img/lake-2400.webp 2400w" sizes="100vw">
    <img class="shot" src="assets/img/lake-1600.jpg" srcset="assets/img/lake-1000.jpg 1000w, assets/img/lake-1600.jpg 1600w, assets/img/lake-2400.jpg 2400w" sizes="100vw" width="2400" height="1279" loading="lazy" decoding="async" alt="A still alpine lake at dawn with a snow covered peak reflected on the surface and dark conifers along both shores.">
  </picture>
  <img class="motif" src="assets/img/rings-motif.svg" alt="" aria-hidden="true" width="400" height="400">
  <div class="inner">
    <div>
      <blockquote>True healing begins when we recognize what is in our control.</blockquote>
      <p class="by">Lisa Wallace, LPC</p>
    </div>
    <div class="side">
      <p>Contemplative psychotherapy for people who are ready to stop managing themselves and start knowing themselves. Telehealth across Colorado, based in Boulder.</p>
      <p><a class="tlink" href="contact/">Book a free consult</a></p>
    </div>
  </div>
</section>
</main>

<div class="scrim" id="scrim"></div>
<div class="panel" id="panel" role="dialog" aria-modal="true" aria-labelledby="panelTitle" aria-hidden="true">
  <span class="grab" aria-hidden="true"></span>
  <div class="panel-top">
    <button class="x" id="closeBtn" aria-label="Close">&times;</button>
    <div class="swatch" id="pSwatch"></div>
    <p class="eyebrow" id="pEyebrow"></p>
    <h2 id="panelTitle"></h2>
    <blockquote id="pQuote"></blockquote>
  </div>
  <div class="panel-body">
    <p id="pIntro"></p>
    <ul class="bits" id="pBits"></ul>
  </div>
  <div class="panel-foot">
    <a class="tlink" href="contact/" id="pCta">Learn more &rarr;</a>
    <span class="note" id="pNote"></span>
  </div>
</div>
"""

build(dict(
  slug="", depth=0, bodyclass="home",
  title="Brilliantly Sane | Contemplative Psychotherapy in Boulder, Colorado",
  desc="Contemplative psychotherapy with Lisa Wallace, LPC. Telehealth across Colorado, based in Boulder. $175 a session, free 20 minute consult.",
  extracss='\n<link rel="stylesheet" href="assets/home.css">',
  extrajs='\n<script src="assets/home.js" defer></script>',
  custom=HOME_BODY,
))
print("home built")
