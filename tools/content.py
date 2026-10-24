#!/usr/bin/env python3
"""Page content for brilliantlysane. Run: python3 tools/content.py"""
import os, sys, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import build, SITE, rel, NAME, WHO, TEL, MAIL

P = []

# ---------------------------------------------------------------- about
P.append(dict(
    slug="about", ring="about",
    title="About Lisa Wallace, LPC | Brilliantly Sane",
    desc="Lisa Wallace is a contemplative psychotherapist in Boulder, Naropa trained, licensed in Colorado. Where she comes from, what she studied, and how she works.",
    eyebrow="The Center",
    h1="Lisa Wallace, <em>LPC</em>",
    standfirst="Contemplative psychotherapist. Naropa, 2017. Boulder, by way of a mountain town, two degrees I use sideways, and a meditation practice I started because nothing else was working.",
    crumbs=[("", "Home"), ("about", "About")],
    schema=[{"@context": "https://schema.org", "@type": "Person", "name": "Lisa Wallace",
             "honorificSuffix": "LPC", "jobTitle": "Licensed Professional Counselor",
             "worksFor": {"@id": SITE + "/#practice"},
             "url": SITE + "/about/", "image": SITE + "/assets/img/lisa.jpg",
             "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Naropa University"},
                          {"@type": "CollegeOrUniversity", "name": "University of Colorado Boulder"}],
             "knowsAbout": ["Contemplative psychotherapy", "Internal Family Systems", "EMDR",
                            "Gender affirming care", "Religious trauma", "Mindfulness"]}],
    sheets=[
        dict(h2="Where I come from", note="A Colorado mountain town, and a long stretch of not being okay.",
             body="""<figure class="portrait-fig">
  <picture><source srcset="../assets/img/lisa.webp" type="image/webp">
  <img src="../assets/img/lisa.jpg" width="640" height="640" alt="Lisa Wallace smiling in a knit cap and dark glasses, one hand raised in a wave."></picture>
  <figcaption>Lisa Wallace, LPC &middot; Boulder, Colorado</figcaption>
</figure>
<p class="lead">I grew up in a middle class mountain community in Colorado. That's where my attachment to the earth comes from, and probably my impatience with people who talk about nature preciously.</p>
<p>For a long stretch I was in pain and depressed. I didn't come to meditation because it sounded restorative. I came to it because I'd run out of other ideas. I studied seriously with Micheal Gregory at Mindfulness Meditation Centers, and that practice is what first let me see my own queerness clearly.</p>
<p>It's also where I began to understand my privilege as a White person in this country. That's work I'm still doing and expect to be doing for the rest of my life. I mention it here because you deserve to know what your therapist is and isn't paying attention to.</p>"""),
        dict(h2="What I studied", note="Film production and religious studies. Neither was a detour.",
             body="""<p>I have two undergraduate degrees from CU Boulder, in film production and religious studies. The religious studies degree is why faith deconstruction doesn't rattle me. The film degree is probably why I pay so much attention to how a person tells their own story, and to which scenes they keep cutting out.</p>
<p>In 2014 I went back to school to become a therapist. I graduated from Naropa University's Contemplative Psychotherapy program in 2017, then spent three years at Umbrella Collective, a practice built around LGBTQIA+ clients.</p>
<p>Since then: WPATH training for gender affirming care, EMDR, Level I Internal Family Systems, and a mindfulness instructor certification through Naropa and iBme.</p>"""),
        dict(h2="How I actually work", note="You're in the driver seat. I have a map.",
             body="""<p>There's no single model I apply to everyone. You're driving. I have a map, I know some of these roads, and now and then I'll mention that a turn looks worth taking.</p>
<p class="pull">You're already sane. Not fine, not unbothered, not finished. Sane.</p>
<p>Whatever you're doing made sense given what happened to you. Once that's clear, the question stops being what's wrong with you and starts being what you want instead. That shift is most of the work.</p>
<p>I ask for feedback and I mean it. If something I said landed badly, say so. I'm accountable to my clients and to my community, which isn't a slogan. It's how I avoid turning into a therapist who's certain about people.</p>
<p>Being human is messy. Let's see if we can find a way to come together in that mess.</p>"""),
    ],
    band=dict(quote="I can help you fall in love with yourself only insofar as I've done it myself.",
              by="Lisa Wallace, LPC",
              img="A still alpine lake at dawn with a snow covered peak reflected on the surface and dark conifers along both shores.",
              side="""<p>Licensed Professional Counselor in Colorado. Telehealth statewide, in person in Boulder some weeks.</p><p><a class="tlink" href="../contact/">Book a free consult</a></p>"""),
))

