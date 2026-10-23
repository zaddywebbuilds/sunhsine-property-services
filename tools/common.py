# -*- coding: utf-8 -*-
"""Shared data and HTML partials for the Sunshine Property Services site.

Run tools/build.py to regenerate every page from these partials.
"""

import io
import os
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ----------------------------------------------------------------------
# Business facts. Source: the company Google Business Profile, Oct 2026.
# ----------------------------------------------------------------------
NAME = "Sunshine Property Services"
TAGLINE = "Toronto &middot; Property Care"
PHONE = "+1 416-788-8942"
PHONE_TEL = "+14167888942"
PHONE_WA = "14167888942"
AREA = "Toronto &amp; the GTA"
HOURS_SHORT = "Mon to Fri 7am-7pm &middot; Sat &amp; Sun 9am-5pm"
BASE = "https://zaddywebbuilds.github.io/sunhsine-property-services"
MAPS = ("https://www.google.com/maps/place/sunhsine+property+services/"
        "@43.7198354,-79.3776555,11z/data=!4m6!3m5!"
        "1s0x2fea3e30a5188191:0xabf613fe45d4fafc!8m2!3d43.7198354!4d-79.3776555")
LAT, LON = "43.7198", "-79.3777"


def wa(message):
    """WhatsApp deep link with a pre-filled message."""
    return "https://wa.me/%s?text=%s" % (
        PHONE_WA, urllib.parse.quote("Hi Sunshine Property Services, " + message))


WA_GENERAL = wa("I'd like a quote for property cleaning. Here's what I need:")
WA_QUOTE = wa("I'd like a free quote. Here's the property and what needs doing:")

# ----------------------------------------------------------------------
# Service catalogue. Every entry owns its own photograph.
# ----------------------------------------------------------------------
SERVICES = [
    dict(slug="house-cleaning-toronto", short="House Cleaning", ring=True,
         img="images/residential-cleaning.jpg", thumb="images/t-floor-care.jpg",
         title="House Cleaning in Toronto",
         alt="Cleaner vacuuming a bright Toronto living room",
         thumb_alt="Floor care in a Toronto living room",
         blurb="Weekly, every other week or monthly. The same careful run through every room, every visit."),
    dict(slug="deep-cleaning-toronto", short="Deep Cleaning", ring=True,
         img="images/kitchen-deep-clean.jpg", thumb="images/t-kitchen-detail.jpg",
         title="Deep Cleaning in Toronto",
         alt="Cleaner wiping down a marble kitchen island",
         thumb_alt="Close detail work on a modern kitchen counter",
         blurb="The reset clean. Inside appliances, behind furniture, grout, baseboards and all the edges."),
    dict(slug="move-out-cleaning-toronto", short="Move In &amp; Move Out", ring=True,
         img="images/move-out-cleaning.jpg", thumb="images/t-turnover.jpg",
         title="Move In &amp; Move Out Cleaning in Toronto",
         alt="Empty apartment being cleaned before handover",
         thumb_alt="Vacant unit cleaned and ready for the next tenant",
         blurb="Empty unit, top to bottom, ready for the walkthrough, the listing or the new keys."),
    dict(slug="commercial-cleaning-toronto", short="Office &amp; Commercial", ring=True,
         img="images/office-cleaning.jpg", thumb="images/t-commercial-floor.jpg",
         title="Office &amp; Commercial Cleaning in Toronto",
         alt="Cleaner wiping desks in a downtown Toronto office",
         thumb_alt="Commercial floor care in an open plan office",
         blurb="Offices, clinics, studios and common areas, cleaned after hours or before you open."),
    dict(slug="post-construction-cleaning-toronto", short="Post-Construction", ring=True,
         img="images/post-reno-cleanup.jpg", thumb="images/t-staircase.jpg",
         title="Post-Construction &amp; Renovation Cleanup in Toronto",
         alt="Construction dust being vacuumed after a renovation",
         thumb_alt="Stair treads and handrail wiped down after a build",
         blurb="Fine dust off every surface, sill and vent so the finished work actually looks finished."),
    dict(slug="window-cleaning-toronto", short="Window Cleaning", ring=True,
         img="images/window-cleaning.jpg", thumb="images/t-highrise-windows.jpg",
         title="Window Cleaning in Toronto",
         alt="Interior window being squeegeed clean",
         thumb_alt="High rise window cleaning above the Toronto skyline",
         blurb="Glass, frames and tracks. Interior panes, balcony glass and reachable exteriors."),
    dict(slug="pressure-washing-toronto", short="Pressure Washing", ring=True,
         img="images/t-power-washing.jpg", thumb="images/t-driveway.jpg",
         title="Pressure Washing in Toronto",
         alt="Pressure washing a house exterior",
         thumb_alt="Driveway and walkway washed clean",
         blurb="Driveways, walkways, patios, siding and garage doors brought back a few shades."),
    dict(slug="junk-removal-toronto", short="Junk Removal", ring=True,
         img="images/svc-junk-removal.svg", thumb="images/svc-estate-cleanout.svg",
         title="Junk Removal &amp; Cleanouts in Toronto",
         alt="Illustration of a junk removal truck being loaded",
         thumb_alt="Illustration of a full property cleanout",
         blurb="Single items or a full cleanout. We carry it out, load it and sweep the space after."),
    dict(slug="snow-removal-toronto", short="Snow Removal", ring=False,
         img="images/t-snow-removal.jpg", thumb="images/t-driveway.jpg",
         title="Snow Removal &amp; Winter Maintenance in Toronto",
         alt="Snow blower clearing a Toronto driveway in winter",
         thumb_alt="Cleared driveway after a winter storm",
         blurb="Driveways, walkways and entrances cleared and salted through the Toronto winter."),
    dict(slug="property-turnover-toronto", short="Property Turnovers", ring=False,
         img="images/t-turnover.jpg", thumb="images/t-staircase.jpg",
         title="Rental &amp; Property Turnovers in Toronto",
         alt="Vacant rental unit prepared for the next tenant",
         thumb_alt="Stairs and railings detailed during a turnover",
         blurb="For landlords and managers. One call between tenants: clear, clean, photograph, done."),
]
BY_SLUG = dict((s["slug"], s) for s in SERVICES)
RING = [s for s in SERVICES if s["ring"]][:8]

