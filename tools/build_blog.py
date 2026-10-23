# -*- coding: utf-8 -*-
"""Builds the blog index and every article."""

from common import (NAME, PHONE, PHONE_TEL, AREA, BASE, SERVICES, BY_SLUG, WA_QUOTE,
                    head, ld_breadcrumb, ld_faq, hero_small, photo_strip, cta_strip,
                    footer, sidebar, faq_block, write, strip)

BUILT = []
D = 1  # every article lives in /blog/

POSTS = [
dict(slug="how-much-does-house-cleaning-cost-in-toronto",
     title="How Much Does House Cleaning Cost in Toronto?",
     date="2026-09-08", pretty="8 September 2026", read="6 min",
     img="images/kitchen-deep-clean.jpg",
     alt="Cleaner wiping a kitchen island in a Toronto home",
     teaser="Why nobody honest quotes a flat number over the phone, and the six things that actually move the price.",
     service="deep-cleaning-toronto",
     body=[
      ("", ["Ask five Toronto cleaning companies what a three bedroom house costs and you will get five answers, three of which will change once someone actually sees the place. That is not always dishonesty. It is that square footage on its own tells you almost nothing about how long a property takes to clean.",
            "Here is what genuinely drives the number, so you can judge any quote you are given, including ours."]),
      ("1. Size, but less than you think", [
       "Square footage sets a floor on the time. What sets the ceiling is the number of bathrooms and the number of floors. Bathrooms are the slowest rooms in any house by a wide margin, and a second one adds more time than another bedroom does. Stairs slow everything down, because equipment has to be carried rather than wheeled."]),
      ("2. How long since the last proper clean", [
       "This is the single biggest variable and the one most quotes get wrong. A home cleaned every two weeks takes a fraction of the time of the same home untouched for a year. Soap scum, grease and limescale all harden with age, and hardened residue is scrubbing time, not wiping time.",
       "It is also why a first visit is usually priced higher than the ones that follow. The first visit is catching up. Everything after is maintaining."]),
      ("3. Occupied or empty", [
       "Empty properties clean faster, because there is nothing to work around. They also get judged harder, because with the furniture gone every mark is visible. Move out and turnover cleans are priced on that higher standard rather than on the easier access."]),
      ("4. What is in scope", [
       "Inside the oven, inside the fridge, inside cabinets, interior windows, balcony glass: every one of these is real time and should be listed in the quote rather than assumed. A cheap quote that leaves them out is not cheaper, it is smaller. Ask what is included before comparing two numbers."]),
      ("5. Access", [
       "Parking, elevators, loading dock bookings and walk up distance cost time, especially downtown and in condo buildings. None of it is cleaning, but all of it is hours. Mention your access situation when you ask for a quote and the number you get will hold."]),
      ("6. Frequency", [
       "Recurring work costs less per visit, because each visit is shorter. Weekly, every other week and monthly schedules all price below a comparable one off. If you are deciding between a single deep clean and a schedule, the honest answer is usually one deep clean to reset, then a schedule to hold it."]),
      ("So what should you actually do", [
       "Take photos of your kitchen, your bathrooms and any room you are worried about. Send them with the number of bedrooms and bathrooms and whether the place is occupied. Any competent cleaner can price that accurately within the hour, and you avoid the quote that changes at the door."]),
     ]),

dict(slug="deep-clean-vs-regular-clean",
     title="Deep Clean or Regular Clean: Which One Do You Actually Need?",
     date="2026-09-15", pretty="15 September 2026", read="5 min",
     img="images/residential-cleaning.jpg",
     alt="Cleaner vacuuming a bright Toronto living room",
     teaser="One resets the property, the other holds it there. Booking the wrong one is how people end up disappointed.",
     service="deep-cleaning-toronto",
     body=[
      ("", ["These two get used interchangeably and they should not be. They are different jobs, with different times, different prices and different results. Booking a regular clean when the house needs a deep clean is the most common reason people feel let down by a cleaning service."]),
      ("What a regular clean does", [
       "A regular clean maintains a standard that already exists. Surfaces, sinks, toilets, showers, mirrors, floors, bins, touch points. It is fast because it is repeating work that was done recently, and the dirt has not had time to bond to anything.",
       "On a maintained home, a regular clean leaves the place genuinely clean. On a neglected one, it leaves the place tidy, which is not the same thing, and the difference will be obvious to whoever is paying."]),
      ("What a deep clean does", [
       "A deep clean goes after everything a regular clean never touches. Inside the oven and the fridge. Grout, rather than tile. The range hood filter. The tops of door frames. Behind and under appliances and furniture where they move. Vents, blinds, radiators and baseboards.",
       "It takes a crew most of a day on an average home, and it is the only kind of clean where the result is visible from the doorway."]),
      ("How to tell which one you need", [
       "Run a finger along the top of a door frame. Open the oven. Look at the grout line where the shower meets the floor, and at the track of a window you open often. If any of those make you wince, a regular clean will not fix it, because a regular clean was never supposed to.",
       "The other test is time. If it has been more than six months since anything got cleaned properly, start with a deep clean."]),
      ("The sensible sequence", [
       "One deep clean to reset the property, then a recurring schedule to hold it. That combination is cheaper over a year than repeatedly booking rescue cleans, and the recurring visits stay short because nothing gets a chance to build up again.",
       "If budget is tight, deep clean the kitchen and bathrooms only, and keep the rest on a regular schedule. Those two rooms are where ninety percent of the difference lives."]),
     ]),

dict(slug="move-out-cleaning-checklist-toronto",
     title="The Move Out Cleaning Checklist Toronto Landlords Actually Inspect",
     date="2026-09-22", pretty="22 September 2026", read="7 min",
     img="images/move-out-cleaning.jpg",
     alt="Empty Toronto apartment cleaned before handover",
     teaser="An empty unit hides nothing. Here is the order to work in, and the eight places inspections always check.",
     service="move-out-cleaning-toronto",
     body=[
      ("", ["Cleaning an occupied home and cleaning an empty one are different problems. In an empty unit there is no furniture, no clutter and nothing to soften the view. Every mark on a wall, every ring inside a cupboard and every dusty track in a window frame is on display.",
            "Work in this order and nothing gets cleaned twice."]),
      ("Work top down, and leave the floors until last", [
       "Start with light fittings, vents and the tops of door frames. Then walls and fixtures. Then surfaces and inside cupboards. Then the floors. Cleaning the floor first guarantees you will be cleaning it again, because everything above it drops dust as you go."]),
      ("The eight places inspections always check", [
       "<strong>Inside the oven.</strong> First thing opened, every time.",
       "<strong>Inside and behind the fridge.</strong> Including the seal and the floor underneath.",
       "<strong>Inside every cupboard and drawer.</strong> Crumbs and rings in an empty kitchen are glaring.",
       "<strong>Shower glass and grout.</strong> Limescale and soap film are what people point at.",
       "<strong>Window tracks and sills.</strong> Grit sits there and nobody ever cleans it.",
       "<strong>Skirting and door frames.</strong> Scuffs at ankle height and dust at head height.",
       "<strong>Closet shelving and rails.</strong> Empty closets show dust immediately.",
       "<strong>Behind the toilet and around its base.</strong> The spot most people skip and every inspector checks."]),
      ("Clean after the movers, not before", [
       "A half empty unit is the worst possible time to clean, because the half that is left has to be moved and the floor underneath it cleaned again. Get everything out, then clean once, properly."]),
      ("Take photos when you finish", [
       "Photograph every room once it is done. If a deposit dispute comes up weeks later, photos end it in a minute. This is standard practice on professional turnovers for exactly that reason."]),
      ("What about the things left behind", [
       "Almost every move out leaves something: a mattress, a broken shelf, bags in a closet. Dragging them to the curb is not always allowed and never pleasant. Handle it as a removal in the same visit as the clean, and the unit is finished in one go rather than two."]),
     ]),

dict(slug="how-to-prepare-for-a-cleaning-visit",
     title="How to Prepare for a Cleaning Visit (and Get More for Your Money)",
     date="2026-09-29", pretty="29 September 2026", read="4 min",
     img="images/t-floor-care.jpg",
     alt="Floor care in a Toronto living room",
     teaser="Fifteen minutes of preparation buys you an extra hour of actual cleaning. Here is where to spend it.",
     service="house-cleaning-toronto",
     body=[
      ("", ["You are paying for time. Anything a cleaner has to do that is not cleaning comes out of the same budget, and tidying is the big one. Fifteen minutes of preparation can easily buy an extra hour of real work."]),
      ("Clear the flat surfaces", [
       "Counters, tables, desks and bedside tables. A cleaner cannot wipe a surface covered in objects, so they either clean around them, which looks bad, or move each one and put it back, which eats the clock. Clearing the surfaces is the single highest value thing you can do."]),
      ("Deal with the floor, not the dirt", [
       "Pick up clothes, toys, cables and bags. You are not cleaning the floor, you are clearing it so somebody else can. Leave the actual dirt entirely alone, that part is the job."]),
      ("Decide about the dishes", [
       "A sink full of dishes blocks the most useful two square feet in the house. Either empty it beforehand, or say clearly that you want dishes handled as part of the visit so the time is included."]),
      ("Say what matters most", [
       "Every household has a thing. Streaks on the glass, the smell of the bins, pet hair on one particular chair. Say it once, early, and it becomes part of every visit. Cleaners are not mind readers and most people never mention the one thing they actually care about."]),
      ("Sort out access and pets", [
       "Confirm how the crew gets in, where to park and which door to use. If a pet is nervous, say so, and shut them somewhere quiet if that is easier for everyone."]),
      ("Name the rooms to skip", [
       "A home office mid project, a nursery with a sleeping baby, a storage room you would rather nobody entered. Say which rooms are out of bounds and the time gets spent where you want it instead."]),
     ]),

dict(slug="post-renovation-dust-guide",
     title="Why Renovation Dust Keeps Coming Back",
     date="2026-10-02", pretty="2 October 2026", read="5 min",
     img="images/post-reno-cleanup.jpg",
     alt="Construction dust cleared after a Toronto renovation",
     teaser="You cleaned it twice and it is back. That is not failure, it is physics, and here is how to actually finish the job.",
     service="post-construction-cleaning-toronto",
     body=[
      ("", ["The renovation finished, you cleaned the place, and two days later every surface has a film on it again. Nothing went wrong. Construction dust behaves differently from household dust, and cleaning it the way you clean normal dust guarantees it comes back."]),
      ("It is still in the air", [
       "Drywall sanding, cutting and demolition produce particles fine enough to stay airborne for days. When you clean on day one, most of the dust has not landed yet. It settles afterwards, onto the surfaces you just cleaned, which is why it looks like your work undid itself.",
       "This is why a proper post construction clean is usually two visits, not one. The first makes the property usable. The second, a few days later, catches what came out of the air."]),
      ("Dry wiping just moves it", [
       "A dry cloth on construction dust lifts some of it and launches the rest back into the room. Microfibre, used damp, traps it instead. The same goes for vacuuming: a vacuum without proper filtration takes fine dust in one end and sprays it out the other."]),
      ("Work top down, more than once", [
       "Ceilings, fittings, fans, frames, ledges, then walls, then surfaces, then floors. Then do it again. On a dusty job the second pass is not optional, because the first pass disturbs as much as it removes."]),
      ("Do not forget the vents", [
       "Dust gets into returns and registers during the work and the system redistributes it for weeks afterwards. Wiping and vacuuming the vents is what stops the property from re dusting itself every time the heating comes on."]),
      ("Window tracks hold the evidence", [
       "Tracks and sills collect the gritty heavy fraction, and it migrates back onto the glass every time a window opens. Vacuum them out before cleaning the panes, or you will be cleaning the panes twice."]),
      ("When to book the cleaners", [
       "After the last dusty trade has gone and after the big debris has been removed. Cleaning before the final sanding is money set on fire. If debris is still on site, get it taken out in the same booking and save the second trip."]),
     ]),

dict(slug="landlord-turnover-checklist",
     title="Turning Over a Rental in Toronto: A Landlord's Checklist",
     date="2026-10-06", pretty="6 October 2026", read="6 min",
     img="images/t-turnover.jpg",
     alt="Vacant Toronto rental unit prepared for the next tenant",
     teaser="The gap between tenants is the expensive part. Most of it is waiting on trades, not working.",
     service="property-turnover-toronto",
     body=[
      ("", ["An empty unit costs you every single day. The cleaning is rarely what makes a turnover slow. What makes it slow is waiting for one trade to finish so the next can be booked, then waiting for that one."]),
      ("Day one: inspect and photograph before anything moves", [
       "Walk the unit and photograph everything, damage included, before a single item is removed. Photographs taken at this point protect the deposit conversation and give you a dated record of condition."]),
      ("Day one: clear it out", [
       "Whatever was left behind comes out before cleaning starts, not during. Cleaning around a leftover mattress means cleaning that spot again later. If you can arrange clearing and cleaning in one booking, the whole thing compresses into a single day."]),
      ("Day two: clean to inspection standard", [
       "Empty unit standard, not occupied home standard. Inside appliances, inside cupboards, grout, glass, tracks, skirting, closets, floors wall to wall. Prospective tenants viewing an empty unit look at exactly the things an inspection would."]),
      ("Day two: flag maintenance while you can still act", [
       "A turnover is the only time the unit is empty and accessible. Note the dripping tap, the sticking window, the cracked tile and the failed seal now. Finding them later means scheduling around a tenant."]),
      ("Day three: photograph for the listing", [
       "Listing photos of a freshly cleaned empty unit outperform photos of a tired one by a wide margin, and the unit will never look better than the hour after the clean. Shoot it then."]),
      ("What a combined turnover saves", [
       "Clear out, clean, photograph and report, booked once. One crew, one invoice, one day instead of three, and a photo set at the end so you can check the result without driving across the city. For anyone running more than a couple of properties, that compression is the entire value."]),
     ]),

dict(slug="when-to-pressure-wash-in-toronto",
     title="When to Pressure Wash in Toronto (and What Not to Blast)",
     date="2026-10-10", pretty="10 October 2026", read="5 min",
     img="images/t-power-washing.jpg",
     alt="Pressure washing a house exterior in Toronto",
     teaser="Spring, after the salt. And the surfaces where high pressure does more damage than good.",
     service="pressure-washing-toronto",
     body=[
      ("", ["Toronto is hard on exterior surfaces. Freeze and thaw cycles, road salt all winter, pollen in spring and algae anywhere that stays damp. The grey creeps in so slowly that most owners never notice until a strip gets washed and the contrast is obvious."]),
      ("The best window is spring", [
       "Wash once the salt is off the roads and the overnight freezes have stopped. Salt residue is corrosive and sits in concrete all winter, so getting it off in spring protects the surface as well as the look.",
       "Autumn is the second best window. Clearing algae and organic growth before winter stops it from being locked under ice for months."]),
      ("Pressure is not the point", [
       "The common mistake is treating pressure as the measure of quality. High pressure on the wrong surface etches concrete permanently, tears up wood fibres on a deck, blows the sand out of interlock joints and forces water behind siding, where it causes problems you will not see for a year.",
       "Technique is matching pressure, nozzle, distance and detergent to the material. Soft washing, which uses low pressure and the right cleaning solution, is the correct answer for siding and anything delicate."]),
      ("What washes well", [
       "Concrete driveways and walkways, asphalt, interlock, stone, brick, patios, garage doors, fencing and most siding. Garage doors and fences are the easiest visible wins on any property, because they are large, dirty and in everyone's eyeline."]),
      ("What needs care or a different method", [
       "Older wood decks, painted surfaces that are already failing, soft mortar on old brickwork, and anything with a compromised seal. A good operator tells you which of yours falls into this group before starting, not after."]),
      ("What to expect afterwards", [
       "Interlock may need joint sand topped up. Old oil stains in porous concrete will lighten but rarely vanish completely. Anyone promising a brand new driveway from a wash is selling you something.",
       "Book it with window cleaning on the same visit. The two together change how a property reads from the street more than either does alone."]),
     ]),

dict(slug="how-often-should-windows-be-cleaned",
     title="How Often Should Windows Be Cleaned in Toronto?",
     date="2026-10-14", pretty="14 October 2026", read="4 min",
     img="images/window-cleaning.jpg",
     alt="Interior window being cleaned in a Toronto home",
     teaser="Twice a year for most homes, three times near a main road, and why the tracks matter as much as the glass.",
     service="window-cleaning-toronto",
     body=[
      ("", ["Clean glass is the cheapest way to make a property look cared for. Dirty glass undoes an otherwise spotless house, because it is the thing you look through all day and the thing a visitor sees from the street."]),
      ("Twice a year suits most homes", [
       "Spring and autumn. Spring clears the winter salt spray and the grime that built up while nobody opened a window. Autumn clears summer pollen and dust before the glass spends months behind condensation."]),
      ("Three times if you are near the action", [
       "Main roads, construction sites and the lake all accelerate the cycle. Road grime is greasy and bonds to glass, construction dust is abrasive and sits in the tracks, and lake air leaves mineral deposits. Properties in those spots benefit from a third visit."]),
      ("Commercial glass is on a different clock", [
       "Any glass the public touches, entrance doors above all, needs attention monthly or more. Fingerprints at the entrance are the first thing anyone sees about a business."]),
      ("The tracks matter as much as the glass", [
       "Window tracks collect grit, and every time the window opens it drags that grit back across the pane. Clean glass over a dirty track stays clean for days rather than months. Any window cleaning worth paying for includes the frames and tracks, not just the panes."]),
      ("Why professional glass stays clear longer", [
       "It is mostly about drying. Streaks come from cleaning solution drying on the glass before it is cleared, which is why windows cleaned in direct sun look worse afterwards. Working on an overcast day, or on the shaded side, and squeegeeing properly is most of the difference.",
       "The other part is that the edges get dried by hand. Edges are where streaks start, and they are where a rushed job gives itself away."]),
     ]),

dict(slug="what-junk-removal-can-and-cannot-take",
     title="What Junk Removal Can and Cannot Take",
     date="2026-10-17", pretty="17 October 2026", read="5 min",
     img="images/svc-junk-removal.svg",
     alt="Illustration of a junk removal truck being loaded",
     teaser="Most of it goes. The short list that does not, and where it has to go instead.",
     service="junk-removal-toronto",
     body=[
      ("", ["Almost everything in a house can be taken away in a truck. The exceptions are short, specific and worth knowing before you book, because finding out on the day means the item stays where it is."]),
      ("What goes without a second thought", [
       "Furniture of every kind, including sectionals and mattresses. Appliances, including fridges and freezers. Electronics. Renovation debris, offcuts, old cabinetry and fixtures. Yard material, branches, soil bags and broken patio furniture. Boxes, bags and general household clutter. Whole garages, basements, sheds and storage lockers."]),
      ("What cannot go in the truck", [
       "<strong>Paint, solvents and fuel.</strong> These are household hazardous waste and go to a municipal depot.",
       "<strong>Chemicals and pesticides.</strong> Same route, and never mixed together.",
       "<strong>Asbestos or anything containing it.</strong> Older tiles, insulation and some textured ceilings. This needs licensed abatement, full stop.",
       "<strong>Pressurised containers.</strong> Propane tanks, fire extinguishers and gas cylinders.",
       "<strong>Medical and biohazard waste.</strong> Sharps and anything contaminated.",
       "If you are unsure, send a photo before the visit. It takes a minute and saves a wasted trip."]),
      ("Fridges and freezers are a special case", [
       "Units with refrigerant have to be handled properly, which is a specific process and a disposal cost rather than a simple drop off. They can absolutely be taken, they just need to be mentioned when you get the quote so the price is right the first time."]),
      ("Where it actually ends up", [
       "This is the part worth asking any removal company. Usable furniture and household goods should go to a charity or reuse centre. Metal goes to scrap. Electronics go to e waste recycling. Only what is genuinely finished should end up at disposal.",
       "A company that cannot answer that question is taking everything to the same place, and you are paying for it."]),
      ("You do not need to move anything first", [
       "The carrying is the job. Getting a sectional out of a basement and up a stairwell is precisely what you are paying for, and attempting it yourself is how people hurt their backs and scratch their walls. Point at it, and leave it where it is."]),
     ]),

dict(slug="how-often-should-an-office-be-cleaned",
     title="How Often Should an Office Be Cleaned?",
     date="2026-10-19", pretty="19 October 2026", read="4 min",
     img="images/office-cleaning.jpg",
     alt="Desks being cleaned in a downtown Toronto office",
     teaser="Daily, three times a week or weekly. It depends on headcount, footfall and whether the public walks in.",
     service="commercial-cleaning-toronto",
     body=[
      ("", ["Office cleaning schedules usually get set once and never revisited, which is why so many are wrong. Headcount changes, hybrid patterns change, and the right frequency changes with them."]),
      ("Start with the washrooms", [
       "Washrooms set the floor for any schedule. They need servicing daily in any office with regular daily occupancy, and more than daily in anywhere public facing. Everything else can flex. Washrooms cannot, and they are the first thing anyone judges a workplace by."]),
      ("Then count the desks actually in use", [
       "A thirty desk office running at full occupancy needs daily attention. The same office at forty percent occupancy on a hybrid pattern is comfortable on three days a week, scheduled to match the busy days rather than spread evenly.",
       "The trap is leaving the schedule at five days when half the desks are empty, or cutting to weekly when the office filled up again."]),
      ("Public facing spaces run on their own clock", [
       "Reception, entrance glass and waiting areas get judged by people who do not work there, so they need attention every day regardless of headcount. Entrance doors in particular: fingerprints on the glass are the first impression a visitor gets."]),
      ("Clinics and studios are different again", [
       "Treatment rooms, studios and anywhere with skin contact surfaces are driven by their own standards and their own product requirements, not by a general cleaning schedule. Tell your cleaner the rules and expect them to follow them exactly."]),
      ("Build in the periodic work", [
       "Daily and weekly cleaning does not cover carpets, hard floor treatment, interior glass or high dusting. Put those on a quarterly or twice yearly rotation when you set the schedule, rather than noticing a year later that nobody has done them."]),
      ("A sensible default", [
       "For a standard Toronto office: washrooms and kitchen daily, desks and floors three times a week, reception and entrance glass daily, deep floor and glass work quarterly. Adjust up for high footfall, down for a quiet hybrid office, and revisit it once a year."]),
     ]),

dict(slug="spring-property-reset-checklist",
     title="The Spring Property Reset, Inside and Out",
     date="2026-10-23", pretty="23 October 2026", read="5 min",
     img="images/property-exterior.jpg",
     alt="Well kept Toronto home exterior in spring",
     teaser="One weekend of the right work in spring carries a Toronto property through the rest of the year.",
     service="pressure-washing-toronto",
     body=[
      ("", ["Toronto properties take a beating between November and March. Salt, grit, freeze and thaw outside, and a sealed up house concentrating dust inside. Spring is the one moment where fixing both at once makes obvious sense."]),
      ("Outside: get the salt off first", [
       "Salt residue sits in concrete all winter and corrodes it slowly. Washing the driveway, walkways and entrance in spring is as much about protecting the surface as making it look better. Do this before anything else outdoors, because it changes what the rest of the property needs."]),
      ("Outside: the two easy wins", [
       "The garage door and the fence. Both are large, both are in everyone's eyeline from the street, and both are filthy after a winter nobody looked at them. Washing those two alone changes how the whole property reads."]),
      ("Outside: clear before you clean", [
       "Branches down over winter, bags of soil, broken patio furniture, the thing behind the shed. Clear it first, wash second. Washing around a pile just means moving the pile and washing again."]),
      ("Inside: the air is the problem", [
       "A house sealed for four months concentrates dust in soft furnishings, vents and the places nobody reaches. That is why homes feel stale by March even when they look fine. The fix is a deep clean that includes vents, blinds, high surfaces and behind furniture, not another pass over the same visible surfaces."]),
      ("Inside: the windows matter more than you think", [
       "Winter leaves a film of road grime and condensation residue on glass, and because it builds gradually nobody notices how much light they lost. Cleaning the glass and the tracks is the single biggest visible change you can make to an interior in spring."]),
      ("Do it in one booking", [
       "Wash, clear and deep clean are three visits if you book three companies and one visit if you book one. The crew is already on site, the equipment is already out, and the whole property gets reset on the same day."]),
     ]),

dict(slug="toronto-winter-property-checklist",
     title="A Toronto Winter Property Checklist",
     date="2026-10-21", pretty="21 October 2026", read="5 min",
     img="images/t-snow-removal.jpg",
     alt="Snow blower clearing a Toronto driveway",
     teaser="What to sort out in November so January is somebody else's problem.",
     service="snow-removal-toronto",
     body=[
      ("", ["Toronto winters punish properties that were not prepared in the autumn. Almost everything on this list is cheap and quick in November and expensive or impossible in January."]),
      ("Before the first snow", [
       "<strong>Wash the exterior.</strong> Driveway, walkways and entrance. Clean surfaces shed water and ice better than surfaces coated in organic growth.",
       "<strong>Clear the gutters and drains.</strong> Blocked drainage is how you get ice dams and a sheet of ice across the walkway.",
       "<strong>Clear the yard.</strong> Furniture, hoses, toys and planters. Anything left out disappears under snow and gets hit by a shovel.",
       "<strong>Mark the hazards.</strong> Low lighting, edging, sprinkler heads and garden features all vanish under the first storm.",
       "<strong>Decide where snow gets piled.</strong> Not across a drain, not where it blocks the view pulling out of the driveway, and not where meltwater refreezes on the walkway."]),
      ("Arrange clearing before you need it", [
       "The worst moment to find a snow clearing service is during a storm, when every other property owner is calling the same numbers. Arrange it in the autumn and your property is already on the round."]),
      ("Clear early, and clear to the surface", [
       "Snow cleared before it gets walked on and driven over takes a fraction of the effort. Once compacted it turns to ice, and ice is a different and far more dangerous problem. Clearing down to the surface, rather than leaving a packed layer, is what actually prevents falls.",
       "Salt goes down after clearing, not before, and it belongs on the walkways and steps where people put their feet."]),
      ("Inside, do not forget the air", [
       "Sealed up houses in winter concentrate dust. Vents, filters and soft furnishings all contribute, and the house gets stuffy by February. A deep clean partway through winter makes a noticeable difference to how a closed up home feels."]),
      ("In spring, undo the salt", [
       "Salt stains concrete and corrodes it over time. A pressure wash once the salt season ends takes the residue off and resets the property for the year. Book it early, because spring is the busiest washing season."]),
     ]),
]


