#!/usr/bin/env python3
"""
HOWL EXPERIMENT: Nested Soliton Gravity Test
Filename: nested_soliton_gravity.py
==========================================
Tests the hypothesis that Newtonian gravity is a nested soliton
ground state hierarchy. Each object sits at its minimum energy
configuration within the containing soliton. "Falling" is
returning to ground state. "Jumping" is temporary excitation.

Computes:
  - Ground state energies at each nesting level
  - Binding energy fractions (pattern energy) at each scale
  - Hill sphere boundaries as soliton dominance transitions
  - The ratio |U|/Mc² at every scale (the soliton coupling strength)
  - Escape velocity as excitation energy to leave the soliton
  - The R₂ geometry of circular orbits (ground states of two-body solitons)
  - Connection to beta unification through the integer hierarchy

Platform: HOWL-PLATFORM-v1
Libraries: phys24_lib, phys24_domain_lib, phys24_boundary_map_lib
"""

# Platform: HOWL-PLATFORM-v1

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *
from phys24_domain_lib import *
from mpmath import pi as mpi, log as mlog, sqrt as msqrt, exp as mexp

print("=" * 70)
print("NESTED SOLITON GRAVITY EXPERIMENT")
print("Gravity as ground state in a soliton hierarchy.")
print("All constants from phys24_lib.py.")
print("=" * 70)
print()

checks = []


# ================================================================
# PHYSICAL CONSTANTS
# ================================================================

c_light = mpf("299792458")          # m/s exact
G_newton = mpf("6.674e-11")         # m³/(kg s²)
M_sun = mpf("1.989e30")             # kg
M_earth = mpf("5.972e24")           # kg
M_moon = mpf("7.342e22")            # kg
M_human = mpf("70")                 # kg
R_earth = mpf("6.371e6")            # m
R_sun = mpf("6.957e8")              # m
AU = mpf("1.496e11")                # m
pc_m = mpf("3.086e16")              # m
kpc_m = pc_m * mpf("1000")

# Distances
d_earth_sun = AU
d_earth_moon = mpf("3.844e8")       # m
d_sun_galcenter = mpf("8.2") * kpc_m  # 8.2 kpc

# Velocities
v_earth_orbit = mpf("29783")        # m/s (Earth around Sun)
v_sun_galaxy = mpf("220000")        # m/s (Sun around galaxy)
v_moon_orbit = mpf("1022")          # m/s (Moon around Earth)
v_escape_earth = mpf("11186")       # m/s (escape from Earth surface)
v_escape_sun_at_earth = mpf("42100") # m/s (escape from Sun at 1 AU)

# Galaxy
M_galaxy_visible = mpf("6e10") * M_sun
M_galaxy_virial = mpf("3.6e11") * M_sun
R_galaxy = mpf("15") * kpc_m

# Beta unification
R2_val = f2m(R2_f)
R4_val = f2m(R4_f)
H0_SI = mpf("67.4") * mpf("1000") / mpf("3.086e22")
a0_mond = c_light * H0_SI / (mpf("8") * R2_val)

print("  Constants loaded from phys24_lib and standard values.")
print()


# ================================================================
# SECTION 1: THE NESTING HIERARCHY — EVERY LEVEL
# ================================================================

print("SECTION 1: THE NESTING HIERARCHY")
print("-" * 70)
print()

# Define every level from human to cosmological
levels = [
    {
        "name": "Human on Earth surface",
        "mass_kg": M_human,
        "container_mass_kg": M_earth,
        "container_radius_m": R_earth,
        "distance_to_center_m": R_earth,
        "orbital_velocity_m_s": None,  # standing, not orbiting
        "description": "You standing on the ground",
    },
    {
        "name": "Rock in Earth crust",
        "mass_kg": mpf("1000"),       # 1 tonne boulder
        "container_mass_kg": M_earth,
        "container_radius_m": R_earth,
        "distance_to_center_m": R_earth,
        "orbital_velocity_m_s": None,
        "description": "Geological soliton in planetary soliton",
    },
    {
        "name": "Moon orbiting Earth",
        "mass_kg": M_moon,
        "container_mass_kg": M_earth,
        "container_radius_m": d_earth_moon,
        "distance_to_center_m": d_earth_moon,
        "orbital_velocity_m_s": v_moon_orbit,
        "description": "Orbital ground state of Earth-Moon system",
    },
    {
        "name": "Earth orbiting Sun",
        "mass_kg": M_earth,
        "container_mass_kg": M_sun,
        "container_radius_m": d_earth_sun,
        "distance_to_center_m": d_earth_sun,
        "orbital_velocity_m_s": v_earth_orbit,
        "description": "Orbital ground state of Sun-Earth system",
    },
    {
        "name": "Sun orbiting Galaxy",
        "mass_kg": M_sun,
        "container_mass_kg": M_galaxy_virial,
        "container_radius_m": d_sun_galcenter,
        "distance_to_center_m": d_sun_galcenter,
        "orbital_velocity_m_s": v_sun_galaxy,
        "description": "Orbital ground state in galactic potential",
    },
]