# ---------------------------------------------------------------- approach
P.append(dict(
    slug="approach", ring="approach",
    title="Therapeutic Approach | Contemplative Psychotherapy, IFS, EMDR",
    desc="Contemplative psychotherapy begins from the premise that you're already sane. How that plays out in session, plus IFS, EMDR, mindfulness and gender affirming care.",
    eyebrow="Ring 01 · The Practical",
    h1="Already sane, then we get <em>specific</em>.",
    standfirst="Contemplative psychotherapy is the ground everything stands on. IFS, EMDR and mindfulness are what I reach for, and only when they fit.",
    crumbs=[("", "Home"), ("approach", "Approach")],
    sheets=[
        dict(h2="Contemplative psychotherapy", note="Naropa University, 2017.",
             body="""<p class="lead">Most models open by naming what's broken. This one opens somewhere else: underneath whatever brought you here, you're already basically sane. Naropa calls it brilliant sanity. I named the practice after it because it's the one idea I'd keep if I had to throw out everything else.</p>
<p>That isn't positive thinking. Plenty is genuinely hard and some of it was done to you. The premise is just that the hard parts are responses rather than defects.</p>
<p>Social expectation, trauma, how you were raised, what your circumstances have been: none of that was in your control. How you relate to yourself is, and that's where the room to move is.</p>"""),
        dict(h2="Internal Family Systems", note="Level I trained.",
             body="""<p>IFS assumes you aren't one voice but several, and that even the harshest one is trying to protect you. The part that keeps you awake rehearsing conversations isn't your enemy. It has a job, and it's been doing that job since long before you could have chosen otherwise.</p>
<p>So we get curious about those parts instead of arguing with them. People tend to soften toward themselves faster this way than they do by being talked out of anything.</p>"""),
        dict(h2="EMDR", note="For memory that still has teeth.",
             body="""<p>Some memories never finished processing. They arrive at full volume, out of order, with your body behaving as though it's happening now rather than then.</p>
<p>EMDR works on that directly. I don't use it with everyone and I rarely use it early. When it fits, it can shift something that years of talking has only circled.</p>"""),
        dict(h2="Mindfulness", note="Certified instructor, Naropa and iBme.",
             body="""<p>I teach mindfulness and I practice it. Those are different things and both matter.</p>
<p>In session it's seldom a formal exercise. More often it's me asking what's happening in your body right now, then being quiet while you find out. That pause is where a surprising amount of the useful material shows up.</p>
<p>I also run mindfulness groups for teens. Details on those are still coming together.</p>"""),
        dict(h2="Gender affirming care", note="WPATH trained.",
             body="""<p>I'm WPATH trained and I spent three years at an LGBTQIA+ practice before going out on my own. If you need letters or coordination with other providers, ask on the consult call and I'll tell you plainly what I can and can't do.</p>
<p><a href="../lgbtqia-therapy/">More on queer and gender affirming therapy</a>.</p>"""),
    ],
))

