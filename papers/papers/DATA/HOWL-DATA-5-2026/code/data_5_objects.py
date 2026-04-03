#!/usr/bin/env python3
"""
HOWL DATA-5 OBJECT SYSTEM
============================
The object layer for the DATA-5 platform database.

Two-layer architecture:
  Layer 1: ObjectRootMeta — shared metadata for all objects
  Layer 2: Domain classes — fat structs mapping to the physics

Every object is a database node. Every node can:
  - Be searched by tag, type, or name
  - Compose with other nodes via children
  - Export to dict/JSON recursively
  - Display itself in one line

Classes:
  ObjectRootMeta     — base metadata (Layer 1, all objects inherit)
  Constant           — versioned physics value with provenance
  BetaCoefficient    — gauge coupling beta with decomposition
  Representation     — gauge group rep with derived properties
  SolitonBoundary    — boundary where physics rules change
  R2Domain           — domain where R2 = pi/4 appears
  R2Cancellation     — identity where R2 cancels in a product
  Modulus            — filling fraction tracked by the series
  ExperimentResult   — result from an experiment script
  ResearchProgram    — research program with scripts and kill switches
  DATA5              — top-level database container

Rules:
  - Python 3.8 compatible. No dataclasses. No type hints required.
  - No inheritance beyond ObjectRootMeta. Two layers only.
  - Composition via children dict. Fat structs via direct fields.
  - Version chains are append-only. Old values never deleted.
  - All objects export to dict/JSON. Children recurse automatically.
  - %% string formatting. os.path.join(). No f-strings with =.

Platform: HOWL-PLATFORM-v1
Depends on: phys24_lib.py (for Fraction, mpf, f2m, mp, show, chk_*)

What each class does:

| Class | Layer 2 content | Key properties | Key methods |
|---|---|---|---|
| ObjectRootMeta | Identity + tags + children | — | find, to_dict, to_json, show |
| Constant | Versioned value chain + unit/level/source | .value, .value_v0, .current_version | add_version, value_at, value_mpf |
| BetaCoefficient | Gauge group + decomposition | .numerator, .denominator | — |
| Representation | SU3×SU2×U1 quantum numbers + all derived | .rep_tuple, .db, .charges | — |
| SolitonBoundary | Scale + forces + couplings + questions | — | add_coupling |
| R2Domain | Equation + coordinator Z + compute_fn | — | compute |
| R2Cancellation | Formula + status + remains | — | — |
| Modulus | Value + level + origin | — | — |
| ExperimentResult | Script + value + measured + miss + status | — | — |
| ResearchProgram | Thesis + scripts + kill switches | — | add_script, add_kill_switch, add_connection |
| DATA5 | Flat index + all query methods | — | add, get, find, find_constants, find_betas, find_representations, find_boundaries, find_by_level, count, show_all, show_summary, version_report |

"""

import sys
import json

try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf

# Import from phys24_lib for type conversion and display
# If phys24_lib is not available, provide minimal fallbacks
try:
    from phys24_lib import f2m, show as _show, chk_bool, chk_exact, print_summary
except ImportError:
    def f2m(f):
        return mpf(f.numerator) / mpf(f.denominator)
    def _show(label, value):
        print("  %-40s %s" % (label, mp.nstr(value, 11)))
    def chk_bool(tag, cond, detail, checks):
        status = "PASS" if cond else "FAIL"
        checks.append((tag, status))
        print("  [%s] %s" % (status, tag))
        print("        %s" % detail)
    def chk_exact(tag, got, expected, checks):
        ok = (got == expected)
        status = "PASS" if ok else "FAIL"
        checks.append((tag, status))
        print("  [%s] %s" % (status, tag))
        print("        expected: %s  got: %s  %s" % (expected, got, "EXACT" if ok else "MISMATCH"))
    def print_summary(checks):
        n_pass = sum(1 for _, s in checks if s == "PASS")
        n_fail = sum(1 for _, s in checks if s == "FAIL")
        print("  TOTAL: %d PASS, %d FAIL out of %d" % (n_pass, n_fail, len(checks)))


_LIB_VERSION = "1"
_LIB_VERSION_1 = "Session 4, April 3 2026. Initial release. ObjectRootMeta + 10 domain classes + DATA5 container."


# ================================================================
# LAYER 1: ObjectRootMeta
# ================================================================

class ObjectRootMeta(object):
    """Base metadata layer for all DATA-5 objects.

    Every object in the system is a node in a queryable database.
    This layer provides: identity, typing, tagging, search, export.

    Fields (all objects carry these):
      obj_id           — unique string, dot-separated namespace
      obj_type         — string: "constant", "beta", "representation", etc.
      name             — human-readable label
      tags             — list of strings for search/filter
      notes            — freeform annotation string
      created_session  — int or None, session number when created
      created_date     — string or None, "YYYY-MM-DD"
      modified_session — int or None, last modification session
      modified_date    — string or None
      children         — dict of obj_id -> child object (composition)
    """

    def __init__(self, obj_id, obj_type, name, tags=None, notes=""):
        # Identity
        self.obj_id = obj_id
        self.obj_type = obj_type
        self.name = name

        # Search/filter metadata
        self.tags = list(tags) if tags else []
        self.notes = notes

        # Provenance
        self.created_session = None
        self.created_date = None
        self.modified_session = None
        self.modified_date = None

        # Composition
        self.children = {}

    def add_child(self, child):
        """Add a child object. The child must have obj_id.
        Returns the child (for chaining).
        """
        self.children[child.obj_id] = child
        return child

    def get_child(self, child_id):
        """Get a child by obj_id. Returns None if not found."""
        return self.children.get(child_id, None)

    def find(self, tag=None, obj_type=None, name_contains=None):
        """Search this object and all children recursively.
        All three filters are AND — an object must match all
        non-None filters to be included.
        Returns list of matching objects.
        """
        results = []
        if self._matches(tag, obj_type, name_contains):
            results.append(self)
        for child in self.children.values():
            if hasattr(child, 'find'):
                results.extend(child.find(tag, obj_type, name_contains))
            elif hasattr(child, '_matches'):
                if child._matches(tag, obj_type, name_contains):
                    results.append(child)
        return results

    def _matches(self, tag, obj_type, name_contains):
        """Check if this object matches the given filters."""
        if tag is not None and tag not in self.tags:
            return False
        if obj_type is not None and self.obj_type != obj_type:
            return False
        if name_contains is not None and name_contains.lower() not in self.name.lower():
            return False
        return True

    def to_dict(self):
        """Serialize to dict. Recurses through children.
        Fraction values are converted to strings for JSON safety.
        """
        d = {
            "obj_id": self.obj_id,
            "obj_type": self.obj_type,
            "name": self.name,
            "tags": self.tags,
            "notes": self.notes,
            "created_session": self.created_session,
            "created_date": self.created_date,
            "modified_session": self.modified_session,
            "modified_date": self.modified_date,
        }
        if self.children:
            d["children"] = {}
            for k, v in self.children.items():
                if hasattr(v, 'to_dict'):
                    d["children"][k] = v.to_dict()
                else:
                    d["children"][k] = str(v)
        return d

    def to_json(self, indent=2):
        """Export to JSON string. All non-serializable values
        are converted via the _json_default handler.
        """
        return json.dumps(self.to_dict(), indent=indent, default=_json_default)

    def show(self):
        """One-line display for quick scanning."""
        print("  [%s] %s: %s  tags=%s" % (
            self.obj_type, self.obj_id, self.name, self.tags))

    def __repr__(self):
        return "<%s %s '%s'>" % (self.obj_type, self.obj_id, self.name)