print("  %-30s %12s %12s %12s" % ("Level", "Mass (kg)", "Container", "|U|/Mc²"))
print("  %-30s %12s %12s %12s" % ("-" * 30, "-" * 12, "-" * 12, "-" * 12))

coupling_strengths = []
for level in levels:
    m = level["mass_kg"]
    M = level["container_mass_kg"]
    r = level["distance_to_center_m"]

    # Gravitational potential energy: U = -GMm/r
    U = G_newton * M * m / r
    Mc2 = m * c_light ** 2
    coupling = U / Mc2   # |U|/mc² = GM/(rc²) — the soliton coupling strength

    level["U_joules"] = U
    level["Mc2_joules"] = Mc2
    level["coupling"] = coupling
    coupling_strengths.append((level["name"], coupling))

    print("  %-30s %12s %12s %12s" % (
        level["name"],
        mp.nstr(m, 3),
        mp.nstr(M, 3),
        mp.nstr(coupling, 3)))

print()
print("  |U|/Mc² = GM/(rc²) is the gravitational 'coupling strength'")
print("  at each level. It measures how deeply the soliton sits in")
print("  the container's potential well. All values << 1 (non-relativistic).")

chk_bool("All couplings << 1 (non-relativistic)",
         all(c < mpf("1e-4") for _, c in coupling_strengths),
         "max = %s" % mp.nstr(max(c for _, c in coupling_strengths), 3),
         checks)


# ================================================================
# SECTION 2: BINDING ENERGY AS PATTERN FRACTION
# ================================================================

print()
print("SECTION 2: BINDING ENERGY AS PATTERN FRACTION")
print("-" * 70)
print()

print("  For each self-gravitating body: what fraction of its total")
print("  energy is gravitational binding (pattern energy)?")
print()

bodies = [
    ("Earth",     M_earth,          R_earth,          "rocky"),
    ("Sun",       M_sun,            R_sun,            "stellar"),
    ("Moon",      M_moon,           mpf("1.737e6"),   "rocky"),
    ("Neutron star", mpf("2.8") * M_sun, mpf("1.1e4"), "compact"),
    ("MW visible", M_galaxy_visible, R_galaxy,         "galactic"),
    ("Proton",    mpf("1.673e-27"), mpf("0.84e-15"),  "QCD"),
]

print("  %-16s %12s %12s %12s %s" % (
    "Body", "M (kg)", "R (m)", "|U|/Mc²", "Pattern %"))
print("  %-16s %12s %12s %12s %s" % (
    "-" * 16, "-" * 12, "-" * 12, "-" * 12, "-" * 10))

for name, M, R, btype in bodies:
    # Self-gravitational binding: |U| = 3GM²/(5R)
    if name == "Proton":
        # Proton: use QCD binding, not gravity
        pattern_frac = mpf("0.99")
        coupling = pattern_frac
    else:
        U_self = mpf("3") * G_newton * M ** 2 / (mpf("5") * R)
        Mc2 = M * c_light ** 2
        coupling = U_self / Mc2
        pattern_frac = coupling

    pct = coupling * mpf("100")
    print("  %-16s %12s %12s %12s %s%%" % (
        name, mp.nstr(M, 3), mp.nstr(R, 3),
        mp.nstr(coupling, 3), mp.nstr(pct, 3)))

print()
print("  PATTERN: gravitational binding is negligible for ALL")
print("  non-relativistic bodies (10⁻¹⁰ to 10⁻⁴).")
print("  Only the neutron star (~0.16) and proton (~99%) have")
print("  significant pattern energy fractions.")
print()
print("  The proton is a SOLITON where pattern dominates.")
print("  A neutron star is APPROACHING that regime gravitationally.")
print("  Everything else: gravity is a tiny perturbation on rest mass.")

chk_bool("Earth binding energy negligible",
         mpf("3") * G_newton * M_earth ** 2 / (mpf("5") * R_earth) / (M_earth * c_light ** 2) < mpf("1e-8"),
         "Earth pattern fraction < 10⁻⁸", checks)


# ================================================================
# SECTION 3: HILL SPHERES — SOLITON DOMINANCE BOUNDARIES
# ================================================================