LOCATIONS = [
    dict(slug="property-services-north-york", area="North York",
         note="Willowdale, Don Mills, Bayview Village, Downsview and the Yonge corridor.",
         img="images/property-exterior.jpg", alt="Detached North York home with a clean driveway and lawn"),
    dict(slug="property-services-scarborough", area="Scarborough",
         note="Agincourt, Malvern, Guildwood, Birch Cliff and the Kingston Road strip.",
         img="images/t-driveway.jpg", alt="Freshly washed driveway outside a Scarborough home"),
    dict(slug="property-services-etobicoke", area="Etobicoke",
         note="Mimico, Humber Bay, Islington, Rexdale and The Kingsway.",
         img="images/t-highrise-windows.jpg", alt="Window cleaning in an Etobicoke lakeshore condo"),
    dict(slug="property-services-vaughan", area="Vaughan",
         note="Woodbridge, Maple, Thornhill, Concord and Kleinburg.",
         img="images/t-snow-removal.jpg", alt="Snow cleared from a Vaughan driveway"),
    dict(slug="property-services-markham", area="Markham",
         note="Unionville, Milliken, Cornell, Thornhill and Box Grove.",
         img="images/t-turnover.jpg", alt="Markham rental unit cleaned between tenants"),
]

# ----------------------------------------------------------------------
# Inline SVG icons
# ----------------------------------------------------------------------
SVG = dict(
    menu='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
    wa='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.52 3.48A11.78 11.78 0 0 0 12 0C5.37 0 0 5.37 0 12c0 2.11.55 4.17 1.6 5.99L0 24l6.2-1.63A11.95 11.95 0 0 0 12 24c6.63 0 12-5.37 12-12 0-3.2-1.25-6.21-3.48-8.52z"/></svg>',
    phone='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.8a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.35 1.84.59 2.8.72A2 2 0 0 1 22 16.92z"/></svg>',
    pin='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    clock='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    truck='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="6" width="13" height="10" rx="1"/><path d="M14 9h4l3 3v4h-7z"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
    spray='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="7" y="9" width="9" height="12" rx="2"/><path d="M10 9V5h4v4M14 3h4M18 3v3M18 7h-2"/></svg>',
    tag='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 12l-8 8-9-9V3h8z"/><circle cx="7.5" cy="7.5" r="1.5"/></svg>',
    chat='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-9 8.5 8.5 8.5 0 0 1-7.6-3.5L3 21l4.5-1.4A8.38 8.38 0 0 0 21 11.5z"/></svg>',
    check='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>',
    sun='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>',
    key='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="8" cy="15" r="5"/><path d="M11.5 11.5L21 2M18 5l2 2M15 8l2 2"/></svg>',
)


