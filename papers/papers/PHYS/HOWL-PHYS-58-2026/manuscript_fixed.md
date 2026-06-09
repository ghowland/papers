# Channel Geometric Mismatch and the Domain Impedance Z

## The Velocity-Dependent L1/L2 Framework Applied to PCTRM Channel Mechanics

**Registry:** [@HOWL-PHYS-58-2026]

**Series Path:** [@HOWL-PHYS-55-2026] → [@HOWL-PHYS-56-2026] → [@HOWL-PHYS-57-2026] → [@HOWL-PHYS-58-2026]

**DOI:** 10.5281/zenodo.20617609

**Date:** June 2026

**Domain:** Physics / PCTRM / Channel Mechanics / L1/L2 Conversion Theory

**Status:** Complete (Layer 1). Experimental verification pending.

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. THE CHANNEL VELOCITY PRINCIPLE

Every physical interaction in the PCTRM framework is mediated by a channel. A channel extends adjacency between two solitons — two stable, self-sustaining patterns in the substrate's discrete arithmetic. Channels have endpoints, direction, throughput, and activation state. These properties are specified in the PCTRM master specification. This paper identifies one additional property that has not been made explicit: every channel has a characteristic propagation velocity, and that velocity determines the channel's geometric ratio.

The geometric ratio β was established in prior work as the conversion factor between rectilinear (L1) and Euclidean (L2) measurements on circular geometry. At rest, β =  $\pi$ /4 ≈ 0.785. A separate result showed that β is not a constant but a function of velocity: β(v) = E(v/c)/(1 + 1/γ), where E is the complete elliptic integral of the second kind and γ is the Lorentz factor. At v = 0, β =  $\pi$ /4. At v = c, β = 1. The geometry transitions continuously from circular to rectilinear as velocity increases. [@HOWL-MATH-13-2026]

Applying this result to channels: if a channel's content propagates at velocity v_ch, the channel's geometric ratio is β(v_ch). An electromagnetic channel propagates at c — photons advance one cell per tick by substrate construction. Its β is 1. The geometry of electromagnetic propagation is fully rectilinear. A thermal channel propagates at molecular thermal velocity — for room-temperature air, approximately 500 m/s, giving v/c ≈ 1.7  $\times$  10⁻⁶. Its β is indistinguishable from  $\pi$ /4. The geometry of thermal molecular interaction is fully circular at any achievable measurement precision.

The full PCTRM channel catalog, with propagation velocity and geometric ratio for each type, is as follows.

**Electromagnetic channels** propagate at c. This is structural — the photon pattern advances one cell per tick with no Higgs interaction to reduce its advance rate. β_channel = 1. These channels mediate charge-to-charge interaction and are always active between charged solitons.

**Gravitational drain channels** propagate at c. Gravitational waves propagate at light speed in both general relativity and PCTRM. The drain from parent to child soliton is applied per tick at the parent's hierarchy level, and the information about the drain configuration propagates at c. β_channel = 1.

**Strong confinement channels** operate within the nucleon boundary. Quarks within a nucleon are effectively relativistic — their velocities are close to c within the confinement region. Color charge propagates at speeds near c. β_channel is close to 1 but not exactly 1, because massive quarks move at less than c. The precise value depends on the quark effective velocity within the nucleon.

**Strong residual channels** operate between nucleons, conditional on proximity. The mediating mechanism is pion exchange. The pion mass (≈ 140 MeV) gives a characteristic velocity that depends on the interaction energy. At nuclear energy scales, v/c is of order 0.1–0.3 for the pion. β_channel is close to  $\pi$ /4 but with small corrections.

**Weak channels** are conditional on specific interaction events. The W and Z bosons are massive (80.4 and 91.2 GeV respectively) and short-lived. The relevant propagation velocity depends on the interaction energy relative to the boson mass. At low energies (below M_W), the effective propagation is slow and β_channel is close to  $\pi$ /4. At electroweak scale energies, the channel becomes relativistic and β_channel moves toward 1.

**Thermal channels** propagate at molecular thermal velocity. For a gas at temperature T, the thermal velocity is v_th = √(3k_BT/m). At room temperature for nitrogen: v_th ≈ 515 m/s. v/c ≈ 1.7  $\times$  10⁻⁶. β_channel =  $\pi$ /4 to better than one part in 10¹². These channels are omnidirectional and always active.

**Higgs channels** modulate per-tick cost for massive solitons. The Higgs interaction is local to the soliton — it operates at the soliton's own position, not across a distance. The relevant velocity is the soliton's velocity through the substrate, which determines the geometric context in which the Higgs tick-cost is applied. β_channel = β(v_soliton).

**Entanglement channels** have binary activation triggered by specific interactions. Once established, the channel-sharing between two solitons makes them one pattern with two handles. The channel does not propagate in the conventional sense — it is a graph relationship, not a spatial traversal. Assigning a velocity to entanglement channels requires care. The correlation is instantaneous in the graph but does not transmit usable information. For the purposes of geometric mismatch, entanglement channels are excluded from the β analysis because they do not have a well-defined propagation velocity.

The principle is general. Every channel that propagates through the substrate has a velocity. That velocity determines the channel's geometric ratio via the MATH-13 formula. The channel's β is as physical as its throughput or its direction. It is a property of how the channel's content traverses the substrate's cell geometry.

---

## II. THE MISMATCH EQUATION

A physical interaction involves a geometry and a channel. The geometry is the cross-section through which the interaction occurs — a pipe bore, an antenna dish, a capacitor plate, a scattering target. The channel is the mechanism that carries the interaction's content — fluid molecules, electromagnetic waves, thermal photons, gluon flux.

The geometry has a β determined by its shape and its velocity relative to the observer. For a stationary circular cross-section, β_geom =  $\pi$ /4. For a moving one, β_geom = β(v_geom) from MATH-13.

The channel has a β determined by its propagation velocity. β_channel = β(v_channel).

The unified equation from MATH-1 is Q = F · β · d² · Z, where β · d² is the geometric invariant (the circular cross-section as a fraction of its rectilinear bounding area) and Z is the domain-specific impedance. The equation was written with β =  $\pi$ /4 as a constant. MATH-13 showed β depends on velocity. PHYS-58 now decomposes Z into its geometric and mechanical components.