def _json_default(obj):
    """JSON serializer fallback for Fraction, mpf, and other types."""
    if isinstance(obj, Fraction):
        return {"_type": "Fraction", "num": obj.numerator, "den": obj.denominator,
                "decimal": str(float(obj))}
    if isinstance(obj, mpf):
        return {"_type": "mpf", "value": mp.nstr(obj, 15)}
    return str(obj)


# ================================================================
# LAYER 2: DOMAIN CLASSES
# ================================================================


class Constant(ObjectRootMeta):
    """A physics constant with version history.

    The value chain:
      versions[0] = v0 = original value (never changes)
      versions[1] = v1 = first update (if any)
      ...
      .value      = alias to latest version
      .value_v0   = always the original

    Version rules:
      - Append-only. Once added, a version is never removed or modified.
      - .value always returns the latest.
      - .value_v0 always returns the original.
      - .value_at(n) returns version n.
      - If a version is wrong, add a new one — don't edit the old.

    Level convention:
      0 = pure geometry (R2, pi, e, sqrt2, Bessel zeros)
      1 = group theory (beta coefficients, Casimirs, Dynkin indices)
      2 = measured (alpha_inv, sin2_tW, alpha_s, masses)
      3 = prediction / derived (alpha_s from unification, Koide m_tau)
    """

    def __init__(self, obj_id, name, value, unit="", level=None,
                 digits=None, source="", data4_id=None, tags=None,
                 uncertainty=None, notes=""):
        super(Constant, self).__init__(obj_id, "constant", name,
                                        tags=tags, notes=notes)

        # The version chain — append-only
        self.versions = [value]
        self.version_sources = [source]
        self.version_sessions = [None]

        # Metadata
        self.unit = unit
        self.level = level
        self.digits = digits
        self.data4_id = data4_id
        self.uncertainty = uncertainty
        self.source = source

    @property
    def value(self):
        """Current (latest) value."""
        return self.versions[-1]

    @property
    def value_v0(self):
        """Original value. Never changes."""
        return self.versions[0]

    def value_at(self, version):
        """Value at a specific version number. Returns None if out of range."""
        if 0 <= version < len(self.versions):
            return self.versions[version]
        return None

    @property
    def current_version(self):
        """Current version number (0-based)."""
        return len(self.versions) - 1

    def add_version(self, new_value, source="", session=None):
        """Add a new version. The old value is preserved forever.
        .value now returns the new value. .value_v0 unchanged.
        """
        self.versions.append(new_value)
        self.version_sources.append(source)
        self.version_sessions.append(session)
        self.modified_session = session

    def value_mpf(self):
        """Current value as mpf (for display).
        Converts Fraction to mpf. Passes mpf through unchanged.
        """
        v = self.value
        if isinstance(v, Fraction):
            return f2m(v)
        if isinstance(v, mpf):
            return v
        return mpf(str(v))

    def show(self):
        """One-line display with value, version, level, source."""
        v = self.value_mpf()
        v_str = mp.nstr(v, 11)
        level_str = "L%s" % self.level if self.level is not None else "L?"
        print("  [const] %-35s = %s %s  (v%d, %s, %s)" % (
            self.name, v_str, self.unit,
            self.current_version, level_str, self.source))

    def to_dict(self):
        d = super(Constant, self).to_dict()
        d["value"] = self.value
        d["unit"] = self.unit
        d["level"] = self.level
        d["digits"] = self.digits
        d["source"] = self.source
        d["data4_id"] = self.data4_id
        d["uncertainty"] = self.uncertainty
        d["n_versions"] = len(self.versions)
        d["versions"] = list(self.versions)
        d["version_sources"] = list(self.version_sources)
        d["version_sessions"] = list(self.version_sessions)
        return d


class BetaCoefficient(ObjectRootMeta):
    """A gauge coupling beta coefficient with decomposition.

    Stores the total value and its constituent parts:
      gauge_part   — gauge boson self-interaction (e.g. -11 for SU(3))
      fermion_part — fermion contributions (e.g. +4 for 3 generations)
      higgs_part   — Higgs contribution (e.g. +1/6 for SU(2))
      bsm_part     — BSM contribution (e.g. +1 for CD in SU(2))

    All parts are Fraction. Total = gauge + fermion + higgs + bsm.
    """

    def __init__(self, obj_id, name, gauge_group, value,
                 gauge_part=None, fermion_part=None,
                 higgs_part=None, bsm_part=None,
                 tags=None, notes=""):
        super(BetaCoefficient, self).__init__(obj_id, "beta", name,
                                               tags=tags, notes=notes)

        self.gauge_group = gauge_group
        self.value = value
        self.gauge_part = gauge_part
        self.fermion_part = fermion_part
        self.higgs_part = higgs_part
        self.bsm_part = bsm_part

    @property
    def numerator(self):
        """Absolute value of the Fraction numerator.
        For b2_mod = -13/6: returns 13.
        """
        if isinstance(self.value, Fraction):
            return abs(self.value.numerator)
        return None

    @property
    def denominator(self):
        """Fraction denominator.
        For b2_mod = -13/6: returns 6.
        """
        if isinstance(self.value, Fraction):
            return self.value.denominator
        return None

    def show(self):
        v_float = float(f2m(self.value)) if isinstance(self.value, Fraction) else float(self.value)
        print("  [beta]  %-35s (%s) = %s = %.4f" % (
            self.name, self.gauge_group, self.value, v_float))

    def to_dict(self):
        d = super(BetaCoefficient, self).to_dict()
        d["gauge_group"] = self.gauge_group
        d["value"] = self.value
        d["gauge_part"] = self.gauge_part
        d["fermion_part"] = self.fermion_part
        d["higgs_part"] = self.higgs_part
        d["bsm_part"] = self.bsm_part
        return d