# ----------------------------------------------------------------------
# Partials
# ----------------------------------------------------------------------
def head(title, desc, canonical, depth=0, extra_ld="", og_type="website", og_image=None):
    up = "../" * depth
    img = og_image or "images/logo-og.jpg"
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#1F5C92" />
  <meta name="format-detection" content="telephone=yes" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-title" content="{NAME}" />
  <meta name="geo.region" content="CA-ON" />
  <meta name="geo.placename" content="Toronto, Ontario" />
  <meta name="geo.position" content="{LAT};{LON}" />
  <meta name="ICBM" content="{LAT}, {LON}" />
  <title>{TITLE}</title>
  <meta name="description" content="{DESC}" />
  <link rel="canonical" href="{CANON}" />
  <link rel="icon" href="{UP}images/favicon.svg" type="image/svg+xml" />

  <meta property="og:type" content="{OGTYPE}" />
  <meta property="og:site_name" content="{NAME}" />
  <meta property="og:title" content="{TITLE}" />
  <meta property="og:description" content="{DESC}" />
  <meta property="og:url" content="{CANON}" />
  <meta property="og:image" content="{BASE}/{IMG}" />
  <meta property="og:locale" content="en_CA" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{UP}css/theme.css?v=1">
{LD}</head>
<body>
""".format(NAME=NAME, TITLE=title, DESC=desc, CANON=canonical, UP=up, BASE=BASE,
           LAT=LAT, LON=LON, OGTYPE=og_type, LD=extra_ld, IMG=img)


def ld_business():
    return """  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": "{NAME}",
    "image": "{BASE}/images/logo-og.jpg",
    "logo": "{BASE}/images/logo.svg",
    "url": "{BASE}/",
    "telephone": "{PHONE}",
    "priceRange": "$$",
    "address": {{"@type":"PostalAddress","addressLocality":"Toronto","addressRegion":"ON","addressCountry":"CA"}},
    "geo": {{"@type":"GeoCoordinates","latitude":{LAT},"longitude":{LON}}},
    "areaServed": [
      {{"@type":"City","name":"Toronto"}},{{"@type":"City","name":"North York"}},
      {{"@type":"City","name":"Scarborough"}},{{"@type":"City","name":"Etobicoke"}},
      {{"@type":"City","name":"Vaughan"}},{{"@type":"City","name":"Markham"}}
    ],
    "openingHoursSpecification":[
      {{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"07:00","closes":"19:00"}},
      {{"@type":"OpeningHoursSpecification","dayOfWeek":["Saturday","Sunday"],"opens":"09:00","closes":"17:00"}}
    ],
    "hasMap":"{MAPS}",
    "sameAs":["{MAPS}"]
  }}
  </script>
""".format(NAME=NAME, BASE=BASE, PHONE=PHONE, LAT=LAT, LON=LON, MAPS=MAPS)


def ld_service(svc):
    return """  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Service","name":"{T}","serviceType":"{S}",
   "provider":{{"@type":"HomeAndConstructionBusiness","name":"{N}","telephone":"{P}","url":"{B}/"}},
   "areaServed":{{"@type":"City","name":"Toronto"}},
   "url":"{B}/{SL}.html"}}
  </script>