The decomposition is:

**Z = Z_mismatch · Z_mechanical**

Z_mismatch is the geometric coupling between the cross-section's velocity regime and the channel's velocity regime:

**Z_mismatch = β_geom / β_channel**

When geometry and channel are at the same velocity, Z_mismatch = 1. The coupling is geometrically perfect — both are in the same L1/L2 regime. Whatever impedance exists is entirely mechanical.

When the geometry is at rest and the channel propagates at c, Z_mismatch = ( $\pi$ /4)/1 =  $\pi$ /4 ≈ 0.785. The rest-frame circular geometry couples to the rectilinear channel geometry at a maximum efficiency of 78.5%. The remaining 21.5% is not lost to friction or diffraction or turbulence. It is lost to the geometric mismatch between circular and rectilinear measurement — the same gap that the staircase paradox measures, the same gap that β quantifies, now appearing as a coupling ceiling in a physical interaction.

Z_mechanical is everything else. Friction in pipes. Turbulence at orifices. Diffraction at antenna edges. Surface roughness in emitters. Feed blockage in dishes. These are mechanical properties of the specific system that reduce coupling below the geometric ceiling. Z_mechanical ≤ 1 always, with equality for a mechanically perfect system.

The total Z is therefore bounded:

**Z ≤ Z_mismatch = β_geom / β_channel**

No mechanical improvement can push Z above the geometric ceiling. A perfect antenna with zero diffraction loss, zero feed blockage, and zero surface error still cannot exceed  $\pi$ /4 efficiency when coupling rest-frame circular geometry to c-frame electromagnetic radiation. The geometry sets the ceiling. The mechanics set the floor.

---

## III. THE NINE DOMAINS DECOMPOSED

The nine cross-section domains from the original β observation are now re-examined with their channel types identified, channel velocities assigned, and Z decomposed into geometric and mechanical components. [@HOWL-MATH-1-2026]

### 3.1 Pipe Flow

**Channel type:** Thermal/molecular interaction between fluid and pipe wall. Fluid molecules bounce off the wall surface, exchanging momentum. The interaction is mediated by molecular contact at thermal velocity.

**Channel velocity:** Thermal molecular velocity. For water at room temperature: v_th ≈ 640 m/s. For air: v_th ≈ 515 m/s. In all cases v/c < 10⁻⁵.

**Channel β:**  $\pi$ /4 to better than 10⁻¹⁰.

**Geometry β:**  $\pi$ /4 (stationary pipe).

**Mismatch:** ( $\pi$ /4)/( $\pi$ /4) = 1.

**Z_mismatch:** 1. No geometric ceiling.

**Z_mechanical:** The friction factor f. Depends on Reynolds number, wall roughness, flow regime. Ranges from approximately 0.01 (smooth turbulent) to 0.1 (rough turbulent). No geometric bound constrains it — its value is entirely determined by the mechanical properties of the flow and the wall.

**Assessment:** Pipe flow Z is purely mechanical. The channel and the geometry are in the same velocity regime. The β framework adds no geometric constraint. This is expected: pipe flow involves no interaction between different velocity regimes.

### 3.2 Drag

**Channel type:** Pressure and shear interaction between fluid and body surface. Momentum transfer through molecular collisions at the surface, pressure distribution from the flow field, wake formation behind the body.

**Channel velocity:** Free-stream velocity for the pressure distribution, thermal velocity for the molecular interactions at the surface. Both non-relativistic.

**Channel β:**  $\pi$ /4.

**Geometry β:**  $\pi$ /4 (stationary or slowly moving sphere).

**Mismatch:** 1.

**Z_mismatch:** 1.

**Z_mechanical:** Drag coefficient C_d. Depends on Reynolds number, surface roughness, Mach number, body shape. Ranges from approximately 0.05 (streamlined body) to greater than 1.0 (bluff body). No geometric ceiling — the drag coefficient can exceed 1 because the effective drag area can exceed the geometric cross-section (through wake effects).

**Assessment:** Same as pipe flow. No mixed-regime interaction. Z is purely mechanical.

### 3.3 Orifice Flow

**Channel type:** Fluid mechanics through a constriction. Same molecular interaction regime as pipe flow and drag.

**Channel velocity:** Thermal/flow velocity. Non-relativistic.

**Channel β:**  $\pi$ /4.

**Geometry β:**  $\pi$ /4.

**Mismatch:** 1.

**Z_mismatch:** 1.

**Z_mechanical:** Discharge coefficient C_d ≈ 0.61 for a sharp-edged orifice. The value is less than 1 due to the vena contracta — the flow contracts downstream of the orifice, and the effective flow area is smaller than the geometric opening. This is a purely mechanical (fluid dynamics) effect.

**Assessment:** No β mismatch. Z is entirely mechanical. The 0.61 value of C_d has been measured and computed from fluid dynamics for over a century. The β framework adds no geometric constraint.

### 3.4 Circular Plate Capacitor

**Channel type:** Electromagnetic. The electric field between the plates is established and maintained by charge on the plates. The field itself was established at c (electromagnetic information propagates at c), but the operational state is static — no energy is propagating, the field just sits between the plates.

**Channel velocity:** This is the bridge case. The field was established at c. The charges are stationary. The channel has two phases: a dynamic establishment phase (electromagnetic, v = c, β = 1) and a static maintenance phase (electrostatic, v = 0, β =  $\pi$ /4).

**Channel β:** Context-dependent. For the static capacitor, the relevant β is the maintenance phase: β_channel =  $\pi$ /4.

**Geometry β:**  $\pi$ /4 (stationary plates).

**Mismatch:** 1 (both geometry and channel are in the rest frame during static operation).

**Z_mismatch:** 1.

**Z_mechanical:** ε₀/t, where ε₀ is the permittivity of free space and t is the plate separation. The permittivity ε₀ is an electromagnetic property of the substrate — it describes how the electromagnetic channel interacts with the vacuum. The /t is geometric (inverse separation). The ε₀ itself contains factors of 4 $\pi$  through its relationship to Coulomb's law: F = e²/(4 $\pi$ ε₀r²). The 4 $\pi$  = 16β² represents two L1/L2 conversions in the electromagnetic field geometry (one per transverse dimension). These are counted in the electromagnetic coupling constant, not in Z.

