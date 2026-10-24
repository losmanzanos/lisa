#!/usr/bin/env python3
"""Contact page, 404, and the sitewide static files."""
import os, datetime, html
from build import SITE, NAME, WHO, TEL, MAIL

TODAY = datetime.date.today().isoformat()

FORM = """<form class="form" id="contactForm" novalidate>
  <div class="field">
    <label for="f-name">Your name</label>
    <input id="f-name" name="from_name" type="text" autocomplete="name" required>
    <p class="msg">Please add a name I can call you.</p>
  </div>
  <div class="field">
    <label for="f-email">Email</label>
    <input id="f-email" name="reply_to" type="email" autocomplete="email" inputmode="email" required>
    <p class="msg">That email address doesn't look complete.</p>
  </div>
  <div class="field">
    <label for="f-phone">Phone <span style="text-transform:none;letter-spacing:0">(optional)</span></label>
    <input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel">
    <p class="hint">Only if you'd rather I call than email.</p>
  </div>
  <div class="field">
    <label for="f-reach">Best way to reach you</label>
    <select id="f-reach" name="preferred_contact">
      <option>Email</option>
      <option>Phone call</option>
      <option>Text message</option>
    </select>
  </div>
  <div class="field">
    <label for="f-msg">What's going on</label>
    <textarea id="f-msg" name="message" required></textarea>
    <p class="hint">As much or as little as you want. A sentence is plenty to start.</p>
    <p class="msg">Tell me something, even briefly, so I know how to reply.</p>
  </div>
  <div class="hp" aria-hidden="true"><label for="f-web">Leave this empty</label><input id="f-web" name="website" type="text" tabindex="-1" autocomplete="off"></div>
  <button class="submit" type="submit" id="f-send">Send it</button>
  <p class="form-status" id="f-status" role="status" aria-live="polite"></p>
</form>"""

PAGES = [
    dict(
        slug="contact",
        title="Reach Out | Book a Free Consult | Brilliantly Sane",
        desc="Book a free twenty minute consult with Lisa Wallace, LPC. Call 970-368-9185, email lisa@brilliantlysane.org, or use the form.",
        eyebrow="Ring 01 · The Practical",
        h1="Twenty minutes, <em>free</em>.",
        standfirst="The first call costs nothing and commits you to nothing. Bring the question you think is too basic to ask.",
        crumbs=[("", "Home"), ("contact", "Reach out")],
        extrajs='\n<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4.4.1/dist/email.min.js" defer></script>\n<script src="../assets/contact.js" defer></script>',
        sheets=[
            dict(h2="Send a note", note="I answer these myself, usually within two business days.",
                 body=FORM),
            dict(h2="Or skip the form", note="Some people would rather just call. Do that.",
                 body=f"""<p><a href="tel:+19703689185">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
<p>If I don't pick up, leave a message with a good time to call back and I'll work around it.</p>
<p class="hint" style="margin-top:22px;font-size:13.5px;color:var(--ink-50);max-width:46ch">Email and voicemail aren't monitored for emergencies. If you're in crisis, call or text 988 for the Suicide and Crisis Lifeline, or call 911.</p>"""),
            dict(h2="What happens next", note="So the wait isn't strange.",
                 body="""<p>I get back to you, we find twenty minutes, and we talk. You tell me roughly what's going on. I tell you how I work and whether I think I'm the right person for it.</p>
<p>If I'm not, I'll say so on that call and point you somewhere better. That happens sometimes and it isn't a bad outcome.</p>
<p>If I am, we schedule a first session. $175 for fifty five minutes, mostly by video, CO Access Medicaid accepted. <a href="../rates/">The rest of the details are here</a>.</p>"""),
        ],
        band=dict(quote="Bring your doubts to the free call. That's a good use of it.",
                  side="""<p>Telehealth across Colorado. In person in Boulder when it works out.</p><p><a class="tlink" href="../faq/">Read the questions first</a></p>"""),
    ),
    dict(
        slug="", file="404.html", depth=0,
        title="Page not found | Brilliantly Sane",
        desc="That page isn't here. Links to the rest of the site, and a way to get in touch.",
        eyebrow="404",
        h1="That page isn't <em>here</em>.",
        standfirst="Either it moved or the link was wrong. Both happen. Here's where everything actually is.",
        sheets=[dict(h2="Try one of these", note="Or call 970-368-9185.",
                     body=f"""<ul class="index-list">
<li><a href="{SITE}/about/"><span class="meta">The center</span><span><h3>About Lisa</h3><p>Where she trained, where she comes from, and how she works.</p></span></a></li>
<li><a href="{SITE}/work-with/"><span class="meta">Ring 02</span><span><h3>Who I work with</h3><p>Young adults, introspective clients, LGBTQIA+, religious trauma.</p></span></a></li>
<li><a href="{SITE}/rates/"><span class="meta">Ring 01</span><span><h3>Rates</h3><p>$175 for fifty five minutes, and a free call first.</p></span></a></li>
<li><a href="{SITE}/contact/"><span class="meta">Ring 01</span><span><h3>Reach out</h3><p>Book the free twenty minute consult.</p></span></a></li>
</ul>"""),
                ],
    ),
]