""".format(T=strip(svc["title"]), S=strip(svc["short"]), N=NAME, P=PHONE, B=BASE, SL=svc["slug"])


def ld_faq(pairs):
    items = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (strip(q), strip(a)) for q, a in pairs)
    return ('  <script type="application/ld+json">\n'
            '  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}\n'
            '  </script>\n' % items)


def ld_breadcrumb(trail):
    items = ['{"@type":"ListItem","position":1,"name":"Home","item":"%s/"}' % BASE]
    for i, (label, href) in enumerate(trail, start=2):
        items.append('{"@type":"ListItem","position":%d,"name":"%s","item":"%s/%s"}'
                     % (i, strip(label), BASE, href))
    return ('  <script type="application/ld+json">\n'
            '  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}\n'
            '  </script>\n' % ",".join(items))


def strip(text):
    """Plain text for JSON-LD and alt attributes."""
    return (text.replace("&amp;", "and").replace("&middot;", "-")
                .replace("&rsaquo;", ">").replace('"', "'"))


def topbar(depth=0):
    up = "../" * depth
    return """    <header class="osw-bar">
      <div class="osw-bar-left">
        <a class="glass-chip" href="{UP}services.html">{MENU} Services</a>
        <a class="glass-chip" href="{UP}pricing.html">Pricing</a>
        <a class="glass-chip" href="{UP}contact.html">Contact</a>
      </div>

      <div class="osw-logo">{NAME}<small>{TAGLINE}</small></div>

      <div class="osw-bar-right">
        <a class="glass-chip" href="{WA}" target="_blank" rel="noopener">{WAICON} WhatsApp</a>
        <a class="glass-icon-btn" href="tel:{TEL}" aria-label="Call {NAMEP}">{PHONEICON}</a>
        <span class="osw-avatar"><img src="{UP}images/logo.svg" alt="{NAMEP} logo"></span>
      </div>
    </header>
""".format(UP=up, MENU=SVG["menu"], NAME=NAME, NAMEP=strip(NAME), TAGLINE=TAGLINE,
           WA=WA_GENERAL, WAICON=SVG["wa"], TEL=PHONE_TEL, PHONEICON=SVG["phone"])


def crumbs(trail, depth=0):
    up = "../" * depth
    parts = ['<a href="%sindex.html">Home</a>' % up]
    for label, href in trail[:-1]:
        parts.append('<a href="%s%s">%s</a>' % (up, href, label))
    parts.append("<span>%s</span>" % trail[-1][0])
    return '    <nav class="crumbs" aria-label="Breadcrumb">%s</nav>\n' % " &rsaquo; ".join(parts)


def btns(depth=0, quote_label="Free Quote on WhatsApp"):
    up = "../" * depth
    return ('<a class="btn btn-whatsapp" href="%s" target="_blank" rel="noopener">%s %s</a>'
            '<a class="btn btn-gold" href="%scontact.html">Book a Visit</a>'
            '<a class="btn btn-glass" href="tel:%s">Call %s</a>'
            % (WA_QUOTE, SVG["wa"], quote_label, up, PHONE_TEL, PHONE))


def hero_media(depth=0, media=None, alt=""):
    """The floating 9:16 panel in a hero. Defaults to the walkthrough video."""
    up = "../" * depth
    if media is None:
        return """          <video muted loop playsinline autoplay poster="{UP}videos/hero-poster.jpg" preload="metadata" aria-label="Walkthrough of a Toronto home before and after a Sunshine clean">
            <source src="{UP}videos/hero.mp4" type="video/mp4">
            <img src="{UP}videos/hero-poster.jpg" alt="Walkthrough of a Toronto home before and after a Sunshine clean" />
          </video>""".format(UP=up)
    return '          <img src="%s%s" alt="%s" />' % (up, media, alt)


def hero_small(depth, trail, h1, glow, sub, media=None, alt="", buttons=None):
    return """  <section class="osw osw-small">
    <div class="osw-arch"><span></span><span></span><span></span><span></span><span></span></div>
{TOPBAR}{CRUMBS}
    <div class="osw-stage">
      <div class="osw-scene">
        <div class="osw-product-aura"></div>
        <div class="osw-product-aura cool"></div>
        <div class="osw-product">
{MEDIA}
        </div>
      </div>
    </div>

    <div class="osw-title">
      <h1>{H1} <span class="glow">{GLOW}</span></h1>
      <p class="sub">{SUB}</p>
      <div class="btn-row" style="margin-top:1.4rem;">{BTNS}</div>
    </div>
  </section>
