# -*- coding: utf-8 -*-
"""Builds the ten service pages and the five service-area pages."""

from common import (NAME, PHONE, PHONE_TEL, AREA, BASE, MAPS, SVG, SERVICES, BY_SLUG,
                    LOCATIONS, wa, head, ld_service, ld_faq, ld_breadcrumb, hero_small,
                    photo_strip, service_tiles, cta_strip, footer, sidebar, faq_block,
                    write, strip)

BUILT = []

# ----------------------------------------------------------------------
# Per-service copy
# ----------------------------------------------------------------------
COPY = {
"house-cleaning-toronto": dict(
    h1="House Cleaning", glow="IN TORONTO",
    sub="Weekly, every other week or monthly. The same rooms, the same standard, the same crew, so the house never drifts back to square one.",
    intro=[
      "A recurring clean is a different animal from a one off. The point is not a dramatic transformation every visit, it is that the house never gets far enough from clean to need one. Each visit is shorter, cheaper and more thorough than a rescue mission would be.",
      "We work room by room in the same order every time, which is how nothing gets skipped on a busy day. You tell us once which rooms matter most and which to leave alone, and that sticks."],
    includes_title="What a standard visit covers",
    includes=[
      "<strong>Kitchen.</strong> Counters, backsplash, sink and taps, cabinet fronts, exterior of appliances, cooktop, microwave inside and out, floor.",
      "<strong>Bathrooms.</strong> Shower and tub scrubbed, glass cleared of soap film, toilet inside and out, sink, mirror, fixtures polished, floor.",
      "<strong>Bedrooms and living areas.</strong> Dusting including sills, ledges and skirting, mirrors and glass, vacuum throughout, mop hard floors, beds made if sheets are left out.",
      "<strong>Everywhere.</strong> Light switches, door handles, bannisters, bins emptied and relined, a final walk to catch anything missed."],
    extras_title="Add on when you need it",
    extras=[
      "Inside the oven and inside the fridge",
      "Inside cupboards and drawers, emptied first",
      "Interior windows and balcony glass",
      "Laundry folded, or beds stripped and remade",
      "Balcony or patio swept and wiped down"],
    good=[
      "Pets are fine. Tell us names and whether they are nervous, and we will work around them.",
      "Products come with us. If you prefer your own, leave them out and leave a note.",
      "You do not need to be home. Most recurring clients leave a key or a code.",
      "First visit usually takes longer than the ones after it, and is priced accordingly."],
    faq=[
      ("How often should I book?", "Most households land on every two weeks. Weekly suits busy family homes and anyone with pets or allergies. Monthly works if you keep on top of things yourself and want the deeper jobs handled."),
      ("Will it be the same cleaners each time?", "Wherever scheduling allows, yes. Familiarity is most of what makes a recurring clean good: they know your floors, your products and which cupboard the bin bags live in."),
      ("What if I need to skip a week?", "Just tell us. There is no penalty for skipping, though if the gap gets long the next visit may take extra time."),
      ("Do you clean inside the oven every visit?", "Not as standard, because it adds real time. Add it when you want it, or set it on a rotation, for instance every third visit.")],
    strip=[("images/t-kitchen-detail.jpg", "Kitchen counters cleaned", "Kitchens"),
           ("images/t-bathroom-detail.jpg", "Shower glass cleaned", "Bathrooms"),
           ("images/t-floor-care.jpg", "Floor care in a living room", "Floors"),
           ("images/t-staircase.jpg", "Stairs and handrails wiped", "Stairs")],
    related=["deep-cleaning-toronto", "window-cleaning-toronto", "move-out-cleaning-toronto"]),

"deep-cleaning-toronto": dict(
    h1="Deep Cleaning", glow="IN TORONTO",
    sub="The reset. Inside appliances, behind furniture, grout, vents, frames and all the places a weekly clean never gets to.",
    intro=[
      "A deep clean is what you book when the normal clean stopped being enough. Grease that has gone sticky, grout that has gone grey, dust on the tops of door frames, a fridge nobody has emptied in a year. It takes a crew most of a day on an average home, and it is the one job where the difference is obvious from the doorway.",
      "People usually book it for one of four reasons: spring, a new baby, guests arriving, or taking over a property from someone else. All four need the same thing, which is for everything to be genuinely clean at the same time, once."],
    includes_title="What a deep clean covers",
    includes=[
      "<strong>Kitchen, properly.</strong> Inside the oven, inside the fridge, inside the microwave, range hood and filter, backsplash degreased, cabinet fronts and tops, under and behind what can be moved.",
      "<strong>Bathrooms, properly.</strong> Grout scrubbed, limescale off glass and taps, shower head descaled, extractor vent, behind the toilet, tile floor edges.",
      "<strong>Dust at every height.</strong> Door frames, picture rails, light fittings, ceiling fan blades, vents and registers, blinds, radiators, baseboards.",
      "<strong>Floors and edges.</strong> Furniture moved where safe, carpets vacuumed underneath, hard floors mopped to the edges rather than the middle.",
      "<strong>Glass and fittings.</strong> Interior windows, mirrors, switch plates, handles, bannisters and skirting wiped by hand."],
    extras_title="Common add ons",
    extras=[
      "Inside all cupboards and wardrobes",
      "Exterior window panes within reach",
      "Balcony, patio or garage sweep out",
      "Wall spot cleaning and scuff removal",
      "Junk removal for anything you decide goes"],
    good=[
      "Allow most of a day. A thorough deep clean on a three bedroom home is not a two hour job.",
      "Clearing surfaces beforehand gets you more cleaning for the same money.",
      "Some marks are damage, not dirt. We will tell you which is which rather than scrub a finish off.",
      "After a deep clean, a recurring visit holds the standard for a fraction of the cost."],
    faq=[
      ("How is this different from a regular clean?", "A regular clean maintains. A deep clean resets. The regular clean wipes the front of the oven, the deep clean takes the racks out and does the inside."),
      ("How long does it take?", "Most homes take a crew most of a working day. Larger or heavily soiled properties can take two visits, which we will tell you before booking, not halfway through."),
      ("Can you get grout back to white?", "Usually much closer than it is now. Grout that has been stained for years may not come all the way back, and we would rather say that up front than overpromise."),
      ("Do I need a deep clean before starting a recurring schedule?", "Not always, but if the property has been neglected it is cheaper overall. One deep clean, then maintenance, beats paying rescue prices every visit.")],
    strip=[("images/t-kitchen-detail.jpg", "Kitchen surfaces degreased", "Kitchen"),
           ("images/t-bathroom-detail.jpg", "Shower glass and tile", "Tile and grout"),
           ("images/t-floor-care.jpg", "Deep floor care", "Floors"),
           ("images/t-staircase.jpg", "Handrails and stair edges", "Detail work")],
    related=["house-cleaning-toronto", "post-construction-cleaning-toronto", "window-cleaning-toronto"]),

"move-out-cleaning-toronto": dict(
    h1="Move In &amp; Move Out", glow="CLEANING",
    sub="Empty unit, top to bottom, finished to the standard a walkthrough is judged by. Photos sent when we are done.",
    intro=[
      "An empty property is the hardest kind to clean, because there is nothing left to hide behind. Every mark on a wall, every ring in a cupboard and every corner of a floor is visible, and whoever inspects it will be looking for exactly those things.",
      "We clean move outs for tenants trying to get a deposit back, landlords preparing for the next tenant, and owners handing over keys on a sale. Same work, different person doing the inspecting."],
    includes_title="What is covered",
    includes=[
      "<strong>Kitchen stripped and cleaned.</strong> Inside and behind the oven and fridge where they move, all cupboards inside and out, drawers, counters, sink, backsplash and the floor underneath everything.",
      "<strong>Bathrooms to inspection standard.</strong> Limescale, grout, glass, fittings, vent, behind and around the toilet base.",
      "<strong>Every room.</strong> Closets and shelving inside, skirting, door frames, switch plates, handles, light fittings, vents.",
      "<strong>Floors.</strong> Vacuumed and mopped wall to wall now that the furniture is gone.",
      "<strong>Glass.</strong> Interior panes, sills and tracks, plus balcony glass where there is one.",
      "<strong>Finish.</strong> Photos of each room sent to you when we lock up."],
    extras_title="Often added",
    extras=[
      "Removal of whatever got left behind",
      "Wall scuff and mark removal",
      "Carpet cleaning arranged alongside",
      "Balcony or garage sweep out",
      "Exterior entry and porch wash"],
    good=[
      "Book for after the movers, not before. Cleaning a half empty unit means cleaning it twice.",
      "If there is a handover time, tell us. We start at 7am precisely so these deadlines are makeable.",
      "Keys, lockboxes and concierge instructions are all normal for us.",
      "Anything left behind can go in the same visit if you want it gone."],
    faq=[
      ("Will this satisfy a landlord inspection?", "That is the standard we clean to. We also send photos of every room, which settles most disputes before they start."),
      ("Can you clean before the furniture is out?", "We can, but you will get a worse result for the same money. Wherever possible, book us once the property is empty."),
      ("Do you take away what the last tenant left?", "Yes, as a cleanout alongside the clean. Tell us roughly how much there is and we will size the job properly."),
      ("What about a move in clean?", "Same job, opposite direction. Nobody wants to unpack into someone else's dust, and an empty property is the only chance to clean it properly.")],
    strip=[("images/t-turnover.jpg", "Unit cleaned ready for handover", "Empty units"),
           ("images/t-kitchen-detail.jpg", "Kitchen cleaned inside and out", "Kitchens"),
           ("images/t-bathroom-detail.jpg", "Bathroom to inspection standard", "Bathrooms"),
           ("images/t-floor-care.jpg", "Floors cleaned wall to wall", "Floors")],
    related=["property-turnover-toronto", "junk-removal-toronto", "deep-cleaning-toronto"]),

"commercial-cleaning-toronto": dict(
    h1="Office &amp; Commercial", glow="CLEANING",
    sub="Offices, clinics, studios and common areas, cleaned after hours or before you open, on a schedule that does not interrupt anyone.",
    intro=[
      "Commercial cleaning is judged on consistency more than intensity. Nobody notices a good clean, everybody notices the week it slipped. We run the same checklist every visit so the standard does not depend on who turned up.",
      "Most clients book us outside working hours. Early morning before the doors open, or evenings once the last person has gone. Either way the space is ready and nobody has to work around a vacuum."],
    includes_title="A standard commercial visit",
    includes=[
      "<strong>Desks and workstations.</strong> Surfaces wiped, monitors and keyboards dusted, bins emptied and relined.",
      "<strong>Kitchens and break rooms.</strong> Counters, sink, appliance exteriors, microwave inside, tables and chairs, floor.",
      "<strong>Washrooms.</strong> Sanitised throughout, fixtures polished, mirrors, supplies restocked from your stock.",
      "<strong>Floors.</strong> Vacuumed across carpet, mopped on hard floors, entrance mats lifted and cleaned under.",
      "<strong>Touch points.</strong> Door handles, switches, lift buttons, rails and reception surfaces.",
      "<strong>Common areas.</strong> Reception, meeting rooms, corridors and stairwells."],
    extras_title="Periodic work",
    extras=[
      "Interior and reachable exterior window cleaning",
      "Carpet and hard floor deep treatment",
      "Post event or post move cleanup",
      "Pressure washing entrances and walkways",
      "Winter clearing of the entrance and lot"],
    good=[
      "Scheduling is fixed. You get set days and a set window, not a vague promise.",
      "Keys, fobs and alarm codes are handled the way your building requires.",
      "Clinics and studios often have specific product rules. Tell us and we follow them.",
      "Multi site accounts are quoted together, which usually lands better per site."],
    faq=[
      ("Can you work outside business hours?", "Yes, and most clients prefer it. Early mornings from 7am and evenings both work."),
      ("How are supplies handled?", "We bring our own cleaning equipment and products. Consumables like paper and soap are usually your stock, and we restock from it. We can also source them if you would rather."),
      ("Do you cover common areas in a building?", "Yes. Lobbies, corridors, stairwells and shared washrooms are routine work for us."),
      ("Can we start with a trial?", "Yes. Book a single clean, see the result, then decide on a schedule. We would rather earn the contract than argue you into one.")],
    strip=[("images/t-commercial-floor.jpg", "Office floor care", "Office floors"),
           ("images/t-highrise-windows.jpg", "Window cleaning in a tower", "Glass"),
           ("images/t-staircase.jpg", "Stairwell handrails cleaned", "Stairwells"),
           ("images/t-driveway.jpg", "Entrance walkway washed", "Entrances")],
    related=["window-cleaning-toronto", "pressure-washing-toronto", "snow-removal-toronto"]),

"post-construction-cleaning-toronto": dict(
    h1="Post-Construction", glow="CLEANUP",
    sub="Fine dust off every surface, sill, track and vent, so the work you just paid for is actually visible.",
    intro=[
      "Construction dust is not normal dust. It is fine, it is everywhere, and it keeps reappearing for days because it settles out of the air in layers. A single wipe down moves it around. Cleaning it properly means working top to bottom, more than once, with the right equipment.",
      "We come in after the trades are finished and the debris is out. If the debris is not out, we can handle that too in the same visit."],
    includes_title="What the cleanup covers",
    includes=[
      "<strong>Top down dust removal.</strong> Ceilings, fittings, fans, door frames, ledges, then walls, then surfaces, then floors, in that order and more than once.",
      "<strong>Glass and frames.</strong> Paint specks and adhesive off panes, sills and tracks vacuumed out, balcony glass cleared.",
      "<strong>Fittings and finishes.</strong> Stickers and film off new appliances and fixtures, handles, plates, rails and vents wiped.",
      "<strong>Kitchen and bathrooms.</strong> New cabinetry inside and out, new appliances inside and out, grout haze off tile, fixtures polished.",
      "<strong>Floors.</strong> Vacuumed with proper filtration then mopped, repeated until the cloth comes up clean.",
      "<strong>Vents and registers.</strong> Wiped and vacuumed so the system is not redistributing dust after you move back in."],
    extras_title="Often needed alongside",
    extras=[
      "Removal of leftover materials and packaging",
      "A second visit a few days later for settled dust",
      "Exterior pressure washing of the work area",
      "Full window clean inside and out",
      "Garage or driveway clear down"],
    good=[
      "Book once the trades are genuinely finished. Cleaning before the last sanding is money wasted.",
      "A follow up visit a few days later catches what settles out of the air afterwards.",
      "Tell us about new, delicate or unsealed finishes so we use the right approach on them.",
      "Debris removal and cleaning in one booking saves a separate trip charge."],
    faq=[
      ("When should we book you in?", "After the last dusty trade leaves and after large debris is removed. If debris is still there, say so and we will quote both together."),
      ("Why do you recommend a second visit?", "Because fine dust stays airborne for days and keeps settling. One clean gets the property usable, a short follow up gets it finished."),
      ("Can you remove the renovation waste as well?", "Yes. Offcuts, packaging, old fixtures and general debris can go out in the same booking."),
      ("Will you damage new finishes?", "Not if we know what they are. Point out anything unsealed, delicate or newly painted and we will adjust the method.")],
    strip=[("images/t-staircase.jpg", "Stairs cleaned after a build", "After the trades"),
           ("images/t-kitchen-detail.jpg", "New kitchen surfaces detailed", "New kitchens"),
           ("images/t-highrise-windows.jpg", "Glass cleared of construction film", "Glass"),
           ("images/t-floor-care.jpg", "Floors vacuumed and mopped", "Floors")],
    related=["deep-cleaning-toronto", "junk-removal-toronto", "window-cleaning-toronto"]),

"window-cleaning-toronto": dict(
    h1="Window Cleaning", glow="IN TORONTO",
    sub="Glass, frames and tracks. Interior panes, balcony glass and reachable exteriors, finished without streaks.",
    intro=[
      "Windows are the fastest visible win on any property. A clean house with dirty glass still reads as neglected, and a tired house with clear glass reads as looked after. It is also the job most people put off longest, because doing it badly leaves streaks that look worse than the dirt did.",
      "We clean the glass, the frames and the tracks. Tracks matter more than people expect: they hold the grit that gets dragged back onto the glass the next time a window opens."],
    includes_title="What is included",
    includes=[
      "<strong>Interior panes.</strong> Washed and squeegeed to a streak free finish, edges dried by hand.",
      "<strong>Frames and sills.</strong> Wiped down, including the lip where water and grit collect.",
      "<strong>Tracks.</strong> Vacuumed out then wiped, so sliding doors and windows run properly again.",
      "<strong>Balcony and patio glass.</strong> Both faces where it is safe to reach them.",
      "<strong>Reachable exteriors.</strong> Ground floor and anything accessible safely from a ladder or a pole system.",
      "<strong>Mirrors and interior glass.</strong> Added on request while we are there."],
    extras_title="Add ons",
    extras=[
      "Screens removed, washed and refitted",
      "Hard water stain treatment on exterior glass",
      "Skylights where safely reachable",
      "Full deep clean of the rooms at the same time",
      "Pressure washing the exterior while we are on site"],
    good=[
      "Overcast days give the best finish. Direct sun dries the glass before it can be cleared, which is what causes streaks.",
      "High exterior glass above safe reach is a specialist access job. We will tell you plainly if yours is.",
      "Twice a year suits most Toronto homes, usually spring and autumn.",
      "Book windows with a deep clean and the whole property lifts at once."],
    faq=[
      ("Do you do high rise exteriors?", "We clean interior glass and balcony glass in condos and towers. Exterior faces above safe reach need rope or lift access, which your building normally arranges on a schedule."),
      ("Will the frames and tracks be done?", "Yes, both, as standard. Cleaning the glass and leaving grit in the track is half a job."),
      ("How often should windows be cleaned?", "Twice a year for most homes. Properties near a main road, a construction site or the lake usually want three."),
      ("What about screens?", "They can be taken out, washed and refitted. Mention it when you ask for a quote so the time is included.")],
    strip=[("images/t-highrise-windows.jpg", "High rise window cleaning", "Condo glass"),
           ("images/t-bathroom-detail.jpg", "Shower screen cleared", "Shower glass"),
           ("images/t-kitchen-detail.jpg", "Kitchen surfaces detailed", "Interiors"),
           ("images/t-driveway.jpg", "Exterior entrance washed", "Exteriors")],
    related=["deep-cleaning-toronto", "pressure-washing-toronto", "commercial-cleaning-toronto"]),

"pressure-washing-toronto": dict(
    h1="Pressure Washing", glow="IN TORONTO",
    sub="Driveways, walkways, patios, siding, decks and garage doors brought back several shades, without damaging the surface underneath.",
    intro=[
      "Most Toronto driveways are a few shades lighter than their owners think. Years of road salt, algae, engine drip and general grey build up so gradually that nobody notices until a strip gets washed and the difference is obvious.",
      "Pressure matters less than technique. Too much pressure on the wrong surface etches concrete, strips wood and forces water behind siding. We match the pressure and the nozzle to the material rather than blasting everything at maximum."],
    includes_title="What we wash",
    includes=[
      "<strong>Driveways and parking pads.</strong> Concrete, asphalt, interlock and stone, including the edges people skip.",
      "<strong>Walkways, steps and porches.</strong> The approach to the front door, which is what visitors actually see.",
      "<strong>Patios and decks.</strong> Washed at a pressure the material can take, especially on wood.",
      "<strong>Siding and exterior walls.</strong> Soft washed where the material calls for it, to lift algae and grime without driving water behind it.",
      "<strong>Garage doors and fencing.</strong> Usually the two dirtiest things on a property and the easiest wins.",
      "<strong>Bins, furniture and equipment.</strong> Done while the gear is already set up."],
    extras_title="Pairs well with",
    extras=[
      "Window cleaning on the same visit",
      "Yard and property clearing beforehand",
      "Gutter clear out where accessible",
      "Junk removal of anything in the way",
      "Seasonal bookings each spring"],
    good=[
      "Spring is the busiest season, once the salt is off the roads and before the summer.",
      "Interlock may need sand topped up afterwards. We will tell you if yours does.",
      "Some staining is permanent. Old oil in porous concrete lightens but rarely vanishes entirely.",
      "We need access to an outdoor tap unless arranged otherwise."],
    faq=[
      ("Will it damage my driveway or siding?", "Not when pressure and nozzle are matched to the surface. Softer materials get a soft wash rather than a high pressure jet, which is the part cheap operators skip."),
      ("How long does a driveway take?", "A typical residential driveway is a few hours, depending on size, surface and how long since the last wash."),
      ("When is the best time of year?", "Spring, once the salt has gone. Autumn is the second best window, before the freeze arrives."),
      ("Can you do the house and the driveway together?", "Yes, and it is cheaper than two visits. Most clients add window cleaning to the same booking.")],
    strip=[("images/t-power-washing.jpg", "Pressure washing a house exterior", "Siding"),
           ("images/t-driveway.jpg", "Driveway washed clean", "Driveways"),
           ("images/t-snow-removal.jpg", "The same driveway in winter", "Seasonal care"),
           ("images/t-highrise-windows.jpg", "Glass cleaned on the same visit", "Add windows")],
    related=["window-cleaning-toronto", "snow-removal-toronto", "junk-removal-toronto"]),

"junk-removal-toronto": dict(
    h1="Junk Removal", glow="&amp; CLEANOUTS",
    sub="Single items or a whole property. We carry it out from wherever it sits, load it, sweep the space and donate or recycle what we can.",
    intro=[
      "The part people underestimate is the carrying. Getting an old sectional out of a basement, up a stairwell and through a doorway is the job. The truck is the easy bit. You do not need to drag anything to the curb before we arrive, and you should not try.",
      "This is the category the business is listed under on Google, and it runs alongside the cleaning work for a reason: most properties need clearing before they can be cleaned properly."],
    includes_title="What we take",
    includes=[
      "<strong>Furniture.</strong> Sofas, sectionals, mattresses, bed frames, dressers, desks, tables, chairs and shelving.",
      "<strong>Appliances.</strong> Fridges, stoves, washers, dryers, dishwashers and freezers, disconnected and carried out.",
      "<strong>Full cleanouts.</strong> Garages, basements, sheds, storage lockers, estates and whole properties.",
      "<strong>Renovation debris.</strong> Offcuts, old cabinetry, fixtures, flooring, packaging and general construction waste.",
      "<strong>Yard material.</strong> Branches, soil bags, old fencing, broken patio furniture and play equipment.",
      "<strong>General household clutter.</strong> Boxes, bags, electronics and whatever accumulated in the corner."],
    extras_title="What we cannot take",
    extras=[
      "Paint, solvents, fuel and chemicals",
      "Asbestos or anything containing it",
      "Pressurised tanks and cylinders",
      "Medical or biohazard waste",
      "Ask before the visit and we will point you to the right drop off"],
    good=[
      "Nothing is removed unless you have pointed it out. If you are unsure about an item, leave it and tell us.",
      "Usable furniture and goods go to a charity or reuse centre where we can find one that takes them.",
      "Metal and electronics go to recycling rather than landfill.",
      "Price follows volume in the truck plus disposal cost, which is why photos give a better quote than a description."],
    faq=[
      ("Do I have to move things to the curb?", "No. Carrying it out is what you are paying for. Point at it and leave the rest to us."),
      ("Can you take just one item?", "Yes. Single item pickups are common, usually a mattress, a fridge or a couch."),
      ("What happens to it afterwards?", "Anything usable goes to a charity or reuse centre where we can. Metal and electronics go to recycling. Only what is genuinely finished goes to disposal."),
      ("How is it priced?", "By how much space it takes in the truck and what it costs to dispose of properly. Send photos and you will get a real figure rather than a range.")],
    strip=[("images/svc-estate-cleanout.svg", "Illustration of a full property cleanout", "Full cleanouts"),
           ("images/svc-garage-cleanout.svg", "Illustration of a garage being cleared", "Garages and basements"),
           ("images/svc-furniture-removal.svg", "Illustration of furniture removal", "Furniture"),
           ("images/svc-appliance-removal.svg", "Illustration of appliance removal", "Appliances"),
           ("images/svc-mattress-removal.svg", "Illustration of mattress removal", "Mattresses"),
           ("images/svc-construction-debris.svg", "Illustration of a construction debris bin", "Reno debris"),
           ("images/svc-yard-cleanup.svg", "Illustration of yard waste cleanup", "Yard waste"),
           ("images/svc-junk-removal.svg", "Illustration of a junk removal truck", "Single items")],
    related=["move-out-cleaning-toronto", "post-construction-cleaning-toronto", "property-turnover-toronto"]),

"snow-removal-toronto": dict(
    h1="Snow Removal", glow="&amp; WINTER CARE",
    sub="Driveways, walkways and entrances cleared and salted through the Toronto winter, so nobody has to risk the steps.",
    intro=[
      "Winter work is about timing more than effort. Snow cleared early, before it gets driven over and compacted, takes a fraction of the time and leaves a surface that is actually safe. Left until the afternoon, the same driveway becomes an ice rink with a shovel problem on top.",
      "We clear residential driveways and walkways, and commercial entrances where people arrive before opening. Salt goes down after clearing, on the surfaces that need it."],
    includes_title="What a visit covers",
    includes=[
      "<strong>Driveway cleared.</strong> Full width, including the windrow the plough leaves across the bottom.",
      "<strong>Walkways and steps.</strong> Cleared down to the surface, which is the part that actually prevents falls.",
      "<strong>Entrances and landings.</strong> The front door, the side door and the path people really use.",
      "<strong>Salting.</strong> Applied after clearing on walkways, steps and problem patches.",
      "<strong>Commercial entrances.</strong> Cleared before opening hours so customers and staff arrive safely."],
    extras_title="Also available",
    extras=[
      "Seasonal arrangements rather than call by call",
      "Clearing around parking pads and bin storage",
      "Ice build up at the base of steps",
      "Spring wash of the salt stained driveway",
      "Storm follow up visits"],
    good=[
      "Arrange before the first storm. Mid storm is when everyone calls at once.",
      "Tell us where you want snow piled so it does not block sightlines or drains.",
      "Mark anything hidden under the snow, like low lighting, edging or garden features.",
      "Once the salt season ends, a pressure wash takes the staining off."],
    faq=[
      ("Do you offer seasonal contracts?", "Seasonal arrangements are the usual way to book winter work, so you are not calling during a storm. Ask when you get a quote and we will set it up."),
      ("How soon after snowfall do you come?", "Timing depends on the storm and the route, which is why arranging ahead matters. Properties on a seasonal arrangement get cleared on the round."),
      ("Do you salt as well as clear?", "Yes, salt goes down after clearing on walkways, steps and anywhere that ices up."),
      ("Can you clear a commercial entrance before we open?", "Yes. Tell us your opening time and we schedule around it.")],
    strip=[("images/t-snow-removal.jpg", "Snow blower clearing a driveway", "Driveways"),
           ("images/t-driveway.jpg", "The same driveway cleared", "Walkways"),
           ("images/t-power-washing.jpg", "Spring wash after salt season", "Spring reset"),
           ("images/t-commercial-floor.jpg", "Commercial entrance kept clear", "Commercial")],
    related=["pressure-washing-toronto", "commercial-cleaning-toronto", "house-cleaning-toronto"]),

"property-turnover-toronto": dict(
    h1="Rental &amp; Property", glow="TURNOVERS",
    sub="For landlords and managers. One call between tenants: clear the unit, clean it to inspection standard, photograph it, hand it back ready to list.",
    intro=[
      "A vacant unit costs money every day it stays vacant. The gap between one tenant leaving and the next one viewing is where that money goes, and most of that gap is spent waiting on separate trades to show up in sequence.",
      "A turnover rolls it into one booking. Whatever was left behind gets removed, the unit gets cleaned the way an inspection judges it, and you get photographs of every room without having to drive across the city to check."],
    includes_title="What a turnover includes",
    includes=[
      "<strong>Clear out.</strong> Anything the previous tenant left, from a few bags to a full unit of furniture.",
      "<strong>Full empty unit clean.</strong> Kitchen inside and out, bathrooms to inspection standard, closets, floors wall to wall.",
      "<strong>Detail pass.</strong> Skirting, door frames, switch plates, handles, vents, light fittings and closet rails.",
      "<strong>Glass.</strong> Interior windows, sills, tracks and balcony glass.",
      "<strong>Photo report.</strong> Every room photographed and sent when we lock up.",
      "<strong>Flagged issues.</strong> Damage or maintenance problems we spot get reported with photos, before your next tenant finds them."],
    extras_title="Portfolio options",
    extras=[
      "Standing arrangement across several properties",
      "Key and lockbox handling as routine",
      "Listing photography prep on the same visit",
      "Pressure washing of entrances and shared paths",
      "Winter clearing for the whole portfolio"],
    good=[
      "Book the moment the keys come back. The clean is the shortest part of the gap, the waiting is the long part.",
      "A photo report settles deposit disputes faster than any argument.",
      "Multi property accounts are quoted together, which prices better per unit.",
      "We flag maintenance issues rather than clean around them."],
    faq=[
      ("Can you work from a lockbox without anyone there?", "Yes. Most turnovers run exactly that way. We lock up and send photos."),
      ("Do you handle several properties at once?", "Yes. Portfolio accounts are quoted as a block and scheduled together."),
      ("What if the tenant left furniture behind?", "It goes in the same visit. Tell us roughly how much and we will size the job before arriving."),
      ("Will you tell us about damage?", "Yes, with photos. Finding it during the turnover is far cheaper than finding it after the next tenant moves in.")],
    strip=[("images/t-turnover.jpg", "Unit cleaned between tenants", "Turnovers"),
           ("images/t-floor-care.jpg", "Floors cleaned wall to wall", "Floors"),
           ("images/t-staircase.jpg", "Common stairs and rails", "Common areas"),
           ("images/t-bathroom-detail.jpg", "Bathroom to inspection standard", "Bathrooms")],
    related=["move-out-cleaning-toronto", "junk-removal-toronto", "commercial-cleaning-toronto"]),
}