**Assessment:** The capacitor's Z is electromagnetic substrate properties (ε₀) combined with geometry (1/t). The β mismatch is unity for the static case. The interesting question is whether a rapidly charging or discharging capacitor — where current flows and the field changes at rates approaching c — develops a β mismatch during the dynamic phase. This is beyond the scope of the static analysis.

### 3.5 Poynting Flux Through Circular Aperture

**Channel type:** Electromagnetic propagation. Photons traverse the aperture at c.

**Channel velocity:** c.

**Channel β:** 1.

**Geometry β:**  $\pi$ /4 (stationary aperture).

**Mismatch:** ( $\pi$ /4)/1 =  $\pi$ /4.

**Z_ideal:** 1 in the standard equation.

This requires careful counting. The unified equation is Q = F · β · d² · Z. The factor β · d² already converts the rectilinear bounding area d² to the circular aperture area  $\pi$ d²/4. The radiation propagating at c with β_channel = 1 "sees" the full bounding area d². The aperture passes only β · d² = ( $\pi$ /4)d² of that. The mismatch is already counted in the β · d² factor.

**Z_mismatch:** Already inside β · d². Not double-counted.

**Z_mechanical:** 1 for an ideal aperture (no edge effects, no thickness, no diffraction). For a real aperture, Z_mechanical < 1 due to edge diffraction at the aperture boundary.

**Assessment:** The Poynting case reveals that for electromagnetic channels at c interacting with rest-frame geometry, the β mismatch IS the β · d² factor. The unified equation already captures the mismatch. Z = 1 for the ideal case because no additional impedance exists beyond what β · d² already describes.

### 3.6 Antenna Effective Aperture

**Channel type:** Electromagnetic at c. Radiation arrives from a distant source and is collected by the dish.

**Channel velocity:** c.

**Channel β:** 1.

**Geometry β:**  $\pi$ /4 (stationary dish).

**Mismatch:**  $\pi$ /4 (same as Poynting — the aperture is circular, the radiation is rectilinear at c).

**Z = η:** Aperture efficiency. Measured values: 0.55–0.75 for typical parabolic dishes. The standard antenna literature gives the theoretical maximum for a uniformly illuminated circular aperture as approximately 0.83 (for optimal edge taper), with practical designs achieving 0.55–0.75 due to edge diffraction, feed blockage, spillover, and surface errors.

The β mismatch framework predicts Z ≤  $\pi$ /4 = 0.7854 as the geometric ceiling, with Z_mechanical accounting for the reduction below this ceiling.

The measured maximum efficiencies of 0.75 fall below  $\pi$ /4 = 0.785. The theoretical maximum with optimal taper is quoted at approximately 0.83 in some references, which would exceed  $\pi$ /4. However, this 0.83 figure includes the effect of non-uniform illumination that effectively changes the aperture shape from circular to a weighted profile — no longer a simple circular cross-section.

The prediction is specific: for a uniformly illuminated circular aperture with no mechanical losses, the maximum efficiency is  $\pi$ /4. Real antennas fall below this due to Z_mechanical. The 0.83 figure from optimal taper represents a different geometry (weighted illumination, effectively non-circular) where the β analysis would need to account for the modified cross-section shape.

**Assessment:** This is the strongest prediction from the mismatch framework. The geometric ceiling at  $\pi$ /4 is testable. The key test is whether any uniformly illuminated circular antenna has been measured with efficiency exceeding 0.785. The literature survey is pending.

### 3.7 Gaussian Beam Cross-Section

**Channel type:** Photon propagation at c.

**Channel velocity:** c.

**Channel β:** 1.

**Geometry β:**  $\pi$ /4 (beam cross-section as measured in the lab frame).

**Mismatch:**  $\pi$ /4.

**Z = 1/M²:** Beam quality factor. M² = 1 for a perfect TEM₀₀ Gaussian beam. M² > 1 for real beams with phase distortions, higher-order modes, or thermal lensing.

The mismatch framework says the beam's coupling to any rest-frame circular aperture is bounded by  $\pi$ /4, and M² measures additional degradation. A perfect beam (M² = 1) couples at the geometric maximum. An imperfect beam couples at less than the geometric maximum.

**Assessment:** Consistent with the framework. Z = 1/M² operates below the geometric ceiling, and the ceiling is already counted in the β · d² factor.

### 3.8 Stefan-Boltzmann Hemispheric Integration

**Channel type:** Thermal photon emission at c. The surface emits photons in all directions into the hemisphere above it.

**Channel velocity:** c.

**Channel β:** 1.

**Geometry β:**  $\pi$ /4 (stationary emitting surface).

**Mismatch:**  $\pi$ /4.

**Z = ε:** Emissivity. ε = 1 for a perfect blackbody. ε < 1 for all real surfaces.

The Stefan-Boltzmann constant is σ = 2 $\pi$ ⁵k_B⁴/(15h³c²). The  $\pi$ ⁵ = (4β)⁵ represents five L1/L2 conversions: three from the angular integration over the hemisphere (one per spatial dimension) and two from the Planck distribution integral (the ζ(4) =  $\pi$ ⁴/90 factor). These five conversions account for the full geometric coupling between the rest-frame surface and the c-frame radiation field.

If the five conversions already fully account for the surface-to-radiation coupling, then no additional β mismatch exists beyond what the Stefan-Boltzmann law already contains. Z_mismatch is already inside σ, not in the Z of the unified equation.

**Assessment:** The thermal case is similar to the Poynting case. The β mismatch between the rest-frame surface and the c-frame radiation is already counted in the physics — in this case, inside the Stefan-Boltzmann constant itself through the (4β)⁵ factor. Z = ε measures only the mechanical coupling of the surface to the radiation field (surface finish, material properties). The framework adds a geometric interpretation of the known constant but does not predict a new constraint.

### 3.9 Summary Table

