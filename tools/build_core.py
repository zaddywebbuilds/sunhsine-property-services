# -*- coding: utf-8 -*-
"""Builds the core pages: home, services, pricing, about, contact, reviews, legal."""

from common import *  # noqa: F401,F403
from common import (NAME, TAGLINE, PHONE, PHONE_TEL, AREA, BASE, MAPS, SVG, SERVICES,
                    RING, LOCATIONS, WA_QUOTE, WA_GENERAL, wa, head, ld_business, ld_faq,
                    ld_breadcrumb, topbar, crumbs, btns, hero_small, photo_strip,
                    service_tiles, wa_mock, cta_strip, footer, sidebar, faq_block,
                    write, strip, HOURS_SHORT)

BUILT = []


def page(path, html):
    BUILT.append(write(path, html))


# ======================================================================
# HOME
# ======================================================================
HOME_FAQ = [
    ("Do you bring your own supplies and equipment?",
     "Yes. Vacuums, cloths, mops and products all come with the crew. If you'd rather we used your products, for a scent or a surface you're particular about, just leave them out and say the word."),
    ("How do I get a price?",
     "Send photos of the space on WhatsApp, or call and describe it. You get a quote before anyone shows up, and the price is agreed before we start work."),
    ("Can you come on short notice?",
     "Often yes. We start at 7am on weekdays and work weekends, so same week slots are common. Call early in the day for the best chance of a same-day visit."),
    ("Do I need to be home?",
     "No. Plenty of clients leave a key, a lockbox code or a concierge instruction. We lock up and message you when the job is done."),
    ("What areas do you cover?",
     "Toronto and the surrounding GTA, including North York, Scarborough, Etobicoke, Vaughan and Markham."),
    ("Is it the same crew each time?",
     "For recurring cleans we keep the same people on your property wherever we can. They learn the quirks of the place, and you stop having to explain them."),
]

ring_cards = []
for i, s in enumerate(RING, start=1):
    ring_cards.append(
        '<div class="svc-item p%d"><a class="svc-card" href="%s.html">'
        '<img src="%s" alt="%s" loading="lazy">'
        '<span class="svc-card-label">%s</span></a></div>'
        % (i, s["slug"], s["img"], s["alt"], s["short"]))