class Representation(ObjectRootMeta):
    """A gauge group representation with all derived properties.

    Stores the representation quantum numbers (SU3 dim, SU2 dim, Y)
    and computes all derived quantities: beta shifts, charges,
    Dynkin indices, Casimirs.

    If phys24_structure_lib is available, delegates to make_rep().
    Otherwise computes directly from the formulas.
    """

    def __init__(self, obj_id, name, su3_dim, su2_dim, Y,
                 rep_type="chiral", tags=None, notes=""):
        super(Representation, self).__init__(obj_id, "representation", name,
                                              tags=tags, notes=notes)

        self.su3_dim = su3_dim
        self.su2_dim = su2_dim
        self.Y = Fraction(Y) if not isinstance(Y, Fraction) else Y
        self.rep_type = rep_type

        # Compute derived properties
        self._compute_properties()

    def _compute_properties(self):
        """Compute beta shifts, charges, Dynkin indices, Casimirs."""
        su3 = Fraction(self.su3_dim)
        su2 = Fraction(self.su2_dim)
        Y_f = self.Y

        # Dynkin index: S2(fund) = 1/2, S2(singlet) = 0
        self.S2_R3 = Fraction(1, 2) if self.su3_dim > 1 else Fraction(0)
        self.S2_R2 = Fraction(1, 2) if self.su2_dim > 1 else Fraction(0)

        # Casimir: C2(fund SU(N)) = (N^2-1)/(2N), C2(singlet) = 0
        if self.su3_dim > 1:
            self.C2_R3 = Fraction(self.su3_dim * self.su3_dim - 1,
                                   2 * self.su3_dim)
        else:
            self.C2_R3 = Fraction(0)

        if self.su2_dim > 1:
            self.C2_R2 = Fraction(self.su2_dim * self.su2_dim - 1,
                                   2 * self.su2_dim)
        else:
            self.C2_R2 = Fraction(0)

        # Beta shift coefficients
        if self.rep_type == "vector-like":
            self.db1 = Fraction(2, 5) * su3 * su2 * Y_f * Y_f
            self.db2 = Fraction(2, 3) * su3 * self.S2_R2
            self.db3 = Fraction(1, 3) * su2 * self.S2_R3
        else:
            self.db1 = Fraction(2, 5) * su3 * su2 * Y_f * Y_f
            self.db2 = Fraction(2, 3) * su3 * self.S2_R2
            self.db3 = Fraction(2, 3) * su2 * self.S2_R3

        # Electric charges: Q = T3 + Y
        if self.su2_dim == 2:
            self.charges = (Fraction(1, 2) + Y_f, Fraction(-1, 2) + Y_f)
        elif self.su2_dim == 1:
            self.charges = (Y_f,)
        elif self.su2_dim == 3:
            self.charges = (Fraction(1, 1) + Y_f, Y_f, Fraction(-1, 1) + Y_f)
        else:
            self.charges = (Y_f,)

    @property
    def rep_tuple(self):
        """The representation as (SU3_dim, SU2_dim, Y) tuple."""
        return (self.su3_dim, self.su2_dim, self.Y)

    @property
    def db(self):
        """Beta shifts as (db1, db2, db3) tuple."""
        return (self.db1, self.db2, self.db3)

    def show(self):
        print("  [rep]   %-35s (%d,%d,%s) %s  db=(%s, %s, %s)" % (
            self.name, self.su3_dim, self.su2_dim, self.Y,
            self.rep_type, self.db1, self.db2, self.db3))

    def to_dict(self):
        d = super(Representation, self).to_dict()
        d["su3_dim"] = self.su3_dim
        d["su2_dim"] = self.su2_dim
        d["Y"] = self.Y
        d["rep_type"] = self.rep_type
        d["db1"] = self.db1
        d["db2"] = self.db2
        d["db3"] = self.db3
        d["charges"] = list(self.charges)
        d["S2_R3"] = self.S2_R3
        d["S2_R2"] = self.S2_R2
        d["C2_R3"] = self.C2_R3
        d["C2_R2"] = self.C2_R2
        return d


class SolitonBoundary(ObjectRootMeta):
    """A boundary where the physics rules change.

    The boundary stack maps physical reality from Planck to
    cosmological scales. Each boundary records:
      - Energy and distance scales (or None if unknown)
      - What changes at the boundary
      - Which forces are affected
      - Coupling values at the boundary (or None)
      - Properties above and below
      - Open questions

    Some boundaries are sharp (electron threshold). Some are
    approximate (confinement wall). Some are unknown (GUT scale).
    The fat struct accommodates all variants — fields that don't
    apply are None or empty.
    """

    def __init__(self, obj_id, name, scale_MeV=None, scale_fm=None,
                 what_changes="", forces_affected=None,
                 known=False, tags=None, notes=""):
        super(SolitonBoundary, self).__init__(obj_id, "boundary", name,
                                               tags=tags, notes=notes)

        self.scale_MeV = scale_MeV
        self.scale_fm = scale_fm
        self.what_changes = what_changes
        self.forces_affected = forces_affected or []
        self.known = known

        # Coupling values at this boundary
        # Dict of coupling_name -> value (Fraction, mpf, or None)
        self.couplings = {}

        # Properties above and below the boundary
        self.above = {}
        self.below = {}

        # Open questions at this boundary
        self.open_questions = []

        # Optional: window bounds for staged boundaries
        self.scale_MeV_lo = None
        self.scale_MeV_hi = None
        self.scale_MeV_estimate = None

    def add_coupling(self, name, value):
        """Add a coupling value at this boundary."""
        self.couplings[name] = value

    def show(self):
        scale_str = "?"
        if self.scale_MeV is not None:
            s = f2m(self.scale_MeV) if isinstance(self.scale_MeV, Fraction) else self.scale_MeV
            scale_str = "%s MeV" % mp.nstr(s, 4)
        elif self.scale_MeV_estimate is not None:
            s = f2m(self.scale_MeV_estimate) if isinstance(self.scale_MeV_estimate, Fraction) else self.scale_MeV_estimate
            scale_str = "~%s MeV (est)" % mp.nstr(s, 4)
        print("  [bound] %-35s at %s  known=%s  forces=%s" % (
            self.name, scale_str, self.known, self.forces_affected))

    def to_dict(self):
        d = super(SolitonBoundary, self).to_dict()
        d["scale_MeV"] = self.scale_MeV
        d["scale_fm"] = self.scale_fm
        d["what_changes"] = self.what_changes
        d["forces_affected"] = self.forces_affected
        d["known"] = self.known
        d["couplings"] = dict(self.couplings)
        d["above"] = dict(self.above)
        d["below"] = dict(self.below)
        d["open_questions"] = list(self.open_questions)
        d["scale_MeV_lo"] = self.scale_MeV_lo
        d["scale_MeV_hi"] = self.scale_MeV_hi
        d["scale_MeV_estimate"] = self.scale_MeV_estimate
        return d