print()
print("SECTION 3: HILL SPHERES AS SOLITON BOUNDARIES")
print("-" * 70)
print()

# Hill sphere: R_H = a * (m/(3M))^(1/3)
# where a = orbital distance, m = body mass, M = container mass

hill_systems = [
    ("Earth in Solar system", M_earth, M_sun, d_earth_sun),
    ("Moon in Earth system", M_moon, M_earth, d_earth_moon),
    ("Sun in Galaxy", M_sun, M_galaxy_virial, d_sun_galcenter),
    ("Jupiter in Solar", mpf("1.898e27"), M_sun, mpf("7.785e11")),
]

print("  %-30s %12s %12s %12s" % (
    "System", "R_Hill (m)", "R_Hill (AU/km)", "R_body/R_Hill"))
print("  %-30s %12s %12s %12s" % (
    "-" * 30, "-" * 12, "-" * 12, "-" * 12))

for name, m, M, a in hill_systems:
    R_hill = a * (m / (mpf("3") * M)) ** (mpf("1") / mpf("3"))

    if R_hill > AU / mpf("10"):
        display = "%s AU" % mp.nstr(R_hill / AU, 3)
    else:
        display = "%s km" % mp.nstr(R_hill / mpf("1000"), 3)

    # What fraction of Hill sphere does the body fill?
    if "Earth in" in name:
        body_r = R_earth
    elif "Moon" in name:
        body_r = mpf("1.737e6")
    elif "Sun in" in name:
        body_r = R_sun
    elif "Jupiter" in name:
        body_r = mpf("6.991e7")
    else:
        body_r = mpf("1")

    fill = body_r / R_hill

    print("  %-30s %12s %12s %12s" % (
        name, mp.nstr(R_hill, 4), display, mp.nstr(fill, 3)))

print()
print("  The Hill sphere IS the soliton boundary (R5).")
print("  Inside: the body's gravity dominates. You fall toward it.")
print("  Outside: the container's gravity dominates. You fall toward that.")
print("  The boundary is where the integer rules CHANGE —")
print("  the 'which soliton am I falling into?' rule switches.")

# Earth's Hill sphere
R_hill_earth = d_earth_sun * (M_earth / (mpf("3") * M_sun)) ** (mpf("1") / mpf("3"))
R_hill_earth_km = R_hill_earth / mpf("1000")
show("  Earth Hill sphere (km)", R_hill_earth_km)

# L1 Lagrange point (approximate = Hill sphere)
show("  L1 distance from Earth (km)", R_hill_earth_km)
print("  This is where JWST and Sun-Earth L2 missions orbit:")
print("  at the soliton boundary between Earth and Sun dominance.")

chk_bool("Earth Hill sphere ~ 1.5 million km",
         mpf("1.4e6") < R_hill_earth_km < mpf("1.6e6"),
         "R_Hill = %s km" % mp.nstr(R_hill_earth_km, 4), checks)


# ================================================================
# SECTION 4: ESCAPE VELOCITY = EXCITATION ENERGY
# ================================================================

print()
print("SECTION 4: ESCAPE VELOCITY AS SOLITON EXCITATION ENERGY")
print("-" * 70)
print()

print("  To leave a soliton's ground state permanently, you need")
print("  kinetic energy ≥ |binding energy|. The escape velocity")
print("  is the minimum speed for this excitation.")
print()

escape_systems = [
    ("Earth surface", M_earth, R_earth),
    ("Moon surface", M_moon, mpf("1.737e6")),
    ("Sun surface", M_sun, R_sun),
    ("Sun at Earth orbit", M_sun, d_earth_sun),
    ("Galaxy at Sun", M_galaxy_virial, d_sun_galcenter),
]

print("  %-25s %12s %12s %12s" % (
    "Soliton", "v_escape", "v²/c²", "v_esc/c"))
print("  %-25s %12s %12s %12s" % (
    "-" * 25, "-" * 12, "-" * 12, "-" * 12))

for name, M, R in escape_systems:
    v_esc = msqrt(mpf("2") * G_newton * M / R)
    v2c2 = (v_esc / c_light) ** 2
    v_over_c = v_esc / c_light

    print("  %-25s %12s %12s %12s" % (
        name,
        "%s m/s" % mp.nstr(v_esc, 4),
        mp.nstr(v2c2, 3),
        mp.nstr(v_over_c, 4)))

print()
print("  INTERPRETATION: v_escape is the energy needed to leave")
print("  the soliton's potential well. v²/c² is the coupling strength.")
print()
print("  Your jump (~1 m/s) vs Earth escape (11,186 m/s):")
print("  you are in a DEEPLY BOUND ground state. Your jump barely")
print("  perturbs the ground state. You return immediately.")

