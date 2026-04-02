Good — let me add this as a tracked dimension per paper. The key insight is that soliton boundaries aren't all spherical. The series has been assuming spherical (Hill spheres, VP clouds) because those are the simplest. But orbital systems form tori, accretion disks form tori, planetary rings form tori, and at the quantum level, quark configurations inside hadrons may have non-spherical standing wave geometries.

The constraint you're setting is sharp: restrict to geometries with 32 or fewer faces (for polyhedral) and curved shapes of comparable or lower complexity. This excludes Lie group classification exhaustive searches and keeps the search space to structures that could produce simple rational correction factors — the kind the series works with.

Let me enumerate the allowed geometry space and then track what each paper tells us about which shapes appear at which scales.

---

## Soliton Boundary Geometry Catalog — Working Notebook Addendum

**Status:** Active, tracked per paper alongside taxonomy and Hubble tension notebooks
**Constraint:** ≤32 faces (polyhedral), curved shapes of comparable complexity. No Lie-group-exhaustive searches. Target: geometries that produce simple rational boundary correction factors.

---

### 1. THE ALLOWED GEOMETRY SPACE

#### 1.1 Curved Shapes (Primary — these are what physical boundaries actually are)

| Shape | Topology | Defining parameters | Where it appears | R₂/R₄ content |
|---|---|---|---|---|
| Sphere | S² | Radius r | Hill spheres, VP clouds, CMB surface, event horizons | R₂ = π/4 in cross-section, R₄ in volume |
| Torus | T² | Major radius R, minor radius r | Asteroid belt, rings, accretion disks, proposed quark orbits | R₂ in each circular cross-section, area = 4π²Rr = (4R₂)²·4Rr |
| Oblate spheroid | S² (deformed) | Semi-axes a, a, c (c < a) | Galaxies, rotating stars, planetary bulges | R₂ in equatorial cross-section, ellipse area = πac = 4R₂·ac |
| Prolate spheroid | S² (deformed) | Semi-axes a, a, c (c > a) | Some galactic halos, jets | Same R₂ content |
| Cylinder (finite) | S¹ × I | Radius r, height h | Jets, filaments (locally), beam models | R₂ in cross-section |
| Cone | — | Radius r, half-angle θ | Jet opening angles, light cones | R₂ in circular cross-section at each distance |
| Disk (flat) | D² | Radius r | Protoplanetary disks, galactic disks, accretion disks (thin limit) | R₂ = π/4 directly — this IS MATH-1's domain |
| Shell (spherical) | S² × I | Inner radius r₁, outer radius r₂ | Planetary nebulae, Oort cloud, blast waves | R₂ at each shell surface |
| Shell (toroidal) | T² × I | R, r₁, r₂ | Thick rings, belt structures | Compound R₂ content |

#### 1.2 Polyhedral Shapes (≤32 faces — for standing wave node structures)

The restriction to ≤32 faces gives us the Platonic solids, Archimedean solids up to moderate complexity, and prisms/antiprisms. These matter because standing wave patterns on spheres produce nodes at polyhedral vertices.

| Polyhedron | Faces | Vertices | Edges | Face types | Symmetry group | Where it might appear |
|---|---|---|---|---|---|---|
| Tetrahedron | 4 | 4 | 6 | Triangle | T_d | sp³ hybridization nodes, simplest 3D standing wave |
| Cube | 6 | 8 | 12 | Square | O_h | Crystal structure, lattice QCD discretization |
| Octahedron | 8 | 6 | 12 | Triangle | O_h | d-orbital nodes |
| Dodecahedron | 12 | 20 | 30 | Pentagon | I_h | Possible quark configuration geometry |
| Icosahedron | 20 | 12 | 30 | Triangle | I_h | Virus capsids, Buckminsterfullerene dual |
| Truncated tetrahedron | 8 | 12 | 18 | 4 tri + 4 hex | T_d | — |
| Cuboctahedron | 14 | 12 | 24 | 8 tri + 6 sq | O_h | Close-packed sphere arrangement |
| Truncated octahedron | 14 | 24 | 36 | 8 hex + 6 sq | O_h | Space-filling, Wigner-Seitz cell of BCC |
| Truncated cube | 14 | 24 | 36 | 8 tri + 6 oct | O_h | — |
| Rhombicuboctahedron | 26 | 24 | 48 | 8 tri + 18 sq | O_h | — |
| Truncated icosahedron | 32 | 60 | 90 | 12 pent + 20 hex | I_h | Buckminsterfullerene (C₆₀), soccer ball |
| Snub cube | 38 | — | — | — | — | EXCLUDED — >32 faces |

