# Venus Foam

**Semyon Bochkaryov**

*Preprint v1 — August 28, 2026*

*Document status: engineering-physics analysis of a floating infrastructure concept. Calculations are based on archival data from the Venera, Vega, Pioneer Venus, and Venus Express missions.*

A floating modular station in the cloud layer of Venus. Stays aloft through the difference in gas densities (Archimedean buoyancy in a compressible medium), not tethers or engines. The structure is a mass of identical inflatable cells, not a single hull: it grows by adding cells, and damage to one does not risk the whole.

---

## Environment

**Planetary rotation and the station's day/night cycle** are not the same thing. Venus's solid surface rotates retrograde over 243 Earth days, on human timescales essentially motionless. But the atmosphere at cloud-layer altitude completes a full circuit of the planet in 4–6 days, superrotation, 40–60 times faster than the planet itself. The platform is not anchored and drifts with the atmosphere, not with the surface, so its own day/night cycle is set precisely by superrotation: about 2–3 days of daylight and 2–3 days of night per circuit, not the 243-day surface rotation and not the 117 solar days measured at the surface.

**The atmosphere is already "burned out."** CO₂ is 96.5% of the composition, carbon in its most oxidized state. This is not a fuel or an oxidizer for anything else, it is a reaction end product, not a reactant. N₂ is 3.5%. The rest is trace SO₂, H₂O (in the gas phase, single to tens of ppm), HCl, HF.

Altitude profile (Wikipedia/Venera/Venus Express data, mutually consistent)[^1]:

| Altitude | Temperature | Pressure | Wind |
|---|---|---|---|
| 0 km (surface) | 462°C / 735 K | 92.1 atm | <2.8 m/s |
| 10 km | 385°C | 47.4 atm | — |
| 20 km | 306°C | 22.5 atm | — |
| 30 km | 222°C | 9.85 atm | — |
| 40 km | 143°C | 3.50 atm | — |
| 50 km | 75°C | 1.07 atm | — |
| 55 km | 27°C | 0.53 atm | 66–70 m/s[^2] |
| 55.7 km (platform) | 22°C | 0.49 atm | 66–70 m/s[^2] |
| 60 km | −10°C | 0.24 atm | increases toward cloud top |
| 65–70 km (cloud top) | −30°C and below | 0.10 atm and below | ~100 m/s |

Wind grows with altitude from near zero at the surface to ~100 m/s at cloud top: for any probe descending through the whole profile, this means not only a 470-degree temperature swing but also a roughly 35-fold change in the wind regime (from <2.8 to ~100 m/s) over the 55 km descent.

Fig. 1. Temperature and pressure by altitude, with the platform's operating point marked.

**At the surface, CO₂** is neither a gas nor a liquid but a supercritical fluid. The critical point of CO₂ is 31°C / 72.8 atm; surface conditions on Venus (462°C / 92 atm) lie far past that point. Density in this state is about 68 kg/m³, almost two orders of magnitude (~76×) higher than the density of CO₂ at platform altitude (0.89 kg/m³), the medium behaves as a dense fluid, not a rarefied gas, which sharply changes both heat exchange and buoyancy for any probe operating at the surface.

