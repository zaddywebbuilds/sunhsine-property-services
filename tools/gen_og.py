# -*- coding: utf-8 -*-
"""Builds 1200x630 share cards for link previews (WhatsApp, iMessage, Facebook, X).

Every card fits its photograph whole, never cropped, on a brand background, with the
business name and phone on a solid bar underneath rather than printed over the picture.
Output goes to images/og/.
"""

import io
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")
OUT = os.path.join(IMG, "og")
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 630
BAR = 104
NAVY = (22, 41, 63)
ROOF = (31, 61, 92)
BLUE = (46, 98, 145)
GOLD = (240, 183, 78)
SUN = (255, 194, 74)
CREAM = (253, 247, 236)
SAND = (250, 226, 180)
SAND_SOFT = (252, 237, 204)
SKY = (220, 235, 248)
LIGHT_ROOF = (92, 135, 180)

FONTS = r"C:\Windows\Fonts"
f_name = ImageFont.truetype(os.path.join(FONTS, "georgiab.ttf"), 34)
f_name_big = ImageFont.truetype(os.path.join(FONTS, "georgiab.ttf"), 56)
f_sub = ImageFont.truetype(os.path.join(FONTS, "segoeui.ttf"), 25)
f_small = ImageFont.truetype(os.path.join(FONTS, "segoeuib.ttf"), 24)
f_tag = ImageFont.truetype(os.path.join(FONTS, "segoeuib.ttf"), 20)

PHONE = "+1 416-788-8942"
NAME = "SUNSHINE PROPERTY SERVICES"


def gradient(w, h, top, bottom):
    base = Image.new("RGB", (1, h))
    px = base.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    return base.resize((w, h))


def sun_house(draw, cx, cy, scale, roof_col=None):
    """The logo mark: a sun behind a house, drawn to match images/logo.svg."""
    roof_col = roof_col or ROOF
    s = scale
    r = int(52 * s)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD)
    for dx, dy in ((0, -1), (-0.72, -0.72), (0.72, -0.72), (-1, -0.12), (1, -0.12)):
        x1, y1 = cx + dx * 70 * s, cy + dy * 70 * s
        x2, y2 = cx + dx * 96 * s, cy + dy * 96 * s
        draw.line([x1, y1, x2, y2], fill=GOLD, width=max(2, int(12 * s)))
    hw, roof_h, body_h = int(96 * s), int(62 * s), int(72 * s)
    top = cy - int(8 * s)
    draw.polygon([(cx, top), (cx + hw, top + roof_h), (cx - hw, top + roof_h)], fill=roof_col)
    bx = int(60 * s)
    draw.rectangle([cx - bx, top + roof_h, cx + bx, top + roof_h + body_h], fill=BLUE)
    draw.rectangle([cx - int(76 * s), top + roof_h + body_h,
                    cx + int(76 * s), top + roof_h + body_h + int(7 * s)], fill=roof_col)
    dw, dh = int(17 * s), int(40 * s)
    draw.rectangle([cx - dw, top + roof_h + body_h - dh, cx + dw, top + roof_h + body_h], fill=CREAM)
    ww = int(14 * s)
    for side in (-1, 1):
        wx = cx + side * int(34 * s)
        draw.rectangle([wx - ww, top + roof_h + int(14 * s),
                        wx + ww, top + roof_h + int(14 * s) + int(22 * s)], fill=CREAM)