def article(p):
    svc = BY_SLUG[p["service"]]
    trail = [("Blog", "blog/index.html"), (p["title"], "blog/%s.html" % p["slug"])]
    sections = []
    for heading, paras in p["body"]:
        if heading:
            sections.append("          <h2>%s</h2>" % heading)
        # Consecutive runs that open with <strong> become a list, in place.
        run = []
        for para in paras:
            if para.startswith("<strong>"):
                run.append(para)
                continue
            if run:
                sections.append("          <ul>%s</ul>" % "".join("<li>%s</li>" % b for b in run))
                run = []
            sections.append("          <p>%s</p>" % para)
        if run:
            sections.append("          <ul>%s</ul>" % "".join("<li>%s</li>" % b for b in run))

    ld_article = """  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BlogPosting","headline":"{T}",
    "datePublished":"{D}","dateModified":"{D}",
    "image":"{B}/{IMG}",
    "author":{{"@type":"Organization","name":"{N}"}},
    "publisher":{{"@type":"Organization","name":"{N}","logo":{{"@type":"ImageObject","url":"{B}/images/logo.svg"}}}},
    "mainEntityOfPage":"{B}/blog/{S}.html"}}
  </script>
""".format(T=strip(p["title"]), D=p["date"], B=BASE, IMG=p["img"], N=NAME, S=p["slug"])

    others = [q for q in POSTS if q["slug"] != p["slug"]][:3]
    more = "".join(
        '<article class="service-tile"><div class="service-tile-media">'
        '<img src="../%s" alt="%s" loading="lazy"></div>'
        '<div class="service-tile-body"><h3>%s</h3><p>%s</p>'
        '<div class="row"><a href="%s.html">Read &rarr;</a></div></div></article>'
        % (q["img"], q["alt"], q["title"], q["teaser"], q["slug"]) for q in others)

    html = head(
        title=strip(p["title"]) + " | " + NAME,
        desc=strip(p["teaser"]),
        canonical="%s/blog/%s.html" % (BASE, p["slug"]),
        depth=D, og_type="article", og_image=p["img"],
        extra_ld=ld_article + ld_breadcrumb(trail),
    ) + hero_small(
        D, trail, p["title"], "", p["teaser"], media=p["img"], alt=p["alt"],
    ) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <p class="note-pill">{PRETTY} &middot; {READ} read</p>
{BODY}

          <figure class="media-figure">
            <img src="../{SIMG}" alt="{SALT}" loading="lazy">
            <figcaption>Need this handled instead of read about? {SSHORT} across {AREA}.</figcaption>
          </figure>

          <div class="btn-row" style="margin:1.4rem 0;">
            <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">Get a Free Quote</a>
            <a class="btn btn-gold" href="../{SSLUG}.html">{SSHORT}</a>
            <a class="btn btn-glass" href="tel:{TEL}">Call {PHONE}</a>
          </div>

          <h2>More from the blog</h2>
          <div class="grid grid-3" style="margin-top:1rem;">{MORE}</div>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(PRETTY=p["pretty"], READ=p["read"], BODY="\n".join(sections),
                      SIMG=svc["img"], SALT=svc["alt"], SSHORT=strip(svc["short"]),
                      SSLUG=svc["slug"], AREA=AREA, WA=WA_QUOTE, TEL=PHONE_TEL,
                      PHONE=PHONE, MORE=more,
                      SIDEBAR=sidebar(D, photo=svc["thumb"], photo_alt=svc["thumb_alt"],
                                      photo_cap=strip(svc["short"])),
                      CTA=cta_strip(D), FOOT=footer(D))
    BUILT.append(write("blog/%s.html" % p["slug"], html))