""".format(TOPBAR=topbar(depth), CRUMBS=crumbs(trail, depth),
           MEDIA=hero_media(depth, media, alt), H1=h1, GLOW=glow, SUB=sub,
           BTNS=buttons if buttons is not None else btns(depth))


def photo_strip(depth, items, wide=False):
    """A plain row of pictures, each with its caption printed underneath."""
    up = "../" * depth
    cls = "photo-card wide" if wide else "photo-card"
    cards = "".join(
        '<figure class="%s"><img src="%s%s" alt="%s" loading="lazy"><span>%s</span></figure>'
        % (cls, up, src, alt, cap) for src, alt, cap in items)
    return '<div class="photo-strip">%s</div>' % cards


def service_tiles(depth, services):
    up = "../" * depth
    out = []
    for s in services:
        out.append("""        <article class="service-tile">
          <div class="service-tile-media"><img src="{UP}{IMG}" alt="{ALT}" loading="lazy"></div>
          <div class="service-tile-body">
            <h3>{SHORT}</h3>
            <p>{BLURB}</p>
            <div class="row"><a href="{UP}{SLUG}.html">Learn more &rarr;</a><a class="btn btn-gold" style="padding:.5rem .9rem; font-size:.8rem;" href="{WA}" target="_blank" rel="noopener">Quote</a></div>
          </div>
        </article>""".format(UP=up, IMG=s["img"], ALT=s["alt"], SHORT=s["short"],
                             BLURB=s["blurb"], SLUG=s["slug"],
                             WA=wa("I'd like a quote for " + strip(s["short"]).lower() + ". Here's the property:")))
    return "\n".join(out)


def wa_mock(depth=0, lines=None):
    up = "../" * depth
    lines = lines or [
        ("out", "m1", "Hi, can you do a move out clean on Friday?", "9:12"),
        ("in", "m2", "Yes. Send the address and size and I'll quote it.", "9:12"),
        ("out", "m3", "2 bed condo, Scarborough. Keys at 9.", "9:13"),
    ]
    bubbles = []
    for i, (side, cls, text, time) in enumerate(lines):
        if i == 1:
            bubbles.append('<div class="wa-typing"><span></span><span></span><span></span></div>')
        bubbles.append('<div class="wa-bub %s %s">%s<span class="t">%s</span></div>' % (side, cls, text, time))
    return """<div class="wa-mock" aria-label="Animated WhatsApp quote conversation">
                <div class="wa-mock-head">
                  <span class="wa-mock-av"><img src="{UP}images/logo.svg" alt=""></span>
                  <span class="wa-mock-name">{NAME}<small>online</small></span>
                  <span class="wa-ico">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>
                    {PHONEICON}
                  </span>
                </div>
                <div class="wa-mock-body">{BUBBLES}</div>
                <div class="wa-mock-foot">
                  <span class="field">Message</span>
                  <span class="send"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 21l21-9L2 3v7l15 2-15 2v7z"/></svg></span>
                </div>
              </div>""".format(UP=up, NAME=NAME, PHONEICON=SVG["phone"], BUBBLES="".join(bubbles))


def cta_strip(depth=0, heading="Ready for a clean you don't have to redo?",
              sub="Send a few photos on WhatsApp and get a price back the same day, or call and we'll sort it out in a minute."):
    up = "../" * depth
    return """  <section class="section">
    <div class="container">
      <div class="cta-strip">
        <h2>{HEAD}</h2>
        <p>{SUB}</p>

        <div class="cta-demos">
          <div class="demo-wrap">
            <div class="demo">
              {WAMOCK}
            </div>
            <div class="demo-cap">&#128172; Photo quote on WhatsApp</div>
          </div>

          <div class="demo-wrap">
            <div class="demo bk" aria-label="Animated booking of a cleaning visit">
              <div class="bk-head"><span class="bk-dot"></span> Pick a visit window <span class="bk-when">This week</span></div>
              <div class="bk-dates">
                <span class="d">M</span><span class="d">T</span><span class="d">W</span><span class="d">T</span><span class="d">F</span>
                <span class="bk-pick"></span>
              </div>
              <div class="bk-slots">
                <span class="slot">8:00</span><span class="slot s2">1:00 PM</span><span class="slot">4:30</span>
              </div>
              <div class="bk-confirm"><span class="chk">&#10003;</span> Visit booked!</div>
            </div>
            <div class="demo-cap">&#128197; Early starts, 7 days</div>
          </div>

          <div class="demo-wrap">
            <div class="demo call" aria-label="Animated phone call">
              <div class="call-avwrap">
                <span class="ring"></span><span class="ring"></span><span class="ring"></span>
                <div class="call-av"><img src="{UP}images/logo.svg" alt=""></div>
              </div>
              <div class="call-name">{NAME}</div>
              <div class="call-status">calling<i></i><i></i><i></i></div>
              <div class="call-actions">
                <span class="cbtn decline"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24 11.36 11.36 0 0 0 3.57.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.36 11.36 0 0 0 .57 3.57 1 1 0 0 1-.24 1.02l-2.2 2.2z"/></svg></span>
                <span class="cbtn accept"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24 11.36 11.36 0 0 0 3.57.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.36 11.36 0 0 0 .57 3.57 1 1 0 0 1-.24 1.02l-2.2 2.2z"/></svg></span>
              </div>
            </div>
            <div class="demo-cap">&#128222; Call {PHONE}</div>
          </div>
        </div>

        <div class="btn-row">
          <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">Get a Free Quote</a>
          <a class="btn btn-gold" href="{UP}contact.html">Book a Visit</a>
          <a class="btn btn-glass" href="tel:{TEL}">Call Now</a>
        </div>
      </div>
    </div>
  </section>