def bottom_bar(card, tagline):
    d = ImageDraw.Draw(card)
    d.rectangle([0, H - BAR, W, H], fill=NAVY)
    d.rectangle([0, H - BAR, W, H - BAR + 5], fill=SUN)
    sun_house(d, 66, H - BAR // 2 - 4, 0.30, roof_col=LIGHT_ROOF)
    d.text((118, H - BAR + 24), NAME, font=f_tag, fill=(255, 255, 255))
    d.text((118, H - BAR + 52), tagline, font=ImageFont.truetype(
        os.path.join(FONTS, "segoeui.ttf"), 20), fill=(190, 212, 233))
    right = PHONE
    w = d.textlength(right, font=f_small)
    d.text((W - w - 40, H - BAR + 38), right, font=f_small, fill=SUN)
    return card


def fit(photo_path, box_w, box_h):
    im = Image.open(photo_path).convert("RGB")
    ratio = min(box_w / im.width, box_h / im.height)
    return im.resize((max(1, int(im.width * ratio)), max(1, int(im.height * ratio))),
                     Image.LANCZOS)


def photo_card(src, dest, tagline):
    """Photo fitted whole above a solid bar. Nothing is cropped or overprinted."""
    card = gradient(W, H, SKY, SAND)
    area_h = H - BAR
    im = fit(os.path.join(IMG, src), W - 80, area_h - 40)
    card.paste(im, ((W - im.width) // 2, (area_h - im.height) // 2))
    bottom_bar(card, tagline)
    card.save(os.path.join(OUT, dest), "JPEG", quality=86, optimize=True)
    return dest


def brand_card(src, dest):
    """Home card: navy panel of text on the left, photograph fitted on the right."""
    card = gradient(W, H, SKY, SAND)
    d = ImageDraw.Draw(card)
    panel_w = 540
    d.rectangle([0, 0, panel_w, H], fill=NAVY)
    d.rectangle([panel_w - 6, 0, panel_w, H], fill=SUN)

    sun_house(d, 108, 118, 0.52, roof_col=LIGHT_ROOF)
    d.text((56, 212), "Sunshine", font=f_name_big, fill=(255, 255, 255))
    d.text((56, 276), "Property Services", font=f_name, fill=SUN)
    d.text((56, 338), "Cleaning, cleanouts and", font=f_sub, fill=(196, 216, 236))
    d.text((56, 370), "seasonal property care", font=f_sub, fill=(196, 216, 236))
    d.text((56, 402), "across Toronto and the GTA", font=f_sub, fill=(196, 216, 236))
    d.line([56, 456, 300, 456], fill=(70, 100, 134), width=2)
    d.text((56, 476), PHONE, font=f_small, fill=SUN)
    d.text((56, 512), "Open 7 days  |  from 7am weekdays", font=ImageFont.truetype(
        os.path.join(FONTS, "segoeui.ttf"), 20), fill=(170, 194, 218))

    right_w = W - panel_w
    im = fit(os.path.join(IMG, src), right_w - 60, H - 60)
    card.paste(im, (panel_w + (right_w - im.width) // 2, (H - im.height) // 2))
    card.save(os.path.join(OUT, dest), "JPEG", quality=88, optimize=True)
    return dest


# ----------------------------------------------------------------------
# One card per photograph that any page uses for its preview
# ----------------------------------------------------------------------
CARDS = [
    ("property-exterior.jpg", "Toronto and the GTA, seven days a week"),
    ("residential-cleaning.jpg", "House cleaning across Toronto"),
    ("kitchen-deep-clean.jpg", "Deep cleaning across Toronto"),
    ("move-out-cleaning.jpg", "Move in and move out cleaning"),
    ("office-cleaning.jpg", "Office and commercial cleaning"),
    ("post-reno-cleanup.jpg", "Post-construction cleanup"),
    ("window-cleaning.jpg", "Window cleaning across Toronto"),
    ("bathroom-cleaning.jpg", "Deep cleaning, down to the grout"),
    ("t-power-washing.jpg", "Pressure washing across Toronto"),
    ("t-snow-removal.jpg", "Snow removal and winter care"),
    ("t-turnover.jpg", "Rental and property turnovers"),
    ("t-driveway.jpg", "Driveways and exteriors"),
    ("t-highrise-windows.jpg", "Glass, frames and tracks"),
    ("t-staircase.jpg", "Property care across Toronto"),
    ("t-kitchen-detail.jpg", "Kitchens cleaned properly"),
    ("t-bathroom-detail.jpg", "Bathrooms cleaned properly"),
    ("t-floor-care.jpg", "Floors and carpet care"),
    ("t-commercial-floor.jpg", "Commercial floor care"),
    ("svc-junk-removal.svg", "Junk removal and cleanouts"),
]

made = []
for src, tag in CARDS:
    if src.endswith(".svg"):
        continue
    made.append(photo_card(src, src, tag))

# The junk removal page has no photograph, so it gets the brand card.
made.append(brand_card("property-exterior.jpg", "og-default.jpg"))

for name in made:
    size = os.path.getsize(os.path.join(OUT, name))
    print("%-34s %6.1f KB" % (name, size / 1024.0))
print("\n%d share cards in images/og/" % len(made))