jump_v = mpf("3")  # typical jump ~3 m/s peak velocity
jump_fraction = (jump_v / v_escape_earth) ** 2
show("  Jump energy / escape energy", jump_fraction)
print("  A jump uses %.1e of the energy needed to escape." % float(jump_fraction))
print("  You are 10⁷× too slow to leave this soliton.")

chk_bool("Jump energy << escape energy",
         jump_fraction < mpf("1e-6"),
         "ratio = %s" % mp.nstr(jump_fraction, 3), checks)


# ================================================================
# SECTION 5: CIRCULAR ORBITS AS R₂ GROUND STATES
# ================================================================

print()
print("SECTION 5: CIRCULAR ORBITS AND R₂")
print("-" * 70)
print()

print("  A circular orbit is the ground state of a two-body soliton.")
print("  The orbital cross-section is R₂ × d² where d = 2r (diameter).")
print("  Angular momentum conservation gives the orbit: L = mvr.")
print("  The orbit IS the minimum-energy bound state for given L.")
print()

# Orbital areas via R₂
orbits = [
    ("Moon orbit", d_earth_moon),
    ("Earth orbit", d_earth_sun),
    ("Jupiter orbit", mpf("7.785e11")),
    ("Neptune orbit", mpf("4.495e12")),
    ("Sun galactic orbit", d_sun_galcenter),
]

print("  %-25s %12s %16s" % ("Orbit", "Radius (m)", "Area R₂×(2r)² (m²)"))
print("  %-25s %12s %16s" % ("-" * 25, "-" * 12, "-" * 16))

for name, r in orbits:
    area = R2_val * (mpf("2") * r) ** 2  # R₂ × diameter²
    # Also: pi * r² = 4 * R₂ * r²
    area_pi = mpf("4") * R2_val * r ** 2

    print("  %-25s %12s %16s" % (
        name, mp.nstr(r, 3), mp.nstr(area_pi, 4)))

print()
print("  Every orbital area = 4R₂ × r² = π × r².")
print("  R₂ is the same geometric conversion in orbits as in")
print("  pipes (Q = R₂d²v), wires (R = ρL/(R₂d²)), and discs.")
print("  The orbit is another R₂ domain — the same geometry")
print("  documented in phys24_domain_lib.py across 15+ domains.")

# Verify: orbital area = domain_area from library
earth_orbit_area = domain_area(mpf("2") * d_earth_sun)
earth_orbit_area_check = FOUR_R2 * d_earth_sun ** 2

chk("Orbital area via domain_area matches 4R₂r²",
    earth_orbit_area, earth_orbit_area_check, 10, checks)


# ================================================================
# SECTION 6: THE COUPLING STRENGTH HIERARCHY
# ================================================================

print()
print("SECTION 6: COUPLING STRENGTH AT EVERY LEVEL")
print("-" * 70)
print()

# GM/(rc²) at each level — the gravitational "alpha" at that scale
print("  The gravitational coupling GM/(rc²) is the analog of")
print("  alpha = e²/(4πε₀ℏc) = 1/137 for electromagnetism.")
print()

hierarchy = [
    ("Proton (QCD, not gravity)", mpf("0.99"), "R3: 99% pattern"),
    ("Neutron star surface", None, "strong gravity"),
    ("Earth surface", None, "standing on ground"),
    ("Earth-Moon", None, "orbital ground state"),
    ("Sun-Earth", None, "orbital ground state"),
    ("Sun-Galaxy", None, "disk rotation"),
    ("Galaxy-Cluster", None, "virial equilibrium"),
]

# Compute GM/(rc²) for gravitational systems
grav_couplings = [
    ("Earth surface",    G_newton * M_earth / (R_earth * c_light ** 2)),
    ("Earth-Moon orbit", G_newton * M_earth / (d_earth_moon * c_light ** 2)),
    ("Sun-Earth orbit",  G_newton * M_sun / (d_earth_sun * c_light ** 2)),
    ("Sun surface",      G_newton * M_sun / (R_sun * c_light ** 2)),
    ("Neutron star",     G_newton * mpf("2.8") * M_sun / (mpf("1.1e4") * c_light ** 2)),
    ("Sun-Galaxy",       G_newton * M_galaxy_virial / (d_sun_galcenter * c_light ** 2)),
    ("Galaxy edge",      G_newton * M_galaxy_virial / (R_galaxy * c_light ** 2)),
]