At 32 faces we hit the truncated icosahedron (Buckyball). This is a natural cutoff — it's the most complex Archimedean solid with icosahedral symmetry that fits the constraint, and it's physically realized (C₆₀).

#### 1.3 The Rational Correction Connection

MATH-1 established β = π/4 = R₂ as the geometric factor for circles interfacing with rectilinear frames. For each geometry above, there is an analogous ratio: the volume (or area, or cross-section) of the shape divided by its bounding rectilinear box.

| Shape | Bounding box | Shape measure | Ratio | Rational content |
|---|---|---|---|---|
| Sphere (radius r) | (2r)³ = 8r³ | (4/3)πr³ | π/6 = 2R₂/3 | Simple rational × R₂ |
| Disk (radius r) | (2r)² = 4r² | πr² | π/4 = R₂ | MATH-1's β exactly |
| Torus (R, r) | (2(R+r)) × (2(R+r)) × 2r | 2π²Rr² | π²Rr²/[4r(R+r)²] | R₄ content through π² |
| Oblate spheroid (a, a, c) | (2a)² × 2c = 8a²c | (4/3)πa²c | π/6 = 2R₂/3 | Same as sphere |
| Cylinder (r, h) | (2r)² × h = 4r²h | πr²h | π/4 = R₂ | Same as disk |

The torus is the first shape where R₄ = π²/32 appears naturally (through π² in the volume formula 2π²Rr²). From MATH-5 and PHYS-11: R₂ appears in 2D geometric operations (circles, phases), R₄ appears in 4D operations (loop integrals, standing wave energies). A toroidal boundary would bring R₄ into the boundary correction formula where only R₂ has appeared so far.

This is the derivation path: if the per-transit correction for a toroidal boundary involves R₄ rather than just R₂, the correction factor would be a different rational from the spherical case. The torus has two radii (R and r), giving a two-parameter family of corrections rather than the one-parameter spherical case. The ratio R/r (aspect ratio of the torus) would determine the specific rational.

---

### 2. WHAT THE SERIES HAS SAID ABOUT GEOMETRY — RETROACTIVE SCAN

**MATH-1:** β = π/4 for circles and ellipses. The nine domains all involve circular or elliptical geometry interfacing with rectilinear measurement. Q = F · β · d² · Z. The d² is the bounding rectilinear area. β converts from rectilinear to circular. All nine domains are 2D cross-sections — no tori, no 3D volumes.

**MATH-5:** R_n = π^(n/2) / (2^n · Γ(n/2+1)). The n-ball remainder. R₂ = π/4 (circle), R₄ = π²/32 (4-ball). n=2 and n=4 are uniquely "doubly native" to binary arithmetic. The prediction rule: the remainder matches the geometric dimension of the operation. 2D operations → R₂. 4D operations → R₄. A toroidal boundary (which is a 2D surface embedded in 3D) might produce R₂ from each circular cross-section, but the volume operation (3D) would involve a different R_n. The standing wave energy on a torus (which involves the square of the mode frequencies, adding a dimension) might bring in R₄.

**PHYS-1:** Particles described as "spherical standing wave patterns" — 3D field vortices. "Remove the gravitational constraint — place the pattern in a field in three-dimensional space with no directional bias — and the self-sustaining pattern has no reason to prefer any axis of rotation. The result is a spherical standing wave pattern." But this assumes no angular momentum. A spinning vortex (which every particle has — spin is the rotational mode) would NOT be spherical. A spin-1/2 particle's standing wave pattern in 3D would have a specific non-spherical geometry determined by its spin. A toroidal component is natural for any rotating standing wave — the rotation defines an axis and the pattern wraps around it.