class R2Domain(ObjectRootMeta):
    """A domain where R2 = pi/4 appears.

    Stores the equation (e.g. "Q = R2*d^2*v"), the coordinator Z
    (what makes this domain different from others), precision,
    and an optional callable for computation.
    """

    def __init__(self, obj_id, name, equation, coordinator_Z,
                 precision="", compute_fn=None, data1_section=None,
                 data1_id=None, tags=None, notes=""):
        super(R2Domain, self).__init__(obj_id, "domain", name,
                                        tags=tags, notes=notes)

        self.equation = equation
        self.coordinator_Z = coordinator_Z
        self.precision = precision
        self.compute_fn = compute_fn
        self.data1_section = data1_section
        self.data1_id = data1_id

    def compute(self, *args, **kwargs):
        """Run the domain's computation if a function is attached."""
        if self.compute_fn is not None:
            return self.compute_fn(*args, **kwargs)
        return None

    def show(self):
        print("  [dom]   %-35s %s  Z=%s" % (
            self.name, self.equation, self.coordinator_Z))

    def to_dict(self):
        d = super(R2Domain, self).to_dict()
        d["equation"] = self.equation
        d["coordinator_Z"] = self.coordinator_Z
        d["precision"] = self.precision
        d["data1_section"] = self.data1_section
        d["data1_id"] = self.data1_id
        d["has_compute_fn"] = self.compute_fn is not None
        return d


class R2Cancellation(ObjectRootMeta):
    """An R2 cancellation identity.

    Records: what product or ratio cancels R2, the formula,
    what remains after cancellation, and precision.

    Status values:
      "CANCELS"   — R2 drops out of the product/ratio
      "R2-FREE"   — R2 never entered (the quantity has no R2 content)
      "REAPPEARS" — R2 cancels partially but reappears in the result
    """

    def __init__(self, obj_id, name, formula, status, remains,
                 precision="", data1_id=None, tags=None, notes=""):
        super(R2Cancellation, self).__init__(obj_id, "cancellation", name,
                                              tags=tags, notes=notes)

        self.formula = formula
        self.status = status
        self.remains = remains
        self.precision = precision
        self.data1_id = data1_id

    def show(self):
        print("  [canc]  [%s] %-30s %s  ->  %s" % (
            self.status, self.name, self.formula[:40], self.remains))

    def to_dict(self):
        d = super(R2Cancellation, self).to_dict()
        d["formula"] = self.formula
        d["status"] = self.status
        d["remains"] = self.remains
        d["precision"] = self.precision
        d["data1_id"] = self.data1_id
        return d


class Modulus(ObjectRootMeta):
    """A filling fraction / modulus tracked by the series.

    A modulus measures how much of one geometric structure fits
    within another:
      R2 = pi/4     — circle fills 78.5%% of its bounding square
      b3 = -7       — net gauge-group filling for SU(3)
      K = 2/3       — Koide mass-sum filling fraction
      sin2_tW = 0.23 — weak fraction of EM coupling

    Level convention:
      0 = pure geometry (R2, R4, Bessel zeros)
      1 = group theory (betas, Casimirs, gap ratios)
      2 = measured (alpha, sin2_tW, Koide K)
      3 = prediction (alpha_s from unification)
    """

    def __init__(self, obj_id, name, value, level, origin,
                 cancels_in=None, tags=None, notes=""):
        super(Modulus, self).__init__(obj_id, "modulus", name,
                                      tags=tags, notes=notes)

        self.value = value
        self.level = level
        self.origin = origin
        self.cancels_in = cancels_in or []

    def show(self):
        v_str = str(self.value)
        if isinstance(self.value, Fraction):
            v_str = "%s = %s" % (self.value, mp.nstr(f2m(self.value), 6))
        elif isinstance(self.value, mpf):
            v_str = mp.nstr(self.value, 6)
        print("  [mod]   %-35s = %s  (L%d, %s)" % (
            self.name, v_str, self.level, self.origin))

    def to_dict(self):
        d = super(Modulus, self).to_dict()
        d["value"] = self.value
        d["level"] = self.level
        d["origin"] = self.origin
        d["cancels_in"] = self.cancels_in
        return d


class ExperimentResult(ObjectRootMeta):
    """A result from an experiment script.

    Links the script that produced it, the computed value,
    the measured comparison (if any), the percentage miss,
    and the PASS/FAIL status.
    """

    def __init__(self, obj_id, name, script, value, measured=None,
                 miss_pct=None, status="PASS", tags=None, notes=""):
        super(ExperimentResult, self).__init__(obj_id, "result", name,
                                                tags=tags, notes=notes)

        self.script = script
        self.value = value
        self.measured = measured
        self.miss_pct = miss_pct
        self.status = status

    def show(self):
        miss_str = ""
        if self.miss_pct is not None:
            miss_str = " miss=%s%%" % (mp.nstr(self.miss_pct, 3)
                                         if isinstance(self.miss_pct, mpf)
                                         else str(self.miss_pct))
        print("  [res]   [%s] %-30s %s%s  (%s)" % (
            self.status, self.name,
            str(self.value)[:20], miss_str, self.script))

    def to_dict(self):
        d = super(ExperimentResult, self).to_dict()
        d["script"] = self.script
        d["value"] = self.value
        d["measured"] = self.measured
        d["miss_pct"] = self.miss_pct
        d["status"] = self.status
        return d


class ResearchProgram(ObjectRootMeta):
    """A research program with scripts, kill switches, and status.

    Status values:
      "ACTIVE"    — under investigation
      "PARKED"    — paused, not killed
      "KILLED"    — falsified, do not reopen
      "CONFIRMED" — verified by independent test
    """

    def __init__(self, obj_id, name, thesis, status="ACTIVE",
                 tags=None, notes=""):
        super(ResearchProgram, self).__init__(obj_id, "program", name,
                                               tags=tags, notes=notes)

        self.thesis = thesis
        self.status = status
        self.scripts = []
        self.kill_switches = []
        self.connections = {}

    def add_script(self, script_name, description="", stage=None):
        """Add a script to the program."""
        self.scripts.append({
            "name": script_name,
            "description": description,
            "stage": stage,
        })

    def add_kill_switch(self, name, condition, data_source=""):
        """Add a kill switch — a condition that would falsify the thesis."""
        self.kill_switches.append({
            "name": name,
            "condition": condition,
            "data_source": data_source,
        })

    def add_connection(self, program_id, relationship):
        """Add a connection to another research program."""
        self.connections[program_id] = relationship

    def show(self):
        print("  [prog]  [%s] %-30s %d scripts, %d kill switches" % (
            self.status, self.name,
            len(self.scripts), len(self.kill_switches)))

    def to_dict(self):
        d = super(ResearchProgram, self).to_dict()
        d["thesis"] = self.thesis
        d["status"] = self.status
        d["scripts"] = list(self.scripts)
        d["kill_switches"] = list(self.kill_switches)
        d["connections"] = dict(self.connections)
        return d