| Domain | Channel type | v ch | β ch | β geom | Mismatch | Z mismatch | Z mechanical | Notes |
|---|---|---|---|---|---|---|---|---|
| Pipe flow | Thermal | ~500 m/s |  $\pi$ /4 |  $\pi$ /4 | 1 | 1 | f (friction) | No mismatch |
| Drag | Pressure/shear | ~thermal |  $\pi$ /4 |  $\pi$ /4 | 1 | 1 | C d (drag) | No mismatch |
| Orifice | Fluid | ~thermal |  $\pi$ /4 |  $\pi$ /4 | 1 | 1 | C d ≈ 0.61 | No mismatch |
| Capacitor | EM (static) | 0 (static) |  $\pi$ /4 |  $\pi$ /4 | 1 | 1 | ε₀/t | Bridge case |
| Poynting | EM at c | c | 1 |  $\pi$ /4 |  $\pi$ /4 | In β·d² | 1 (ideal) | Already counted |
| Antenna | EM at c | c | 1 |  $\pi$ /4 |  $\pi$ /4 | In β·d² | η = 0.55–0.75 | Ceiling at  $\pi$ /4 |
| Beam optics | Photon at c | c | 1 |  $\pi$ /4 |  $\pi$ /4 | In β·d² | 1/M² | M²=1 is ceiling |
| Thermal | Photon at c | c | 1 |  $\pi$ /4 |  $\pi$ /4 | In σ | ε = 0–1 | Already in σ |
---

## IV. TWO REGIMES OF Z

The nine domains separate into two clean regimes. The separation is not by physical domain — it is not about fluids versus electromagnetism versus thermal physics. It is about whether the channel and the geometry are in the same velocity regime.

### 4.1 Non-Relativistic Z

Pipe flow, drag, and orifice flow have channels propagating at thermal velocity and geometry at rest. Both are at β ≈  $\pi$ /4. The mismatch is unity. Z contains no geometric component. The impedance is entirely mechanical — friction, turbulence, wake structure, vena contracta.

In these domains, Z can take any value. There is no geometric ceiling. The drag coefficient can exceed 1 (bluff body drag where the effective area exceeds the geometric cross-section through wake effects). The friction factor can be very small (smooth pipe, laminar flow) or moderately large (rough pipe, turbulent flow). The discharge coefficient can be close to 1 (well-rounded orifice) or much less (sharp-edged orifice).

The β framework says nothing about these domains because there is nothing geometric to say. When channel and geometry share the same β, the conversion between L1 and L2 is the same on both sides, and no mismatch arises. This is not a failure of the framework — it is a correct identification that the framework's geometric content is absent in this regime.

### 4.2 Mixed-Regime Z

Poynting flux, antenna aperture, beam optics, and thermal radiation all have channels propagating at c (β = 1) and geometry at rest (β =  $\pi$ /4). The mismatch is  $\pi$ /4. A geometric ceiling exists.

In these domains, the β mismatch is already counted in the physics — either inside the β · d² factor (Poynting, antenna, beam) or inside a fundamental constant that contains the appropriate powers of  $\pi$  (Stefan-Boltzmann). The Z that appears in the unified equation measures only the mechanical coupling below the geometric ceiling.

The geometric ceiling is  $\pi$ /4 for each L1/L2 conversion. Domains with multiple conversions (thermal radiation with five) have the ceiling already compounded inside the relevant constant. The engineering Z (aperture efficiency, beam quality, emissivity) operates below the ceiling that the physics has already established.

### 4.3 The Capacitor as Bridge

The capacitor sits between the two regimes. The electromagnetic field that defines the capacitance was established at c, but the operational state is static. During steady-state operation, both the channel (static field) and the geometry (stationary plates) are at rest, and the mismatch is unity.

During transient operation — charging or discharging at high rates — the field changes propagate at c. The channel temporarily operates in the mixed regime. Whether this produces a measurable β mismatch effect on the transient capacitance is an open question. For typical electronic circuits, the transient propagation time across the capacitor gap is negligible (picoseconds for millimeter gaps). For extremely high-frequency operation or very large plate separations, the mixed-regime phase may become significant.

### 4.4 The Classification Principle

The two regimes are determined by a single question: does the channel propagate at a significantly different velocity than the geometry moves?

If no: Z is purely mechanical. No geometric ceiling. The β framework adds nothing.

If yes: Z has a geometric component from the β mismatch. A ceiling exists. The β framework identifies the ceiling and separates it from the mechanical impedance below the ceiling.

The question is frame-independent in the following sense: the channel propagation velocity is a property of the channel type (electromagnetic channels propagate at c, thermal channels at v_thermal), not of the observer. The geometry velocity is the velocity of the cross-section relative to the channel endpoints. The mismatch β_geom/β_channel is determined by the physics, not by the choice of reference frame.

---

## V. THE CROSSOVER ENERGY

The β mismatch between rest-frame geometry and c-velocity channels is exactly  $\pi$ /4 — a fixed ratio independent of the interaction energy. But the β of the geometry itself becomes velocity-dependent when the geometry is in motion. At what energy does the geometry's velocity become large enough for β(v_geom) to deviate measurably from  $\pi$ /4?

From MATH-13, β(v) deviates from  $\pi$ /4 by more than 1% at v/c ≈ 0.87, by more than 5% at v/c ≈ 0.95, and by more than 10% at v/c ≈ 0.97.

For a proton, the kinetic energy at various velocities is:

| v/c | γ | Kinetic energy | β(v) deviation from  $\pi$ /4 |
|---|---|---|---|
| 0.50 | 1.15 | 142 MeV | 0.13% |
| 0.87 | 2.03 | 968 MeV | ~1% |
| 0.90 | 2.29 | 1.21 GeV | 3.9% |
| 0.95 | 3.20 | 2.07 GeV | 6.8% |
| 0.99 | 7.09 | 5.72 GeV | 13.4% |
| 0.999 | 22.4 | 20.1 GeV | 22.1% |
| 0.9999 | 70.7 | 65.4 GeV | 25.6% |
The crossover energy — where the geometric correction exceeds typical measurement precision — is in the GeV range for protons. This is within the energy range of existing accelerator experiments. At LHC energies (6.5 TeV per proton, v/c = 0.9999999), the correction approaches the full mismatch of 27.3%.