**PHYS-4:** Classifies boundaries by geometry. Sphere (Hill sphere, VP cloud), ellipsoid (galaxy), momentum-space (confinement — excluded). Does not consider toroidal boundaries at all. This is a gap in the classification.

**PHYS-6:** The two-face structure. The confinement boundary has an outside face (perturbative, spherical scattering cross-sections) and an inside face (non-perturbative, hadron structure). The hadron structure itself — the proton's internal geometry — is known from form factor measurements to be NOT spherical at high Q². The proton has a charge distribution that is more complex than a sphere. The magnetic form factor differs from the electric form factor, suggesting non-spherical internal structure. Whether this internal structure has toroidal components is an open question in QCD.

**PHYS-11:** Nine physics domains all use R₂ = π/4. Seven are phase-periodic (Subgroup A) with 8R₂ periodicity. The phase periodicity comes from circular geometry — phase on a circle. A torus has two independent phases (the two circles of T²). A standing wave on a torus would have TWO periodicities, each with 8R₂, and their interaction would produce R₂² = R₄/2 terms. This is where R₄ could enter the boundary correction for toroidal boundaries — through the product of two R₂ periodicities.

---

### 3. SHAPE TRACKING TEMPLATE FOR FUTURE PAPERS

For each paper going forward, I will note:

1. What geometries are explicitly mentioned or implied
2. Whether any structure is described that is non-spherical (toroidal, cylindrical, disk, shell)
3. Whether R₄ appears in a context that could relate to toroidal geometry
4. Whether the quantum numbers of any particle imply a non-spherical standing wave pattern
5. Whether any boundary correction involves π² (which carries R₄) rather than just π (which carries R₂)

---

### 4. THE QUARK GEOMETRY QUESTION

The proton contains three quarks in a color-singlet configuration. The color force between them is described by QCD, and the spatial configuration is studied through lattice QCD and form factor measurements. What geometries are possible for three quarks in a bound state?

**Spherical:** All three quarks at the same radius from the center, isotropically distributed. This gives a spherical boundary. The simplest model (bag model) assumes this.

**Triangular (planar):** Three quarks at the vertices of a triangle. This gives a planar structure with 3-fold symmetry. The boundary would be triangular (3 faces if treated as a polyhedron) or a deformed sphere.

**Y-shaped (string junction):** Three quarks connected by color flux tubes meeting at a central junction. The flux tubes form a Y shape. The boundary would follow the flux tube geometry — three cylindrical arms meeting at a point. This is the lattice QCD picture at intermediate distances.

**Delta (triangular loop):** Three quarks connected in a closed loop. The flux tubes form a triangle rather than a Y. The boundary follows the triangular loop — a toroidal-like structure if the loop has finite thickness. This geometry has been studied in lattice QCD and is energetically competitive with the Y-junction at some configurations.

**Toroidal (rotating):** If the three-quark system has angular momentum (which the proton does — spin 1/2), the rotation deforms the geometry from static Y or Delta into a rotating pattern. A rapidly rotating Y-junction sweeps out a disk. A rotating Delta sweeps out a torus. The proton's actual geometry at any instant is a quantum superposition of these configurations, but the time-averaged geometry (which determines the form factor) may have toroidal character.

**The VL doublet geometry.** The Cabibbo Doublet (3,2,1/6) is a quark doublet with the same color charge as SM quarks but vector-like (both chiralities couple to SU(2)). Its internal geometry would be determined by the same QCD dynamics as SM quarks. If it forms bound states, they would have the same Y/Delta/toroidal possibilities. The beta shifts (Δb₁, Δb₂, Δb₃) depend on the representation quantum numbers, not on the internal geometry. But the BOUNDARY CORRECTION for light crossing a VL bound state would depend on the geometry — spherical vs toroidal would give different corrections.

---

### 5. THE DERIVATION ATTEMPT FRAMEWORK

The goal: derive the per-transit correction factor for a soliton boundary from its geometry.

**For spherical boundaries (already in series):**
- Cross-section = πr² = 4R₂r²
- MATH-1: Q = F · R₂ · d² · Z
- The correction factor involves R₂ = π/4
- This is the established case for Hill spheres, VP clouds