# ---------------------------------------------------------------- work with (hub)
SPECIALTIES = [
    ("young-adult-therapy/", "Ages 16 to 24", "Young adults",
     "The questions turn enormous and the language for them arrives late. I talk to young adults as people capable of depth, because they are."),
    ("work-with/#introspective", "Already introspective", "People who already look inward",
     "You journal, you notice, you have the vocabulary. What's missing is rhythm, and a second read on what you keep circling."),
    ("lgbtqia-therapy/", "Queer and trans clients", "LGBTQIA+",
     "WPATH trained, queer myself, three years at an LGBTQIA+ practice. You can skip the part where you explain yourself first."),
    ("religious-trauma-therapy/", "Faith and its aftermath", "Religious trauma",
     "Deconstruction, reconstruction, and the long middle where you're not sure which one you're doing."),
]
P.append(dict(
    slug="work-with", ring="work-with",
    title="Who I Work With | Individual Therapy in Colorado",
    desc="Young adults, people who already think hard about themselves, LGBTQIA+ clients, and anyone sorting through religious trauma. Individual therapy, Boulder and statewide.",
    eyebrow="Ring 02 · Who This Is For",
    h1="Four kinds of people keep <em>finding me</em>.",
    standfirst="Not a complete list. Just the honest one. Individuals only, no couples.",
    crumbs=[("", "Home"), ("work-with", "Who I work with")],
    sheets=[
        dict(h2="What they have in common", note="Roughly fifty one percent of the way in.",
             body="""<p class="lead">It isn't a diagnosis. It's that something has already tipped. My clients are usually past the question of whether to do this, even if they're nowhere near sure what they want out of it.</p>
<p>Most have been to therapy before. Often it was fine and it taught them some skills, and they're back because they want something with more depth than skills this time.</p>
<p>If you're still genuinely undecided about being in therapy at all, that's allowed. I'd just rather you spend a free twenty minute call asking me about it than book eight sessions to find out.</p>"""),
        dict(h2="The four", note="Each has a page of its own.",
             body="""<ul class="index-list">""" + "".join(
                 f"""<li><a href="{'../' + h if not h.startswith('work-with') else '#introspective'}"><span class="meta">{m}</span><span><h3>{t}</h3><p>{d}</p></span></a></li>"""
                 for h, m, t, d in SPECIALTIES) + """</ul>"""),
        dict(h2="People who already look inward", note="There's no separate page for this one. It's here.",
             body="""<p id="introspective">Some people arrive with the groundwork laid. You've done the reading. You keep a journal. You can name a feeling while it's still happening, which is genuinely rarer than it sounds.</p>
<p>The work is different then. Less teaching, more interpretation. I'm not going to walk you through identifying an emotion. What I can do is help with timing, with precision, and with the question underneath all that noticing, which is usually some version of so what do I do now.</p>
<p class="pull">You have the material. What you want is a way to read it.</p>
<p>Three things tend to come up: when to stay with something and when to set it down, finding words exact enough to hold what you actually mean, and understanding what the noticing has been pointing at the whole time.</p>"""),
        dict(h2="Who this isn't for", note="Said plainly, so nobody wastes a consult.",
             body="""<p>I don't work with couples.</p>
<p>I don't prescribe, and I'm not the right fit if medication management is the most urgent thing on your list, or if you need a higher level of care than weekly outpatient therapy. I'll coordinate with a prescriber happily. I just can't be one.</p>
<p>My clients start at sixteen. If you're younger than that I'm not your therapist, though I can usually point you toward someone who is.</p>"""),
    ],
))