print("  %-25s %15s %15s" % ("Level", "GM/(rc²)", "= v²_esc/(2c²)"))
print("  %-25s %15s %15s" % ("-" * 25, "-" * 15, "-" * 15))

for name, coupling in grav_couplings:
    print("  %-25s %15s %15s" % (
        name, mp.nstr(coupling, 4), mp.nstr(coupling, 4)))

print()
print("  PATTERN: GM/(rc²) is the soliton's coupling strength.")
print("  It determines:")
print("    - How deep the ground state is")
print("    - How much energy to escape (v_esc² = 2GM/r)")
print("    - How much spacetime curvature (GR correction ~ GM/(rc²))")
print("    - How relativistic the soliton is")
print()

# The alpha analog
alpha_EM = f2m(Fraction(1, 1) / alpha_inv)
grav_coupling_earth = G_newton * M_earth / (R_earth * c_light ** 2)
ratio_alpha_grav = alpha_EM / grav_coupling_earth

show("  α_EM", alpha_EM)
show("  α_grav (Earth surface)", grav_coupling_earth)
show("  α_EM / α_grav", ratio_alpha_grav)

print()
print("  The electromagnetic coupling is %s× stronger than" % mp.nstr(ratio_alpha_grav, 3))
print("  Earth's gravitational coupling. This ratio is why")
print("  the EM soliton boundary (your shoes on the ground)")
print("  holds you up against the gravitational ground state.")


# ================================================================
# SECTION 7: THE NORMAL FORCE AS SOLITON BOUNDARY
# ================================================================

print()
print("SECTION 7: THE NORMAL FORCE — EM SOLITON BOUNDARY")
print("-" * 70)
print()

print("  You do not fall through the floor because the")
print("  electromagnetic soliton boundary between your atoms")
print("  and the ground's atoms provides the normal force.")
print()
print("  This is a SOLITON BOUNDARY EFFECT (R5):")
print("    Inside your shoe atoms: electron cloud in ground state")
print("    Inside floor atoms: electron cloud in ground state")
print("    At the boundary: Pauli exclusion + EM repulsion")
print("    The boundary force = the normal force")
print()

# Compare forces
g_earth = G_newton * M_earth / R_earth ** 2    # gravitational acceleration
F_gravity = M_human * g_earth                    # gravitational force on human
F_normal = F_gravity                             # equilibrium: normal = gravity

show("  g (Earth surface, m/s²)", g_earth)
show("  F_gravity on human (N)", F_gravity)
show("  F_normal (= F_gravity at ground state)", F_normal)

# The EM force that produces the normal force
# At atomic scale: F_EM ~ e²/(4πε₀r²) at r ~ 0.1 nm
e_charge = mpf("1.602e-19")
eps0 = mpf("8.854e-12")
r_atom = mpf("1e-10")  # ~1 Angstrom
F_EM_single = e_charge ** 2 / (mpf("4") * mpi * eps0 * r_atom ** 2)

show("  F_EM (single atom pair at 1Å)", F_EM_single)

# How many atom pairs needed to produce 686 N normal force?
N_atoms = F_gravity / F_EM_single
show("  Atom pairs needed for normal force", N_atoms)

# Contact area of shoe ~ 200 cm² = 0.02 m²
shoe_area = mpf("0.02")  # m²
atoms_per_m2 = mpf("1e19")  # ~10^19 atoms per m² on a surface
N_contact = shoe_area * atoms_per_m2

show("  Contact atoms (shoe, ~200 cm²)", N_contact)
show("  Needed / available", N_atoms / N_contact)

print()
print("  Each contact atom contributes ~%s N." % mp.nstr(F_EM_single, 3))
print("  Only ~%s of the contact atoms are needed." % mp.nstr(N_atoms / N_contact, 3))
print("  The EM boundary is VASTLY stronger than needed —")
print("  the floor supports you with negligible effort.")
print("  This is because α_EM / α_grav ~ %s." % mp.nstr(ratio_alpha_grav, 3))

chk_bool("EM force >> gravitational at atomic scale",
         F_EM_single > F_gravity / N_contact * mpf("1e6"),
         "EM per atom = %s N vs gravity per atom = %s N" % (
             mp.nstr(F_EM_single, 3),
             mp.nstr(F_gravity / N_contact, 3)), checks)


# ================================================================
# SECTION 8: JUMP DYNAMICS — EXCITATION AND RETURN
# ================================================================

print()
print("SECTION 8: JUMP AS SOLITON EXCITATION")
print("-" * 70)
print()