The separate crossover from MATH-12 — the toroidal transition at four-loop QED — occurs at approximately 22 MeV (the energy where the muon Compton wavelength resolves toroidal structure in the electron anomalous magnetic moment). The velocity crossover at ~1 GeV and the toroidal crossover at ~22 MeV are different scales probing different aspects of the same geometric framework. The velocity crossover probes the v axis (how contracted is the geometry). The toroidal crossover probes the k axis (what manifold does the internal structure live on). Both move the effective β away from the rest-frame  $\pi$ /4.

At sufficiently high energy, both corrections are active simultaneously. A proton at LHC energies has its geometric cross-section contracted (v axis) and its internal structure probed at a scale that resolves toroidal gluon flux tubes (k axis). The full geometric description requires the three-parameter family β(p, k, v) from MATH-13, which has not been computed for combined non-trivial parameters.

---

## VI. CHANNEL β ACROSS THE HIERARCHY

PCTRM organizes matter into a soliton hierarchy with seven levels, from the substrate at Level 0 to the universal soliton at Level 6. At each level, characteristic channel types operate at characteristic velocities. The β of each channel follows from its velocity via the MATH-13 formula.

### Level 0 — Substrate

The substrate updates every cell every tick. This is not propagation in the conventional sense — it is the substrate's own per-tick arithmetic. No channel velocity is defined. The substrate is below the framework's domain of applicability.

### Level 1 — Subatomic

Strong confinement channels operate within nucleons. Quarks move at speeds close to c within the confinement boundary. The effective velocity depends on the quark momentum fraction carried during interaction. At the parton level, quark velocities are v/c > 0.99 for light quarks. β_channel is close to 1.

Electromagnetic channels at c (β = 1) mediate quark charge interactions. Gluon channels mediate color charge at c (massless gluons propagate at light speed within the confinement boundary). β_channel = 1 for gluon channels.

The geometry at this level — the nucleon cross-section — is small (r_p ≈ 0.88 fm) and effectively at rest in the nucleon's rest frame. β_geom =  $\pi$ /4 in the rest frame. The mismatch between the nucleon geometry (β =  $\pi$ /4) and the internal channels (β ≈ 1) is  $\pi$ /4 — the same mismatch as in the macroscopic electromagnetic domains.

### Level 2 — Atomic

Electromagnetic channels between nucleus and electrons propagate at c (β = 1). The electron orbital velocity in hydrogen is v/c ≈ α ≈ 1/137 for the ground state. β_geom for the orbital is indistinguishable from  $\pi$ /4. The mismatch is  $\pi$ /4.

The fine structure constant α = e²/(4 $\pi$ ε₀ℏc) ≈ 1/137 measures the strength of the electromagnetic coupling. The 4 $\pi$  = 16β² in the denominator is two L1/L2 conversions. The geometric framework identifies these as the same β mismatch operating at the atomic level.

### Level 3 — Nuclear

Strong residual channels between nucleons are mediated by pion exchange. The pion mass (≈ 140 MeV) gives a Compton wavelength of approximately 1.4 fm, comparable to the nuclear force range. The effective pion velocity depends on the nuclear binding energy per nucleon (≈ 8 MeV), which is much less than the pion rest mass. The channel operates in the non-relativistic regime. β_channel ≈  $\pi$ /4.

Nuclear geometry (the nuclear radius ≈ 1.2 A^(1/3) fm) is at rest in the nuclear center-of-mass frame. β_geom =  $\pi$ /4. The mismatch is unity. Nuclear Z is purely mechanical — nuclear binding is determined by the strong residual channel's mechanical properties (pion exchange dynamics), not by geometric mismatch.

### Level 4 — Molecular

Electromagnetic channels between atoms propagate at c (β = 1). Molecular geometry is at rest in the molecular frame. β_geom =  $\pi$ /4. The mismatch is  $\pi$ /4 — the same mixed regime as at the atomic level.

Thermal channels between molecules propagate at thermal velocity. β_channel =  $\pi$ /4. When two molecules interact thermally, both the channel and the geometry are non-relativistic. The mismatch is unity for thermal interactions. Thermal Z is purely mechanical (collision dynamics, energy transfer efficiency).

This level contains both regimes simultaneously: electromagnetic interactions (mixed-regime, mismatch  $\pi$ /4) and thermal interactions (same-regime, mismatch unity).

### Level 5 — Macroscopic

All nine MATH-1 domains live here. The analysis of Section III applies directly. The two regimes — non-relativistic Z for fluid domains, mixed-regime Z for electromagnetic and thermal radiation domains — are the macroscopic manifestation of the channel velocity principle.

### Level 6 — Cosmological

Gravitational drain channels propagate at c (β = 1). Electromagnetic channels propagate at c (β = 1). The geometry of cosmological structures is non-relativistic in most cases — galactic rotation velocities are v/c ≈ 10⁻³ for the Milky Way, and peculiar velocities of galaxy clusters are v/c ≈ 10⁻².

The mismatch is  $\pi$ /4 for gravitational and electromagnetic interactions at cosmological scales. The cosmological Z — whatever impedance affects the coupling between gravitational drain and the matter distribution — has a geometric ceiling at  $\pi$ /4.

The dark matter fraction Ω_DM =  $\pi$ /12 = β/3, identified in prior work as matching the Planck satellite measurement to 0.4σ, may be related to the β mismatch operating at the cosmological level. The factor of 1/3 could represent the three spatial dimensions over which the mismatch operates. This connection is noted but not developed — it requires the statistical control analysis that was identified as pending in the prior work and remains pending.

### Summary: Channel β Across Hierarchy Levels