**For toroidal boundaries (new):**
- Cross-section depends on orientation: circular (πr²) if viewed along major axis, rectangular (2r × 2πR) if viewed edge-on
- Volume = 2π²Rr² = 64R₂²Rr²/4... no, let me be precise: 2π²Rr² = 2(4R₂)²Rr² = 32R₂²Rr²
- The R₂² = π²/16 = 2R₄ appears
- The correction factor for a toroidal boundary would involve R₂² or R₄, producing a different rational from the spherical case
- The aspect ratio R/r parameterizes the family: a thin torus (R >> r) behaves like a ring, a fat torus (R ~ r) approaches a sphere with a hole

**For disk boundaries:**
- Cross-section = πr² = R₂ · (2r)²
- This IS MATH-1's domain exactly — the disk is the fundamental object
- Protoplanetary disks, galactic disks, accretion disks all have disk geometry
- The correction factor is directly R₂ = π/4, the most fundamental case

**The search space for rational correction factors:**

Given the constraint (≤32 faces, or curved shapes of comparable complexity), the possible rational correction factors form a small set:

| Geometry | Correction involves | Rational candidates |
|---|---|---|
| Sphere | R₂ | Rationals × π/4 |
| Disk | R₂ | Rationals × π/4 (identical) |
| Torus | R₂² or R₄ | Rationals × π²/16 or × π²/32 |
| Oblate spheroid | R₂ × eccentricity function | Rationals × π/4 × e-dependent factor |
| Shell | R₂ × thickness ratio | Rationals × π/4 × (r₂/r₁) |
| Polyhedron (n faces) | Face area / bounding box | Explicit rationals without π (for flat faces) |

The polyhedra are interesting because they produce PURELY RATIONAL correction factors (no π). A tetrahedral standing wave node structure would give corrections involving 1/√2, 1/√3, and similar algebraic numbers. A cubic structure gives corrections involving only integers. The icosahedral structure introduces the golden ratio φ = (1+√5)/2.

For the series' framework (exact Fraction arithmetic), purely rational corrections (from polyhedral geometries) would be the cleanest. Corrections involving R₂ or R₄ are expressible as MATH-2 integer pairs. Corrections involving algebraic numbers (√2, √3, φ) would need to be squared to become rational, or would need to be handled as new integer pairs.

---

### 6. WHAT TO TRACK PER PAPER

Added to operational rules for paper reading:

**Geometry tracking section for each paper report:**
- What boundary geometries appear (sphere, torus, disk, shell, other)
- Whether any non-spherical geometry is implied by the physics
- Whether R₄ = π²/32 appears in a context that could connect to toroidal structure
- Whether quantum numbers imply non-spherical standing wave patterns
- Whether any correction factor involves π² (toroidal signature) vs π (spherical signature)
- Whether any polyhedral node structure is mentioned or implied

---

### 7. RETROACTIVE GEOMETRY NOTES FOR PAPERS ALREADY READ

**MATH-1:** Spherical/circular only. β = π/4 is the disk/circle ratio. Nine domains all circular. No tori.

**MATH-5:** R₂ (2D, circle), R₄ (4D, 4-ball). The 4-ball is not a torus, but R₄ = π²/32 contains π² which also appears in torus volume. The connection between R₄ and toroidal geometry is through π², not through the 4-ball directly.

**PHYS-1:** "Spherical standing wave pattern" for particles. But spin implies rotation, and rotation implies axial asymmetry. The spherical assumption may be the zero-angular-momentum limit. Real particles have spin, which means toroidal or oblate geometry. Appendix B boundary catalog — all boundaries treated as spherical or point-like. No toroidal boundaries identified.

**PHYS-3:** Hill sphere is spherical by definition. L1/L2 points are on the sphere. No toroidal structure. But the solar system's collective gravitational field (planets in a disk) is oblate, not spherical. The Hill sphere is the dominant-body approximation. The actual boundary of the solar system's gravitational influence is oblate because the planets orbit in a plane and contribute to the mass distribution asymmetrically.