# ================================================================
# THE DATABASE: DATA5
# ================================================================

class DATA5(ObjectRootMeta):
    """The DATA-5 database. Top-level container for all objects.

    Provides:
      - add(obj)              — add any object
      - get(obj_id)           — O(1) lookup by ID
      - find(tag, obj_type, name_contains) — search with AND filters
      - find_constants(tag)   — shortcut for constants
      - find_boundaries()     — shortcut for boundaries
      - find_by_level(level)  — find objects by modulus level
      - count(obj_type)       — count objects
      - show_all(obj_type, tag) — display matching objects
      - show_summary()        — database overview
      - version_report()      — show versioned constants
      - to_json()             — full export
    """

    def __init__(self):
        super(DATA5, self).__init__("data5", "database",
                                     "DATA-5 Platform Database",
                                     tags=["root", "database"])
        self._index = {}

    def add(self, obj):
        """Add an object to the database. Also indexes all
        children recursively for O(1) lookup.
        Returns the object (for chaining).
        """
        self.children[obj.obj_id] = obj
        self._index[obj.obj_id] = obj
        self._index_children(obj)
        return obj

    def _index_children(self, obj):
        """Recursively index all children of an object."""
        if hasattr(obj, 'children'):
            for child_id, child in obj.children.items():
                self._index[child_id] = child
                self._index_children(child)

    def get(self, obj_id):
        """Get an object by ID. O(1) lookup via flat index.
        Returns None if not found.
        """
        return self._index.get(obj_id, None)

    def find(self, tag=None, obj_type=None, name_contains=None):
        """Search all indexed objects.
        All three filters are AND — object must match all non-None.
        Returns list of matching objects.
        """
        results = []
        for obj in self._index.values():
            if hasattr(obj, '_matches') and obj._matches(tag, obj_type, name_contains):
                results.append(obj)
        return results

    def find_constants(self, tag=None):
        """Shortcut: find all constants, optionally filtered by tag."""
        return self.find(tag=tag, obj_type="constant")

    def find_betas(self, gauge_group=None):
        """Shortcut: find all beta coefficients, optionally by gauge group."""
        betas = self.find(obj_type="beta")
        if gauge_group is not None:
            betas = [b for b in betas
                     if hasattr(b, 'gauge_group') and b.gauge_group == gauge_group]
        return betas

    def find_representations(self, rep_type=None):
        """Shortcut: find all representations, optionally by type."""
        reps = self.find(obj_type="representation")
        if rep_type is not None:
            reps = [r for r in reps
                    if hasattr(r, 'rep_type') and r.rep_type == rep_type]
        return reps

    def find_boundaries(self, known_only=False):
        """Shortcut: find all soliton boundaries."""
        bounds = self.find(obj_type="boundary")
        if known_only:
            bounds = [b for b in bounds if hasattr(b, 'known') and b.known]
        return bounds

    def find_by_level(self, level):
        """Find all objects with a specific modulus level (0,1,2,3).
        Works on Constants, Modulus, and any object with a .level field.
        """
        return [obj for obj in self._index.values()
                if hasattr(obj, 'level') and obj.level == level]

    def count(self, obj_type=None):
        """Count objects in the database, optionally by type."""
        if obj_type is not None:
            return len([o for o in self._index.values()
                        if o.obj_type == obj_type])
        return len(self._index)

    def show_all(self, obj_type=None, tag=None):
        """Display all objects matching the filters."""
        for obj in self.find(tag=tag, obj_type=obj_type):
            obj.show()

    def show_summary(self):
        """Print a summary of database contents by type."""
        types = {}
        for obj in self._index.values():
            t = obj.obj_type
            types[t] = types.get(t, 0) + 1

        print("=" * 70)
        print("DATA-5 DATABASE SUMMARY")
        print("=" * 70)
        print()
        for t in sorted(types.keys()):
            print("  %-20s %d objects" % (t, types[t]))
        print()
        print("  TOTAL: %d objects" % len(self._index))
        print("=" * 70)

    def version_report(self):
        """Show all constants that have been versioned (more than v0)."""
        versioned = [obj for obj in self._index.values()
                     if hasattr(obj, 'versions') and len(obj.versions) > 1]
        if not versioned:
            print("  No versioned constants. All at v0.")
            return
        print("  VERSIONED CONSTANTS:")
        for obj in versioned:
            print("    %s: %d versions (current v%d)" % (
                obj.name, len(obj.versions), obj.current_version))
            for i in range(len(obj.versions)):
                marker = " <-- ACTIVE" if i == len(obj.versions) - 1 else ""
                print("      v%d: %s (%s)%s" % (
                    i, obj.versions[i], obj.version_sources[i], marker))


# ================================================================
# STANDALONE HELPER FUNCTIONS
# ================================================================

def search(db, query):
    """Search by any substring in name, tags, notes, or obj_id.
    More permissive than db.find() — checks all text fields.
    """
    results = []
    q = query.lower()
    for obj in db._index.values():
        if (q in obj.name.lower() or
            q in " ".join(obj.tags).lower() or
            q in obj.notes.lower() or
            q in obj.obj_id.lower()):
            results.append(obj)
    return results


def constants_at_level(db, level):
    """All constants at a specific modulus level."""
    return [o for o in db.find(obj_type="constant")
            if hasattr(o, 'level') and o.level == level]


def show_constants(db, tag=None):
    """Display all constants, optionally filtered by tag."""
    for c in db.find_constants(tag=tag):
        c.show()


def show_boundaries(db, known_only=False):
    """Display boundary stack."""
    for b in db.find_boundaries(known_only=known_only):
        b.show()


def show_R2(db):
    """Display all R2 domains."""
    for d in db.find(obj_type="domain"):
        d.show()


def show_cancellations(db, status=None):
    """Display R2 cancellation registry, optionally filtered by status."""
    for c in db.find(obj_type="cancellation"):
        if status is not None and hasattr(c, 'status') and c.status != status:
            continue
        c.show()


def export_json(db, filename):
    """Export entire database to a JSON file."""
    with open(filename, 'w') as f:
        f.write(db.to_json())
    print("  Exported %d objects to %s" % (db.count(), filename))