home = head(
    title="Property Cleaning &amp; Junk Removal in Toronto | " + NAME,
    desc=("Sunshine Property Services cleans and clears Toronto properties. House and deep cleaning, "
          "move out and turnovers, offices, post construction, windows, pressure washing, junk removal "
          "and snow. Free quotes, 7 days a week."),
    canonical=BASE + "/",
    extra_ld=ld_business() + ld_faq(HOME_FAQ),
) + """
  <!-- ============================================================
       OS WINDOW hero
       ============================================================ -->
  <section class="osw">
    <div class="osw-arch"><span></span><span></span><span></span><span></span><span></span></div>

{TOPBAR}
    <div class="osw-stage osw-stage-home">

      <div class="osw-scene osw-scene-left">
        <div class="osw-product-aura"></div>
        <div class="osw-product-aura cool"></div>
        <div class="osw-product">
          <video muted loop playsinline autoplay poster="videos/hero-poster.jpg" preload="metadata" aria-label="Walkthrough of a Toronto home before and after a Sunshine clean">
            <source src="videos/hero.mp4" type="video/mp4">
            <img src="videos/hero-poster.jpg" alt="Walkthrough of a Toronto home before and after a Sunshine clean" />
          </video>
        </div>
      </div>

      <div class="osw-scene">
        <div class="svc-ring" aria-label="What Sunshine Property Services does">
          <div class="svc-ring-rotor">
            {RING}
          </div>
          <div class="svc-ring-center">
            <span class="crown">&#9728;</span>
            <strong>SUNSHINE</strong>
            <small>Property Services</small>
          </div>
        </div>
      </div>
    </div>

    <div class="osw-title">
      <h1>Toronto <span class="glow">PROPERTY CARE</span></h1>
      <p class="sub">One crew for the whole property. Cleaning that holds up, cleanouts that actually finish, and the outside jobs nobody wants to do. Free quote by photo, seven days a week.</p>
      <div class="btn-row" style="margin-top: 1.5rem;">
        <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WAICON} Free Quote on WhatsApp</a>
        <a class="btn btn-primary" href="contact.html">Book a Visit</a>
        <a class="btn btn-glass" href="tel:{TEL}">Call {PHONE}</a>
      </div>
    </div>
  </section>

  <!-- ============================================================
       WHY SUNSHINE
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Why Sunshine</span>
        <h2>The property looked after, not just tidied</h2>
        <p>Cleaning companies disappear when the job gets awkward. Awkward is most of what property owners actually need: the empty unit, the dusty reno, the garage, the driveway in February.</p>
      </div>
      <div class="why-grid">
        <div class="why-card">
          <div class="why-media">
            <img src="images/residential-cleaning.jpg" alt="Cleaner vacuuming a bright Toronto living room" loading="lazy">
            <span class="icon sun">{SPRAY}</span>
          </div>
          <div class="why-body">
            <h3>Inside and Outside</h3>
            <p>Kitchens, bathrooms and floors, plus windows, driveways, cleanouts and snow. One number covers the lot.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            <img src="images/move-out-cleaning.jpg" alt="Empty Toronto apartment cleaned before handover" loading="lazy">
            <span class="icon steel">{KEY}</span>
          </div>
          <div class="why-body">
            <h3>Built for Handovers</h3>
            <p>Move outs, tenant turnovers and listing prep, done to the standard a walkthrough is judged by.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            <img src="images/post-reno-cleanup.jpg" alt="Construction dust vacuumed after a Toronto renovation" loading="lazy">
            <span class="icon gold">{CHECK}</span>
          </div>
          <div class="why-body">
            <h3>Price Agreed First</h3>
            <p>You get a quote from photos before anyone arrives. No hourly surprises at the door.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            {WAMOCK}
            <span class="icon slate">{CHAT}</span>
          </div>
          <div class="why-body">
            <h3>Quote by WhatsApp</h3>
            <p>Photos in, price out. Most quotes come back the same day, often within the hour.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       Two feature tiles: media on top, words underneath
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">A look at the work</span>
        <h2>Before the visit, and after it</h2>
      </div>
      <div class="grid grid-2">
        <a class="bx-tile" href="{WA}" target="_blank" rel="noopener">
          <div class="bx-media">
            <video muted loop playsinline autoplay poster="videos/hero-poster.jpg" preload="metadata"><source src="videos/hero.mp4" type="video/mp4"></video>
            <div class="bx-play"><svg viewBox="0 0 24 24" fill="currentColor"><polygon points="6 4 20 12 6 20"/></svg></div>
          </div>
          <h3>GET A QUOTE <span class="arrow">&#8599;</span></h3>
          <p>Send photos of the space on WhatsApp and get a price back today.</p>
        </a>
        <a class="bx-tile" href="services.html">
          <div class="bx-media">
            <img class="bg" src="images/office-cleaning.jpg" alt="Office being cleaned in downtown Toronto" loading="lazy">
          </div>
          <h3>SERVICES <span class="arrow">&#8599;</span></h3>
          <p>House and deep cleans, turnovers, offices, post construction, windows, washing, junk, snow.</p>
        </a>
      </div>
    </div>
  </section>

  <!-- ============================================================
       SERVICES grid
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Services</span>
        <h2>What we do across {AREA}</h2>
        <p>Pick the one you need, or ask for a few at once. Most properties book two or three together and save a trip.</p>
      </div>
      <div class="grid grid-3">
{TILES}
      </div>
      <div style="text-align:center; margin-top:2rem;"><a class="btn btn-glass" href="services.html">See all services</a></div>
    </div>
  </section>

  <!-- ============================================================
       Gallery
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">The detail</span>
        <h2>Where the time actually goes</h2>
        <p>Anyone can run a vacuum down the middle of a room. The difference shows in the edges, the glass, the grout and the parts of a property people stop noticing until they are wrong.</p>
      </div>
      {STRIP}
    </div>
  </section>

  <!-- ============================================================
       What you can count on
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Our standards</span>
        <h2>What you can count on</h2>
        <p>Plain commitments, no fine print.</p>
      </div>
      <div class="grid grid-3">
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av a">1</span><span class="rev-name"><strong>A price before we start</strong><small>No hourly creep</small></span></div>
          <p class="quote">You approve the quote first. If we find more than the photos showed, we tell you and agree the change before carrying on.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av b">2</span><span class="rev-name"><strong>We finish the job</strong><small>Including the awkward part</small></span></div>
          <p class="quote">Behind the fridge, the top of the frames, the balcony glass. We'd rather stay the extra twenty minutes than leave it obvious.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av c">3</span><span class="rev-name"><strong>Walk it with us</strong><small>Before we pack up</small></span></div>
          <p class="quote">If you're on site, we walk the space together at the end. If you're not, you get photos. Anything missed gets put right.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av d">4</span><span class="rev-name"><strong>Early starts, seven days</strong><small>7am weekdays</small></span></div>
          <p class="quote">Trades at nine, cleaners at seven. We work around handover times, listing photos and tenant moves.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av e">5</span><span class="rev-name"><strong>Careful in an empty home</strong><small>Keys, codes, concierge</small></span></div>
          <p class="quote">Plenty of our work happens with nobody there. We lock up, report in and leave the place exactly as we found it, minus the mess.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av a">6</span><span class="rev-name"><strong>Donate and recycle first</strong><small>On cleanouts</small></span></div>
          <p class="quote">Usable furniture and goods go to a charity or a reuse centre where we can. Metal and electronics go to recycling, not landfill.</p>
        </div>
      </div>
      <div style="text-align:center; margin-top:2rem;"><a class="btn btn-glass" href="reviews.html">Reviews &amp; feedback</a></div>
    </div>
  </section>

  <!-- ============================================================
       FAQ
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">FAQ</span>
        <h2>Frequently asked questions</h2>
      </div>
      <div class="faq-layout">
        <div class="faq-deco">
          <div class="deco-media"><img src="images/bathroom-cleaning.jpg" alt="Shower glass being cleaned in a Toronto bathroom" loading="lazy"></div>
          <div class="deco-tag"><span class="dot"></span>Glass, tile and grout</div>
        </div>

        {FAQ}

        <div class="faq-deco">
          <div class="deco-media"><img src="images/window-cleaning.jpg" alt="Interior window being cleaned in a Toronto home" loading="lazy"></div>
          <div class="deco-tag"><span class="dot"></span>Windows, frames and tracks</div>
        </div>
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    TOPBAR=topbar(0), RING="\n            ".join(ring_cards), WA=WA_QUOTE,
    WAICON=SVG["wa"], TEL=PHONE_TEL, PHONE=PHONE, SPRAY=SVG["spray"], KEY=SVG["key"],
    CHECK=SVG["check"], CHAT=SVG["chat"], WAMOCK=wa_mock(0), AREA=AREA,
    TILES=service_tiles(0, [s for s in SERVICES if s["slug"] != "property-turnover-toronto"]),
    STRIP=photo_strip(0, [
        ("images/t-kitchen-detail.jpg", "Kitchen counter and backsplash detail", "Kitchen surfaces"),
        ("images/t-bathroom-detail.jpg", "Shower screen and tile detail", "Showers and tile"),
        ("images/t-floor-care.jpg", "Living room floor care", "Floors and carpet"),
        ("images/t-staircase.jpg", "Staircase and handrail cleaned", "Stairs and railings"),
        ("images/t-highrise-windows.jpg", "High rise window cleaning in Toronto", "Glass and balconies"),
        ("images/t-commercial-floor.jpg", "Commercial floor care in an office", "Commercial floors"),
        ("images/t-driveway.jpg", "Washed driveway outside a Toronto home", "Driveways and walkways"),
        ("images/t-snow-removal.jpg", "Snow cleared from a Toronto driveway", "Winter clearing"),
    ]),
    FAQ=faq_block(HOME_FAQ), CTA=cta_strip(0), FOOT=footer(0))

page("index.html", home)


# ======================================================================
# SERVICES
# ======================================================================
services_page = head(
    title="Cleaning &amp; Property Services in Toronto | " + NAME,
    desc=("Every service from Sunshine Property Services: house cleaning, deep cleaning, move out and "
          "turnovers, office cleaning, post construction cleanup, windows, pressure washing, junk removal "
          "and snow clearing across Toronto."),
    canonical=BASE + "/services.html",
    extra_ld=ld_breadcrumb([("Services", "services.html")]),
) + hero_small(
    0, [("Services", "services.html")],
    "Everything We", "LOOK AFTER",
    "Ten services, one crew, one invoice. Most properties book two or three at a time: a deep clean with the windows, a turnover with a cleanout, a wash with the driveway.",
    media="images/property-exterior.jpg",
    alt="Well kept Toronto home exterior with a clean driveway",
) + """
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Inside the property</span>
        <h2>Cleaning services</h2>
        <p>Recurring or one off, occupied or empty.</p>
      </div>
      <div class="grid grid-3">
{INSIDE}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Outside and in between</span>
        <h2>Property services</h2>
        <p>The jobs that keep a building looking cared for from the street.</p>
      </div>
      <div class="grid grid-2">
{OUTSIDE}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Bundles</span>
        <h2>What people usually book together</h2>
      </div>
      <div class="grid grid-3">
        <div class="glass-card">
          <h3>The handover</h3>
          <p>Move out clean, interior windows and a small cleanout. Everything a walkthrough or a listing photo picks up on.</p>
          <p><a href="move-out-cleaning-toronto.html">Move out cleaning &rarr;</a></p>
        </div>
        <div class="glass-card">
          <h3>The reset</h3>
          <p>Deep clean inside, pressure wash the driveway and entrance outside. Usually booked in spring or before guests arrive.</p>
          <p><a href="deep-cleaning-toronto.html">Deep cleaning &rarr;</a></p>
        </div>
        <div class="glass-card">
          <h3>After the trades</h3>
          <p>Post construction cleanup with debris removal and a window pass, so the finished work is actually visible.</p>
          <p><a href="post-construction-cleaning-toronto.html">Post construction &rarr;</a></p>
        </div>
      </div>
      {STRIP}
    </div>
  </section>