def statics(pages, posts):
    urls = []
    for p in pages:
        if p.get("file") == "404.html":
            continue
        urls.append(SITE + "/" + (p["slug"] + "/" if p["slug"] else ""))
    urls.insert(0, SITE + "/")
    seen, ordered = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            ordered.append(u)

    body = "".join(
        f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod>"
        f"<changefreq>{'monthly' if '/journal/' in u and u.rstrip('/').split('/')[-1] != 'journal' else 'monthly'}</changefreq>"
        f"<priority>{'1.0' if u == SITE + '/' else '0.8'}</priority></url>\n" for u in ordered)
    open("sitemap.xml", "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")

    open("robots.txt", "w").write(
        "User-agent: *\nAllow: /\n\n"
        "# Housekeeping\nDisallow: /tools/\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n")

    post_lines = "".join(
        f"- [{p['title']}]({SITE}/journal/{p['slug']}/): {p['desc']}\n" for p in reversed(posts))
    open("llms.txt", "w").write(f"""# Brilliantly Sane

> Contemplative psychotherapy with Lisa Wallace, LPC. Individual therapy by video across Colorado, based in Boulder. $175 for a 55 minute session, CO Access Medicaid accepted, free 20 minute consult.

Lisa Wallace is a Licensed Professional Counselor who graduated from Naropa University's Contemplative Psychotherapy program in 2017. She is WPATH trained, EMDR trained, Level I trained in Internal Family Systems, and a certified mindfulness instructor through Naropa and iBme. She works with individuals only, age 16 and up. She does not work with couples and does not prescribe medication.

## Core pages
- [About Lisa Wallace]({SITE}/about/): background, training and credentials.
- [Therapeutic approach]({SITE}/approach/): contemplative psychotherapy, IFS, EMDR, mindfulness, gender affirming care.
- [Who she works with]({SITE}/work-with/): young adults 16 to 24, introspective clients, LGBTQIA+ clients, religious trauma.
- [Rates and payment]({SITE}/rates/): $175 per 55 minute session, CO Access Medicaid, free consult.
- [Questions]({SITE}/faq/): twelve common questions with plain answers.
- [Reach out]({SITE}/contact/): free 20 minute consult, {TEL}, {MAIL}.

## Specialties
- [Therapy for young adults, ages 16 to 24]({SITE}/young-adult-therapy/)
- [Queer and gender affirming therapy]({SITE}/lgbtqia-therapy/)
- [Religious trauma and faith deconstruction]({SITE}/religious-trauma-therapy/)

## Journal
{post_lines}
## Contact
Phone: {TEL}
Email: {MAIL}
Service area: Colorado, telehealth statewide. Office in Boulder, Colorado.
""")

    # TinaCMS source of truth for the journal
    os.makedirs("content/journal", exist_ok=True)
    for p in posts:
        md = (f"---\ntitle: \"{p['title']}\"\ndate: {p['date']}\n"
              f"readingTime: \"{p['read']}\"\nexcerpt: \"{p['desc']}\"\ndraft: false\n---\n\n"
              + p["body"].replace("</p>", "\n").replace('<p class="lead">', "").replace('<p class="pull">', "> ")
                         .replace("<p>", "").replace('<p id="introspective">', "").strip() + "\n")
        open(f"content/journal/{p['slug']}.md", "w").write(md)
    print("statics written")