# ---------------------------------------------------------------- specialty: young adults
P.append(dict(
    slug="young-adult-therapy", ring="young-adult-therapy",
    title="Therapy for Young Adults in Colorado | Ages 16 to 24 | Boulder",
    desc="Therapy for sixteen to twenty four year olds across Colorado, by video or in person in Boulder. Identity, pressure, and being taken seriously by an adult who isn't grading you.",
    eyebrow="Who I work with",
    h1="Finding your <em>footing</em>.",
    standfirst="Therapy for sixteen to twenty four year olds. Video anywhere in Colorado, in person in Boulder when it works out.",
    crumbs=[("", "Home"), ("work-with", "Who I work with"), ("young-adult-therapy", "Young adults")],
    schema=[{"@context": "https://schema.org", "@type": "Service",
             "serviceType": "Therapy for young adults", "provider": {"@id": SITE + "/#practice"},
             "areaServed": {"@type": "State", "name": "Colorado"},
             "audience": {"@type": "PeopleAudience", "suggestedMinAge": 16, "suggestedMaxAge": 24}}],
    facts=[("Fee", '$175<small>Fifty five minutes. CO Access Medicaid accepted.</small>'),
           ("Format", 'Video<small>Anywhere in Colorado. In person in Boulder some weeks.</small>'),
           ("First step", 'Free consult<small>Twenty minutes. The young person is welcome on it.</small>')],
    sheets=[
        dict(h2="This stretch of life", note="Sixteen to twenty four.",
             body="""<p class="lead">The questions get enormous somewhere around sixteen, and the language for them doesn't show up until years later. That gap is miserable, and most of the adults around you will try to close it by answering questions you didn't ask.</p>
<p>I work with young adults who are taking all of this seriously. You'll get talked to like someone capable of depth, because you are, and because being handled gently by one more adult is probably not what you came for.</p>"""),
        dict(h2="If you're the young person", note="What actually happens.",
             body="""<p>You bring what's going on. I ask about it. Sometimes I ask what your body is doing while you talk, which sounds odd the first time and stops being odd quickly.</p>
<p>Identity usually comes up, whether that's gender, sexuality, faith, what you want to do with your life, or who you are when your family isn't in the room. None of it's a phase I'm waiting out. It's a shape still forming, and I'd like to be useful while it does.</p>
<p>You can tell me I'm wrong. Please do. I'd rather be corrected than agreed with politely.</p>"""),
        dict(h2="If you're the parent", note="Where the lines are.",
             body="""<p>My client is your kid, which shapes how this goes.</p>
<p>I'll talk with you about logistics: scheduling, payment, safety concerns. I won't report back on what your kid said in session. That confidentiality is the reason therapy works for this age group at all, and the moment it's conditional, it stops being useful.</p>
<p>If something comes up that genuinely requires your involvement, I'll tell your kid first, and then we'll figure out together how you get told. That's the arrangement I'd want if it were my family.</p>"""),
    ],
))

# ---------------------------------------------------------------- specialty: lgbtqia
P.append(dict(
    slug="lgbtqia-therapy", ring="lgbtqia-therapy",
    title="Queer and Gender Affirming Therapy | Boulder and Colorado",
    desc="WPATH trained, queer, three years at an LGBTQIA+ practice. Gender affirming therapy by video across Colorado and in person in Boulder.",
    eyebrow="Who I work with",
    h1="No translation <em>tax</em>.",
    standfirst="Queer and gender affirming therapy. You shouldn't have to teach your therapist who you are before you can use the hour.",
    crumbs=[("", "Home"), ("work-with", "Who I work with"), ("lgbtqia-therapy", "Queer and gender affirming")],
    schema=[{"@context": "https://schema.org", "@type": "Service",
             "serviceType": "Queer and gender affirming therapy", "provider": {"@id": SITE + "/#practice"},
             "areaServed": {"@type": "State", "name": "Colorado"}}],
    facts=[("Fee", '$175<small>Fifty five minutes. CO Access Medicaid accepted.</small>'),
           ("Training", 'WPATH<small>Plus three years at an LGBTQIA+ practice.</small>'),
           ("First step", 'Free consult<small>Twenty minutes, by phone or video.</small>')],
    sheets=[
        dict(h2="Where I'm coming from", note="Queer, WPATH trained, three years at Umbrella Collective.",
             body="""<p class="lead">I'm queer. Meditation was how I first understood that about myself, years before I had a vocabulary for it, so I have some feeling for how long the gap between knowing and saying can be.</p>
<p>Professionally: WPATH trained for gender affirming care, and three years at Umbrella Collective, a Boulder practice built specifically around LGBTQIA+ clients. That's where a lot of my practical knowledge came from, and it's why I'm not learning on you.</p>"""),
        dict(h2="What that changes in session", note="Mostly, what you can skip.",
             body="""<p>You don't start from scratch each time. You don't explain your pronouns, your relationship structure, or your family's reaction, and then watch me recalibrate.</p>
<p>Your identity can be the center of this work or it can barely come up. Some clients are here for transition related questions. Others are here about grad school and a bad breakup, and being queer is simply the weather. Both are fine, and you get to decide which it is week to week.</p>"""),
        dict(h2="Gender affirming care", note="Letters and coordination.",
             body="""<p>I'm WPATH trained. If you need documentation or want me coordinating with a prescriber, surgeon or primary care provider, bring it up on the consult call and I'll tell you exactly what I can do rather than making you guess.</p>"""),
    ],
))