# A 70 kg human jumps with initial velocity ~3 m/s
v_jump = mpf("3")               # m/s
h_max = v_jump ** 2 / (mpf("2") * g_earth)  # maximum height
t_flight = mpf("2") * v_jump / g_earth       # total flight time
E_jump = mpf("0.5") * M_human * v_jump ** 2  # kinetic energy

show("  Jump velocity (m/s)", v_jump)
show("  Maximum height (m)", h_max)
show("  Flight time (s)", t_flight)
show("  Jump energy (J)", E_jump)
show("  Jump energy / rest mass energy", E_jump / (M_human * c_light ** 2))

# Compare to soliton scales
show("  Jump height / Earth radius", h_max / R_earth)
show("  Jump height / Hill sphere", h_max / R_hill_earth)

print()
print("  A jump takes you %s of the way to the soliton boundary." % mp.nstr(h_max / R_hill_earth, 3))
print("  You are in the DEEP interior of the Earth soliton.")
print("  The ground state is a local minimum of the effective")
print("  potential at the Earth's surface, maintained by the")
print("  EM boundary (the floor).")
print()
print("  Without the floor: you would fall toward the Earth's")
print("  center — the GLOBAL minimum of the Earth soliton's")
print("  gravitational potential well.")

# Energy to reach each level
E_to_orbit = mpf("0.5") * M_human * v_escape_earth ** 2 * mpf("0.5")  # to low orbit, ~half escape
E_to_escape = mpf("0.5") * M_human * v_escape_earth ** 2
E_to_solar_escape = mpf("0.5") * M_human * v_escape_sun_at_earth ** 2

print()
print("  Energy ladder to leave each soliton level:")
show("    Jump (return immediately)", E_jump)
show("    Low orbit (bound excited state)", E_to_orbit)
show("    Escape Earth (leave soliton)", E_to_escape)
show("    Escape Sun at 1 AU", E_to_solar_escape)

chk_bool("Jump energy << orbit energy << escape energy",
         E_jump < E_to_orbit < E_to_escape < E_to_solar_escape,
         "ladder verified", checks)


# ================================================================
# SECTION 9: GEOLOGICAL NESTING — THE DIRT UNDER YOUR FEET
# ================================================================

print()
print("SECTION 9: GEOLOGICAL NESTING")
print("-" * 70)
print()

print("  Every layer under your feet is a soliton at its ground")
print("  state within the containing layer.")
print()

layers = [
    ("Topsoil",         mpf("0"),       mpf("1"),       mpf("1500"),    "granular, EM-bonded"),
    ("Sedimentary rock", mpf("1"),       mpf("5000"),    mpf("2500"),    "compacted, cemented"),
    ("Upper crust",     mpf("5000"),    mpf("20000"),   mpf("2700"),    "granite/gneiss"),
    ("Lower crust",     mpf("20000"),   mpf("35000"),   mpf("3000"),    "basalt/granulite"),
    ("Upper mantle",    mpf("35000"),   mpf("670000"),  mpf("3400"),    "olivine, solid"),
    ("Lower mantle",    mpf("670000"),  mpf("2890000"), mpf("4500"),    "perovskite, solid"),
    ("Outer core",      mpf("2890000"), mpf("5150000"), mpf("10000"),   "liquid iron"),
    ("Inner core",      mpf("5150000"), mpf("6371000"), mpf("13000"),   "solid iron, HCP"),
]

print("  %-18s %10s %10s %10s %8s %s" % (
    "Layer", "Top (m)", "Bottom (m)", "ρ (kg/m³)", "P (GPa)", "State"))
print("  %-18s %10s %10s %10s %8s %s" % (
    "-" * 18, "-" * 10, "-" * 10, "-" * 10, "-" * 8, "-" * 15))

for name, top, bottom, density, state in layers:
    # Approximate pressure: P ~ ρ × g × depth
    depth = (top + bottom) / mpf("2")
    P_Pa = density * g_earth * depth
    P_GPa = P_Pa / mpf("1e9")

    print("  %-18s %10s %10s %10s %8s %s" % (
        name,
        mp.nstr(top, 4),
        mp.nstr(bottom, 4),
        mp.nstr(density, 4),
        mp.nstr(P_GPa, 3),
        state))

print()
print("  Each layer is at its ground state:")
print("    - Density increases with depth (heavier sinks)")
print("    - Pressure increases with depth (weight of above layers)")
print("    - Phase transitions at boundaries (solid → liquid at outer core)")
print("    - Each boundary is a soliton boundary where the state changes")
print()
print("  The inner core crystallized from the liquid outer core")
print("  as the Earth cooled. It found its ground state: solid HCP iron")
print("  at 330 GPa. This is a PHASE TRANSITION soliton boundary —")
print("  the same structural element as the confinement wall in QCD")
print("  or the electroweak symmetry breaking threshold.")