""".format(UP=up, HEAD=heading, SUB=sub, WAMOCK=wa_mock(depth), NAME=NAME,
           PHONE=PHONE, WA=WA_QUOTE, TEL=PHONE_TEL)


def footer(depth=0):
    up = "../" * depth
    svc = "".join('<li><a href="%s%s.html">%s</a></li>' % (up, s["slug"], s["short"])
                  for s in SERVICES[:7])
    loc = "".join('<li><a href="%s%s.html">%s</a></li>' % (up, l["slug"], l["area"])
                  for l in LOCATIONS)
    return """  <footer class="foot">
    <div class="foot-grid">
      <div class="foot-brand">
        <div class="osw-logo" style="text-align:left;">{NAME}<small>{TAGLINE}</small></div>
        <p style="margin-top:1rem;">Cleaning, cleanouts and seasonal property care across {AREA}. One crew you can call for the inside and the outside.</p>
        <div class="foot-contact" style="margin-top:1rem;">
          <div>{PIN} Serving {AREA}</div>
          <div>{PHONEICON} <a href="tel:{TEL}">{PHONE}</a></div>
          <div>{CLOCK} {HOURS}</div>
        </div>
      </div>
      <div><h4>Services</h4><ul>{SVC}<li><a href="{UP}services.html">All Services</a></li></ul></div>
      <div><h4>Service Areas</h4><ul>{LOC}<li><a href="{MAPS}" target="_blank" rel="noopener">Google Profile</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="{UP}about.html">About</a></li><li><a href="{UP}pricing.html">Pricing</a></li><li><a href="{UP}reviews.html">Reviews</a></li><li><a href="{UP}blog/index.html">Blog</a></li><li><a href="{UP}contact.html">Contact</a></li></ul></div>
    </div>
    <div class="foot-bottom">&copy; <span id="yr">2026</span> {NAME} &middot; {AREA} &middot; <a href="tel:{TEL}">{PHONE}</a> &middot; <a href="{UP}privacy.html">Privacy</a> &middot; <a href="{UP}terms.html">Terms</a></div>
  </footer>

  <a class="float-wa" href="{WA}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp">{WAICON}</a>
  <div class="mobile-cta">
    <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
    <a class="btn btn-primary" href="tel:{TEL}">Call</a>
    <a class="btn btn-gold" href="{UP}contact.html">Free Quote</a>
  </div>

  <script src="{UP}js/main.js?v=1"></script>
  <script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