def build_service(svc):
    c = COPY[svc["slug"]]
    short_plain = strip(svc["short"]).lower()
    trail = [("Services", "services.html"), (strip(svc["short"]), svc["slug"] + ".html")]
    related = [BY_SLUG[r] for r in c["related"]]

    body = """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
{INTRO}
          <figure class="media-figure">
            <img src="{IMG}" alt="{ALT}" loading="lazy">
            <figcaption>{CAPTION}</figcaption>
          </figure>

          <h2>{INCTITLE}</h2>
          <ul>{INCLUDES}</ul>

          <h2>{EXTITLE}</h2>
          <ul>{EXTRAS}</ul>

          <h2>Worth knowing before you book</h2>
          <ul>{GOOD}</ul>

          <h2>In the detail</h2>
          {STRIP}

          <h2>Questions about {SHORT}</h2>
          {FAQ}

          <h2>Often booked with this</h2>
          <div class="grid grid-3" style="margin-top:1rem;">
{RELATED}
          </div>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
        INTRO="\n".join("          <p>%s</p>" % p for p in c["intro"]),
        IMG=svc["img"], ALT=svc["alt"],
        CAPTION="%s across %s. Quote first, work second." % (strip(svc["short"]), strip(AREA)),
        INCTITLE=c["includes_title"],
        INCLUDES="".join("<li>%s</li>" % x for x in c["includes"]),
        EXTITLE=c["extras_title"],
        EXTRAS="".join("<li>%s</li>" % x for x in c["extras"]),
        GOOD="".join("<li>%s</li>" % x for x in c["good"]),
        STRIP=photo_strip(0, c["strip"]),
        SHORT=short_plain,
        FAQ=faq_block(c["faq"]),
        RELATED=service_tiles(0, related),
        SIDEBAR=sidebar(0, photo=svc["thumb"], photo_alt=svc["thumb_alt"],
                        photo_cap=strip(svc["short"]) + " detail"),
        CTA=cta_strip(0), FOOT=footer(0))

    html = head(
        title=strip(svc["title"]) + " | " + NAME,
        desc=strip(c["sub"])[:300],
        canonical="%s/%s.html" % (BASE, svc["slug"]),
        og_image=svc["img"],
        extra_ld=ld_service(svc) + ld_breadcrumb(trail) + ld_faq(c["faq"]),
    ) + hero_small(
        0, trail, c["h1"], c["glow"], c["sub"], media=svc["img"], alt=svc["alt"],
    ) + body
    BUILT.append(write(svc["slug"] + ".html", html))


for s in SERVICES:
    build_service(s)


# ----------------------------------------------------------------------
# Service area pages
# ----------------------------------------------------------------------
def build_location(loc):
    area = loc["area"]
    trail = [(area, loc["slug"] + ".html")]
    faq = [
        ("Do you charge extra to come out to %s?" % area,
         "No. %s is part of the regular service area, so travel is not added on top of your quote." % area),
        ("How quickly can you get to %s?" % area,
         "Same week is normal and same day is often possible if you call early. Winter storms and end of month moving dates are the two busy periods worth booking ahead for."),
        ("Do you work on condos and apartments in %s?" % area,
         "Yes. Condo work is routine, including elevator bookings, loading dock times and concierge access. Tell us the building rules and we will work to them."),
        ("Can you work when nobody is home?",
         "Yes. Keys, lockboxes and concierge handover are all normal. We lock up and send photos when the job is done."),
    ]
    tiles = service_tiles(0, [BY_SLUG[s] for s in (
        "house-cleaning-toronto", "deep-cleaning-toronto", "move-out-cleaning-toronto",
        "window-cleaning-toronto", "pressure-washing-toronto", "junk-removal-toronto")])
    others = "".join(
        '<li><a href="%s.html">%s</a></li>' % (l["slug"], l["area"])
        for l in LOCATIONS if l["slug"] != loc["slug"])

    html = head(
        title="Cleaning &amp; Property Services in %s | %s" % (area, NAME),
        desc=("Cleaning, cleanouts, windows, pressure washing and snow clearing in %s. "
              "Free photo quotes from Sunshine Property Services, open seven days." % area),
        canonical="%s/%s.html" % (BASE, loc["slug"]),
        og_image=loc["img"],
        extra_ld=ld_breadcrumb(trail) + ld_faq(faq),
    ) + hero_small(
        0, trail, "Property Services in", area.upper(),
        "The full list, delivered in %s: house and deep cleaning, move outs and turnovers, offices, windows, pressure washing, junk removal and winter clearing. %s" % (area, loc["note"]),
        media=loc["img"], alt=loc["alt"],
    ) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Working in {AREA}</h2>
          <p>{NOTE} Whether it is a standing clean for a family home, a unit that needs turning around between tenants, or a driveway that has not been washed since it was poured, it is the same crew and the same number.</p>
          <p>Properties in {AREA} run the full range, from older detached homes to newer condo stock, and each asks for something different. Older houses tend to need the deep clean and the exterior work. Newer units tend to need turnovers, glass and post construction dust. We quote from photos either way, so the price fits the property rather than an average.</p>

          <figure class="media-figure">
            <img src="{IMG}" alt="{ALT}" loading="lazy">
            <figcaption>Serving {AREA} and the surrounding neighbourhoods, seven days a week.</figcaption>
          </figure>

          <h2>What gets booked most in {AREA}</h2>
          <div class="grid grid-3" style="margin-top:1rem;">
{TILES}
          </div>

          <h2>Getting a quote in {AREA}</h2>
          <p>Send photos on WhatsApp with your neighbourhood and the service you want. If parking is tight, if there is an elevator to book, or if a concierge handles access, mention it, because those details change the timing more than the cleaning does.</p>

          <h2>Questions from {AREA} clients</h2>
          {FAQ}

          <h2>Other areas we cover</h2>
          <ul>{OTHERS}</ul>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(AREA=area, NOTE=loc["note"], IMG=loc["img"], ALT=loc["alt"],
                      TILES=tiles, FAQ=faq_block(faq), OTHERS=others,
                      SIDEBAR=sidebar(0, photo="images/t-turnover.jpg",
                                      photo_alt="Unit cleaned and ready for handover",
                                      photo_cap="Booked across " + area),
                      CTA=cta_strip(0), FOOT=footer(0))
    BUILT.append(write(loc["slug"] + ".html", html))


for l in LOCATIONS:
    build_location(l)

if __name__ == "__main__":
    for p in BUILT:
        print("built", p)