{CTA}{FOOT}""".format(
    INSIDE=service_tiles(0, [s for s in SERVICES if s["slug"] in (
        "house-cleaning-toronto", "deep-cleaning-toronto", "move-out-cleaning-toronto",
        "commercial-cleaning-toronto", "post-construction-cleaning-toronto",
        "property-turnover-toronto")]),
    OUTSIDE=service_tiles(0, [s for s in SERVICES if s["slug"] in (
        "window-cleaning-toronto", "pressure-washing-toronto", "junk-removal-toronto",
        "snow-removal-toronto")]),
    STRIP=photo_strip(0, [
        ("images/t-turnover.jpg", "Vacant unit ready for the next tenant", "Turnovers"),
        ("images/t-power-washing.jpg", "Pressure washing a house exterior", "Exterior washing"),
        ("images/t-highrise-windows.jpg", "High rise window cleaning", "High glass"),
        ("images/t-commercial-floor.jpg", "Office floor care", "Office floors"),
    ]),
    CTA=cta_strip(0), FOOT=footer(0))

page("services.html", services_page)


# ======================================================================
# PRICING
# ======================================================================
PRICING_FAQ = [
    ("Why are there no prices listed on this page?",
     "Because an honest number needs two minutes of information. A three bedroom semi with pets is not the same job as a three bedroom semi that was cleaned last week. Send photos and you get a real figure, not a starting-from price that changes at the door."),
    ("How fast do quotes come back?",
     "Usually the same day, often within the hour during working hours. Weekends included."),
    ("Is the quote fixed?",
     "The quote holds for the work described. If we arrive and the job is clearly bigger than the photos showed, we stop, show you, and agree the difference before carrying on. We never add to an invoice after the fact."),
    ("Do you charge by the hour or by the job?",
     "By the job for most cleaning and cleanout work, so you know the cost in advance. Ongoing maintenance and seasonal contracts are usually priced per visit."),
    ("What affects the price most?",
     "Size of the space, how long since the last clean, whether the property is occupied or empty, access and parking, and how much needs removing."),
    ("How do I pay?",
     "Payment is arranged directly with the business when the work is booked. Ask when you get your quote and we'll confirm what is accepted."),
]

pricing = head(
    title="Pricing &amp; Free Quotes | " + NAME + " Toronto",
    desc=("How Sunshine Property Services prices cleaning and property work in Toronto. Free photo quotes, "
          "price agreed before we start, no hourly surprises."),
    canonical=BASE + "/pricing.html",
    extra_ld=ld_breadcrumb([("Pricing", "pricing.html")]) + ld_faq(PRICING_FAQ),
) + hero_small(
    0, [("Pricing", "pricing.html")],
    "Know the Price", "BEFORE WE START",
    "Send photos, get a figure, decide. Nothing begins until you have agreed a number, and that number does not move unless the job does.",
    media="images/kitchen-deep-clean.jpg",
    alt="Cleaner wiping down a kitchen island in a Toronto home",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>How a quote works</h2>
          <p>Three steps, and the first two cost you nothing.</p>

          <div class="grid grid-3" style="margin:1.5rem 0;">
            <div class="glass-card">
              <h3>1. Show us</h3>
              <p>Photos on WhatsApp, or a quick description on the phone. Rooms, rough size, and anything unusual.</p>
            </div>
            <div class="glass-card">
              <h3>2. Get a number</h3>
              <p>A price for the work as described, with what is included spelled out. Same day, usually within the hour.</p>
            </div>
            <div class="glass-card">
              <h3>3. Pick a window</h3>
              <p>Choose a day and a start time. From 7am on weekdays, 9am weekends.</p>
            </div>
          </div>

          <h2>What a price is built from</h2>
          <p>Every quote comes down to the same handful of things. Knowing them helps you tell whether any quote, ours or anyone else's, is reasonable.</p>
          <ul>
            <li><strong>Size and layout.</strong> Square footage, number of bathrooms, number of floors and whether there are stairs.</li>
            <li><strong>Condition.</strong> A maintained home and a home that has not been cleaned in a year are different jobs, and pretending otherwise is how surprise invoices happen.</li>
            <li><strong>Occupied or empty.</strong> Empty units clean faster but get judged harder, because there is no furniture hiding anything.</li>
            <li><strong>Scope.</strong> Inside the oven, inside the fridge, inside cabinets, windows, balcony glass: each one adds time, so each one is priced, not assumed.</li>
            <li><strong>Access.</strong> Elevator bookings, loading docks, parking and walk-up distance all cost time on cleanouts and removals.</li>
            <li><strong>Volume.</strong> On junk removal and cleanouts, price follows how much goes in the truck and what it costs to dispose of properly.</li>
          </ul>

          <h2>Recurring work costs less per visit</h2>
          <p>A property cleaned every two weeks never gets far from clean, so each visit takes less time. Weekly, biweekly and monthly schedules are priced per visit and come in under a comparable one off clean. Commercial and landlord accounts with several properties are quoted as a block.</p>

          <figure class="media-figure">
            <img src="images/office-cleaning.jpg" alt="Office desks being cleaned in a downtown Toronto workspace" loading="lazy">
            <figcaption>Office and commercial work is usually quoted per visit on a fixed schedule, after hours or before opening.</figcaption>
          </figure>

          <h2>Questions about pricing</h2>
          {FAQ}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(FAQ=faq_block(PRICING_FAQ),
                      SIDEBAR=sidebar(0, photo="images/t-turnover.jpg",
                                      photo_alt="Vacant Toronto unit cleaned and ready for handover",
                                      photo_cap="Quoted, cleaned, handed over"),
                      CTA=cta_strip(0), FOOT=footer(0))

page("pricing.html", pricing)


# ======================================================================
# ABOUT
# ======================================================================
about = head(
    title="About " + NAME + " | Toronto Property Care",
    desc=("Who we are: a Toronto property services crew handling cleaning, turnovers, cleanouts, windows, "
          "washing and winter work across the GTA, seven days a week."),
    canonical=BASE + "/about.html",
    extra_ld=ld_breadcrumb([("About", "about.html")]),
) + hero_small(
    0, [("About", "about.html")],
    "A Local Crew for", "THE WHOLE PROPERTY",
    "Sunshine Property Services looks after homes, rentals and small commercial spaces across Toronto and the GTA. Cleaning, cleanouts and seasonal work, from one number.",
    media="images/property-exterior.jpg",
    alt="Well kept Toronto home with a clean driveway and trimmed lawn",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Why one crew for everything</h2>
          <p>Most property owners end up with a list of numbers: someone for cleaning, someone else for the windows, a third for hauling away the old couch, a fourth when it snows. Every one of them needs chasing, scheduling and explaining the property to.</p>
          <p>Sunshine exists to shorten that list. The same people who clean the kitchen will clear the garage, wash the driveway and come back in January with a shovel. They already know where the parking is, which door sticks and where the water shut off lives.</p>

          <figure class="media-figure">
            <img src="images/residential-cleaning.jpg" alt="Cleaner working through a bright Toronto living room" loading="lazy">
            <figcaption>Regular visits mean the same crew, who learn the property instead of starting from scratch each time.</figcaption>
          </figure>

          <h2>Who we work for</h2>
          <ul>
            <li><strong>Homeowners</strong> who want a standing clean and someone reliable for the seasonal jobs.</li>
            <li><strong>Landlords and property managers</strong> who need units turned around fast between tenants, with photos to prove it.</li>
            <li><strong>Realtors</strong> getting a property camera ready before listing day.</li>
            <li><strong>Renovators and builders</strong> who need the dust gone before the client walks in.</li>
            <li><strong>Small offices, clinics and studios</strong> that need cleaning around their opening hours, not during them.</li>
          </ul>

          <h2>How we work</h2>
          <p>Quote first, always in writing, always before anyone arrives. We bring our own equipment and products. We start early, because 7am on a weekday is when empty properties are easiest to work in. We finish by walking the space, in person if you are there and by photo if you are not.</p>
          <p>On cleanouts, anything still usable goes to a charity or reuse centre where we can find one, and metal and electronics go to recycling. It costs us a detour and saves the landfill a load.</p>

          <h2>Where we work</h2>
          <p>Toronto proper, plus North York, Scarborough, Etobicoke, Vaughan and Markham. If you are just outside that ring, ask anyway. We travel for the right job.</p>
          {STRIP}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    STRIP=photo_strip(0, [
        ("images/t-driveway.jpg", "Driveway washed outside a Toronto home", "North York"),
        ("images/t-highrise-windows.jpg", "Condo window cleaning above the Toronto skyline", "Etobicoke"),
        ("images/t-commercial-floor.jpg", "Office floor care in Toronto", "Downtown"),
        ("images/t-snow-removal.jpg", "Snow clearing from a GTA driveway", "Vaughan"),
    ]),
    SIDEBAR=sidebar(0, photo="images/t-staircase.jpg",
                    photo_alt="Staircase and handrail cleaned during a property visit",
                    photo_cap="The parts people touch"),
    CTA=cta_strip(0), FOOT=footer(0))

page("about.html", about)


# ======================================================================
# CONTACT
# ======================================================================
contact = head(
    title="Contact &amp; Free Quote | " + NAME + " Toronto",
    desc=("Get a free quote from Sunshine Property Services. WhatsApp " + PHONE +
          " with photos, or call. Open 7am to 7pm weekdays, 9am to 5pm weekends."),
    canonical=BASE + "/contact.html",
    extra_ld=ld_breadcrumb([("Contact", "contact.html")]),
) + hero_small(
    0, [("Contact", "contact.html")],
    "Tell Us What", "NEEDS DOING",
    "Photos are the fastest route to a real price. Send them on WhatsApp and you will usually have a number back within the hour.",
    media="images/move-out-cleaning.jpg",
    alt="Empty Toronto apartment being cleaned before a handover",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Three ways to reach us</h2>
          <div class="grid grid-3" style="margin:1.5rem 0;">
            <a class="glass-card" href="{WA}" target="_blank" rel="noopener" style="text-decoration:none;">
              <h3>WhatsApp</h3>
              <p>Best for quotes. Send photos of the space and anything specific you want handled.</p>
              <p><strong>{PHONE}</strong></p>
            </a>
            <a class="glass-card" href="tel:{TEL}" style="text-decoration:none;">
              <h3>Phone</h3>
              <p>Best for scheduling and short notice jobs. Call early for same day availability.</p>
              <p><strong>{PHONE}</strong></p>
            </a>
            <a class="glass-card" href="{MAPS}" target="_blank" rel="noopener" style="text-decoration:none;">
              <h3>Google Profile</h3>
              <p>Find us on Google, check the hours and leave a review after your visit.</p>
              <p><strong>Sunshine Property Services</strong></p>
            </a>
          </div>

          <h2>What to include in your message</h2>
          <p>The more of this you send, the more accurate the quote and the fewer back and forth messages:</p>
          <ul>
            <li>The service you want, or just a description of the problem.</li>
            <li>Property type and rough size: condo, semi, detached, office, number of bedrooms and bathrooms.</li>
            <li>Photos of each space, including the parts you are worried about.</li>
            <li>Whether the property is occupied or empty, and whether someone will be there.</li>
            <li>Your neighbourhood and any parking or elevator details.</li>
            <li>Dates that work, and any hard deadline like a handover or a listing shoot.</li>
          </ul>

          <figure class="media-figure">
            <img src="images/post-reno-cleanup.jpg" alt="Renovation dust being cleared from a Toronto home" loading="lazy">
            <figcaption>If there is a deadline, say so in the first message. Handovers and listing shoots get scheduled around.</figcaption>
          </figure>

          <h2>Hours</h2>
          <div class="info-row">{CLOCK}<div><strong>Monday to Friday</strong><br>7:00am to 7:00pm</div></div>
          <div class="info-row">{CLOCK}<div><strong>Saturday and Sunday</strong><br>9:00am to 5:00pm</div></div>
          <div class="info-row">{PIN}<div><strong>Service area</strong><br>{AREA}</div></div>

          <div class="btn-row" style="margin-top:1.6rem;">
            <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WAICON} Message on WhatsApp</a>
            <a class="btn btn-gold" href="tel:{TEL}">Call {PHONE}</a>
          </div>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(WA=WA_QUOTE, WAICON=SVG["wa"], PHONE=PHONE, TEL=PHONE_TEL, MAPS=MAPS,
                      CLOCK=SVG["clock"], PIN=SVG["pin"], AREA=AREA,
                      SIDEBAR=sidebar(0, photo="images/t-kitchen-detail.jpg",
                                      photo_alt="Kitchen surface detail after a clean",
                                      photo_cap="Send a photo, get a price"),
                      CTA=cta_strip(0), FOOT=footer(0))

page("contact.html", contact)


# ======================================================================
# REVIEWS
# ======================================================================
reviews = head(
    title="Reviews | " + NAME + " Toronto",
    desc=("Sunshine Property Services on Google. Read the profile, leave a review after your visit, and "
          "see the standards every job is held to."),
    canonical=BASE + "/reviews.html",
    extra_ld=ld_breadcrumb([("Reviews", "reviews.html")]),
) + hero_small(
    0, [("Reviews", "reviews.html")],
    "Judge Us on", "THE LAST JOB",
    "Our Google profile is new, so there is nothing here worth dressing up. What we can tell you is exactly what every visit is held to, and where to say so if we miss it.",
    media="images/bathroom-cleaning.jpg",
    alt="Shower glass cleaned to a streak free finish",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Where to leave feedback</h2>
          <p>Sunshine Property Services is listed on Google. If we have worked on your property, a review there is the most useful thing you can do for us, good or bad. If something was wrong, tell us first and we will come back and fix it.</p>
          <div class="btn-row" style="margin:1.2rem 0;">
            <a class="btn btn-primary" href="{MAPS}" target="_blank" rel="noopener">Open our Google profile</a>
            <a class="btn btn-whatsapp" href="{WAFB}" target="_blank" rel="noopener">Send feedback on WhatsApp</a>
          </div>

          <h2>What we hold ourselves to</h2>
          <p>Until there are reviews here to read, this is the honest version of what you are buying.</p>

          <div class="grid grid-2" style="margin:1.4rem 0;">
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av a">{CHECKTXT}</span><span class="rev-name"><strong>The quote is the price</strong><small>Agreed before we start</small></span></div>
              <p class="quote">If the job turns out bigger than the photos showed, we stop and show you before doing anything that changes the cost.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av b">{CHECKTXT}</span><span class="rev-name"><strong>Missed something? We return</strong><small>No argument</small></span></div>
              <p class="quote">Tell us within a couple of days and we come back and put it right. That is cheaper for us than a bad review, and fairer to you.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av c">{CHECKTXT}</span><span class="rev-name"><strong>Photos on empty properties</strong><small>Proof, not promises</small></span></div>
              <p class="quote">Turnovers and move outs finish with photos sent to you, so a landlord in another city can see the unit without driving to it.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av d">{CHECKTXT}</span><span class="rev-name"><strong>Your home, your rules</strong><small>Products, pets, rooms</small></span></div>
              <p class="quote">Rooms you want left alone stay untouched. If you want your own products used, leave them out and say so.</p>
            </div>
          </div>

          <h2>The work speaks first</h2>
          {STRIP}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    MAPS=MAPS, WAFB=wa("I'd like to leave feedback about a job you did for me:"),
    CHECKTXT="&#10003;",
    STRIP=photo_strip(0, [
        ("images/t-bathroom-detail.jpg", "Shower screen cleaned to a clear finish", "Bathrooms"),
        ("images/t-kitchen-detail.jpg", "Kitchen counters and backsplash", "Kitchens"),
        ("images/t-floor-care.jpg", "Floor care in a living room", "Floors"),
        ("images/t-turnover.jpg", "Unit cleaned between tenants", "Turnovers"),
    ]),
    SIDEBAR=sidebar(0, photo="images/t-commercial-floor.jpg",
                    photo_alt="Commercial floor cleaned in a Toronto office",
                    photo_cap="Commercial accounts"),
    CTA=cta_strip(0), FOOT=footer(0))

page("reviews.html", reviews)


# ======================================================================
# LEGAL
# ======================================================================
def legal(slug, title, heading, body):
    return head(
        title=title + " | " + NAME,
        desc=title + " for " + strip(NAME) + ", a property services business operating in Toronto, Ontario.",
        canonical=BASE + "/" + slug,
        extra_ld=ld_breadcrumb([(heading, slug)]),
    ) + hero_small(
        0, [(heading, slug)], heading.split(" ")[0], " ".join(heading.split(" ")[1:]).upper() or "PAGE",
        "The plain version. If anything here is unclear, ask us and we will explain it in a sentence.",
        media="images/t-staircase.jpg", alt="Staircase and handrail in a Toronto property",
    ) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
{BODY}
        </div>
{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(BODY=body, SIDEBAR=sidebar(0), CTA=cta_strip(0), FOOT=footer(0))


privacy_body = """          <h2>What we collect</h2>
          <p>Only what we need to quote and carry out your job: your name, the contact details you message us from, the property address, and any photos or notes you send about the work.</p>

          <h2>How we use it</h2>
          <p>To prepare a quote, schedule the visit, do the work and follow up afterwards. Where a job finishes with completion photos, those are sent to you and kept only as long as they are useful for that job.</p>

          <h2>What we do not do</h2>
          <p>We do not sell your details, we do not share them with marketing companies, and we do not add you to a mailing list because you asked for a quote.</p>

          <h2>Messaging services</h2>
          <p>If you contact us through WhatsApp, that conversation also sits on WhatsApp's own servers under their terms, not ours. The same applies to any review you leave on Google.</p>

          <h2>This website</h2>
          <p>This site is a set of static pages. It does not ask you to log in, it does not run advertising trackers, and the only third party it loads is the Google Fonts service used for the typefaces.</p>

          <h2>Your choices</h2>
          <p>Ask us at any time what we hold about you, or ask us to delete it. Call or message the number on this site and we will deal with it.</p>

          <h2>Contact</h2>
          <p>Questions about privacy go to <a href="tel:{TEL}">{PHONE}</a>.</p>""".format(TEL=PHONE_TEL, PHONE=PHONE)

terms_body = """          <h2>Quotes</h2>
          <p>A quote covers the work described in it, based on the photos and information you provide. If the property turns out to be materially different from what was described, we stop, show you, and agree any change with you before continuing.</p>

          <h2>Access and scheduling</h2>
          <p>You arrange access, whether that is being there, a key, a lockbox code or a concierge instruction. If a crew arrives and cannot get in, we will try to reach you and reschedule.</p>

          <h2>Your property</h2>
          <p>We treat what is in a property as yours unless you tell us otherwise. On cleanouts, nothing is removed that has not been pointed out for removal. If you are unsure about an item, leave it and tell us.</p>

          <h2>Things we cannot take</h2>
          <p>On removals and cleanouts we cannot accept hazardous waste, including paint, solvents, fuel, asbestos, chemicals and pressurised containers. Ask us before the visit and we will point you to the right drop off.</p>

          <h2>If something is wrong</h2>
          <p>Tell us within a couple of days of the visit and we will come back and put it right. If something is damaged while we are working, tell us straight away so we can deal with it properly.</p>

          <h2>Cancellations</h2>
          <p>Let us know as early as you can. Short notice cancellations cost a crew their day, so please call rather than leaving it.</p>

          <h2>Payment</h2>
          <p>Payment terms are confirmed when you book, along with your quote.</p>

          <h2>Contact</h2>
          <p>Questions about these terms go to <a href="tel:{TEL}">{PHONE}</a>.</p>""".format(TEL=PHONE_TEL, PHONE=PHONE)

page("privacy.html", legal("privacy.html", "Privacy Policy", "Privacy Policy", privacy_body))
page("terms.html", legal("terms.html", "Terms of Service", "Terms of Service", terms_body))

if __name__ == "__main__":
    for p in BUILT:
        print("built", p)