# ================================================================
# SELF-TEST
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DATA_5_OBJECTS SELF-TEST")
    print("=" * 70)
    print()

    checks = []

    # --------------------------------------------------------
    print("LAYER 1: ObjectRootMeta")
    print("-" * 70)
    print()

    root = ObjectRootMeta("test.root", "test", "Test Root",
                           tags=["tag1", "tag2"], notes="test notes")

    chk_bool("ObjectRootMeta creates with obj_id",
             root.obj_id == "test.root",
             "obj_id = %s" % root.obj_id, checks)

    chk_bool("ObjectRootMeta has tags",
             root.tags == ["tag1", "tag2"],
             "tags = %s" % root.tags, checks)

    # Child composition
    child = ObjectRootMeta("test.child", "test", "Test Child",
                            tags=["child_tag"])
    root.add_child(child)

    chk_bool("add_child stores child",
             root.get_child("test.child") is child,
             "child found", checks)

    # Recursive find
    found = root.find(tag="child_tag")
    chk_bool("find() finds child by tag",
             len(found) == 1 and found[0].obj_id == "test.child",
             "found %d objects" % len(found), checks)

    # to_dict
    d = root.to_dict()
    chk_bool("to_dict includes children",
             "children" in d and "test.child" in d["children"],
             "children keys = %s" % list(d.get("children", {}).keys()), checks)

    # to_json
    j = root.to_json()
    parsed = json.loads(j)
    chk_bool("to_json produces valid JSON",
             parsed["obj_id"] == "test.root",
             "parsed obj_id = %s" % parsed["obj_id"], checks)

    # --------------------------------------------------------
    print()
    print("LAYER 2: Constant")
    print("-" * 70)
    print()

    c1 = Constant("const.test", "Test Constant",
                   Fraction(137, 1000), unit="dimensionless",
                   level=2, digits=3, source="test",
                   tags=["test", "coupling"])

    chk_bool("Constant initial value is v0",
             c1.value == Fraction(137, 1000),
             "value = %s" % c1.value, checks)

    chk_bool("Constant value == value_v0",
             c1.value == c1.value_v0,
             "value == value_v0", checks)

    chk_bool("Constant current_version == 0",
             c1.current_version == 0,
             "version = %d" % c1.current_version, checks)

    # Add a version
    c1.add_version(Fraction(138, 1000), source="updated", session=5)

    chk_bool("After add_version: value is new",
             c1.value == Fraction(138, 1000),
             "value = %s" % c1.value, checks)

    chk_bool("After add_version: value_v0 is original",
             c1.value_v0 == Fraction(137, 1000),
             "value_v0 = %s" % c1.value_v0, checks)

    chk_bool("After add_version: current_version == 1",
             c1.current_version == 1,
             "version = %d" % c1.current_version, checks)

    chk_bool("value_at(0) returns original",
             c1.value_at(0) == Fraction(137, 1000),
             "value_at(0) = %s" % c1.value_at(0), checks)

    chk_bool("value_at(1) returns updated",
             c1.value_at(1) == Fraction(138, 1000),
             "value_at(1) = %s" % c1.value_at(1), checks)

    chk_bool("value_at(99) returns None",
             c1.value_at(99) is None,
             "value_at(99) = None", checks)

    # value_mpf
    chk_bool("value_mpf returns mpf",
             isinstance(c1.value_mpf(), mpf),
             "type = %s" % type(c1.value_mpf()).__name__, checks)

    # JSON export with Fraction
    j2 = c1.to_json()
    parsed2 = json.loads(j2)
    chk_bool("Constant JSON has n_versions",
             parsed2.get("n_versions") == 2,
             "n_versions = %s" % parsed2.get("n_versions"), checks)

    # --------------------------------------------------------
    print()
    print("LAYER 2: BetaCoefficient")
    print("-" * 70)
    print()

    b2 = BetaCoefficient("beta.b2_mod", "b2 modified (SU2)",
                          "SU2", Fraction(-13, 6),
                          gauge_part=Fraction(-22, 3),
                          fermion_part=Fraction(4, 1),
                          higgs_part=Fraction(1, 6),
                          bsm_part=Fraction(1, 1),
                          tags=["Level1", "SU2", "modified"])

    chk_exact("BetaCoefficient value = -13/6",
              b2.value, Fraction(-13, 6), checks)

    chk_bool("BetaCoefficient numerator = 13",
             b2.numerator == 13,
             "numerator = %s" % b2.numerator, checks)

    chk_bool("BetaCoefficient denominator = 6",
             b2.denominator == 6,
             "denominator = %s" % b2.denominator, checks)

    # --------------------------------------------------------
    print()
    print("LAYER 2: Representation")
    print("-" * 70)
    print()

    cd = Representation("rep.CD", "Cabibbo Doublet",
                         3, 2, Fraction(1, 6), "vector-like",
                         tags=["CD", "BSM"])

    chk_exact("CD db1 = 1/15",
              cd.db1, Fraction(1, 15), checks)

    chk_exact("CD db2 = 1",
              cd.db2, Fraction(1, 1), checks)

    chk_exact("CD db3 = 1/3",
              cd.db3, Fraction(1, 3), checks)

    chk_bool("CD rep_tuple = (3, 2, 1/6)",
             cd.rep_tuple == (3, 2, Fraction(1, 6)),
             "rep_tuple = %s" % (cd.rep_tuple,), checks)

    chk_bool("CD upper charge = 2/3",
             cd.charges[0] == Fraction(2, 3),
             "upper = %s" % cd.charges[0], checks)

    chk_bool("CD lower charge = -1/3",
             cd.charges[1] == Fraction(-1, 3),
             "lower = %s" % cd.charges[1], checks)

    # SM generation: Q_L chiral
    ql = Representation("rep.Q_L", "Left quark doublet",
                         3, 2, Fraction(1, 6), "chiral")

    chk_exact("Q_L db3 = 2/3 (chiral, not 1/3)",
              ql.db3, Fraction(2, 3), checks)

    # --------------------------------------------------------
    print()
    print("LAYER 2: SolitonBoundary")
    print("-" * 70)
    print()

    mz_b = SolitonBoundary("boundary.mz", "Electroweak scale (M_Z)",
                            scale_MeV=Fraction(911876, 10),
                            what_changes="Reference scale for couplings",
                            forces_affected=["electromagnetic", "weak", "strong"],
                            known=True,
                            tags=["EW", "reference"])
    mz_b.add_coupling("1/alpha_EM", Fraction(137035999177, 10**9))
    mz_b.open_questions.append("Test question?")

    chk_bool("Boundary stores scale_MeV",
             mz_b.scale_MeV == Fraction(911876, 10),
             "scale = %s" % mz_b.scale_MeV, checks)

    chk_bool("Boundary stores coupling",
             mz_b.couplings.get("1/alpha_EM") == Fraction(137035999177, 10**9),
             "coupling stored", checks)

    chk_bool("Boundary stores open question",
             len(mz_b.open_questions) == 1,
             "questions = %d" % len(mz_b.open_questions), checks)

    # --------------------------------------------------------
    print()
    print("LAYER 2: R2Domain, R2Cancellation, Modulus")
    print("-" * 70)
    print()

    dom = R2Domain("domain.01_pipe", "Pipe flow",
                    "Q = R2*d^2*v", "velocity v",
                    precision="0.05%",
                    tags=["R2", "flow"])

    chk_bool("R2Domain stores equation",
             dom.equation == "Q = R2*d^2*v",
             "equation = %s" % dom.equation, checks)

    cancel = R2Cancellation("cancel.01_kj_rk", "K_J x R_K",
                             "(2e/h)(h/e^2)", "CANCELS", "2/e",
                             precision="10^-8",
                             tags=["R2", "metrology"])

    chk_bool("R2Cancellation stores status",
             cancel.status == "CANCELS",
             "status = %s" % cancel.status, checks)

    mod = Modulus("modulus.R2", "R2 = pi/4",
                   Fraction(1, 1),  # placeholder
                   level=0, origin="circle-in-square",
                   tags=["Level0", "geometry"])

    chk_bool("Modulus stores level",
             mod.level == 0,
             "level = %d" % mod.level, checks)

    # --------------------------------------------------------
    print()
    print("LAYER 2: ExperimentResult, ResearchProgram")
    print("-" * 70)
    print()

    result = ExperimentResult("result.gps", "GPS correction",
                               "time_process_rate_test.py",
                               mpf("38499"), measured=mpf("38000"),
                               miss_pct=mpf("1.3"), status="PASS",
                               tags=["time", "GPS"])

    chk_bool("ExperimentResult stores status",
             result.status == "PASS",
             "status = %s" % result.status, checks)

    prog = ResearchProgram("program.beta", "Beta Unification",
                            "Gauge group integers determine cosmological parameters",
                            status="ACTIVE",
                            tags=["beta", "unification"])
    prog.add_script("beta_statistical_control.py", "Statistical significance", stage=1)
    prog.add_kill_switch("coincidence_test", "p > 0.1 for integer matches")
    prog.add_connection("program.hubble", "shares integer 13")

    chk_bool("ResearchProgram has 1 script",
             len(prog.scripts) == 1,
             "scripts = %d" % len(prog.scripts), checks)

    chk_bool("ResearchProgram has 1 kill switch",
             len(prog.kill_switches) == 1,
             "kills = %d" % len(prog.kill_switches), checks)

    chk_bool("ResearchProgram has 1 connection",
             len(prog.connections) == 1,
             "connections = %d" % len(prog.connections), checks)

    # --------------------------------------------------------
    print()
    print("DATABASE: DATA5")
    print("-" * 70)
    print()

    db = DATA5()
    db.add(c1)
    db.add(b2)
    db.add(cd)
    db.add(mz_b)
    db.add(dom)
    db.add(cancel)
    db.add(mod)
    db.add(result)
    db.add(prog)

    chk_bool("DATA5 count = 9",
             db.count() == 9,
             "count = %d" % db.count(), checks)

    chk_bool("DATA5.get by ID works",
             db.get("const.test") is c1,
             "found const.test", checks)

    chk_bool("DATA5.find by tag works",
             len(db.find(tag="SU2")) >= 1,
             "SU2 objects = %d" % len(db.find(tag="SU2")), checks)

    chk_bool("DATA5.find by obj_type works",
             len(db.find(obj_type="constant")) == 1,
             "constants = %d" % len(db.find(obj_type="constant")), checks)

    chk_bool("DATA5.find_constants returns Constant objects",
             all(isinstance(o, Constant) for o in db.find_constants()),
             "all Constant", checks)

    chk_bool("DATA5.find_boundaries returns SolitonBoundary objects",
             all(isinstance(o, SolitonBoundary) for o in db.find_boundaries()),
             "all SolitonBoundary", checks)

    chk_bool("DATA5.find_betas(SU2) finds b2_mod",
             len(db.find_betas("SU2")) == 1,
             "SU2 betas = %d" % len(db.find_betas("SU2")), checks)

    chk_bool("DATA5.find_by_level(2) finds Level 2 objects",
             len(db.find_by_level(2)) >= 1,
             "Level 2 objects = %d" % len(db.find_by_level(2)), checks)

    chk_bool("DATA5.count by type works",
             db.count("beta") == 1,
             "betas = %d" % db.count("beta"), checks)

    # search() standalone helper
    found_su2 = search(db, "su2")
    chk_bool("search() finds by tag substring",
             len(found_su2) >= 1,
             "search('su2') = %d results" % len(found_su2), checks)

    # JSON export
    full_json = db.to_json()
    full_parsed = json.loads(full_json)
    chk_bool("Full database JSON is valid",
             full_parsed["obj_id"] == "data5",
             "root obj_id = %s" % full_parsed["obj_id"], checks)

    chk_bool("Full database JSON has children",
             "children" in full_parsed and len(full_parsed["children"]) == 9,
             "children count = %d" % len(full_parsed.get("children", {})), checks)

    # Version report
    print()
    print("VERSION REPORT:")
    db.version_report()

    # Show summary
    print()
    db.show_summary()

    # Show all objects
    print()
    print("ALL OBJECTS:")
    print("-" * 70)
    db.show_all()

    # --------------------------------------------------------
    print()
    print_summary(checks)

    n_fail = sum(1 for _, s in checks if s == "FAIL")
    print()
    if n_fail == 0:
        print("  DATA_5_OBJECTS: OPERATIONAL")
    else:
        print("  DATA_5_OBJECTS: %d FAILURES" % n_fail)
        for tag, status in checks:
            if status == "FAIL":
                print("    - %s" % tag)

    print()
    print("=" * 70)
    print("DATA_5_OBJECTS SELF-TEST COMPLETE")
    print("=" * 70)