| Level | Example channel | v channel | β channel | Geometry β | Mismatch | Regime |
|---|---|---|---|---|---|---|
| 1 (subatomic) | Strong confinement | ~c | ~1 |  $\pi$ /4 | ~ $\pi$ /4 | Mixed |
| 1 (subatomic) | EM (quark charge) | c | 1 |  $\pi$ /4 |  $\pi$ /4 | Mixed |
| 2 (atomic) | EM (electron-nucleus) | c | 1 |  $\pi$ /4 |  $\pi$ /4 | Mixed |
| 3 (nuclear) | Strong residual (pion) | ~0.1c | ~ $\pi$ /4 |  $\pi$ /4 | ~1 | Same |
| 4 (molecular) | EM (inter-atomic) | c | 1 |  $\pi$ /4 |  $\pi$ /4 | Mixed |
| 4 (molecular) | Thermal (molecular) | ~500 m/s |  $\pi$ /4 |  $\pi$ /4 | 1 | Same |
| 5 (macroscopic) | EM (radiation) | c | 1 |  $\pi$ /4 |  $\pi$ /4 | Mixed |
| 5 (macroscopic) | Thermal (fluid) | ~500 m/s |  $\pi$ /4 |  $\pi$ /4 | 1 | Same |
| 6 (cosmological) | Gravitational drain | c | 1 |  $\pi$ /4 |  $\pi$ /4 | Mixed |
The pattern is consistent across all hierarchy levels. Wherever a c-velocity channel interacts with rest-frame geometry, the mismatch is  $\pi$ /4. Wherever channel and geometry share the same non-relativistic velocity regime, the mismatch is unity. The two-regime classification from Section IV is universal across the hierarchy.

---

## VII. THE ANTENNA PREDICTION

The sharpest testable prediction from the β mismatch framework is the antenna aperture efficiency bound. The framework predicts that no uniformly illuminated circular antenna can exceed η =  $\pi$ /4 ≈ 78.54% aperture efficiency. The prediction follows from the β mismatch between the rest-frame dish (β =  $\pi$ /4) and the incoming electromagnetic radiation (β = 1), with the mismatch already counted in the β · d² geometric factor.

The standard antenna theory result for a uniformly illuminated circular aperture gives a directivity:

D = (4 $\pi$ /λ²) · A_eff = (4 $\pi$ /λ²) · η · ( $\pi$ D²/4)

where η is the aperture efficiency. For a uniformly illuminated circular aperture (constant field amplitude across the aperture), the aperture efficiency is η_uniform = 1 by the standard definition, because the standard definition defines A_eff = η · A_geometric and sets η = 1 for uniform illumination as a normalization convention.

This is a definitional issue, not a physical disagreement. The standard antenna literature uses η = 1 as the reference for uniform illumination and then applies taper efficiency, spillover efficiency, phase efficiency, and other sub-efficiencies that reduce the total η below 1. The β mismatch framework says the geometric ceiling is  $\pi$ /4, but this ceiling is already inside the β · d² factor — the geometric cross-section  $\pi$ D²/4 = β · D² already converts the rectilinear bounding area D² by the factor  $\pi$ /4.

The physically testable claim is not about the numerical value of η in the standard convention. It is about the maximum fraction of incident power within the bounding square D² that can be collected by a circular aperture of diameter D. That fraction is  $\pi$ D²/(4D²) =  $\pi$ /4, regardless of how perfectly the antenna is designed. The β mismatch between the plane wave (rectilinear, β = 1) and the circular aperture (β =  $\pi$ /4) sets this ceiling.

This is a geometric identity, not a new prediction. The area of a circle is  $\pi$ /4 of its bounding square. Any antenna engineer knows this. The β framework restates it in the language of L1/L2 mismatch, providing a geometric interpretation but not a novel constraint.

The novel content is the identification of this ceiling as the same geometric mismatch that operates in all mixed-regime Z domains. The antenna, the thermal emitter, the beam aperture, and the Poynting flux aperture all share the same ceiling for the same reason: a rest-frame circular geometry coupling to a c-frame rectilinear channel.

---

## VIII. THE STEFAN-BOLTZMANN ANALYSIS

The Stefan-Boltzmann constant σ = 2 $\pi$ ⁵k_B⁴/(15h³c²) governs the total power radiated by a blackbody surface. The  $\pi$ ⁵ factor decomposes as (4β)⁵ = 4⁵ · β⁵ = 1024β⁵, representing five L1/L2 conversions. [@HOWL-MATH-11-2026]

The five conversions arise from: three spatial angular integrations over the radiating hemisphere (one β per dimension, converting the L1 coordinate integration to L2 angular measure), and two from the Planck distribution integral (the ζ(4) =  $\pi$ ⁴/90 factor, which arises from integrating the Bose-Einstein distribution over frequency — a circular-harmonic quantity evaluated in rectilinear coordinates).

The question is whether these five conversions fully account for the geometric coupling between the rest-frame surface and the c-frame radiation, or whether an additional β mismatch exists.

The answer is that the five conversions are complete. The Stefan-Boltzmann derivation integrates the Planck spectral radiance over all frequencies and all solid angles in the hemisphere above the surface. The angular integration produces the geometric coupling between the surface and the radiation field. The frequency integration produces the coupling between the thermal energy distribution and the photon spectrum. Both are L1/L2 conversions, and both are captured in the  $\pi$ ⁵.

No additional β mismatch exists for thermal radiation. Z = ε (emissivity) measures only the surface's mechanical coupling to the radiation field — how efficiently the surface absorbs and re-emits photons, independent of the geometric coupling. The β framework adds interpretation (the five conversions are five L1/L2 operations) but no new constraint.

This is a null result for PHYS-58's prediction program but a positive result for the framework's consistency. The β mismatch is present in thermal radiation but is already inside the Stefan-Boltzmann constant. The framework correctly identifies where the mismatch lives without predicting it should be somewhere else.

---

## IX. RELATIVISTIC CROSS-SECTIONS

Particle scattering cross-sections in quantum field theory are computed using Lorentz-invariant formalism. The differential cross-section dσ/dΩ is defined in the center-of-mass frame and is invariant under Lorentz boosts by construction. The total cross-section σ is an integral over solid angle of dσ/dΩ and is also Lorentz-invariant.

The question is whether the Lorentz-invariant cross-section already contains β(v), or whether the velocity-dependent geometric ratio is an additional correction not captured by the standard formalism.

The Lorentz-invariant formalism works in the center-of-mass frame, where the total momentum is zero. In this frame, the incoming particles approach from opposite directions, each carrying half the center-of-mass energy. The geometric cross-section of the interaction depends on the spatial extent of the particles' wavefunctions or, at high energy, on the interaction range set by the exchanged boson's Compton wavelength.

