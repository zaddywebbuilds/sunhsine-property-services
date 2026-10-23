# Sunshine Property Services

Static marketing site for Sunshine Property Services, a property cleaning, cleanout and
seasonal maintenance business operating in Toronto and the GTA.

Live target: `https://zaddywebbuilds.github.io/sunhsine-property-services/`

## What is here

36 pages, all generated from Python templates in `tools/`:

| Group | Pages |
| --- | --- |
| Core | `index`, `services`, `pricing`, `about`, `contact`, `reviews`, `privacy`, `terms` |
| Services | 10 pages, one per service, `*-toronto.html` |
| Service areas | 5 pages, `property-services-*.html` |
| Blog | `blog/index.html` plus 12 articles |

Plus `sitemap.xml`, `robots.txt` and `.nojekyll`.

## Business details used

Taken from the company Google Business Profile in October 2026:

- Phone: **+1 416-788-8942** (used for `tel:` links and WhatsApp deep links)
- Hours: Mon to Fri 7:00am to 7:00pm, Sat and Sun 9:00am to 5:00pm
- Service area business, no public street address, so no address is published
- Listed category on Google is junk removal, which is covered by
  `junk-removal-toronto.html`

These values live in one place, at the top of `tools/common.py`. Change them there and
rebuild rather than editing HTML.

## Design

The layout and component set follow the Oasis Massage Studio theme (the cinematic
"OS window" frame, glass chips, rotating service ring, animated contact demos). The
palette was rebuilt around the Sunshine logo: navy `#16293F`, brand blue `#2E6291`,
sun gold `#FFC24A` and `#D49A18`, warm sand `#F3EADA`, sky `#BBD7EE`.

Two house rules are enforced in CSS, both near the end of `css/theme.css`:

`SURFACE MEDIA RULES` - **every photograph sits on the surface as its own block.** No
image is used as a faded background layer with copy printed on top, and no caption
covers a picture. Media on top, words underneath. This changes `.bx-tile`, `.svc-card`
and `.faq-deco` from the original theme's overlay treatment, and moves the why-card
icons off the photo and into the card body.

`WHOLE-IMAGE RULE` - **no picture is cropped to make it fit.** Frames keep a fixed
shape so grid rows stay level, and the image is fitted inside that shape in full
against a brand background rather than cut to fill it. The hero panel takes the shape
of its own picture. Portrait images in landscape frames therefore show sand margins
either side, which is intentional.

## Media

- There is no video on the site. The supplied before and after clip had its
  "BEFORE VS AFTER" caption burned into the picture, which breaks both house rules
  above, so the home page hero uses a text panel in that slot and the rotating service
  ring carries the motion. The clip is still in git history if it is ever wanted back.
- `images/*.jpg` are the 18 supplied concept photographs, resized and, for the ten
  smaller board crops, trimmed of their edge slivers.
- `images/svc-*.svg` and `images/logo.svg` were drawn for this site in the brand
  palette. Regenerate them with `tools/gen_svg.py` if the palette changes.
- `images/og/` holds the 1200x630 link preview cards, one per photograph plus a
  branded default. Each card fits its photo whole on a brand background with the
  business name and phone on a bar underneath, so the same no-crop and no-overprint
  rules apply to shared links. Rebuild them with `tools/gen_og.py`. Every page points
  `og:image`, `og:image:width/height/alt` and `twitter:image` at its card by absolute
  URL, which is what WhatsApp, iMessage, Facebook and X need for a large preview.

### Before this goes in front of customers

- The supplied photographs are **AI generated illustrative assets**, not photographs of
  actual Sunshine jobs or staff. They are used as generic illustration and nothing on
  the site describes them as completed work. Swap in real job photos when you have them.
- **Window cleaning, pressure washing and snow removal** are built as full service pages
  because the supplied imagery covers them. Confirm with the owner that all three are
  actually offered before the site is promoted.
- **No prices are published.** `pricing.html` explains how quotes are built instead.
  Add real figures only once the owner confirms them.
- **No testimonials are published.** The Google profile has no reviews yet, so
  `reviews.html` links to the profile and sets out service standards rather than
  inventing quotes.
- The Google listing spells the name **"sunhsine"**. The site uses **"Sunshine"**
  throughout, matching the logo. Worth correcting on Google.

## Mobile

Checked at 375px and 768px on the home page, a service page and an article:
no horizontal scroll, 16px base text, tap targets at 46px, and the rotating
service ring steps its radius and card size down at 820px and 520px so no card
is clipped by the window frame. A sticky WhatsApp, call and quote bar sits at
the bottom of the viewport below 820px.

## Building

```bash
cd tools
python build.py
```

That writes every HTML page, `sitemap.xml` and `robots.txt`. Nothing else is needed:
no npm, no bundler, no framework.

- `tools/common.py` holds the business facts, the service catalogue and every shared
  partial (head, top bar, hero, sidebar, CTA strip, footer).
- `tools/build_core.py` builds the home page and the standalone pages.
- `tools/build_services.py` builds the service and service area pages from the copy
  dictionary at the top of the file.
- `tools/build_blog.py` builds the blog index and the articles.
- `tools/gen_svg.py` redraws the logo, favicon and service illustrations.

## Local preview

```bash
python -m http.server 8899
```

Then open `http://localhost:8899/`.