**Gravity** is 8.87 m/s² (0.904 g, about 90% of Earth's): an ordinary weight load on the body, not the microgravity of an orbital station and not a third of Earth's as on Mars, the long-term bone/muscle atrophy characteristic of orbital crews does not physically arise here. **Illumination at operating altitude** (520–1300 W/m², diffuse light from the whole sky) feels like an overcast but bright day on Earth, neither twilight nor constant night.

---

## Materials

Two materials for two different jobs, not one "miracle material":

- **Basalt fiber**, molten volcanic rock drawn into filament, the structural layer of the cells. Holds continuous service up to 600–700°C, and can eventually be produced from local basalt.
- **Fluoropolymer film** (PTFE/FEP, Teflon and relatives), the skin facing the environment: the film's outer face is in contact with the cloud layer's acid haze, sulfuric acid is chemically almost inert to this class of polymers, the same principle already used in real Venus-aerobot envelope concepts. The film itself is assembled not as one piece but from hex panels welded at the seams, the same principle real balloon and airship envelopes already use, always cut from separate gore panels rather than cast whole. On the inner face of that same film, facing into the H₂ cell, a separate job: an Al coating that cuts diffusive loss of the load-bearing H₂ through the film. By default, not a single layer but two independent layers of hex patches with seams offset from each other (a running-bond pattern, like brick or shingles), not a monolithic coating: with statistically independent defects between layers, leakage drops by 2-3 orders of magnitude versus a single layer (see open questions), at a mass cost of just 46 kg (92 kg total for the whole skin), not a compromise. Basalt provides strength and heat resistance, fluoropolymer provides chemical protection from acid outside and, with the coating, gas retention inside; the load-bearing layer and the barrier layer are kept separate, not combined in one material. A hex panel is the same geometric solution at a different scale from the platform's cells (Fig. 2/3): a few meters for the skin, for ease of installation and spot repair, versus load-bearing cells for the platform itself, a shared construction principle, not matching sizes. Panels are manufactured on the industrial-chemical platform (see "Platform fleet"), delivery and external servicing (replacing individual damaged panels without opening the cell) use the same aerobot transport already described for cargo exchange between platforms, a spot repair of a skin section from outside, not disassembly of the whole cell.

---

## Platform: buoyancy, structure, key figures

The molecular mass of CO₂ (44 g/mol) is 1.5 times that of air (29 g/mol): at equal temperature and pressure, any gas is buoyant in local CO₂, including unenriched air. Hydrogen is used, it gives more lift per cubic meter of cell (2.6–2.8× more effective than air), and at operating altitude there is no free oxygen in the atmosphere, so the terrestrial ignition risk from a leak does not apply.

The platform consists of many cells filled with this gas, not one tank: part carries solar panels on its skin, part is energy storage, part is structure and payload. Function and load-bearing volume are combined in one body, not split across separate systems.

**Shape.** Not a smooth flat disk. In plan (top view) it is a discoid, an area of 282,740 m² holds specifically because of this profile. In cross-section it is not a uniform thin plate or a clean two-tier sandwich, but a fused swarm of cells of varying size (a "foam" in the literal geometric sense): large load-bearing structural floats around the perimeter (~20 m thick) and smaller panel cells (generation and storage together), living and industrial ones, fused directly to each other, with no open deck or superstructure on top. Each function (generation, energy storage, habitation, production) is implemented as a type of the cell itself, not a room placed on a shared surface: a habitat cell is sealed, with an oxygen atmosphere inside, exactly as a structural cell is sealed for H₂, just with a different medium inside. In profile it is closer to a lens or a dome of variable thickness: thickness at any point of the platform is set by the size of the cells there, not by a single number for the whole structure.

Fig. 2. Longitudinal cross-section of the platform: cells by function (scale is notional, cell count and shapes are schematic).

Fig. 3. Platform from above: layout of zones under the panel skin (scale notional).

**Glazing of habitat modules** is fluoropolymer film (ETFE/FEP, the same class as the cells' barrier skin): transparent, chemically inert to acid haze, already used on Earth as glazing (the Eden Project domes)[^3], one material covers both the barrier and the optical job, not two separate solutions. Window orientation is not critical: the light is diffuse, arriving from the whole sky rather than a directed beam, the same effect that lets the panels work without sun tracking. During the night period (2–3 days) lighting is ordinary artificial lighting from the onboard grid.

| Parameter | Value |
|---|---|
| Operating altitude | 55.7 km |
| Ambient temperature / pressure | 22°C / 0.49 atm |
| Platform area | 282,740 m² (disk ~600 m) |
| Lifting gas | H₂, 0.852 kg/m³ of lift at this altitude |
| Structure | basalt fiber + fluoropolymer skin |
| Panels: area / efficiency | 66,000–85,000 m² (23–30% of platform) / 22% |
| Insolation at altitude | 20–50% of extra-atmospheric (520–1300 W/m²) |
| Energy storage: chemistry / mass | Li-ion, 149 Wh/kg (pack)[^4] / 644–966 t |
| Night (free drift) | 2–3 days |

Standardized modules for energy harvesting and storage: panel skin (generation) and lithium-ion storage inside their own hydrogen cells (storage, weight offset by the buoyancy of the surrounding gas), standard, interchangeable units of one product line, not two different engineering solutions.

---

## Module docking, airlocks, and internal transport

**Between modules with the same environment** (adjacent habitat/work compartments with air): a standardized docking node with a hermetic latch (functionally closer to orbital-station docking nodes than to a household door) and an ordinary pass-through hatch, with no extra preparation.

**Between a load-bearing hydrogen cell** (battery floats, structural volumes) and any habitable compartment there is not a pass-through hatch but an airlock, with mandatory purging and atmosphere-composition monitoring before the second door opens. The reason is not just flammability by itself: outside the platform there is no oxygen and nothing to burn, but inside a habitat or work module there is an ordinary oxygen atmosphere, and a hydrogen leak into that volume is already as dangerous as it would be on Earth. Load-bearing gas cells are therefore uninhabited volume by default, accessible only through an airlock for servicing, not part of the ordinary movement routes around the station.

Fig. 4. Compartment docking: an airlock chamber with 3 leaves at the load-bearing H₂ cell, and one with 2 leaves between habitable compartments sharing the same environment (scale notional).

**Between adjacent habitat/work cells**: directly through a docking node (see above), on foot, without going outside: the distance and feel of the crossing are comparable to walking through a large terminal, except this is an internal sealed corridor between cells, not open space. For movement across the whole platform (on the order of 600 m) and cargo between distant cells: a rail cart along the main sealed corridors, threaded through a chain of docking nodes (the same principle as an airport people mover, only inside a sealed run rather than an open terminal), plus pneumatic tubes for small cargo and samples (a simple, long-proven Earth technology, used even in hospital systems, requiring no development from scratch). Between separate platforms: not rail or pipe, but short flights by mooring tugs and aerobots with altitude-controlled buoyancy, docking at a mooring node rather than maintaining a permanent physical link.

---

## Power

The station's target load is 2 MW continuous. A closed cycle (daytime station load plus overnight storage recharge, 90% round-trip efficiency) requires an average of 4.22 MW during the day, covered by 5.2–13.0% of the platform area given over to panels.

Fig. 5. Generation and load over the day/night cycle, storage charge level.

The energy-block panel skin (37,800–56,700 m²) adds another 3.3–20.1 MW of daytime, unsmoothed generation on top of this. Trying to fully smooth that as well with storage across the whole night, checked separately by calculation, has no solution: in this regime each added square meter of generation requires more added storage volume than the power it itself adds (a factor of 1.3–3.2×, meaning the process diverges rather than converging to some larger number). The platform's storage is therefore sized exactly to the target 2 MW, not to everything that could theoretically be generated, and this is a self-contained calculation, with no hidden ceiling.

Fig. 6. Coefficient k vs. panel power density, why full smoothing with storage does not converge.

- **Steady (round-the-clock) power of one platform:** 2 MW → 118–167 people (by the ISS yardstick[^5], 84–120 kW for a standing crew of 7, 12–17 kW/person, accounting for science and communications, not just bare life support).
- **Unsmoothed daytime surplus:** 3.3–20.1 MW, for industrial and research tasks that don't need power at night (chemistry, electrolysis, charging transport vehicles).

For a larger population, not one bloated platform but a fleet: for example, 500 people is 3–4 platforms of this basic type.

---

## Propulsion and station-keeping

**There are structurally no main or attitude-correction engines** on the platform itself. Altitude is held by gas balance (venting/topping up H₂, controlled cell heating), not thrust. For a fully flexible envelope at ambient pressure, heating the cells does not hold a new altitude layer but gives a one-time push: at exact equilibrium with the local temperature, the CO₂/H₂ density ratio does not depend on altitude, the platform is neutrally buoyant at any altitude at once, an overheating pulse raises it, the gas then cools to the new surroundings and it stays there, with no continuous heating. Energetically, a 500 m rise costs 11.8–22.3 GJ of potential energy (platform mass 2670–5020 t, see the mass balance below), covered by the unsmoothed daytime surplus (3.3–20.1 MW) in 10 minutes to 1.9 hours. Changing position relative to other platforms or routes is done by choosing an altitude layer: superrotation gives different drift speeds at different altitudes, and this is used as a lever instead of burning fuel (the same principle underlying cargo exchange between platforms, see below). The general approach is not to actively fight the environment but to use its features passively; that is exactly why the platform needs no engines, not because they were "abandoned."

**Dedicated thrust** is not a structural element of the platform but equipment fitted to specific modules for a specific task: mooring tugs for final docking, attitude thrusters on probes descending to the surface, the hub platform's rocket stage for reaching orbit (below). This is payload on individual vehicles, not part of the load-bearing structure. Both intra-fleet tasks are 3–4 orders of magnitude cheaper than reaching orbit: an aerobot changing altitude layer heats gas in its envelope, single-digit megajoules for a few percent of lift, with no fuel burn; a tug's final docking burn is grams to kilograms of fuel for a maneuver of a few m/s. Expensive infrastructure is needed only where large Δv is actually required, at the hub, not in internal logistics.

## Platform fleet, docking, and the link to orbit

**Specialization by function at one altitude** works: a habitat platform and a power platform with expanded panel area, in the same wind layer, move together with low relative shear, and a physical cable link between them is possible.

**Specialization by different altitudes or remote sectors of the planet** also works, but the logistics differ: not cable and not a beam (directed light loses collimation above 47 km in the clouds, attenuation on the order of 14 orders of magnitude across the cloud layer, microwave suffers the same limit at usable frequencies), but batch cargo delivery. An aerobot with altitude-controlled buoyancy suits this: by exploiting the difference in wind speed between altitude layers, such a craft can "hop" between layers to change its position relative to other platforms, a working principle, not a hypothesis: a prototype has already been flight-tested on Earth (Black Rock Desert, tethered flights at the developer's site)[^6].

**Habitat platform.** The fleet's operating altitude (55.7 km, 22°C) was chosen around it: comfortable temperature with no active cooling of habitat modules and batteries, other platform types adapt to this point or move away from it for their own reasons (see below), not the other way around. It is the fleet's family sector, childbirth and permanent residence of children are possible only here (see "Childbirth" below): it is not risk-isolated like the industrial-chemical and bioreactor platforms, not tied up with logistics like the hub, and does not run field work like the research platform. Standard fitout: habitat modules, recreation, basic medicine (see "Emergencies" below), a rail cart and pneumatic tubes along the sealed corridors between cells (see "Module docking" above). Capacity of one platform is 118–167 people (see "Power"); it allows a direct cable power link to a power platform in the same wind layer, unlike platforms at other altitudes. Living area is not a bottleneck: even a generous 100 m²/person (more spacious than the ISS or a submarine) is 11,800–16,700 m², 4.2–5.9% of platform area.

**Industrial-chemical platform.** Not required to sit at a human-comfortable 22°C, it can occupy an altitude where CO₂ is denser (better for CO₂→O₂ electrolysis and for synthesizing CH₄ from the daytime power surplus), is automated, and is physically isolated from habitat platforms by risk (flammable H₂/CH₄, intermediate reagents). Fitout: CO₂ electrolyzers, hydrocarbon-synthesis reactors, finished-product storage (methane/methanol) for transfer to the hub platform as rocket propellant and to habitat platforms for production needs.

**Bioreactor platform.** Enclosed algae/cyanobacteria cultivators (spirulina, chlorella, the same technology class as ESA's MELiSSA program)[^7], fed by CO₂ and diffuse light directly from the skin, water from the same impaction separators for cloud aerosol used across the rest of the fleet. The limiting input is phosphorus, imported (see critical imports). Isolated from habitat platforms by the same logic as the chemical platform: a biological process, not a living space, and an accident there should not reach people.

**Research platform.** Studies the surface and atmosphere beyond the minimum needed for ISRU: systematic geological surveying and drilling instead of one-off samples for a specific feedstock, and a search for signs of life in the cloud layer (moderate T/P at station altitude combined with extreme acidity is a real, open scientific question, including the disputed phosphine story). Experiments deliberately introducing organisms into the atmosphere are a separate, non-engineering question (planetary protection, bioethics), not part of the platform's default program.

**Docking and module exchange.** Not platform-to-platform directly, but through a separate, specialized hub-platform type. Mooring docks for aerobots, a receiving pad for capsules descending from orbit, and the fleet's only rocket infrastructure for sending cargo to orbit are concentrated at one point rather than duplicated on every platform. This is spaceport logic (expensive, rarely used infrastructure is built once, not at every site), not something Venus-specific.

**Receiving from orbit:** a descent capsule brakes aerodynamically (the same method used by every Venera-series probe on entry), the final approach to platform altitude uses a parachute or a small gas envelope, and docking happens in the hub platform's receiving bay. This is how critical imports arrive (see the list above).

**Sending to orbit** is a fundamentally different, costlier task than a balloon lift of surface samples to the platform: accelerating from 55.7 km to orbital velocity through the still-unflown part of the atmosphere requires a full rocket stage, comparable in scale to a launch to Earth orbit. Orbital velocity at a nominal low Venus orbit (200 km) is 7.21 km/s, not counting gravity and aerodynamic losses during ascent (the loss figure itself is not modeled). On methane-oxygen (Isp 350–380 s) this means a propellant mass 6–7 times the dry mass of the stage plus payload, comparable to an Earth orbital launch not just in description but in the actual numbers. Its propellant is methane and oxygen, the same chemistry already described in the production section (CO₂ → O₂ by electrolysis, carbon chemistry → CH₄), so the propellant is not entirely imported, though the rocket stage itself and the launch infrastructure are an expensive specialization reasonably concentrated on a single hub platform, not replicated across the fleet.

**Fleet growth trajectory** is not only outward (more platforms of the same type for a larger population) but also deeper in time: the architecture itself is built for cloud-layer conditions (22°C, 0.49 atm), not the surface, precisely because materials science for continuous operation at +460°C and 92 atm is not yet ready (521 hours of electronics demonstration, NASA Glenn Research Center, an SiC circuit in GEER at 460°C/93 atm, 2017[^8], against the decades actually needed, see open questions). This is not a permanent ceiling but a current status: as that specific technology advances, the same fleet, the same modular-growth principle, and the same hub-platform logic for expensive infrastructure naturally extend downward, from short probes to permanent surface stations, with no need to redesign the architecture from scratch once the threshold is crossed.

---

## Resources and production

From the atmosphere:
- **CO₂ → O₂ by electrolysis.** The chemistry is proven (a Mars analogue: peak rate 10.56 g/h[^9]), the demonstrated scale is 391–554× (nearly three orders of magnitude, not exactly) below what's needed for 118–167 people at the standard 0.84 kg O₂/person/day rate.
- **N₂ → breathing buffer, feedstock for nitrogen fixation.**
- **Cloud aerosol**, not a gas but droplets of H₂SO₄+H₂O solution with dissolved metals (iron oxide has been detected), per a reanalysis of Pioneer Venus 2 probe data (September 2025)[^10], about 60% of droplet mass is water, not 25% as previously thought. Extraction uses impaction separators (droplets settle inertially on an obstacle in the flow, the light gas passes by, the standard fog-harvester principle), after which fractional distillation separates water and acid by vapor-pressure difference, with metals left behind as sediment/sulfates after separation. Household demand (drinking plus hygiene, excluding the bioreactor and industrial processes) is 1077–1524 t/year per platform (118–167 people, 25 L/person/day); the extraction rate itself (kg/hour per separator) is not estimated, there is no data on droplet density in Venus's clouds or separator performance, an honestly open question.

**From the surface, by short-lived probes:** basalt rock (data from Venera-13/14 and Vega-2[^11], measurement precision low): silicon, basalt fiber, iron, probably titanium. Lifting a sample back up has never been flown, but the physics of lift right at the bottom is trivial: CO₂ density there is almost two orders of magnitude (~76×) higher than at platform altitude, so a capsule of tens of kilograms needs a balloon only about a meter across. The limiter is the survivability of the deployment mechanism at 462°C for the duration of landing; the drill and pump for loading the sample are moving actuators under load, not a static chip (521 hours is the record specifically for a static SiC circuit), so this is a separate, probably harder question within the same materials science, not the same problem restated.

**Production:** carbon chemistry on the daytime surplus, on the order of 1300–1400 t/year, estimated; food biomass from enclosed bioreactors, limited by phosphorus (absent from the atmosphere and present only in negligible amounts in basalt). Physically shipping product off Venus anywhere does not pay off, the platform is not in microgravity, so the argument that justifies orbital manufacturing on the ISS does not apply here; the role of production is import substitution for the station itself.

---

## Critical imported components

What technically cannot be produced locally under any development of the described architecture:

- **Lithium for storage.** Basalt is not the rock type where it concentrates, and there is in fact no data: the X-ray fluorescence instruments flown on landers are not physically sensitive to this element. The imported mass is not the whole battery (644–966 t) but only the metal (1.5–2.2% of pack mass, i.e. 10–22 t), assuming local assembly of the rest of the cell components.
- **Phosphorus for food production.**
- **Fluorine for fluoropolymers** (PTFE/FEP): in the atmosphere it exists only as trace HF, and capturing halogen from the gas phase at such concentrations has not been worked out; unlike basalt fiber, no case is made anywhere in this analysis for local production of the fluoropolymer skin. Volume is 95–236 t of fluorine per platform (for 100–250 μm film over the whole top and bottom of the dome's skin), a one-time construction item, not annual, but by mass an order of magnitude larger than the lithium import for the same platform (10–22 t).
- **Complex electronics, high-purity semiconductors, precision instruments, special alloys, and rare elements** absent from basalt.

---

## Legal status

Not "no man's land" and not an analogue of international waters, despite the first impression: the **Outer Space Treaty (1967)**[^12] directly prohibits national appropriation of sovereignty over celestial bodies (Venus falls under that definition), while preserving state responsibility and jurisdiction over registered objects and their personnel, a logic close to flag-state jurisdiction for ships, not an unpeopled legal void. The practical gap lies elsewhere: law enforcement at interplanetary distance for a truly autonomous colony materially independent of Earth (see the fleet growth trajectory above) is an open question, there is no precedent for a permanent extraterrestrial population in international law. The question is not pursued further here, it belongs to law and policy, not engineering.

---

## Emergencies, medicine, recreation, body disposal

**Evacuation.** A local accident on one platform means evacuation to a neighboring platform in the same wind layer, using the same mooring transport as ordinary cargo exchange, a short flight. Evacuating Venus entirely is the bottleneck: the only route to orbit is the hub platform's rocket stage, meaning not a fast-response tool but a rare operation limited by the throughput of a single point in the fleet.

**Medicine.** A basic unit (stabilization, first aid, minor procedures) is standard equipment on every habitat platform. Complex, rarely used equipment (surgery, long-term treatment) follows the same logic as the rest of the expensive infrastructure, concentrated at one point in the fleet rather than duplicated everywhere.

**Recreation**, unlike medicine, is not centralized: it is part of the standard module set on every habitat platform, not a scarce resource that benefits from concentration.

**Body disposal.** The station is a loop closed on most resources with an explicitly identified deficit, and phosphorus is one of the elements in shortest supply. The engineering-consistent option is to return matter to the same bioreactor cycle as the rest of the organics. This is not a prescribed engineering solution but a question of the colony's own culture and norms, named here only as an open fork.

**Pets** follow the same logic as recreation: not centralized, but competing for the same scarce resources (water, the phosphorus food cycle) as food production. A realistic scale is small, metabolically cheap species within the margin of the bioreactor system, not large animals; distributed by the decision of a given platform's community, not guaranteed by default.

**Childbirth** is not physiologically blocked: the station's gravity of 0.904 g (not the microgravity of orbital stations) removes the main documented class of developmental problems in weightlessness. Radiation shielding is calculable: the atmospheric column above the platform (0.49 atm) gives about 560 g/cm² of mass overhead, about 54% of Earth sea-level (~1033 g/cm²), noticeably more than at airliner cruise altitude but less than Earth's surface.

Fig. 7. Atmospheric column: sea level, airliner altitude, platform.

That said, there is no direct precedent anywhere for gestating and raising a human being off Earth, regardless of gravity or shielding.

In terms of resources, a child's birth occupies the same fixed platform capacity (118–167 people) as the arrival of a new colonist: unlimited childbirth is not compatible with that capacity, population growth of this kind requires growing the number of platforms at the same rate as any other fleet expansion, not a separate budget. The family sector is the habitat platforms, not the industrial-chemical ones (isolated by risk for good reason), not the hub (rocket propellant, logistics), and not the field-work part of the research platform. The specific rules for allocating births against capacity are the same question of colony politics and culture as the legal status above, not something the platform's engineering resolves.

---

## What was considered and rejected

- **Coaxial wind-rotor discoid**, a pair of coaxial disks with a turbine on the shared axis, spun by wind shear between layers. Rejected on physics: an actuator disk applied to the wrong geometry, wind shear overstated by 4–5×, an overestimate of power by about 1400×, the real output is kilowatts.
- **Tether to the surface**, a heat engine running on the temperature gradient, energetically competitive (37% real efficiency, below the 59.8% Carnot limit between the surface and the platform), but dropped over materials science (521 hours of electronics demonstration against the decades of service actually needed) and wind shear loading along the lower stretch of the tether near the surface: qualitatively noticeably larger than the axial tension the tether would otherwise be sized for, but the exact load value and the resulting cross-section diameter/mass are not backed by primary data and are not given here.
- **Lightning energy harvesting via a laser-guided channel.** The very existence of lightning on Venus is unconfirmed, only indirect signs exist. Laser-guided discharge has been tested on Earth only over 50 m and for diverting a strike, not for harvesting energy, rejected at the idea stage.
- **Chemical energy from the atmosphere**, the idea of drawing energy from CO₂ reacting with hydrogen (the Sabatier reaction, CO₂+4H₂→CH₄+2H₂O) instead of the station's solar panels. Doesn't work: CO₂ is already fully oxidized, there is nowhere further for it to release energy, and the reaction as an energy source is a net loss, returning only 14% of what's invested.
- **Orbital laser relay**, the idea of beaming power from a satellite down to the platform. Doesn't work: the platform sits inside the most scattering layer of the clouds itself, the beam loses collimation there just as in NASA NIAC's own estimate (100 kW → 4.9 nW, 14 orders of attenuation)[^13], the same order of magnitude.
- **Lithium-free storage chemistry** (LFP/Na-ion), considered for its slower degradation in heat (Li-ion loses capacity 3.1× faster at 55°C than at 25°C). Became unnecessary once the platform altitude was fixed at 22°C, the degradation that motivated the search for a replacement no longer applies.
- **An engine on the water-collecting aerobot instead of a tether**, the idea of replacing the separator buoy's tether (65–70 km) with active thrust to independently hold the needed relative airflow speed over the nets. Rejected on fuel burn: the separator sail's thrust (220–454 kN) requires 59–132 kg/s on methane-oxygen, 36–79 t of propellant for a 10-minute collection run, against the ~100 kg payload of a vehicle in this class and the grams-to-kilograms maneuvering fuel used by tugs at docking. The engine doesn't remove the load, it reproduces the same load using expendable propellant instead of a one-time structure.
- **A single breathable atmosphere (O₂+N₂) instead of H₂ as the lifting gas**, not rejected as wrong, a real trade-off with a real price on both sides, not adopted for the base (habitat) design. The same principle that already provides lift (any gas lighter than local CO₂, 44 g/mol) works for ordinary air (~29 g/mol) too, not just H₂, the difference is only in efficiency: H₂'s lift per cubic meter of cell is 2.80× that of air. It removes the whole class of problems tied to keeping environments separate: H₂ diffusion loss through the skin and the water budget that goes with it (see open questions), airlocks between load-bearing cells and habitable compartments, servicing in an oxygen mask, the pressure differential across the skin for a shared environment is close to zero (roughly 0.49 atm on both sides) rather than the driving force for diffusion H₂ has. The price is 2.8× more load-bearing cell volume for the same station mass: the platform's equivalent thickness grows from 11–21 m to 31–58 m, the thin-lens profile becomes three times thicker, with a corresponding rise in basalt-fiber consumption for structure and a wind/structural load on the thicker profile not computed here. The same mechanism that gives H₂ lift via impulse overheating (see "Propulsion") works for O₂+N₂ too: heating by +10/+20/+40 K raises air's lift by 6/12/23%, narrowing the gap with H₂ to 2.63×/2.49×/2.27×, but full parity is physically unreachable (it would need ~4000 K), and partial heating directly conflicts with the environment being shared: +40 K over 22°C is 62°C for the whole habitable atmosphere, not just the load-bearing volume, and heating only the load-bearing cells selectively gives back part of the original win (one shared environment with no internal partitions). It fits best on a habitat station with no production equipment: unlike the industrial-chemical platform, it has no own consumption of H₂ as a reagent (hydrocarbon synthesis there runs on the CO₂+H₂ reaction, see "Resources and production"), so giving up H₂ costs no other function, the trade-off becomes purely structure volume/mass against operational complexity, with no lost secondary use. Not for the fleet as a whole, and not for platforms with production, where H₂ is needed as feedstock regardless of its role as lifting gas.

---

## Open questions

- **Mass balance of the whole platform**, an end-to-end check on calibrated assumptions (not measurements from this project): basalt composite at 2000 kg/m³ (a real composite sheet, source Biswas et al. 2023)[^14], flexible thin-film panels at 2.5 kg/m² (real range 2–3 kg/m², ScienceDirect 2023)[^15], habitat modules at 50–75 kg/m² (TransHab gives ~62 kg/m² in open vacuum, NASA TransHab; Venus's conditions are milder)[^16]. The platform's total mass comes out to 2670–5020 t, and the average platform thickness required for that is 11–21 m, consistent with the ~20 m battery floats already stated. Not a rigorous proof, but the design is physically self-consistent within the precision of the assumptions, the numbers converge rather than stay silent.
- **Long-term gas-cell airtightness, over decades.** The best terrestrial analogue is NASA's superpressure stratospheric balloon (the GUSTO mission)[^17], 57 days of continuous flight. What's needed is on the order of 20+ years. The gap is about 127×, a measurable one, not a hypothetical.
- **H₂ diffusion through the fluoropolymer skin, quantitatively, why the skin defaults to two-layer Al patches rather than a monolithic coating, and the real total water budget once recycling is counted.** Household demand (25 L/person/day) is 1074–1521 t/year of gross consumption, but with ECLSS recycling at ISS levels (90–98%: urine + humidity condensate, before and after the Brine Processor Assembly)[^18] the fresh water actually needed for household use is 21–152 t/year, recycling saves 1053–1369 t/year. Pure PTFE's permeability to H₂ is 80–90 Barrer[^19], the skin is 100–250 μm over the whole top and bottom of the dome's area (565,480 m²), pressure differential 0.49 atm: leakage without coating is 191–537 t/year, replenished by water electrolysis (2H₂O→2H₂+O₂, mass ratio 8.94:1): 1705–4796 t/year. A single coating layer cuts leakage to 3.6–4.1% of the original (measured for PET, not PTFE-specific, cross-checked against an independent source giving the same order, 2–4%)[^20], 6.9–22.0 t/year. Thin (~60 nm) aluminum oxide barrier layers begin cracking at only about 0.75% strain[^22], and a surface energy balance for the skin's daily heating (forced convection in CO₂ at 66–70 m/s[^2], gas properties from[^23])[^24] gives a swing of 18–42 K, which with PTFE's coefficient of thermal expansion[^25] gives a strain of 0.23–0.55%, an order-of-magnitude estimate (the Nusselt correlation is calibrated up to Re=10⁷, here Re~10⁹, two to three orders above its validated range), but already comparable to a monolithic layer's cracking threshold. That's why the skin defaults to two independent layers of hex patches with offset seams rather than one layer: a continuous free-standing metal film ruptures above ~1% strain, while an "island" geometry of the same metal on an elastic substrate withstands up to 35% macroscopic strain without cracking the metal, because stretching takes the path of least resistance through the seams between islands rather than tearing the metal itself[^21], a two-order-of-magnitude margin over the computed 0.23–0.55%. The segmented geometry has its own limiting failure mode, delamination (an island peeling off the substrate) rather than metal cracking: onset is around 10–20% strain for a weakly bonded island, and does not occur at all up to 40%+ for a strong or tough bond, so even the low end is an order of magnitude above the computed strain. Patches join by overlapping (like scales) or a butt seam sealed with metallized aluminum tape; they are stamped on the industrial-chemical platform and delivered and spot-replaced from outside by aerobots (see "Materials"). With defects independent by position between the two layers (seams offset, a running-bond pattern), leakage doesn't add, it multiplies: 0.25–0.90 t/year, 2-3 orders below the single-layer figure, at a mass cost of just 46 kg (92 kg total for the whole skin, against 124–311 t of film), not a compromise. This is an upper bound on the effect (full independence of defects between layers isn't measured for this specific geometry, only for packaging laminates in general), but even partial correlation leaves an orders-of-magnitude margin. Replenishment water at two layers (default): 2.2–8.1 t/year, 1.5–37.5% of the post-recycling household budget, not the dominant line item it was at one layer (40–915%). The real total fresh-water requirement (household after recycling plus patched leak replacement) is 24–160 t/year, several times less than both the 1135–1718 t/year without recycling and the 83–349 t/year with a single coating layer. One question remains unresolved either way: the separator's actual extraction rate (kg/hour) is not estimated, whether it can deliver even 24, let alone 160, t/year is unknown. Patches are replaced individually and on demand (above), so the question isn't whether the skin itself survives long-term, but how fast a patch's seam and coating actually degrade in practice, i.e. what replacement frequency operations actually require; that degradation rate itself isn't computed.
- **The real wind profile by altitude** is not mapped precisely enough for final shear and aerobot-navigation calculations between layers.
- **Electronics and deployment-mechanism survivability at 462°C for the duration of a probe's landing** is the same unresolved materials-science question as everywhere else in this environment, and it matters for lifting samples from the surface.
- **Phosphorus for food production** is likely a permanent import item, no local-feedstock alternative is in sight. Volume is 258–366 kg/year per platform (118–167 people), a ceiling under zero recycling: this is the phosphorus in the bioreactor's daily biomass (70–100 kg/day dry mass, ~1% of which is phosphorus), not the fraction actually absorbed by people, the RDA (0.7 g/person/day) gives only the body's physiological minimum, not the flow through the bioreactor, and that figure was previously named as the ceiling in error. The profile is the inverse of fluorine: small by one-time mass but ongoing rather than one-off; actual external import is smaller than the ceiling by however much return from body disposal recycling contributes (not measured).
- **A local alternative to the fluoropolymer barrier layer** was not considered, the whole analysis assumes fluorine import (see critical imports), and a material substitution built around local feedstock has not been worked out.
- **The NASA NIAC numbers for the orbital laser relay** (100 kW → 4.9 nW, 14 orders of attenuation): the report's qualitative conclusion (Brandon, NIAC Phase I, 2019) is confirmed (a beam from orbit indeed does not get through), but that specific pair of numbers is not confirmed in the sources found, not a story invented from nothing the way the tether case was, but the precise source for them was not located.
- **A cloud-water separator cannot be fixed to the platform's own body.** The platform drifts with the atmosphere (see "Environment" above), so the flow hitting a separator mounted on it is not the 66–70 m/s wind[^2] but a speed difference that is close to zero right at the platform: sizing the cross-section by the full wind speed for this geometry is wrong in principle, not just in the precision of the numbers. The working approach is a tether/buoy lowered into a layer with wind shear by altitude (the same principle already used by the JPL Variable-Altitude Aerobot[^6]), where the relative flow is set by the shear, not by the platform's own motion. Estimating LWC from mode-2 cloud droplets (2 μm, 50 cm⁻³ below 58 km, density 1.8 g/cm³)[^26] and a 60% water fraction[^10] gives 0.377 mg/m³, but mode 3, which usually carries most of the fog's mass, is tied in the sources found to the lower tier (48–50 km), not to platform altitude (55.7 km, the middle tier), and that fraction cannot be carried over to the middle altitude without verification. Raising the separator on a tether into the upper tier (65–70 km) gives a shear-driven relative flow of only 30–34 m/s (platform speed corrected per VEGA-1/2[^2], twice the earlier estimate of 50–55 m/s, so the difference from the upper tier is noticeably smaller than it looked before) and a known mode-2 number density, 100 cm⁻³ above 58 km[^26]. That gives a cross-section of 2220–3560 m² (side ~47–60 m), in fact the same order as the physically invalid "fixed" case (2160–3240 m²), meaning raising the tether upward barely helps once the platform's speed is corrected. Lowering the tether down into the lower tier (48–50 km, where mode 3 sits) is not calculated for comparison: wind speed there is not sourced either in Wikipedia/Venera/VEx[^1] or in VEGA (which only measured ~54 km[^2]), the same data gap as with the 40–55 km segments, just moved to a different boundary. The separator sail's thrust at 65–70 km (CO₂ density ~0.22 kg/m³): 220–454 kN; the tether under it (twisted basalt-fiber rope, 1149 MPa[^27], 3× margin) is 27–39 mm in diameter, but its own weight (14–45 t) already gives 124–397 kN, 56–88% of the sail's thrust, and drag on the tether itself along its full length (not included in the cross-section) adds roughly another half of that thrust on top. The tether's weight and windage are comparable in order of magnitude to the load it has to hold, the problem does not close in one pass, it needs an iterative cross-section recalculation not done here. A separate alternative is a passive, engineless collector aerobot (net-towing was rejected above on fuel burn): in steady flight it drifts with its layer just as the platform does, so real collection is only possible during the transient moment of crossing the shear boundary, not "in flight" between altitudes. The energetics of climbing/descending are themselves computed the same way as for the platform (see "Propulsion" above), but the mass of such a vehicle specifically, the duration, and the efficiency of the transient window are nowhere sourced, neither rejected nor confirmed, an honestly unevaluated alternative.

---

## Acknowledgments and a note on method

Calculations (`venus_calc/verify.py`), figures (`preprint/make_figures.py`), and the document text were developed in extended dialogue with AI systems (Claude, Anthropic; Gemini, Google), used as tools for computation, source search and verification, and stress-testing claims; some of the analysis Gemini proposed (including a PTFE permeability constant and a cloud liquid-water-content estimate for a dynamic-buoy collection scheme) did not survive independent verification and was not included in the document, that is also part of the method, not only the results that were kept. Responsibility for all statements rests with the author.

---

## Sources

[^1]: Atmospheric T/P/wind profile: Wikipedia (Atmosphere of Venus), Venera/Venus Express data.
[^2]: Sagdeev, R.Z. et al., 1986. Determination of Venus winds by ground-based radio tracking of the VEGA balloons, 66.0 and 69.4 m/s at ~54 km (VEGA-1/2, VLBI): [Science](https://www.science.org/doi/10.1126/science.231.4744.1414).
[^3]: Eden Project, ETFE glazing film (50–200 μm per layer): [Eden Project](https://www.edenproject.com/mission/architecture).
[^4]: NASA X-57 Maxwell, battery 149 Wh/kg (pack), 225 Wh/kg (cell): [NASA NTRS](https://ntrs.nasa.gov/api/citations/20180005737/downloads/20180005737.pdf).
[^5]: ISS, power 84–120 kW, NASA's official figure for the original 8 arrays, before the iROSA upgrade (after which it became 160–215 kW, a different configuration, not a discrepancy): [NASA](https://www.nasa.gov/image-article/solar-arrays-international-space-station-2/).
[^6]: JPL Variable-Altitude Aerobot, Black Rock Desert tests, July 2022: [JPL](https://www.jpl.nasa.gov/news/jpls-venus-aerial-robotic-balloon-prototype-aces-test-flights/), [arXiv:2411.06643](https://arxiv.org/abs/2411.06643).
[^7]: ESA MELiSSA, closed-loop life support: [ESA](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Melissa/Targets_Scientific_domains).
[^8]: NASA Glenn/GEER, 521 hours of SiC electronics at 460°C/93 atm: [NASA](https://www.nasa.gov/news-release/nasa-glenn-demonstrates-electronics-for-longer-venus-surface-missions/).
[^9]: MOXIE, peak 10.56 g/h O₂: [NASA Science](https://science.nasa.gov/blog/moxie-sets-consecutive-personal-bests-and-mars-records-for-oxygen-production/).
[^10]: Cloud aerosol, 60% water by mass: reanalysis of Pioneer Venus 2 data, J. Geophysical Research: Planets, September 2025, [phys.org](https://phys.org/news/2025-10-venus-clouds-reanalyzed.html), [Cal Poly Pomona](https://www.cpp.edu/news/content/2025/09/venus-cloud-aerosols-contain-reservoirs-of-water-and-iron/index.shtml).
[^11]: Surface (basalt), Venera-13/14, Vega-2, X-ray fluorescence analysis: [Mineralogy of the Venus Surface, Space Science Reviews](https://link.springer.com/article/10.1007/s11214-023-00988-6).
[^12]: Treaty on Principles Governing the Activities of States in the Exploration and Use of Outer Space, including the Moon and Other Celestial Bodies, 1967 (UNTS, vol. 610, No. 8843): [UNOOSA](https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/introouterspacetreaty.html), [treaty text, UN](https://treaties.un.org/doc/publication/unts/volume%20610/volume-610-i-8843-english.pdf).
[^13]: Brandon, N., NASA NIAC Phase I, 2019. Power beaming by laser through the Venus atmosphere: [NIAC report](https://www.nasa.gov/wp-content/uploads/2019/04/niac_2019_phi_brandon_powerbeaming_tagged.pdf).
[^14]: Basalt composite, 2000 kg/m³: [Biswas et al., Polymer Composites, 2023](https://4spepublications.onlinelibrary.wiley.com/doi/abs/10.1002/pc.27238).
[^15]: Flexible thin-film panels, 2–3 kg/m²: [ScienceDirect, 2023](https://www.sciencedirect.com/science/article/pii/S2772940023000218).
[^16]: TransHab, ~62 kg/m² (13,154 kg / ~212 m²): [Wikipedia](https://en.wikipedia.org/wiki/TransHab), [NASA NTRS](https://ntrs.nasa.gov/api/citations/20160011581/downloads/20160011581.pdf).
[^17]: GUSTO, 57 days 7 hours of continuous flight: [JHU APL](https://www.jhuapl.edu/news/news-releases/240224-nasa-gusto-mission-heavy-lift-balloon-record), [Wikipedia](https://en.wikipedia.org/wiki/GUSTO_(telescope)).
[^18]: NASA ISS ECLSS, water recycling 90% (standard operation, urine + humidity condensate) up to 98% (with the Brine Processor Assembly): [Space.com](https://www.space.com/astronaut-pee-iss-water-recycling-98-percent-milestone), [Interesting Engineering](https://interestingengineering.com/innovation/nasa-water-recyclability-drinking-sweat-urine).
[^19]: The permeability of gases through PTFE and other membranes at 25°C, 80–90 Barrer for H₂: [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0013468686871134).
[^20]: Investigation of gas permeation through Al-metallized film for vacuum insulation panels, 3.6–4.1% of original permeability: [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0017931012007077).
[^21]: Kowol, P., Bargmann, S., Görrn, P., Wilmers, J., 2023. Delamination Behavior of Highly Stretchable Soft Islands Multi-Layer Materials. Applied Mechanics, 4(2), 514-527: [MDPI](https://doi.org/10.3390/applmech4020029).
[^22]: US Patent 8,624,487 B2. Barrier film composite, display apparatus including the barrier film composite, method of manufacturing barrier film composite, and method of manufacturing display apparatus including the barrier film composite. ~60 nm aluminum oxide barrier layer cracking at ~0.75% strain: [USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8624487).
[^23]: Gaseous CO₂ properties at ~298 K, ~1 atm: viscosity ~1.5·10⁻⁵ Pa·s, thermal conductivity ~0.0166 W/(m·K), specific heat: [Engineering ToolBox — viscosity](https://www.engineeringtoolbox.com/carbon-dioxide-dynamic-kinematic-viscosity-temperature-pressure-d_2074.html), [Engineering ToolBox — thermal conductivity](https://www.engineeringtoolbox.com/carbon-dioxide-thermal-conductivity-temperature-pressure-d_2019.html), [Engineering ToolBox — specific heat](https://www.engineeringtoolbox.com/carbon-dioxide-d_974.html).
[^24]: Average forced-convection correlation for turbulent flow over a flat plate, Nu = 0.037·Re⁰·⁸·Pr^(1/3), valid for 5·10⁵ ≤ Re ≤ 10⁷: [tec-science](https://www.tec-science.com/thermodynamics/heat/calculation-of-the-nusselt-numbers-for-forced-flows-over-plates-and-in-pipes/).
[^25]: PTFE coefficient of linear thermal expansion, ~100–160·10⁻⁶ /K: [The Plastic Shop](https://www.theplasticshop.co.uk/ptfe-technical-information.html).
[^26]: Knollenberg, R.G., Hunten, D.M., 1980. The microphysics of the clouds of Venus: Results of the Pioneer Venus Particle Size Spectrometer Experiment. J. Geophys. Res. 85(A13), 8039–8058: [Wiley/AGU](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/JA085iA13p08039).
[^27]: Xie, J. et al., 2024. Experimental evaluation on the tensile behavior of a novel basalt fiber-reinforced polymer rope: effects of rope structure and abrasion, 1149–1218 MPa: [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5624222).

```{=latex}
\printendnotes
```