# ---------------------------------------------------------------- specialty: religious trauma
P.append(dict(
    slug="religious-trauma-therapy", ring="religious-trauma-therapy",
    title="Religious Trauma Therapy and Faith Deconstruction | Colorado",
    desc="Deconstruction, reconstruction, and the long middle. Therapy for religious trauma in Colorado with a therapist who studied religion before she studied therapy.",
    eyebrow="Who I work with",
    h1="Faith, taken <em>apart</em>.",
    standfirst="Deconstruction, reconstruction, and the long middle where you're not sure which one you're doing. All three belong here.",
    crumbs=[("", "Home"), ("work-with", "Who I work with"), ("religious-trauma-therapy", "Religious trauma")],
    schema=[{"@context": "https://schema.org", "@type": "Service",
             "serviceType": "Religious trauma and faith transition therapy",
             "provider": {"@id": SITE + "/#practice"},
             "areaServed": {"@type": "State", "name": "Colorado"}}],
    facts=[("Fee", '$175<small>Fifty five minutes. CO Access Medicaid accepted.</small>'),
           ("Background", 'Religious Studies<small>CU Boulder, before the therapy degree.</small>'),
           ("First step", 'Free consult<small>Twenty minutes, no commitment.</small>')],
    sheets=[
        dict(h2="Why me for this", note="Religious studies at CU Boulder, before the therapy degree.",
             body="""<p class="lead">I studied religion before I studied therapy. That means I take it seriously as something people actually lived inside, with its own logic and its own comforts, rather than as a set of bad opinions to be argued out of someone.</p>
<p>It also means I'm not shocked by the specifics. You can use the real words for what happened, including the parts that sound absurd from outside, without stopping to supply background.</p>"""),
        dict(h2="Deconstruction", note="Grief, anger and relief, usually at once.",
             body="""<p>Leaving a belief system takes more than deciding it isn't true. The belief came bundled with a community, a calendar, a vocabulary for suffering, and often your family. Losing the claim is the easy part. Losing the structure is what wakes people up at three in the morning.</p>
<p>People are frequently surprised by how much grief is in this, and how much anger sits right next to the relief without canceling it out.</p>"""),
        dict(h2="Reconstruction", note="If you want it.",
             body="""<p>Some people rebuild. Some find their way to a different tradition, or to the same one held differently. Others want nothing to do with any of it again, and that's a complete answer too.</p>
<p>I'm not steering you. I have my own practice and my own history with this, and neither is the point of your hour.</p>"""),
        dict(h2="The long middle", note="Not knowing yet is a real place.",
             body="""<p class="pull">Leaving a belief system is not the same as leaving yourself.</p>
<p>Most of the people I see are not at either end. They're somewhere in the middle, no longer believing it and not yet anything else, which is lonely in a way that's hard to describe to people who haven't been there.</p>
<p>You can sit in that middle for a while here. It isn't a stage to be moved through on a schedule.</p>"""),
    ],
    band=dict(quote="Losing the claim is the easy part. Losing the structure is what wakes people at three in the morning.",
              side="""<p>$175 for fifty five minutes. Telehealth across Colorado. Free twenty minute call to start.</p><p><a class="tlink" href="../contact/">Reach out</a></p>"""),
))