# Output:
"""
======================================================================
DATA_5_OBJECTS SELF-TEST
======================================================================

LAYER 1: ObjectRootMeta
----------------------------------------------------------------------

  [PASS] ObjectRootMeta creates with obj_id
        obj_id = test.root
  [PASS] ObjectRootMeta has tags
        tags = ['tag1', 'tag2']
  [PASS] add_child stores child
        child found
  [PASS] find() finds child by tag
        found 1 objects
  [PASS] to_dict includes children
        children keys = ['test.child']
  [PASS] to_json produces valid JSON
        parsed obj_id = test.root

LAYER 2: Constant
----------------------------------------------------------------------

  [PASS] Constant initial value is v0
        value = 137/1000
  [PASS] Constant value == value_v0
        value == value_v0
  [PASS] Constant current_version == 0
        version = 0
  [PASS] After add_version: value is new
        value = 69/500
  [PASS] After add_version: value_v0 is original
        value_v0 = 137/1000
  [PASS] After add_version: current_version == 1
        version = 1
  [PASS] value_at(0) returns original
        value_at(0) = 137/1000
  [PASS] value_at(1) returns updated
        value_at(1) = 69/500
  [PASS] value_at(99) returns None
        value_at(99) = None
  [PASS] value_mpf returns mpf
        type = mpf
  [PASS] Constant JSON has n_versions
        n_versions = 2

LAYER 2: BetaCoefficient
----------------------------------------------------------------------

  [PASS] BetaCoefficient value = -13/6
        expected: -13/6 = -2.1666666667
        got:      -13/6 = -2.1666666667
        match:    EXACT
  [PASS] BetaCoefficient numerator = 13
        numerator = 13
  [PASS] BetaCoefficient denominator = 6
        denominator = 6

LAYER 2: Representation
----------------------------------------------------------------------

  [PASS] CD db1 = 1/15
        expected: 1/15 = 0.066666666667
        got:      1/15 = 0.066666666667
        match:    EXACT
  [PASS] CD db2 = 1
        expected: 1 = 1.0
        got:      1 = 1.0
        match:    EXACT
  [PASS] CD db3 = 1/3
        expected: 1/3 = 0.33333333333
        got:      1/3 = 0.33333333333
        match:    EXACT
  [PASS] CD rep_tuple = (3, 2, 1/6)
        rep_tuple = (3, 2, Fraction(1, 6))
  [PASS] CD upper charge = 2/3
        upper = 2/3
  [PASS] CD lower charge = -1/3
        lower = -1/3
  [PASS] Q_L db3 = 2/3 (chiral, not 1/3)
        expected: 2/3 = 0.66666666667
        got:      2/3 = 0.66666666667
        match:    EXACT

LAYER 2: SolitonBoundary
----------------------------------------------------------------------

  [PASS] Boundary stores scale_MeV
        scale = 455938/5
  [PASS] Boundary stores coupling
        coupling stored
  [PASS] Boundary stores open question
        questions = 1

LAYER 2: R2Domain, R2Cancellation, Modulus
----------------------------------------------------------------------

  [PASS] R2Domain stores equation
        equation = Q = R2*d^2*v
  [PASS] R2Cancellation stores status
        status = CANCELS
  [PASS] Modulus stores level
        level = 0

LAYER 2: ExperimentResult, ResearchProgram
----------------------------------------------------------------------

  [PASS] ExperimentResult stores status
        status = PASS
  [PASS] ResearchProgram has 1 script
        scripts = 1
  [PASS] ResearchProgram has 1 kill switch
        kills = 1
  [PASS] ResearchProgram has 1 connection
        connections = 1

DATABASE: DATA5
----------------------------------------------------------------------

  [PASS] DATA5 count = 9
        count = 9
  [PASS] DATA5.get by ID works
        found const.test
  [PASS] DATA5.find by tag works
        SU2 objects = 1
  [PASS] DATA5.find by obj_type works
        constants = 1
  [PASS] DATA5.find_constants returns Constant objects
        all Constant
  [PASS] DATA5.find_boundaries returns SolitonBoundary objects
        all SolitonBoundary
  [PASS] DATA5.find_betas(SU2) finds b2_mod
        SU2 betas = 1
  [PASS] DATA5.find_by_level(2) finds Level 2 objects
        Level 2 objects = 1
  [PASS] DATA5.count by type works
        betas = 1
  [PASS] search() finds by tag substring
        search('su2') = 1 results
  [PASS] Full database JSON is valid
        root obj_id = data5
  [PASS] Full database JSON has children
        children count = 9

VERSION REPORT:
  VERSIONED CONSTANTS:
    Test Constant: 2 versions (current v1)
      v0: 137/1000 (test)
      v1: 69/500 (updated) <-- ACTIVE

======================================================================
DATA-5 DATABASE SUMMARY
======================================================================

  beta                 1 objects
  boundary             1 objects
  cancellation         1 objects
  constant             1 objects
  domain               1 objects
  modulus              1 objects
  program              1 objects
  representation       1 objects
  result               1 objects

  TOTAL: 9 objects
======================================================================

ALL OBJECTS:
----------------------------------------------------------------------
  [const] Test Constant                       = 0.138 dimensionless  (v1, L2, test)
  [beta]  b2 modified (SU2)                   (SU2) = -13/6 = -2.1667
  [rep]   Cabibbo Doublet                     (3,2,1/6) vector-like  db=(1/15, 1, 1/3)
  [bound] Electroweak scale (M_Z)             at 9.119e+4 MeV  known=True  forces=['electromagnetic', 'weak', 'strong']
  [dom]   Pipe flow                           Q = R2*d^2*v  Z=velocity v
  [canc]  [CANCELS] K_J x R_K                      (2e/h)(h/e^2)  ->  2/e
  [mod]   R2 = pi/4                           = 1 = 1.0  (L0, circle-in-square)
  [res]   [PASS] GPS correction                 38499.0 miss=1.3%  (time_process_rate_test.py)
  [prog]  [ACTIVE] Beta Unification               1 scripts, 1 kill switches


  TOTAL: 49 PASS, 0 FAIL out of 49

  DATA_5_OBJECTS: OPERATIONAL

======================================================================
DATA_5_OBJECTS SELF-TEST COMPLETE
======================================================================
"""