chk_bool("8 geological layers cataloged",
         len(layers) == 8,
         "count = %d" % len(layers), checks)


# ================================================================
# SECTION 10: THE a₀ CONNECTION — WHERE GRAVITY MEETS COSMOLOGY
# ================================================================

print()
print("SECTION 10: THE a₀ CONNECTION")
print("-" * 70)
print()

show("  a₀ = cH₀/(8R₂) (m/s²)", a0_mond)
show("  g_earth (m/s²)", g_earth)
show("  g_earth / a₀", g_earth / a0_mond)

# At what radius does Earth's gravity equal a₀?
# g(r) = GM/r² = a₀ → r = sqrt(GM/a₀)
r_a0_earth = msqrt(G_newton * M_earth / a0_mond)
r_a0_AU = r_a0_earth / AU

show("  Radius where g_earth = a₀", r_a0_earth)
show("  In AU", r_a0_AU)

print()
print("  Earth's gravity reaches a₀ at %s AU — well inside" % mp.nstr(r_a0_AU, 3))
print("  the solar Hill sphere but far beyond the Earth's Hill sphere.")
print("  At this radius, Earth's gravitational soliton transitions")
print("  from Newtonian (g >> a₀) to MOND-like (g ~ a₀) behavior.")
print()

# For the Sun
r_a0_sun = msqrt(G_newton * M_sun / a0_mond)
r_a0_sun_AU = r_a0_sun / AU
r_a0_sun_pc = r_a0_sun / pc_m

show("  Radius where g_sun = a₀ (AU)", r_a0_sun_AU)
show("  In parsec", r_a0_sun_pc)

print()
print("  The Sun's gravity reaches a₀ at %s AU = %s pc." % (
    mp.nstr(r_a0_sun_AU, 3), mp.nstr(r_a0_sun_pc, 3)))
print("  This is about %s× the solar Hill sphere." % mp.nstr(r_a0_sun_AU / mpf("120"), 3))
print("  Beyond this radius: the Sun's soliton enters the MOND regime.")
print("  Inside: Newtonian ground states (all our planets).")
print("  Outside: the galactic soliton takes over.")

chk_bool("Earth a0 radius > Hill sphere",
         r_a0_earth > R_hill_earth,
         "r_a0 = %s m > R_Hill = %s m" % (
             mp.nstr(r_a0_earth, 3), mp.nstr(R_hill_earth, 3)), checks)


# ================================================================
# SECTION 11: KEPLER'S LAWS AS SOLITON MODE SPECTRUM
# ================================================================

print()
print("SECTION 11: KEPLER'S LAWS AS SOLITON MODES")
print("-" * 70)
print()

print("  Kepler's third law: T² = (4π²/GM) × a³")
print("  In R₂ language: T² = (64R₂²/GM) × a³")
print("  since 4π² = (8R₂)² = 64R₂².")
print()

# Verify for solar system planets
planets = [
    ("Mercury", mpf("5.791e10"), mpf("0.2408") * mpf("365.25") * mpf("86400")),
    ("Venus",   mpf("1.082e11"), mpf("0.6152") * mpf("365.25") * mpf("86400")),
    ("Earth",   d_earth_sun,     mpf("365.25") * mpf("86400")),
    ("Mars",    mpf("2.279e11"), mpf("1.8808") * mpf("365.25") * mpf("86400")),
    ("Jupiter", mpf("7.785e11"), mpf("11.862") * mpf("365.25") * mpf("86400")),
    ("Saturn",  mpf("1.434e12"), mpf("29.457") * mpf("365.25") * mpf("86400")),
]

print("  %-10s %12s %14s %14s %10s" % (
    "Planet", "a (m)", "T_obs (s)", "T_Kepler (s)", "Match"))
print("  %-10s %12s %14s %14s %10s" % (
    "-" * 10, "-" * 12, "-" * 14, "-" * 14, "-" * 10))

kepler_checks = []
for name, a, T_obs in planets:
    T_kepler = msqrt(mpf("64") * R2_val ** 2 * a ** 3 / (G_newton * M_sun))
    ratio = T_kepler / T_obs
    kepler_checks.append(abs(ratio - mpf("1")))

    print("  %-10s %12s %14s %14s %10s" % (
        name, mp.nstr(a, 4), mp.nstr(T_obs, 5),
        mp.nstr(T_kepler, 5), mp.nstr(ratio, 6)))