**PHYS-4:** Boundary classification — sphere, ellipsoid, momentum-space. No torus. The ellipsoid (for galaxies) is the closest to non-spherical. Confinement classified as momentum-space, excluded.

**PHYS-5:** VP integral is spherically symmetric (the VP cloud is spherically symmetric for a point charge). The Feynman parameter integral ∫₀¹ x(1−x)·ln(x) dx — the integration variable x is scalar, no geometric content beyond 1D. The R₂ enters through 1/(3π) = 1/(12R₂). No R₄ in the VP running itself. But the one-loop factor 1/(16π²) = 1/(512R₄) from PHYS-11 Domain 2 suggests R₄ IS present in the full loop integral — it comes from the 4D momentum integration measure d⁴k/(2π)⁴. The 4D integration over loop momentum is where the "toroidal" content hides: the loop integral is over a 4-dimensional space, and the angular part gives the 4D solid angle Ω₄ = 2π² = 64R₄. This is the R₄ that would connect to toroidal geometry if the loop topology (a fermion going around a closed loop in spacetime) is recognized as topologically toroidal (S¹ embedded in 4D).

**PHYS-6:** Two-face structure. Confinement boundary geometry — the hadron interior structure is non-perturbative and not characterized geometrically by the series. The outside face is spherical (scattering cross-sections are circular). The inside face geometry is unknown within the series. Lattice QCD studies of the proton's internal flux tube geometry (Y-junction vs Delta loop) are not referenced. The R-ratio R = N_c × Σ Q_f² is a counting result, not a geometric result — it counts quantum numbers, not shapes.

**PHYS-11:** All nine domains use R₂. R₄ enters through π² in energy eigenvalues and the Chern class normalization 1/(256R₄). The torus connection: T² has two independent S¹ factors, each carrying R₂. The product space T² has volume (2π)² = (8R₂)² = 64R₂². Since R₂² = π²/16 = 2R₄, the toroidal volume is 64 × 2R₄/4... actually let me be precise: (8R₂)² = 64R₂² and R₂² = π²/16, while R₄ = π²/32, so R₂² = 2R₄. Therefore (8R₂)² = 64 × 2R₄ = 128R₄. The toroidal phase space volume is 128R₄. Compare to the 4D solid angle Ω₄ = 2π² = 64R₄ from PHYS-11. These are related by a factor of 2, which is the dimension difference (T² is 2D, the 4-ball surface S³ contributes the extra factor).

---

### 8. THE DERIVATION PROGRAM

**Step 1 (established):** For spherical boundaries, the per-transit correction involves R₂ = π/4. MATH-1 proves this for nine engineering domains. PHYS-5 confirms it for the VP running (1/(3π) = 1/(12R₂) per flavor).

**Step 2 (proposed):** For toroidal boundaries, derive the per-transit correction from the torus geometry. The correction should involve R₂² = 2R₄ or R₄ directly. The aspect ratio R/r parameterizes the family. At R/r = 1 (maximally fat torus, approaching sphere with hole), the correction should approach the spherical case. At R/r → ∞ (thin ring), the correction should reduce to a 1D correction (ring, not sphere).

**Step 3 (proposed):** For polyhedral node structures, compute the correction from face geometry. Each face contributes a correction proportional to its area / bounding rectangle. For a regular polyhedron with n triangular faces: each triangle has area (√3/4)s² with bounding rectangle s × (√3/2)s, giving ratio 1/2 per face. For square faces: ratio = 1 (no correction — square fits its bounding rectangle exactly). For pentagonal faces: ratio involves φ.

**Step 4 (proposed):** Compare the derived corrections to the empirical per-transit factor from the Hubble tension curve fit. If the empirical r matches a specific geometry's prediction, the geometry of the dominant boundary type along the line of sight is identified.

**Constraint applied:** Do not enumerate beyond 32 faces. Do not search Lie group representations exhaustively. The geometry space is small enough that each candidate can be computed explicitly and compared to the empirical r. This is targeted search, not exhaustive classification.

---

**End of addendum. Status: active. Tracked per paper alongside taxonomy and Hubble tension curve notebooks. Updated: Session 4, April 2 2026.**