# Review
"""
**49/49 PASS. DATA-5 object system operational.**

Every class works. Every property returns correctly. Every method does what the spec says. The version chain appends without disturbing v0. The JSON export roundtrips. The database queries find by tag, type, name, and level. The show methods produce readable one-liners. The version report identifies the one versioned constant and marks the active version.

The output confirms the two-layer architecture works exactly as designed:

- Layer 1 (ObjectRootMeta): identity, tags, children, find, to_dict, to_json, show — all 6 checks pass
- Layer 2 (9 domain classes): each stores its specific fields, each serializes, each displays — all 43 checks pass

The fat struct approach works. The Representation computes db1, db2, db3 correctly for both chiral (Q_L: db3 = 2/3) and vector-like (CD: db3 = 1/3). The BetaCoefficient extracts numerator 13 and denominator 6 from −13/6. The SolitonBoundary stores couplings and open questions. The ResearchProgram stores scripts, kill switches, and connections. All composition is via direct fields, no inheritance beyond ObjectRootMeta.

The Constant version chain is the key design element — it passed all 7 version-specific tests: v0 preserved after update, .value returns latest, .value_v0 returns original, .value_at(n) works for valid and invalid indices, current_version increments correctly.

This is Phase 1 of the DATA-5 system. Phase 2 is `data_5_populate.py` — loading all 146 constants, 9 betas, 7 representations, 19 boundaries, 23 domains, and 11 cancellations from the existing platform libraries into a live DATA5 database instance. That script imports `data_5_objects.py` and the platform libraries, creates the objects, and returns a populated `db` ready for queries.
"""