for post in POSTS:
    article(post)


# ----------------------------------------------------------------------
# Blog index
# ----------------------------------------------------------------------
cards = "".join(
    '<article class="service-tile"><div class="service-tile-media">'
    '<img src="../%s" alt="%s" loading="lazy"></div>'
    '<div class="service-tile-body"><h3>%s</h3><p>%s</p>'
    '<div class="row"><a href="%s.html">Read &rarr;</a><span style="font-size:.78rem;color:var(--c-ink-soft)">%s</span></div>'
    '</div></article>' % (p["img"], p["alt"], p["title"], p["teaser"], p["slug"], p["read"])
    for p in reversed(POSTS))

index = head(
    title="Blog | " + NAME + " Toronto",
    desc=("Practical guides on cleaning, turnovers, cleanouts and seasonal property care in Toronto, "
          "from the crew that does the work."),
    canonical=BASE + "/blog/index.html", depth=D,
    extra_ld=ld_breadcrumb([("Blog", "blog/index.html")]),
) + hero_small(
    D, [("Blog", "blog/index.html")],
    "Notes From", "THE JOB",
    "What we have learned keeping Toronto properties in shape. No filler, no listicles, just the things clients ask us on site.",
    media="images/property-exterior.jpg",
    alt="Well kept Toronto home exterior",
) + """
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Articles</span>
        <h2>Guides and checklists</h2>
        <p>Written from the work, not from a keyword list.</p>
      </div>
      <div class="grid grid-3">{CARDS}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">The work itself</span>
        <h2>Around a Toronto property</h2>
      </div>
      {STRIP}
    </div>
  </section>

{CTA}{FOOT}""".format(CARDS=cards,
                      STRIP=photo_strip(D, [
                          ("images/t-kitchen-detail.jpg", "Kitchen surfaces cleaned", "Kitchens"),
                          ("images/t-bathroom-detail.jpg", "Shower glass cleaned", "Bathrooms"),
                          ("images/t-highrise-windows.jpg", "Window cleaning in a tower", "Glass"),
                          ("images/t-snow-removal.jpg", "Snow cleared from a driveway", "Winter"),
                      ]),
                      CTA=cta_strip(D), FOOT=footer(D))

BUILT.append(write("blog/index.html", index))

if __name__ == "__main__":
    for b in BUILT:
        print("built", b)