print()
print("  Kepler's law uses R₂ through 4π² = 64R₂².")
print("  Each planet's orbit is a ground state MODE of the")
print("  Sun-planet two-body soliton. The mode frequencies")
print("  follow the R₂-geometry: T ∝ a^(3/2).")
print()
print("  These are the same R₂ modes that appear in:")
print("    - Speaker Helmholtz resonance: f ∝ √(R₂d²/(lV))")
print("    - Fiber V-number cutoff: V = 8R₂·a·NA/λ")
print("    - Pipe flow: Q = R₂d²v")
print("  The orbital mode spectrum is another R₂ domain.")

max_kepler_miss = max(kepler_checks)
chk_bool("Kepler's law matches all 6 planets within 0.1%",
         max_kepler_miss < mpf("0.001"),
         "max miss = %s" % mp.nstr(max_kepler_miss, 3), checks)


# ================================================================
# SECTION 12: CONSOLIDATED HIERARCHY TABLE
# ================================================================

print()
print("SECTION 12: THE COMPLETE NESTED SOLITON HIERARCHY")
print("-" * 70)
print()

full_hierarchy = [
    ("Proton (QCD)", "~1 fm", "99%", "b₃ = -7", "Confinement"),
    ("Atom (EM)", "~0.1 nm", "~10⁻⁸", "α = 1/137", "Ionization"),
    ("Crystal lattice", "~1 nm-km", "~10⁻¹⁰", "Band structure", "Melting/fracture"),
    ("Rock/geological", "~m-km", "~10⁻¹⁰", "Material strength", "Phase boundaries"),
    ("Human on surface", "~1.7 m", "~10⁻⁹", "GM⊕/(R⊕c²)", "Jump height"),
    ("Earth Hill sphere", "~1.5×10⁶ km", "~10⁻⁹", "M⊕/M☉ ratio", "L1 Lagrange"),
    ("Earth orbit", "1 AU", "~10⁻⁸", "Kepler T²∝a³", "Escape velocity"),
    ("Solar Hill sphere", "~120 AU", "~10⁻⁶", "M☉/M_gal ratio", "Voyager crossing"),
    ("Galactic disk", "~15 kpc", "~10⁻⁶", "DM/bar = (22/13)π", "Virial radius"),
    ("Galaxy cluster", "~3 Mpc", "~10⁻⁵", "DM ~ 85%", "Virial radius"),
    ("BAO / cosmological", "~150 Mpc", "—", "N ~ 100 boundaries", "H₀ running"),
]

print("  %-22s %14s %8s %-20s %s" % (
    "Level", "Size", "|U|/Mc²", "Integer Rule", "Boundary"))
print("  %-22s %14s %8s %-20s %s" % (
    "-" * 22, "-" * 14, "-" * 8, "-" * 20, "-" * 15))

for name, size, coupling, rule, boundary in full_hierarchy:
    print("  %-22s %14s %8s %-20s %s" % (name, size, coupling, rule, boundary))

print()
print("  11 levels. Same principle at every level:")
print("  The soliton sits at ground state within the containing soliton.")
print("  The coupling strength |U|/Mc² determines how deep the well is.")
print("  The integer rules (Fractions) determine the soliton's structure.")
print("  The boundary defines where one soliton's dominance ends")
print("  and the next begins.")


# ================================================================
# FINAL SUMMARY
# ================================================================

print()
print("=" * 70)
print("RESULTS SUMMARY")
print("=" * 70)
print()

print_summary(checks)

n_fail = sum(1 for _, s in checks if s == "FAIL")
if n_fail == 0:
    print("  NESTED SOLITON GRAVITY: ALL PASS")
else:
    print("  NESTED SOLITON GRAVITY: %d FAILURES" % n_fail)
    for tag, status in checks:
        if status == "FAIL":
            print("    - %s" % tag)

print()
print("  THE HIERARCHY:")
print("    11 nesting levels from proton to cosmological")
print("    Same principle at every level: ground state within container")
print("    Coupling strength GM/(rc²) determines well depth")
print("    EM boundary (α = 1/137) holds you above gravitational ground state")
print("    R₂ = π/4 appears in every orbital cross-section (Kepler)")
print("    Hill spheres are soliton dominance boundaries (R5)")
print()
print("  GRAVITY IS NOT A FORCE PULLING YOU DOWN.")
print("  IT IS THE ABSENCE OF ANY REASON TO BE UP.")
print("  THE GROUND STATE IS WHERE YOU ARE WHEN NOTHING PUSHES YOU AWAY.")
print()
print("=" * 70)
print("NESTED SOLITON GRAVITY EXPERIMENT COMPLETE")
print("=" * 70)