# ---------------------------------------------------------------- rates
P.append(dict(
    slug="rates", ring="rates",
    title="Rates and Payment | Brilliantly Sane | $175 per session",
    desc="$175 for a fifty five minute session, CO Access Medicaid accepted, and a free twenty minute consult first. Fees stated plainly, before you book anything.",
    eyebrow="Ring 01 · The Practical",
    h1="$175, said <em>out loud</em>.",
    standfirst="I'd rather you know the number now than find it in an email after you've already gotten your hopes up.",
    crumbs=[("", "Home"), ("rates", "Rates")],
    schema=[{"@context": "https://schema.org", "@type": "Offer",
             "itemOffered": {"@type": "Service", "serviceType": "Individual psychotherapy session",
                             "provider": {"@id": SITE + "/#practice"}},
             "price": "175", "priceCurrency": "USD",
             "eligibleDuration": {"@type": "QuantitativeValue", "value": 55, "unitCode": "MIN"}}],
    sheets=[
        dict(h2="The numbers", note="Current as of 2026.", cls="wide",
             body="""<ul class="rows">
<li><b>Individual session</b><span class="val"><span class="num">$175<small>55 minutes</small></span></span></li>
<li><b>First consult</b><span class="val"><span class="num">Free<small>20 minutes, by phone or video</small></span></span></li>
<li><b>Insurance</b><span class="val"><p>I accept CO Access Medicaid.</p><p>If you have out of network benefits through another plan, ask me on the consult call and I'll tell you what documentation I can provide.</p></span></li>
<li><b>If cost is the problem</b><span class="val"><p>Say so on the call. I'd rather have that conversation in week one than watch someone quietly disappear in week four.</p></span></li>
</ul>
<!-- TODO confirm with Lisa before launch: cancellation window, accepted payment methods, whether superbills are issued -->"""),
        dict(h2="Why it's on the website", note="Most practices make you ask.",
             body="""<p>Money is one more place we rehearse what we think we deserve. Making people email for a number, then quote it back apologetically, puts that rehearsal right at the front door.</p>
<p>So: $175. If that works, good. If it doesn't, tell me on the free call and we'll talk about it like adults.</p>"""),
        dict(h2="What a session is", note="Fifty five minutes, usually weekly at first.",
             body="""<p>Sessions run fifty five minutes. Most people start weekly, because early momentum matters more than frequency does six months in. We adjust once the work finds its own rhythm.</p>
<p>Almost everything is by video, anywhere in Colorado. If you're in or near Boulder and would rather be in a room, ask me, because some weeks that's possible.</p>"""),
    ],
))