</body>
</html>
""".format(NAME=NAME, TAGLINE=TAGLINE, AREA=AREA, PIN=SVG["pin"], PHONEICON=SVG["phone"],
           TEL=PHONE_TEL, PHONE=PHONE, CLOCK=SVG["clock"], HOURS=HOURS_SHORT,
           SVC=svc, LOC=loc, UP=up, MAPS=MAPS, WA=WA_GENERAL, WAICON=SVG["wa"])


def sidebar(depth=0, photo=None, photo_alt="", photo_cap="", extra=""):
    up = "../" * depth
    svc = "".join('<li><a href="%s%s.html">%s</a></li>' % (up, s["slug"], s["short"]) for s in SERVICES)
    pic = ""
    if photo:
        pic = """        <div class="glass-card">
          <img src="{UP}{IMG}" alt="{ALT}" loading="lazy">
          <h3>{CAP}</h3>
          <p>Every visit finishes the same way: we walk the space with you before we pack up.</p>
        </div>
""".format(UP=up, IMG=photo, ALT=photo_alt, CAP=photo_cap)
    return """      <aside class="sidebar">
        <div class="glass-card">
          <h3>Free quote, no pressure</h3>
          <p>Send a few photos on WhatsApp and you'll get a price back. If it works, we book a window. If it doesn't, nothing lost.</p>
          <div class="btn-row" style="margin-top:1rem;">
            <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">WhatsApp Photos</a>
            <a class="btn btn-glass" href="tel:{TEL}">Call {PHONE}</a>
          </div>
        </div>
{PIC}
        <div class="glass-card">
          <h3>Hours &amp; coverage</h3>
          <div class="info-row">{CLOCK}<div><strong>Mon to Fri</strong><br>7:00am to 7:00pm</div></div>
          <div class="info-row">{CLOCK}<div><strong>Sat and Sun</strong><br>9:00am to 5:00pm</div></div>
          <div class="info-row">{PIN}<div><strong>Service area</strong><br>{AREA}</div></div>
          <div class="info-row">{TRUCK}<div><strong>Short notice</strong><br>Same week slots are common. Call early.</div></div>
        </div>

        <div class="glass-card">
          <h3>All services</h3>
          <ul>{SVC}</ul>
        </div>
{EXTRA}      </aside>
""".format(WA=WA_QUOTE, TEL=PHONE_TEL, PHONE=PHONE, CLOCK=SVG["clock"], PIN=SVG["pin"],
           AREA=AREA, TRUCK=SVG["truck"], SVC=svc, EXTRA=extra, PIC=pic)


def faq_block(pairs):
    items = []
    for q, a in pairs:
        items.append('<div class="faq-item"><button class="faq-q">%s<span class="arrow">+</span></button>'
                     '<div class="faq-a"><p>%s</p></div></div>' % (q, a))
    return '<div class="faq-list">%s</div>' % "".join(items)


def write(relpath, html):
    path = os.path.join(ROOT, relpath.replace("/", os.sep))
    folder = os.path.dirname(path)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder)
    io.open(path, "w", encoding="utf-8", newline="\n").write(html)
    return relpath
