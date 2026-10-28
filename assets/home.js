/* Brilliantly Sane: ring navigation */
(function () {
  'use strict';

  var RINGS = [
    {
      key: 'outer', cls: 'out', rIn: 132, rOut: 192, gap: 2.2, start: -90,
      eyebrow: 'Ring 01 · The Practical',
      segs: [
        {
          fill: '#63554D', label: 'Sessions', href: 'contact/',
          title: 'Mostly from your own couch.',
          tease: 'Telehealth across Colorado. Fifty five minutes. In person in Boulder when it makes sense.',
          quote: '"Most people do their best work somewhere they already feel like themselves."',
          intro: 'I see clients by video anywhere in Colorado. Sessions run fifty five minutes, usually weekly at the start, because early momentum matters more than frequency does later. If you are in or near Boulder and would rather sit in a room together, ask.',
          bits: [
            ['Format', 'Video statewide. In person in Boulder some weeks.'],
            ['Length', 'Fifty five minutes.'],
            ['Starting out', 'Weekly to begin, then we adjust.'],
            ['First step', 'A free twenty minute call.']
          ],
          cta: 'Set up a consult', note: 'Free 20 minute consult'
        },
        {
          fill: '#5A4C44', label: 'Rates', href: 'rates/',
          title: 'Said out loud, up front.',
          tease: '$175 a session, CO Access Medicaid accepted, and a free call before you commit to anything.',
          quote: '"Money is one more place we rehearse what we think we deserve."',
          intro: 'My fee is $175 for a fifty five minute session, and I accept CO Access Medicaid. If cost is the thing standing between you and starting, say so on the consult call. I would rather have that conversation in week one than watch someone quietly disappear in week four.',
          bits: [
            ['Session fee', '$175 for fifty five minutes.'],
            ['Insurance', 'CO Access Medicaid accepted.'],
            ['Consult', 'Twenty minutes, free, no obligation.'],
            ['If money is tight', 'Tell me on the call and I will be straight with you.']
          ],
          cta: 'Rates and payment', note: 'Updated for 2026'
        },
        {
          fill: '#51443C', label: 'Approach', href: 'approach/',
          title: 'Contemplative, then specific.',
          tease: 'Naropa trained. IFS, EMDR and mindfulness, used when they fit rather than on a schedule.',
          quote: '"Contemplative psychotherapy starts from the premise that you are already sane."',
          intro: 'I trained at Naropa in contemplative psychotherapy, which begins from the premise that you are basically sane and have been the whole time. From there the particular tools matter, and I pick them to suit the person in front of me.',
          bits: [
            ['Contemplative psychotherapy', 'Naropa, 2017. The ground the rest stands on.'],
            ['Internal Family Systems', 'Level I. Curiosity toward the parts of you working hardest.'],
            ['EMDR', 'For when a memory still runs the room.'],
            ['Mindfulness', 'Certified through Naropa and iBme.']
          ],
          cta: 'How I work', note: 'Collaborative, not one size fits all'
        },
        {
          fill: '#483C35', label: 'Questions', href: 'faq/',
          title: 'The ones people ask on the call.',
          tease: 'What a first session is like, how long this takes, and what happens if we are not a fit.',
          quote: '"Not knowing what to ask is a reasonable place to start."',
          intro: 'A consult is not a commitment and a first session is not an interrogation. Most people arrive with the same handful of questions, so I wrote them down.',
          bits: [
            ['First session', 'A conversation about what brought you. The paperwork is short.'],
            ['How long', 'As long as it is useful and not one session longer.'],
            ['Fit', 'If I am not your therapist I will say so and help you find who is.'],
            ['Medication', 'I do not prescribe. I will coordinate with whoever does.']
          ],
          cta: 'Read the FAQ', note: 'Twelve questions, plain answers'
        }
      ]
    },
    {
      key: 'mid', cls: 'mid', rIn: 82, rOut: 126, gap: 2.6, start: -90,
      eyebrow: 'Ring 02 · Who This Is For',
      segs: [
        {
          fill: '#CFCDE9', label: 'Young Adults', href: 'young-adult-therapy/',
          title: 'Finding your footing.',
          tease: 'Sixteen to twenty four, when the questions get big and the vocabulary has not caught up.',
          quote: '"You are not behind. You are early, and nobody told you that."',
          intro: 'Sixteen to twenty four is a strange stretch of life. The questions turn enormous and the language for them arrives late. I work with young adults who are taking that seriously, and I talk to them as people capable of depth, because they are.',
          bits: [
            ['Identity in motion', 'Not a phase to correct. A shape still forming.'],
            ['Pressure from outside', 'Family, school and the internet all have opinions about who you are.'],
            ['Parents', 'I work with the young person. Logistics I will discuss with you. Content I will not, without permission.']
          ],
          cta: 'Therapy for young adults', note: 'Individuals, not couples'
        },
        {
          fill: '#C6C4E4', label: 'Introspective', href: 'work-with/',
          title: 'You already look inward.',
          tease: 'You journal, you notice, you have the words. What is missing is rhythm and a second read.',
          quote: '"You have the material. What you want is a way to read it."',
          intro: 'Some people arrive with the groundwork laid. You have done the reading, you keep a journal, you can name a feeling while it is still happening. The work is different then. Less teaching, more interpretation, and some help knowing when to stay with something and when to set it down.',
          bits: [
            ['Rhythm', 'When to stay with something and when to let it rest.'],
            ['Language', 'Words precise enough to hold what you actually mean.'],
            ['A second read', 'Understanding what all that noticing is pointing at.']
          ],
          cta: 'Who I work with', note: 'Past ambivalence, about 51% in'
        },
        {
          fill: '#BDBBDD', label: 'LGBTQIA+', href: 'lgbtqia-therapy/',
          title: 'No translation tax.',
          tease: 'WPATH trained, queer myself, three years at an LGBTQIA+ practice. You can skip the explaining.',
          quote: '"You should not have to teach your therapist who you are before you can use the hour."',
          intro: 'I am queer, I am WPATH trained, and I spent three years at Umbrella Collective, a practice built for LGBTQIA+ clients. Your identity can be the center of this work or barely come up. Either way you are not starting from scratch every session.',
          bits: [
            ['Gender affirming care', 'WPATH trained. Ask me about letters and coordination.'],
            ['A queer therapist', 'Meditation was how I first understood my own queerness.'],
            ['Whatever you brought', 'Identity may be the subject or the backdrop.']
          ],
          cta: 'Queer and gender affirming therapy', note: 'Boulder and statewide'
        },
        {
          fill: '#B4B2D6', label: 'Religious Trauma', href: 'religious-trauma-therapy/',
          title: 'Faith, taken apart.',
          tease: 'Deconstruction, reconstruction, and the long middle where you are not sure which one you are doing.',
          quote: '"Leaving a belief system is not the same as leaving yourself."',
          intro: 'I studied religion before I studied therapy, so I take it seriously as something people actually lived inside rather than a set of opinions to argue over. Deconstruction, reconstruction and the long ambiguous middle all belong here. I am not trying to talk you out of anything, or into anything either.',
          bits: [
            ['Deconstruction', 'Grief, anger and relief, usually all at once.'],
            ['Reconstruction', 'Building something honest from what is left, if you want to.'],
            ['The middle', 'Not knowing yet is a legitimate place to sit for a while.']
          ],
          cta: 'Religious trauma and faith transitions', note: 'Religious Studies, CU Boulder'
        }
      ]
    }
  ];

  var CORE = {
    swatch: 'linear-gradient(140deg,#F3EFEB,#CABFB6)',
    eyebrow: 'The Center · Lisa Wallace, LPC',
    title: 'At the center of the practice.',
    tease: 'Who I am, where I trained, and why I think you are already okay.',
    quote: '"Being human is messy. Let us see if we can find a way to come together in that mess."',
    intro: 'I grew up in a Colorado mountain town and came to meditation through a long stretch of pain and depression, which is also how I came to understand my own queerness. I trained at Naropa and have been practicing since 2017. At the center of my work is helping people fall in love with themselves and, through that, with the world. I am qualified to do it only insofar as I have done it myself.',
    bits: [
      ['The premise', 'You are not broken. You are responding reasonably to things that were not reasonable.'],
      ['The arrangement', 'You are in the driver seat. I have a map and the occasional suggestion.'],
      ['The qualification', 'I have walked this. That is most of what I have to offer.']
    ],
    cta: 'More about Lisa', href: 'about/', note: 'Naropa University, 2017'
  };

  /* ---------- geometry ---------- */
  var CX = 200, CY = 200, NS = 'http://www.w3.org/2000/svg';
  function pol(r, deg) { var a = deg * Math.PI / 180; return [CX + r * Math.cos(a), CY + r * Math.sin(a)]; }
  function annulus(a0, a1, ri, ro) {
    var la = (a1 - a0) > 180 ? 1 : 0;
    var p1 = pol(ro, a0), p2 = pol(ro, a1), p3 = pol(ri, a1), p4 = pol(ri, a0);
    return 'M' + p1 + 'A' + ro + ' ' + ro + ' 0 ' + la + ' 1 ' + p2 +
           'L' + p3 + 'A' + ri + ' ' + ri + ' 0 ' + la + ' 0 ' + p4 + 'Z';
  }
  function textArc(a0, a1, r) {
    var mid = (a0 + a1) / 2, m = ((mid % 360) + 360) % 360;
    var flip = (m > 0 && m < 180);
    var la = (a1 - a0) > 180 ? 1 : 0;
    var p1 = pol(r, a0), p2 = pol(r, a1);
    return flip ? 'M' + p2 + 'A' + r + ' ' + r + ' 0 ' + la + ' 0 ' + p1
                : 'M' + p1 + 'A' + r + ' ' + r + ' 0 ' + la + ' 1 ' + p2;
  }
  function el(n, attrs) {
    var e = document.createElementNS(NS, n);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    return e;
  }

  var svg = document.getElementById('ringSvg');
  if (!svg) return;
  var defs = el('defs', {});
  svg.appendChild(defs);

  var SEGMAP = {};
  RINGS.forEach(function (ring) {
    var n = ring.segs.length, step = 360 / n, rc = (ring.rIn + ring.rOut) / 2;
    ring.segs.forEach(function (s, i) {
      var a0 = ring.start + i * step + ring.gap;
      var a1 = ring.start + (i + 1) * step - ring.gap;
      var mid = (a0 + a1) / 2, rad = mid * Math.PI / 180;
      var id = ring.key + '-' + i;
      SEGMAP[id] = Object.assign({}, s, { eyebrow: ring.eyebrow, swatch: s.fill, ring: ring.cls });

      var g = el('g', {
        'class': 'seg ' + ring.cls, tabindex: '0', role: 'link', 'data-id': id,
        'aria-label': s.label + '. ' + s.title,
        style: '--tx:' + (Math.cos(rad) * 7).toFixed(2) + 'px;--ty:' + (Math.sin(rad) * 7).toFixed(2) + 'px' + ';--i:' + (ring.cls === 'out' ? i + 4 : i)
      });
      g.appendChild(el('path', {
        'class': 'slice', d: annulus(a0, a1, ring.rIn, ring.rOut), fill: s.fill,
        stroke: 'rgba(255,255,255,.14)', 'stroke-width': '1'
      }));

      var pid = 'tp-' + id;
      defs.appendChild(el('path', { id: pid, d: textArc(a0, a1, rc + (ring.cls === 'out' ? 4 : 3)) }));
      var t = el('text', { 'class': 'lbl', 'font-size': ring.cls === 'out' ? '11.5' : '10.5', 'text-anchor': 'middle', dy: '0.34em' });
      var tp = el('textPath', { href: '#' + pid, startOffset: '50%' });
      tp.setAttribute('xlink:href', '#' + pid);
      tp.textContent = s.label;
      t.appendChild(tp);
      g.appendChild(t);

      var d = pol(ring.cls === 'out' ? ring.rOut - 13 : ring.rIn + 11, mid);
      g.appendChild(el('circle', { 'class': 'dot', cx: d[0], cy: d[1], r: '2.6', fill: ring.cls === 'out' ? '#E8DFD7' : '#6E3714' }));

      svg.appendChild(g);
    });
  });
  svg.appendChild(el('circle', { 'class': 'gapline', cx: CX, cy: CY, r: 129, fill: 'none', stroke: 'rgba(65,30,6,.10)', 'stroke-width': '1' }));

  /* ---------- ring 00: Lisa's words ----------
     An outer band that is read rather than clicked, leading into the two
     rings of doors. Her two sentences run along the top and bottom arcs.
     Phones get the same sentences as plain text above and below instead,
     since curved type that long would be too small to read there. */
  var WORDS = { rIn: 201, rOut: 245, top: 'Our actual agency and power lies in our ability to choose how we want to relate to ourselves and the world.',
                bot: 'True healing begins when we recognize what is in our control and that starts with the relationship with ourselves.' };
  var wg = el('g', { 'class': 'words-ring', 'aria-hidden': 'true' });
  var wr = (WORDS.rIn + WORDS.rOut) / 2;
  wg.appendChild(el('circle', { 'class': 'band', cx: CX, cy: CY, r: wr, fill: 'none', 'stroke-width': WORDS.rOut - WORDS.rIn }));
  wg.appendChild(el('circle', { 'class': 'edge', cx: CX, cy: CY, r: WORDS.rOut, fill: 'none' }));
  [[192, 348, WORDS.top, 'wt-top'], [12, 168, WORDS.bot, 'wt-bot']].forEach(function (w) {
    defs.appendChild(el('path', { id: w[3], d: textArc(w[0], w[1], wr) }));
    var t = el('text', { 'class': 'wtxt', 'font-size': '12.5', 'text-anchor': 'middle', dy: '0.32em' });
    var tp = el('textPath', { href: '#' + w[3], startOffset: '50%' });
    tp.setAttribute('xlink:href', '#' + w[3]);
    tp.textContent = w[2];
    t.appendChild(tp);
    wg.appendChild(t);
  });
  [0, 180].forEach(function (deg) {
    var d = pol(wr, deg);
    wg.appendChild(el('circle', { 'class': 'pip', cx: d[0], cy: d[1], r: '2.4' }));
  });
  svg.insertBefore(wg, svg.firstChild.nextSibling);

  /* shrink each sentence to fit its arc once the font has loaded */
  function fitWords() {
    wg.querySelectorAll('.wtxt').forEach(function (t) {
      t.setAttribute('font-size', '12.5');
      var room = Math.PI * wr * (156 / 180) * 0.97, len = t.getComputedTextLength();
      if (len > room) t.setAttribute('font-size', (12.5 * room / len).toFixed(2));
    });
  }
  var compact = window.matchMedia('(max-width:760px)');
  function frame() {
    svg.setAttribute('viewBox', compact.matches ? '0 0 400 400' : '-52 -52 504 504');
    if (!compact.matches) fitWords();
  }
  frame();
  if (compact.addEventListener) compact.addEventListener('change', frame);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(frame);

  /* ---------- interaction ---------- */
  var stage = document.getElementById('stage');
  var wrap = stage.parentNode;
  var readout = document.getElementById('readout');
  var roE = document.getElementById('roEyebrow'), roT = document.getElementById('roTitle');
  var roX = document.getElementById('roText'), roC = document.getElementById('roCta');
  var panel = document.getElementById('panel'), scrim = document.getElementById('scrim');
  var active = null, lastFocus = null, trap = window.bsTrap ? window.bsTrap(panel) : null;

  function showRead(d) {
    active = d;
    roE.textContent = d.eyebrow;
    roT.textContent = d.title;
    roX.textContent = d.tease;
    readout.classList.add('live');
    stage.classList.add('focus');
    wrap.setAttribute('data-ring', d.ring || 'core');
  }
  function clearRead() {
    active = null;
    readout.classList.remove('live');
    stage.classList.remove('focus');
    wrap.removeAttribute('data-ring');
  }

  function openPanel(d) {
    if (!d) return;
    lastFocus = document.activeElement;
    document.getElementById('pSwatch').style.background = d.swatch;
    document.getElementById('pEyebrow').textContent = d.eyebrow;
    document.getElementById('panelTitle').textContent = d.title;
    document.getElementById('pQuote').textContent = d.quote;
    document.getElementById('pIntro').textContent = d.intro;
    var cta = document.getElementById('pCta');
    cta.textContent = d.cta + ' →';
    cta.setAttribute('href', d.href || 'contact/');
    document.getElementById('pNote').textContent = d.note || '';
    document.getElementById('pBits').innerHTML = d.bits.map(function (b) {
      return '<li><b>' + b[0] + '</b><span class="txt">' + b[1] + '</span></li>';
    }).join('');
    panel.scrollTop = 0;
    scrim.classList.add('open');
    panel.classList.add('open');
    panel.setAttribute('aria-hidden', 'false');
    if (window.bsLock) window.bsLock(true);
    if (trap) document.addEventListener('keydown', trap);
    setTimeout(function () { document.getElementById('closeBtn').focus(); }, 60);
  }
  function closePanel() {
    if (!panel.classList.contains('open')) return;
    scrim.classList.remove('open');
    panel.classList.remove('open');
    panel.setAttribute('aria-hidden', 'true');
    if (window.bsLock) window.bsLock(false);
    if (trap) document.removeEventListener('keydown', trap);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  var touch = window.matchMedia('(hover:none)').matches;
  if (touch) {
    var hint = document.getElementById('hint');
    if (hint) hint.textContent = 'Tap a segment to open it';
  }


  function wire(node, data) {
    node.addEventListener('mouseenter', function () { if (!touch) showRead(data); });
    node.addEventListener('focus', function () { showRead(data); node.classList.add('on'); });
    node.addEventListener('blur', function () { clearRead(); node.classList.remove('on'); });
    node.addEventListener('click', function (e) {
      e.preventDefault();
      openPanel(data);
    });
    node.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openPanel(data); }
    });
  }

  document.querySelectorAll('.seg').forEach(function (g) { wire(g, SEGMAP[g.dataset.id]); });
  var core = document.getElementById('core');
  if (core) wire(core, CORE);

  stage.addEventListener('mouseleave', function () { if (!touch) clearRead(); });
  roC.addEventListener('click', function () { openPanel(active); });
  scrim.addEventListener('click', closePanel);
  document.getElementById('closeBtn').addEventListener('click', closePanel);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closePanel(); });

  /* phones: Lisa's words rise in one at a time as they scroll into view */
  var sketch = document.querySelector('.sketch');
  if (sketch && 'IntersectionObserver' in window) {
    sketch.classList.add('js');
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -12% 0px' });
    sketch.querySelectorAll('.sk').forEach(function (li) { io.observe(li); });
  }

  /* logo resets the view */
  var brand = document.getElementById('brand');
  if (brand) {
    var mark = brand.querySelector('.mark');
    brand.addEventListener('click', function (e) {
      e.preventDefault();
      closePanel();
      document.querySelectorAll('.seg,.core').forEach(function (o) { o.classList.remove('on'); });
      if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
      clearRead();
      mark.classList.remove('reset');
      void mark.offsetWidth;
      mark.classList.add('reset');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    mark.addEventListener('animationend', function () { mark.classList.remove('reset'); });
  }
})();