# ---------------------------------------------------------------- faq
FAQ = [
    ("What is contemplative psychotherapy?",
     "<p>A model developed at Naropa University that starts from the premise that you're already basically sane, and that the difficult parts of you are responses to something rather than defects in you. In practice it means less time diagnosing you and more time getting curious about what you're already doing and why it made sense.</p>"),
    ("What happens in a first session?",
     "<p>We talk about what brought you. I'll ask some history, but it isn't an interrogation and the paperwork is short. Most people leave the first session knowing whether they want a second one, which is the main thing I'm hoping for.</p>"),
    ("How long will I be in therapy?",
     "<p>As long as it's useful and not one session longer. Some people come for a few months around a specific thing. Others stay for years. I'll tell you when I think you're done, and you're allowed to disagree.</p>"),
    ("What does it cost?",
     "<p>$175 for a fifty five minute session. The first twenty minute consult is free. <a href=\"../rates/\">Full rates</a>.</p>"),
    ("Do you take insurance?",
     "<p>I accept CO Access Medicaid. If you have out of network benefits through a different plan, ask on the consult call and I'll tell you what documentation I can provide.</p>"),
    ("Do you meet in person or by video?",
     "<p>Mostly video, anywhere in Colorado. I'm in Boulder, and in person is sometimes possible, so ask if that matters to you.</p>"),
    ("Do you work with couples?",
     "<p>No. Individuals only. If you want couples work I can usually suggest someone.</p>"),
    ("How old do your clients have to be?",
     "<p>Sixteen and up. A lot of my work is with the sixteen to twenty four range.</p>"),
    ("What is IFS, in one paragraph?",
     "<p>Internal Family Systems treats you as a system of parts rather than one voice, and assumes even the harsh ones are protecting you. Instead of arguing with the part of you that won't stop rehearsing conversations, we find out what it's worried would happen if it stopped. <a href=\"../approach/\">More on how I work</a>.</p>"),
    ("Will we do EMDR?",
     "<p>Maybe, and not right away. EMDR is for memories that still arrive at full volume with your body reacting as though it's happening now. When that's what's going on, it can move things that talking has only circled. When it isn't, we won't use it.</p>"),
    ("Do you prescribe medication?",
     "<p>No. I'm a licensed professional counselor, not a prescriber. I'll coordinate with whoever handles that for you.</p>"),
    ("What if we're not a good fit?",
     "<p>Then I'll say so, and I'll help you find someone better suited. That's a normal outcome, not a failure, and it's much cheaper to discover in a free consult than in month three.</p>"),
]
P.append(dict(
    slug="faq", ring="faq",
    title="Questions People Ask | Brilliantly Sane",
    desc="What a first session is like, what it costs, whether insurance works, how long therapy takes, and what happens if we're not a fit. Twelve plain answers.",
    eyebrow="Ring 01 · The Practical",
    h1="The ones people ask <em>on the call</em>.",
    standfirst="Twelve questions that come up almost every time, answered here so you don't have to spend your free twenty minutes on them.",
    crumbs=[("", "Home"), ("faq", "Questions")],
    schema=[{"@context": "https://schema.org", "@type": "FAQPage",
             "mainEntity": [{"@type": "Question", "name": q,
                             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}],
    sheets=[dict(h2="Questions", note="If yours isn't here, the free call is a good place to put it.", cls="wide faq-cols",
                 body='<ul class="rows">' + "".join(
                     f'<li><b>{q}</b><span class="val">{a}</span></li>' for q, a in FAQ) + "</ul>")],
))

# ---------------------------------------------------------------- journal
POSTS = [
    dict(slug="why-brilliantly-sane", date="2026-09-18", read="4 min",
         title="Why I named the practice Brilliantly Sane",
         desc="The phrase comes from Naropa, and from a stretch of my life when nobody would have described me that way. Here's what it actually means.",
         body="""<p class="lead">People ask about the name, usually with a slightly raised eyebrow, which is fair. It sounds like a claim.</p>
<p>It comes from Naropa, where the contemplative psychotherapy program uses the phrase brilliant sanity to describe what's underneath everything a person brings into a room. Not their coping. Not their diagnosis. The thing that was there first and stays there regardless.</p>
<p>I didn't believe it when I first heard it. I'd come through a long stretch of pain and depression, and nobody looking at me in those years would have reached for the word sane. I was functional on my better days and barely that on the rest.</p>
<p class="pull">The premise isn't that you're fine. It's that what you're doing made sense.</p>
<p>What changed my mind was sitting still for long enough to watch my own mind do its thing. Not fixing it. Watching it. And noticing that underneath the noise there was something that hadn't been damaged, that was just waiting around for me to stop drowning it out.</p>
<p>That's the whole premise. Societal expectation, trauma, how you were raised, the specific circumstances you landed in: those weren't in your control, and your responses to them were reasonable. What's in your control is how you relate to yourself now.</p>
<p>The joke in the initials is intentional, by the way. Therapy that takes itself too seriously tends to miss things.</p>"""),
    dict(slug="the-long-middle", date="2026-10-02", read="5 min",
         title="The long middle of leaving a faith",
         desc="Most writing about deconstruction covers the leaving or the landing. Almost none of it covers the years in between, which is where most people actually live.",
         body="""<p class="lead">Almost everything written about faith deconstruction covers one of two moments: the crisis, or the arrival somewhere new. The middle gets skipped, which is unfortunate, because the middle is where people spend most of their time.</p>
<p>The middle is not believing it anymore and not being anything else yet. It's still knowing all the songs. It's the reflex to pray during turbulence and the flinch right after. It's your mother asking what church you've found and you saying you're still looking, because the true answer takes forty minutes and will hurt her.</p>
<p>People arrive in my office apologizing for being in this stage. They've read that deconstruction is supposed to lead somewhere, and they're embarrassed to have been in transit for three years.</p>
<p>I want to say clearly: that's not a failure of process. Belief systems aren't opinions you swap. They come bundled with community, a calendar, a vocabulary for suffering, and usually your family. Dropping the claim takes an afternoon. Rebuilding everything the claim was holding up takes much longer.</p>
<p>What helps, in my experience, is naming what you actually lost rather than arguing about what's true. Most people discover they miss specific things. Singing with other people. Having language for grief. A reason for the week to have a shape.</p>
<p>Those are addressable. Some people find them again inside a tradition, some outside it. But you can't go looking for them while you're still insisting the only question is whether any of it was real.</p>"""),
    dict(slug="meditation-did-not-fix-me", date="2026-10-14", read="3 min",
         title="Meditation did not fix me",
         desc="I came to practice because I'd run out of other ideas, not because it sounded restorative. What it actually did was more specific and less marketable.",
         body="""<p class="lead">I started meditating because I'd run out of other ideas. That's less inspiring than the version where someone discovers stillness on a retreat, but it's what happened.</p>
<p>I was in pain and I was depressed, and the things that were supposed to work weren't. So I sat down. Then I did it again the next day, and for a long time after that, with Micheal Gregory at Mindfulness Meditation Centers.</p>
<p>Here is what it did not do: it did not make me calm, it did not resolve the pain, and it did not deliver a single insight that would look good on a poster.</p>
<p>Here's what it did do. It gave me enough distance from my own mind to notice that I was queer. Not decide. Notice. The information had been sitting there for years, drowned out by the volume of everything else, and sitting still turned the volume down enough for me to hear it.</p>
<p>It also made me aware of my privilege as a White person in a way that reading hadn't managed, because it's harder to argue with something you're watching yourself do in real time than with something on a page.</p>
<p>When I use mindfulness with clients, this is what I'm after. Not relaxation. Just enough quiet that the information you already have can finally reach you.</p>"""),
]
P.append(dict(
    slug="journal", noring=True,
    title="Journal | Brilliantly Sane",
    desc="Occasional writing from Lisa Wallace on contemplative practice, faith transitions, and what actually happens in therapy. No posting schedule.",
    eyebrow="Writing",
    h1="Occasional <em>writing</em>.",
    standfirst="No schedule. I write when something has been rattling around long enough to be worth the trouble.",
    crumbs=[("", "Home"), ("journal", "Journal")],
    schema=[{"@context": "https://schema.org", "@type": "Blog", "name": "Brilliantly Sane Journal",
             "url": SITE + "/journal/", "author": {"@type": "Person", "name": "Lisa Wallace"},
             "blogPost": [{"@type": "BlogPosting", "headline": p["title"],
                           "datePublished": p["date"], "description": p["desc"],
                           "url": SITE + "/journal/" + p["slug"] + "/"} for p in POSTS]}],
    sheets=[dict(h2="Posts", note="Three so far.",
                 body='<ul class="index-list">' + "".join(
                     f"""<li><a href="{p['slug']}/"><span class="meta">{datetime.date.fromisoformat(p['date']).strftime('%B %-d, %Y')}<br>{p['read']}</span><span><h3>{p['title']}</h3><p>{p['desc']}</p></span></a></li>"""
                     for p in reversed(POSTS)) + "</ul>")],
))

for i, post in enumerate(POSTS):
    nice = datetime.date.fromisoformat(post["date"]).strftime("%B %-d, %Y")
    P.append(dict(
        slug="journal/" + post["slug"],
        title=post["title"] + " | Brilliantly Sane",
        desc=post["desc"],
        ogtype="article",
        eyebrow=f"Journal · {nice} · {post['read']} read",
        h1=post["title"],
        crumbs=[("", "Home"), ("journal", "Journal"), ("journal/" + post["slug"], post["title"])],
        schema=[{"@context": "https://schema.org", "@type": "BlogPosting",
                 "headline": post["title"], "description": post["desc"],
                 "datePublished": post["date"], "dateModified": post["date"],
                 "author": {"@type": "Person", "name": "Lisa Wallace", "url": SITE + "/about/"},
                 "publisher": {"@id": SITE + "/#practice"},
                 "image": SITE + "/assets/img/og-brilliantly-sane.jpg",
                 "mainEntityOfPage": SITE + "/journal/" + post["slug"] + "/",
                 "isPartOf": {"@type": "Blog", "name": "Brilliantly Sane Journal", "url": SITE + "/journal/"}}],
        layout="post", noring=True,
        byline=f"Lisa Wallace, LPC &middot; {nice}",
        post=post["body"] + '<p style="margin-top:40px"><a class="tlink back" href="../">All posts</a></p>',
        band=dict(quote="Being human is messy. Let's see if we can find a way to come together in that mess.",
                  by="Lisa Wallace, LPC",
                  side="""<p>Contemplative psychotherapy, telehealth across Colorado.</p><p><a class="tlink" href="../../contact/">Book a free consult</a></p>"""),
    ))

if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    import extra
    for page in P + extra.PAGES:
        print(build(page))
    extra.statics(P + extra.PAGES, POSTS)