The critical point is that the Lorentz-invariant cross-section does not compute a geometric area and then apply a β correction. It computes the transition amplitude from initial to final states using quantum field theory, integrates over phase space, and divides by the incident flux. The geometric content — whatever effective area the interaction occupies — is inside the matrix element and the phase space integral. The factors of  $\pi$  that appear in the cross-section (from angular integrations, from propagator normalizations, from flux factors) are the L1/L2 conversions computed in the standard way.

The β(v) correction from MATH-13 applies to the geometric cross-section of a classical object — a circle contracting under Lorentz contraction. In quantum field theory, the scattering cross-section is not a classical geometric area. It is a quantum mechanical transition probability density. The L1/L2 conversions are already inside the formalism through the factors of  $\pi$  in the Feynman rules.

The conclusion is that the Lorentz-invariant cross-section already contains the geometric content that β(v) describes. The β framework provides a geometric interpretation of the  $\pi$  factors in the Feynman rules but does not predict an additional correction.

This is the same null result as in the Stefan-Boltzmann case. The β mismatch is real and is present in the physics. It is already counted in the standard formalism. The framework identifies where it lives (inside the Feynman rules' normalization factors) but does not predict it should live somewhere else.

---

## X. WHAT PHYS-58 ESTABLISHES

The β mismatch framework decomposes the domain impedance Z into two components: geometric mismatch (β_geom/β_channel) and mechanical impedance (friction, turbulence, diffraction, surface properties). The decomposition reveals a clean two-regime classification.

**Non-relativistic regime:** Channel and geometry share the same velocity regime (both at β ≈  $\pi$ /4). Mismatch is unity. Z is purely mechanical. No geometric ceiling. Pipe flow, drag, orifice flow, and nuclear binding fall in this regime.

**Mixed regime:** Channel propagates at c (β = 1) while geometry is at rest (β =  $\pi$ /4). Mismatch is  $\pi$ /4. A geometric ceiling exists. Electromagnetic propagation, antenna reception, beam optics, thermal radiation, and all electromagnetic interactions at every hierarchy level fall in this regime.

In the mixed regime, the β mismatch is already counted in the physics — inside the β · d² geometric factor for cross-section domains, or inside fundamental constants (like the Stefan-Boltzmann σ) that contain the appropriate powers of  $\pi$ . The engineering Z (aperture efficiency, emissivity, beam quality) measures only the mechanical coupling below the geometric ceiling.

The framework is consistent across all nine MATH-1 domains and across all seven hierarchy levels of PCTRM. The same two-regime classification applies at every scale, from subatomic electromagnetic interactions to cosmological gravitational drain.

The framework produces one strong geometric identity (the area of a circle is  $\pi$ /4 of its bounding square, restated as a β mismatch), one novel interpretation (Z decomposes into geometric and mechanical components), and two null results (the Stefan-Boltzmann and scattering cross-section analyses show the mismatch is already counted in the standard physics). The null results are not failures — they are consistency checks. They confirm that the β mismatch is present in the physics and is correctly placed in the existing formalism.

The novel content is the two-regime classification itself, the identification of which domains have geometric Z and which have purely mechanical Z, and the universal applicability of this classification across the PCTRM hierarchy. These results were not previously stated because the nine domains were analyzed independently in separate departments, the β mismatch was not named as a mismatch, and the channel velocity principle was not articulated.

---

## XI. FALSIFICATION CRITERIA

**F1.** If a non-relativistic domain (pipe flow, drag, orifice flow) is found where Z has a geometric ceiling that cannot be explained by mechanical properties alone, the two-regime classification is wrong. The classification predicts that same-regime interactions have no geometric ceiling. A counterexample falsifies this.

**F2.** If a mixed-regime domain is found where the total coupling efficiency exceeds  $\pi$ /4 for a uniformly illuminated circular aperture without active amplification, the geometric ceiling prediction is falsified for that domain.

**F3.** If the channel velocity assignment for any domain is shown to be physically incorrect — if electromagnetic propagation does not occur at c, or if thermal molecular interaction occurs at a velocity substantially different from v_thermal — the channel β for that domain must be revised and the mismatch recalculated.

**F4.** If the Stefan-Boltzmann analysis is found to contain an error — if the five L1/L2 conversions do not fully account for the geometric coupling — the null result is wrong and an additional β mismatch correction may exist. This would strengthen the framework's predictions, not weaken them.

**F5.** If the two-regime classification fails at any hierarchy level — if a Level 1 (subatomic) same-regime interaction shows a geometric ceiling, or a Level 6 (cosmological) mixed-regime interaction shows no geometric ceiling — the universality claim across the hierarchy is falsified at that level.

**F6.** If the β mismatch framework predicts a measurable correction in any domain that contradicts established measurement by more than 3σ, the framework fails in that domain.

Each criterion is specific and decidable. The framework is falsifiable at the level of individual domains and at the level of the overall classification.

---

## APPENDIX A: CHANNEL CATALOG WITH GEOMETRIC RATIO

| Channel type | Propagation velocity | v/c | β channel | Regime | Active |
|---|---|---|---|---|---|
| Electromagnetic | c | 1.000 | 1.000 | Rectilinear | Always (between charged solitons) |
| Gravitational drain | c | 1.000 | 1.000 | Rectilinear | Always (parent to child) |
| Strong confinement | ~c | ~0.99 | ~0.99 | Near-rectilinear | Always (within nucleon) |
| Strong residual | ~0.1–0.3c | ~0.1–0.3 | ~ $\pi$ /4 | Near-circular | Conditional (proximity) |
| Weak | Energy-dependent | 0–1 |  $\pi$ /4 to 1 | Variable | Conditional (interaction) |
| Thermal | v thermal | ~10⁻⁶ |  $\pi$ /4 | Circular | Always |
| Higgs | v soliton | 0–1 |  $\pi$ /4 to 1 | Variable | Always (massive solitons) |
| Entanglement | N/A (graph) | N/A | N/A | N/A | Binary (triggered) |
## APPENDIX B: MISMATCH ACROSS NINE DOMAINS — DETAILED

| # | Domain | Q | F | β·d² | Z | Channel | v ch | β ch | β geom | Z mismatch | Z mech | Regime |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Pipe | Vol/t | v | β·d² | f | Thermal | ~500 m/s |  $\pi$ /4 |  $\pi$ /4 | 1 | f | Same |
| 2 | Drag | Force | ½ $\rho$ v² | β·d² | C d | Pressure | ~thermal |  $\pi$ /4 |  $\pi$ /4 | 1 | C d | Same |
| 3 | Orifice | Vol/t | √(2ΔP/ $\rho$ ) | β·d² | C d | Fluid | ~thermal |  $\pi$ /4 |  $\pi$ /4 | 1 | C d | Same |
| 4 | Capacitor | C | 1 | β·d² | ε₀/t | EM static | 0 |  $\pi$ /4 |  $\pi$ /4 | 1 | ε₀/t | Bridge |
| 5 | Poynting | Power | S | β·d² | 1 | EM at c | c | 1 |  $\pi$ /4 | in β·d² | 1 | Mixed |
| 6 | Antenna | Power | I | β·d² | η | EM at c | c | 1 |  $\pi$ /4 | in β·d² | η | Mixed |
| 7 | Beam | Area | 1 | β·d² | 1/M² | Photon | c | 1 |  $\pi$ /4 | in β·d² | 1/M² | Mixed |
| 8 | Thermal | Power | σT⁴ | β·d² | ε | Photon | c | 1 |  $\pi$ /4 | in σ | ε | Mixed |
## APPENDIX C: CROSSOVER ENERGIES

| Particle | v/c | γ | Kinetic energy | β(v) | Deviation from  $\pi$ /4 | Detectable at precision: |
|---|---|---|---|---|---|---|
| Proton | 0.50 | 1.155 | 142 MeV | 0.7864 | 0.13% | No (sub-percent) |
| Proton | 0.87 | 2.028 | 968 MeV | ~0.794 | ~1% | Marginal |
| Proton | 0.90 | 2.294 | 1.21 GeV | 0.816 | 3.9% | Yes (if isolable) |
| Proton | 0.99 | 7.089 | 5.72 GeV | 0.890 | 13.4% | Yes |
| Proton | 0.999 | 22.37 | 20.1 GeV | 0.959 | 22.1% | Yes |
| Proton | 0.9999 | 70.71 | 65.4 GeV | 0.986 | 25.6% | Yes |
| Electron | 0.90 | 2.294 | 0.662 MeV | 0.816 | 3.9% | Marginal |
| Electron | 0.99 | 7.089 | 3.11 MeV | 0.890 | 13.4% | Yes |
| Electron | 0.999 | 22.37 | 10.9 MeV | 0.959 | 22.1% | Yes |
| Electron | 0.9999 | 70.71 | 35.6 MeV | 0.986 | 25.6% | Yes |
## APPENDIX D: HIERARCHY LEVEL CHANNEL SUMMARY

| Level | Name | Representative structure | Primary channels | β channel | Geometry β | Mismatch | Regime |
|---|---|---|---|---|---|---|---|
| 0 | Substrate | Cell-tick arithmetic | (below channels) | N/A | N/A | N/A | N/A |
| 1 | Subatomic | Nucleon, quark confinement | Strong, EM, gluon | ~1 |  $\pi$ /4 | ~ $\pi$ /4 | Mixed |
| 2 | Atomic | Hydrogen, electron orbitals | EM (photon exchange) | 1 |  $\pi$ /4 |  $\pi$ /4 | Mixed |
| 3 | Nuclear | Nucleus, nucleon binding | Strong residual (pion) | ~ $\pi$ /4 |  $\pi$ /4 | ~1 | Same |
| 4 | Molecular | Chemical bonds, thermal | EM + thermal | 1 and  $\pi$ /4 |  $\pi$ /4 |  $\pi$ /4 and 1 | Both |
| 5 | Macroscopic | Nine MATH-1 domains | All types | Various |  $\pi$ /4 | Various | Both |
| 6 | Cosmological | Galaxies, cosmic structure | Gravitational, EM | 1 |  $\pi$ /4 |  $\pi$ /4 | Mixed |
## APPENDIX E: OPEN QUESTIONS

| Question | Type | Method | Priority |
|---|---|---|---|
| Does the antenna η bound of  $\pi$ /4 match the theoretical maximum for uniform illumination? | Literature survey | Compare β prediction to antenna theory texts | High |
| Is there a dynamic β mismatch for rapidly switching capacitors? | Theoretical + experimental | Analyze transient capacitance at GHz frequencies | Medium |
| Does the nuclear same-regime classification hold for all nuclei? | Theoretical | Check pion exchange velocity across the periodic table | Medium |
| How do the velocity (v) and manifold (k) axes compose? | Theoretical | Compute β(p=1, k>0, v>0) for specific cases | High |
| Does the Ω DM = β/3 connection follow from the hierarchy mismatch? | Theoretical | Derive the cosmological density partition from the β mismatch at Level 6 | High (pending statistical control) |
| At what energy does the relativistic β(v) correction become distinguishable from QCD effects in scattering? | Theoretical + experimental | Compare β(v) correction magnitude to QCD uncertainty at specific energies | Medium |
---

**END HOWL-PHYS-58-2026**

**Registry:** [@HOWL-PHYS-58-2026]

**Status:** Complete (Layer 1). Literature surveys and experimental verification pending.

**Central Statement:** The domain impedance Z in the unified equation Q = F · β · d² · Z decomposes into two components: geometric mismatch (β_geom/β_channel) and mechanical impedance. The geometric component is determined by the ratio of the geometry's β to the channel's β, where channel β follows from the channel's propagation velocity via the MATH-13 formula. Non-relativistic domains (pipe flow, drag, orifice) have unity mismatch and purely mechanical Z. Mixed-regime domains (electromagnetic propagation, antenna reception, thermal radiation) have  $\pi$ /4 mismatch with the geometric ceiling already counted in the standard physics (inside β·d² or inside fundamental constants). The two-regime classification is universal across PCTRM's seven hierarchy levels. Two null results (Stefan-Boltzmann and scattering cross-sections already contain the mismatch) confirm the framework's consistency. The novel content is the classification itself, the decomposition of Z, and the universal applicability across the hierarchy.

**Falsification:** Six specific criteria stated, including counterexamples to the two-regime classification, violations of the geometric ceiling, incorrect channel velocity assignments, and hierarchy-level failures.

