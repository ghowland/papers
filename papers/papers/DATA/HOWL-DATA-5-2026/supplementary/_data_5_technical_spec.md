# DATA-5 Library System Technical Specification

**Document:** data_5_system_spec.md

**Version:** 1.0

**Date:** April 3, 2026

**Purpose:** Complete blueprint for building the DATA-5 object-oriented platform library. A new session should be able to implement this system independently from this document alone.

**Supersedes:** The current flat-library approach (phys24_lib.py + 6 extension libraries) for DATA-5 work. The existing HOWL-PLATFORM-v1 libraries remain operational and are not replaced — DATA-5 wraps and extends them.

---

## 1. The Problem

The current platform has 7 libraries with 322/323 checks. They work. But:

- Constants are flat variables (`alpha_inv = Fraction(137035999177, 10**9)`). No metadata. No version history. No searchability.
- Libraries are separate files with no shared structure. You can't ask "show me everything related to SU(2)" across all libraries.
- Cross-references are manual (DATA4_MAP in structure_lib). No unified query system.
- Versioning is by comment convention (`alpha_s_v2 = ...`). No formal version chain.
- No JSON export. No serialization. No external tool integration.

DATA-5 solves this by wrapping every piece of data in a typed object with metadata, version history, and composition. The objects form a queryable database of physics knowledge.

---

## 2. Design Principles

**P1: Fat structs, not clean hierarchies.** Objects map to the physics, not to software architecture patterns. A "coupling constant" object contains whatever a coupling constant needs — name, value, version history, Level tag, uncertainty, source, related objects. If it needs a field that no other object has, add it. No inheritance beyond the root meta layer.

**P2: Two layers only.** Every object inherits from `ObjectRootMeta` (Layer 1: shared metadata for search/sort/export). Everything else is composition (Layer 2: domain-specific content). No deeper inheritance. No abstract base classes. No mixins.

**P3: Version everything.** Every value has a version chain: `value_v0`, `value_v1`, ... The active value is an alias to the current version. Old versions are never deleted. If we update a constant and the update is wrong, the old version is still there, still testable.

**P4: Compose freely.** Objects contain other objects. A "boundary" object contains "coupling" objects. A "representation" object contains "beta shift" objects. The composition follows the physics, not a schema.

**P5: Export to JSON.** Every object can serialize itself and its children recursively. The JSON is the portable format for external tools, future sessions, and documentation.

**P6: Python 3.8, low tech.** No dataclasses (3.7 has them but we want explicit). No typing module requirements. No metaclasses. No decorators beyond `@staticmethod`. Plain classes with `__init__`, plain dicts where convenient, `%` string formatting, `os.path.join()`.

**P7: One-liner helpers.** Common operations (search, filter, sort, display) are one function call. The API surface is small. The implementation is obvious.

---

## 3. Layer 1: ObjectRootMeta

Every object in the system inherits from this and only this.

```python
class ObjectRootMeta:
    """Base metadata layer for all DATA-5 objects.
    
    Every object in the system is a node in a queryable database.
    This layer provides: identity, typing, tagging, search, export.
    """
    
    def __init__(self, obj_id, obj_type, name, tags=None, notes=None):
        # Identity
        self.obj_id = obj_id          # unique string, e.g. "const.alpha_inv"
        self.obj_type = obj_type      # string, e.g. "constant", "boundary", "representation"
        self.name = name              # human-readable name
        
        # Search/filter metadata
        self.tags = tags or []        # list of strings for search, e.g. ["EM", "coupling", "Level2"]
        self.notes = notes or ""      # freeform notes
        
        # Provenance
        self.created_session = None   # int, session number when created
        self.created_date = None      # string, "YYYY-MM-DD"
        self.modified_session = None  # int, last modified
        self.modified_date = None     # string
        
        # Composition
        self.children = {}            # dict of child obj_id -> child object
    
    def add_child(self, child):
        """Add a child object. The child must have obj_id."""
        self.children[child.obj_id] = child
        return child
    
    def get_child(self, child_id):
        """Get a child by obj_id."""
        return self.children.get(child_id, None)
    
    def find(self, tag=None, obj_type=None, name_contains=None):
        """Search this object and all children recursively.
        Returns list of matching objects.
        """
        results = []
        if self._matches(tag, obj_type, name_contains):
            results.append(self)
        for child in self.children.values():
            if hasattr(child, 'find'):
                results.extend(child.find(tag, obj_type, name_contains))
            elif isinstance(child, ObjectRootMeta):
                if child._matches(tag, obj_type, name_contains):
                    results.append(child)
        return results
    
    def _matches(self, tag, obj_type, name_contains):
        if tag and tag not in self.tags:
            return False
        if obj_type and self.obj_type != obj_type:
            return False
        if name_contains and name_contains.lower() not in self.name.lower():
            return False
        return True
    
    def to_dict(self):
        """Serialize to dict (for JSON export). Recurses through children."""
        d = {
            "obj_id": self.obj_id,
            "obj_type": self.obj_type,
            "name": self.name,
            "tags": self.tags,
            "notes": self.notes,
            "created_session": self.created_session,
            "created_date": self.created_date,
        }
        if self.children:
            d["children"] = {k: v.to_dict() if hasattr(v, 'to_dict') else str(v)
                             for k, v in self.children.items()}
        return d
    
    def to_json(self):
        """Export to JSON string."""
        import json
        return json.dumps(self.to_dict(), indent=2, default=str)
    
    def show(self):
        """One-line display."""
        print("  [%s] %s: %s  tags=%s" % (self.obj_type, self.obj_id, self.name, self.tags))
    
    def __repr__(self):
        return "<%s %s '%s'>" % (self.obj_type, self.obj_id, self.name)
```

That's it for Layer 1. Every object gets: identity, type, name, tags, notes, provenance dates, children, search, export, display.

---

## 4. Layer 2: Domain Objects

Each domain object inherits from `ObjectRootMeta` and adds whatever fields the physics requires. No two domain objects need to share any Layer 2 fields. They compose freely.

### 4.1 Versioned Constant

The core data object. Holds a physics value with full version history.

```python
class Constant(ObjectRootMeta):
    """A physics constant with version history.
    
    The value chain:
        value_v0 = original value (never changes)
        value_v1 = first update (if any)
        value = alias to current version (always points to latest)
    
    Usage:
        alpha_inv = Constant("const.alpha_inv", "1/alpha (CODATA 2022)",
                             Fraction(137035999177, 10**9),
                             unit="dimensionless", level=2, digits=12,
                             source="CODATA 2022", data4_id="B1",
                             tags=["EM", "coupling", "Level2", "CODATA"])
    
        # Later, if CODATA 2026 updates:
        alpha_inv.add_version(Fraction(137035999206, 10**9),
                              source="CODATA 2026", session=7)
        # Now alpha_inv.value gives the new value
        # alpha_inv.value_v0 still gives the original
    """
    
    def __init__(self, obj_id, name, value, unit="", level=None,
                 digits=None, source="", data4_id=None, tags=None,
                 uncertainty=None, notes=""):
        super().__init__(obj_id, "constant", name, tags=tags, notes=notes)
        
        # The version chain
        self.versions = [value]       # list of Fraction or mpf values
        self.version_sources = [source]
        self.version_sessions = [None]  # session number when added
        
        # Current value = latest version
        # Access: obj.value, obj.value_v0, obj.value_v1, ...
        
        # Metadata
        self.unit = unit
        self.level = level            # 0 = geometry, 1 = group theory, 2 = measured
        self.digits = digits          # significant digits in source
        self.data4_id = data4_id      # DATA-4 entry ID if applicable
        self.uncertainty = uncertainty # Fraction or None
        self.source = source
    
    @property
    def value(self):
        """Current (latest) value."""
        return self.versions[-1]
    
    @property
    def value_v0(self):
        """Original value (never changes)."""
        return self.versions[0]
    
    def value_at(self, version):
        """Value at a specific version number."""
        if version < len(self.versions):
            return self.versions[version]
        return None
    
    @property
    def current_version(self):
        """Current version number (0-based)."""
        return len(self.versions) - 1
    
    def add_version(self, new_value, source="", session=None):
        """Add a new version. The old value is preserved.
        The .value property now returns the new value.
        """
        self.versions.append(new_value)
        self.version_sources.append(source)
        self.version_sessions.append(session)
        self.modified_session = session
    
    def value_mpf(self):
        """Current value as mpf (for display)."""
        v = self.value
        if isinstance(v, Fraction):
            return f2m(v)
        return v
    
    def show(self):
        """One-line display with value."""
        v = self.value_mpf()
        print("  [const] %s = %s %s (v%d, L%s, %s)" % (
            self.name, mp.nstr(v, 11) if hasattr(v, '__mpz_manager') or isinstance(v, mpf) else str(v),
            self.unit, self.current_version,
            self.level if self.level is not None else "?",
            self.source))
    
    def to_dict(self):
        d = super().to_dict()
        d.update({
            "value": str(self.value),
            "unit": self.unit,
            "level": self.level,
            "digits": self.digits,
            "source": self.source,
            "data4_id": self.data4_id,
            "n_versions": len(self.versions),
            "versions": [str(v) for v in self.versions],
            "version_sources": self.version_sources,
        })
        return d
```

### 4.2 Beta Coefficient

```python
class BetaCoefficient(ObjectRootMeta):
    """A gauge coupling beta coefficient with decomposition.
    
    Stores the total value and its constituent parts
    (gauge, fermion, Higgs, BSM) as children.
    """
    
    def __init__(self, obj_id, name, gauge_group, value,
                 gauge_part=None, fermion_part=None,
                 higgs_part=None, bsm_part=None,
                 tags=None, notes=""):
        super().__init__(obj_id, "beta", name, tags=tags, notes=notes)
        
        self.gauge_group = gauge_group  # "U1", "SU2", "SU3"
        self.value = value              # Fraction, the total
        self.gauge_part = gauge_part    # Fraction or None
        self.fermion_part = fermion_part
        self.higgs_part = higgs_part
        self.bsm_part = bsm_part
    
    @property
    def numerator(self):
        """Absolute value of numerator × denominator product.
        For b2_mod = -13/6: returns 13.
        """
        return abs(self.value.numerator)
    
    @property
    def denominator(self):
        return self.value.denominator
    
    def show(self):
        print("  [beta] %s (%s) = %s = %.4f" % (
            self.name, self.gauge_group, self.value, float(f2m(self.value))))
```

### 4.3 Representation

```python
class Representation(ObjectRootMeta):
    """A gauge group representation with all derived properties.
    
    Wraps the make_rep() function from phys24_structure_lib.py
    but stores the result as a structured object.
    """
    
    def __init__(self, obj_id, name, su3_dim, su2_dim, Y,
                 rep_type="chiral", tags=None, notes=""):
        super().__init__(obj_id, "representation", name, tags=tags, notes=notes)
        
        self.su3_dim = su3_dim
        self.su2_dim = su2_dim
        self.Y = Fraction(Y) if not isinstance(Y, Fraction) else Y
        self.rep_type = rep_type
        
        # Compute all derived properties using existing library
        from phys24_structure_lib import make_rep
        self._rep = make_rep(name, su3_dim, su2_dim, self.Y, rep_type)
        
        # Expose key properties
        self.db1 = self._rep["db1"]
        self.db2 = self._rep["db2"]
        self.db3 = self._rep["db3"]
        self.charges = self._rep["charges"]
        self.S2_R3 = self._rep["S2_R3"]
        self.S2_R2 = self._rep["S2_R2"]
        self.C2_R3 = self._rep["C2_R3"]
        self.C2_R2 = self._rep["C2_R2"]
    
    @property
    def rep_tuple(self):
        return (self.su3_dim, self.su2_dim, self.Y)
    
    @property
    def db(self):
        return (self.db1, self.db2, self.db3)
    
    def show(self):
        print("  [rep] %s (%d,%d,%s) %s  db=(%s,%s,%s)" % (
            self.name, self.su3_dim, self.su2_dim, self.Y,
            self.rep_type, self.db1, self.db2, self.db3))
```

### 4.4 Soliton Boundary

```python
class SolitonBoundary(ObjectRootMeta):
    """A boundary where the physics rules change.
    
    Can hold: energy scale, distance scale, what changes,
    coupling values, forces affected, open questions.
    """
    
    def __init__(self, obj_id, name, scale_MeV=None, scale_fm=None,
                 what_changes="", forces_affected=None,
                 known=False, tags=None, notes=""):
        super().__init__(obj_id, "boundary", name, tags=tags, notes=notes)
        
        self.scale_MeV = scale_MeV        # Fraction or None
        self.scale_fm = scale_fm           # mpf or None
        self.what_changes = what_changes
        self.forces_affected = forces_affected or []
        self.known = known
        
        # Coupling values at this boundary (dict of name -> Constant or None)
        self.couplings = {}
        
        # Properties above and below
        self.above = {}
        self.below = {}
        
        # Open questions
        self.open_questions = []
    
    def add_coupling(self, name, value):
        """Add a coupling value at this boundary."""
        self.couplings[name] = value
    
    def show(self):
        scale_str = "?"
        if self.scale_MeV is not None:
            scale_str = "%s MeV" % mp.nstr(f2m(self.scale_MeV) if isinstance(self.scale_MeV, Fraction) else self.scale_MeV, 4)
        print("  [boundary] %s at %s  known=%s  forces=%s" % (
            self.name, scale_str, self.known, self.forces_affected))
```

### 4.5 R2 Domain

```python
class R2Domain(ObjectRootMeta):
    """A domain where R2 = pi/4 appears.
    
    Stores the equation, the coordinator Z, precision,
    and a callable function that computes the domain's
    characteristic quantity.
    """
    
    def __init__(self, obj_id, name, equation, coordinator_Z,
                 precision="", compute_fn=None, tags=None, notes=""):
        super().__init__(obj_id, "domain", name, tags=tags, notes=notes)
        
        self.equation = equation          # string, e.g. "Q = R2*d^2*v"
        self.coordinator_Z = coordinator_Z  # string, what makes this domain unique
        self.precision = precision
        self.compute_fn = compute_fn      # callable or None
    
    def compute(self, *args, **kwargs):
        """Run the domain's computation if a function is attached."""
        if self.compute_fn:
            return self.compute_fn(*args, **kwargs)
        return None
    
    def show(self):
        print("  [domain] %s: %s  Z=%s" % (self.name, self.equation, self.coordinator_Z))
```

### 4.6 R2 Cancellation

```python
class R2Cancellation(ObjectRootMeta):
    """An R2 cancellation identity.
    
    Records: what product cancels R2, the formula,
    what remains after cancellation, and precision.
    """
    
    def __init__(self, obj_id, name, formula, status, remains,
                 precision="", tags=None, notes=""):
        super().__init__(obj_id, "cancellation", name, tags=tags, notes=notes)
        
        self.formula = formula
        self.status = status          # "CANCELS", "R2-FREE", "REAPPEARS"
        self.remains = remains        # what's left after R2 drops out
        self.precision = precision
```

### 4.7 Modulus Entry

```python
class Modulus(ObjectRootMeta):
    """A filling fraction / modulus tracked by the series.
    
    Level 0: pure geometry (R2, R4)
    Level 1: group theory (beta coefficients, Casimirs)
    Level 2: measured (alpha, sin2_tW)
    Level 3: predictions (alpha_s from unification)
    """
    
    def __init__(self, obj_id, name, value, level, origin,
                 cancels_in=None, tags=None, notes=""):
        super().__init__(obj_id, "modulus", name, tags=tags, notes=notes)
        
        self.value = value            # Fraction or mpf
        self.level = level            # 0, 1, 2, or 3
        self.origin = origin          # string describing where it comes from
        self.cancels_in = cancels_in or []  # list of cancellation obj_ids
```

### 4.8 Experiment Result

```python
class ExperimentResult(ObjectRootMeta):
    """A result from an experiment script.
    
    Links: the script that produced it, the checks that verified it,
    the constants it used, and the finding.
    """
    
    def __init__(self, obj_id, name, script, value, measured=None,
                 miss_pct=None, status="PASS", tags=None, notes=""):
        super().__init__(obj_id, "result", name, tags=tags, notes=notes)
        
        self.script = script          # filename
        self.value = value            # computed value
        self.measured = measured       # measured comparison value
        self.miss_pct = miss_pct      # percentage miss
        self.status = status          # "PASS" or "FAIL"
```

### 4.9 Research Program

```python
class ResearchProgram(ObjectRootMeta):
    """A research program with scripts, kill switches, and timeline."""
    
    def __init__(self, obj_id, name, thesis, status="ACTIVE",
                 tags=None, notes=""):
        super().__init__(obj_id, "program", name, tags=tags, notes=notes)
        
        self.thesis = thesis
        self.status = status          # "ACTIVE", "PARKED", "KILLED", "CONFIRMED"
        self.scripts = []             # list of script dicts
        self.kill_switches = []       # list of kill switch dicts
        self.connections = {}         # connections to other programs
```

---

## 5. The Database: DATA5

The top-level container. Holds all objects. Provides global search and export.

```python
class DATA5(ObjectRootMeta):
    """The DATA-5 database. Contains all objects.
    
    Usage:
        db = DATA5()
        
        # Add constants
        db.add(Constant("const.alpha_inv", "1/alpha (CODATA 2022)",
                         Fraction(137035999177, 10**9),
                         unit="dimensionless", level=2, digits=12,
                         source="CODATA 2022", data4_id="B1",
                         tags=["EM", "coupling", "Level2"]))
        
        # Search
        em_stuff = db.find(tag="EM")
        constants = db.find(obj_type="constant")
        alpha = db.get("const.alpha_inv")
        
        # Export
        db.to_json()  # entire database as JSON
    """
    
    def __init__(self):
        super().__init__("data5", "database", "DATA-5 Platform Database",
                         tags=["root", "database"])
        self._index = {}  # flat index: obj_id -> object, for O(1) lookup
    
    def add(self, obj):
        """Add an object to the database."""
        self.children[obj.obj_id] = obj
        self._index[obj.obj_id] = obj
        # Also index all children recursively
        if hasattr(obj, 'children'):
            for child_id, child in obj.children.items():
                self._index[child_id] = child
        return obj
    
    def get(self, obj_id):
        """Get an object by ID. O(1) lookup."""
        return self._index.get(obj_id, None)
    
    def find(self, tag=None, obj_type=None, name_contains=None):
        """Search all objects."""
        results = []
        for obj in self._index.values():
            if obj._matches(tag, obj_type, name_contains):
                results.append(obj)
        return results
    
    def find_constants(self, tag=None):
        """Shortcut: find all constants, optionally filtered by tag."""
        return self.find(tag=tag, obj_type="constant")
    
    def find_boundaries(self):
        """Shortcut: find all soliton boundaries."""
        return self.find(obj_type="boundary")
    
    def find_by_level(self, level):
        """Find all constants at a specific modulus level (0,1,2,3)."""
        return [obj for obj in self._index.values()
                if hasattr(obj, 'level') and obj.level == level]
    
    def count(self, obj_type=None):
        """Count objects, optionally by type."""
        if obj_type:
            return len([o for o in self._index.values() if o.obj_type == obj_type])
        return len(self._index)
    
    def show_all(self, obj_type=None, tag=None):
        """Display all objects matching filters."""
        for obj in self.find(tag=tag, obj_type=obj_type):
            obj.show()
    
    def show_summary(self):
        """Print a summary of the database contents."""
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
        """Show all constants that have been versioned."""
        versioned = [obj for obj in self._index.values()
                     if hasattr(obj, 'versions') and len(obj.versions) > 1]
        if not versioned:
            print("  No versioned constants. All at v0.")
            return
        for obj in versioned:
            print("  %s: %d versions (current v%d)" % (
                obj.name, len(obj.versions), obj.current_version))
            for i, (v, s) in enumerate(zip(obj.versions, obj.version_sources)):
                marker = " <-- ACTIVE" if i == len(obj.versions) - 1 else ""
                print("    v%d: %s (%s)%s" % (i, v, s, marker))
```

---

## 6. The Versioning System

### 6.1 How It Works

Every `Constant` object stores a list of values:

```python
alpha_EM = Constant("const.alpha_inv", "1/alpha",
                     Fraction(137035999177, 10**9),  # v0
                     source="CODATA 2022")

# v0 is set at creation. It never changes.
# alpha_EM.value returns v0.
# alpha_EM.value_v0 returns v0.

# Later, CODATA 2026 publishes a new value:
alpha_EM.add_version(Fraction(137035999206, 10**9),
                      source="CODATA 2026", session=7)

# Now:
# alpha_EM.value returns v1 (the new value)
# alpha_EM.value_v0 still returns v0 (the original)
# alpha_EM.value_at(0) returns v0
# alpha_EM.value_at(1) returns v1
```

### 6.2 Why This Works

- Old scripts that used `alpha_EM.value_v0` still get the original value.
- New scripts use `alpha_EM.value` and get the latest.
- If v1 turns out to be wrong, we add v2 with the corrected value. v0 and v1 are still there for historical testing.
- The `version_report()` method shows all versioned constants and their history.

### 6.3 Flat Alias Pattern

For backward compatibility with the current flat-variable approach:

```python
# In the library initialization:
alpha_inv_value = db.get("const.alpha_inv").value
# Scripts can still do: show("alpha_inv", alpha_inv_value)
```

---

## 7. The Population Script

How the database gets populated from existing libraries:

```python
def populate_from_phys24_lib(db):
    """Load all constants from phys24_lib.py into the database."""
    from phys24_lib import *
    
    # SI constants (Level E = exact)
    db.add(Constant("const.c", "Speed of light", c,
                     unit="m/s", level=0, digits=9,
                     source="SI 2019 (exact)", data4_id="A1",
                     tags=["SI", "exact", "Level0"]))
    
    db.add(Constant("const.h", "Planck constant", h_planck,
                     unit="J*s", level=0, digits=9,
                     source="SI 2019 (exact)", data4_id="A2",
                     tags=["SI", "exact", "Level0"]))
    
    db.add(Constant("const.dv_Cs", "Cesium hyperfine", dv_Cs,
                     unit="Hz", level=0, digits=10,
                     source="SI 2019 (exact)", data4_id="A6",
                     tags=["SI", "exact", "Level0", "clock"]))
    
    # Measured constants (Level 2)
    db.add(Constant("const.alpha_inv", "1/alpha (CODATA 2022)",
                     alpha_inv, unit="dimensionless", level=2, digits=12,
                     source="CODATA 2022", data4_id="B1",
                     tags=["EM", "coupling", "Level2", "CODATA"]))
    
    db.add(Constant("const.sin2_tW", "Weak mixing angle",
                     sin2_tW, unit="dimensionless", level=2, digits=5,
                     source="PDG 2024", data4_id="B11",
                     tags=["weak", "coupling", "Level2", "EW"]))
    
    db.add(Constant("const.alpha_s", "Strong coupling",
                     alpha_s, unit="dimensionless", level=2, digits=4,
                     source="PDG 2024", data4_id="B12",
                     tags=["strong", "coupling", "Level2", "QCD"]))
    
    # ... continue for all ~146 DATA-4 entries ...


def populate_beta_coefficients(db):
    """Load all beta coefficients as structured objects."""
    from phys24_lib import *
    
    db.add(BetaCoefficient("beta.b1_SM", "b1 SM (U1)",
                            "U1", b1_SM,
                            gauge_part=Fraction(0),
                            fermion_part=Fraction(4, 1),  # 3 × 4/3
                            higgs_part=Fraction(1, 10),
                            tags=["Level1", "U1", "SM"]))
    
    db.add(BetaCoefficient("beta.b2_SM", "b2 SM (SU2)",
                            "SU2", b2_SM,
                            gauge_part=Fraction(-22, 3),
                            fermion_part=Fraction(4, 1),
                            higgs_part=Fraction(1, 6),
                            tags=["Level1", "SU2", "SM"]))
    
    db.add(BetaCoefficient("beta.b3_SM", "b3 SM (SU3)",
                            "SU3", b3_SM,
                            gauge_part=Fraction(-11, 1),
                            fermion_part=Fraction(4, 1),
                            higgs_part=Fraction(0),
                            tags=["Level1", "SU3", "SM"]))
    
    # Modified betas
    db.add(BetaCoefficient("beta.b2_mod", "b2 modified (SU2 + CD)",
                            "SU2", b2_mod,
                            gauge_part=Fraction(-22, 3),
                            fermion_part=Fraction(4, 1),
                            higgs_part=Fraction(1, 6),
                            bsm_part=Fraction(1, 1),  # CD contribution
                            tags=["Level1", "SU2", "modified", "CD"]))
    
    # ... b1_mod, b3_mod similarly ...


def populate_boundaries(db):
    """Load the boundary stack as structured objects."""
    from phys24_boundary_map_lib import BOUNDARY_STACK
    
    for b in BOUNDARY_STACK:
        boundary = SolitonBoundary(
            "boundary.%s" % b["name"].lower().replace(" ", "_").replace("(", "").replace(")", ""),
            b["name"],
            scale_MeV=b.get("scale_MeV"),
            scale_fm=b.get("scale_fm"),
            what_changes=b.get("what_changes", ""),
            forces_affected=b.get("forces_affected", []),
            known=b.get("known", False),
            tags=["boundary"] + b.get("forces_affected", []))
        
        for q in b.get("open_questions", []):
            boundary.open_questions.append(q)
        
        db.add(boundary)


def populate_R2_domains(db):
    """Load R2 domains from the domain library."""
    from phys24_domain_lib import R2_EQUATIONS, R2_CANCELLATIONS
    from phys24_domain_lib import pipe_flow, wire_resistance, domain_area
    
    for i, eq in enumerate(R2_EQUATIONS):
        domain = R2Domain(
            "domain.%02d_%s" % (i + 1, eq["domain"].lower().replace(" ", "_")),
            eq["domain"],
            equation=eq["equation"],
            coordinator_Z=eq["Z"],
            precision=eq.get("precision", ""),
            tags=["R2", "domain", eq["domain"].split()[0].lower()])
        db.add(domain)
    
    for i, c in enumerate(R2_CANCELLATIONS):
        cancel = R2Cancellation(
            "cancel.%02d_%s" % (i + 1, c["name"].lower().replace(" ", "_").replace("*", "x")),
            c["name"],
            formula=c["formula"],
            status=c["status"],
            remains=c.get("formula", "").split("=")[-1].strip() if "=" in c.get("formula", "") else "",
            precision=c.get("precision", ""),
            tags=["R2", "cancellation", c["status"].lower()])
        db.add(cancel)
```

---

## 8. The Query API

One-liner helpers for common operations:

```python
# === Search helpers (standalone functions) ===

def search(db, query):
    """Search by any substring in name, tags, or notes."""
    results = []
    q = query.lower()
    for obj in db._index.values():
        if (q in obj.name.lower() or
            q in " ".join(obj.tags).lower() or
            q in obj.notes.lower()):
            results.append(obj)
    return results


def constants_at_level(db, level):
    """All constants at a specific modulus level."""
    return [o for o in db.find(obj_type="constant") if hasattr(o, 'level') and o.level == level]


def show_constants(db, tag=None):
    """Display all constants, optionally filtered."""
    for c in db.find_constants(tag=tag):
        c.show()


def show_boundaries(db, known_only=False):
    """Display boundary stack."""
    for b in db.find_boundaries():
        if known_only and not b.known:
            continue
        b.show()


def show_R2(db):
    """Display all R2 domains."""
    for d in db.find(obj_type="domain"):
        d.show()


def show_cancellations(db, status=None):
    """Display R2 cancellation registry."""
    for c in db.find(obj_type="cancellation"):
        if status and c.status != status:
            continue
        print("  [%s] %s: %s" % (c.status, c.name, c.formula))


def export_json(db, filename):
    """Export entire database to JSON file."""
    with open(filename, 'w') as f:
        f.write(db.to_json())
    print("  Exported %d objects to %s" % (db.count(), filename))
```

---

## 9. The Initialization

How a session boots the DATA-5 system:

```python
def init_data5():
    """Initialize the DATA-5 database with all platform data.
    
    Call once at session start:
        db = init_data5()
    
    Then use:
        db.get("const.alpha_inv").value     # get a constant
        db.find(tag="SU2")                  # search by tag
        db.show_summary()                   # database overview
    """
    db = DATA5()
    
    populate_from_phys24_lib(db)
    populate_beta_coefficients(db)
    populate_boundaries(db)
    populate_R2_domains(db)
    # populate_representations(db)      # from structure_lib
    # populate_experiments(db)           # from experiment results
    # populate_research_programs(db)     # from research program docs
    
    return db
```

---

## 10. File Organization

```
DATA/HOWL-DATA-5-2026/
  code/
    # Existing libraries (unchanged, still operational)
    phys24_lib.py
    data_4_derivation_lib.py
    phys24_structure_lib.py
    phys24_boundary_map_lib.py
    phys24_domain_lib.py
    phys24_hubble_lib.py
    data_5_diagram_lib.py
    
    # New DATA-5 system
    data_5_objects.py           # ObjectRootMeta + all Layer 2 classes
    data_5_populate.py          # All populate_* functions
    data_5_helpers.py           # search, show, export helpers
    data_5_init.py              # init_data5() entry point
    
    # Experiment scripts (unchanged)
    beta_unification_test.py
    toroidal_dm_test.py
    dwarf_soliton_ground_state.py
    nested_soliton_gravity.py
    time_process_rate_test.py
    
    # Diagram scripts (unchanged)
    toroidal_dm_diagrams.py
    dwarf_soliton_diagrams.py
    nested_soliton_gravity_diagrams.py
    time_process_rate_diagrams.py
```

---

## 11. Compatibility

### 11.1 With Existing Libraries

DATA-5 imports FROM the existing libraries. It does not replace them. Every `populate_*` function calls `from phys24_lib import *` and reads the existing Fraction constants. The existing libraries continue to work unchanged. Scripts that use `from phys24_lib import *` still work.

### 11.2 With Existing Scripts

All experiment and diagram scripts continue to use the flat import pattern. DATA-5 is an ADDITIONAL layer on top, not a replacement. A script can use both:

```python
from phys24_lib import *             # flat access (existing)
from data_5_init import init_data5   # object access (new)

db = init_data5()

# Both work:
show("alpha_inv", f2m(alpha_inv))                    # flat
show("alpha_inv", db.get("const.alpha_inv").value_mpf())  # object
```

### 11.3 Python 3.8

All classes use plain `__init__`, no dataclasses, no type hints required, no walrus operators, no f-strings with `=`. `%` formatting throughout. `os.path.join()` for paths.

---

## 12. The Structural Upgrade Protocol (inherited)

DATA-5 inherits the five rules from api_demo_script_rules.md:

1. **Classes are never removed.** Deprecated classes stay with a note.
2. **Methods are never renamed.** New names get aliases.
3. **Constructor parameters are never removed.** New params get defaults.
4. **Dict keys in to_dict() are never removed.** New keys added.
5. **Object IDs are never changed.** New objects get new IDs.

Plus one new rule:

6. **Version chains are append-only.** Once a version is added, it is never removed or modified. The chain only grows.

---

## 13. Example Session

What using DATA-5 looks like in practice:

```python
from data_5_init import init_data5

db = init_data5()

# What's in the database?
db.show_summary()
# Output:
#   constant             146 objects
#   beta                   9 objects
#   boundary              19 objects
#   domain                22 objects
#   cancellation           7 objects
#   TOTAL: 203 objects

# Find everything related to SU(2)
su2_stuff = db.find(tag="SU2")
for obj in su2_stuff:
    obj.show()
# Output:
#   [beta] b2 SM (SU2) = -19/6 = -3.1667
#   [beta] b2 modified (SU2 + CD) = -13/6 = -2.1667
#   [boundary] Electroweak scale (M_Z) at 9.119e+4 MeV ...

# Get a specific constant
alpha = db.get("const.alpha_inv")
print(alpha.value)       # Fraction(137035999177, 10**9)
print(alpha.source)      # "CODATA 2022"
print(alpha.level)       # 2
print(alpha.digits)      # 12

# Version it
alpha.add_version(Fraction(137035999206, 10**9),
                   source="CODATA 2026", session=7)
print(alpha.value)       # new value
print(alpha.value_v0)    # original value

# Show all Level 1 moduli
for obj in db.find_by_level(1):
    obj.show()

# Export
db.to_json()  # full database as JSON string
```

---

## 14. What DATA-5 Adds Over Current System

| Feature | Current (flat libs) | DATA-5 (object DB) |
|---|---|---|
| Search by tag | Manual grep | `db.find(tag="SU2")` |
| Search by type | Manual import | `db.find(obj_type="boundary")` |
| Version history | Comment convention | Formal version chain |
| Cross-reference | Manual DATA4_MAP | Automatic via children/tags |
| JSON export | None | `db.to_json()` |
| Level tagging | Implicit | Explicit `level=0,1,2,3` |
| Provenance | `prov()` in diagrams | Built into every object |
| Composition | Separate files | Objects contain objects |
| Global query | Import each lib separately | One `db.find()` searches everything |

---

## 15. Implementation Priority

**Phase 1 (one session):**
- `data_5_objects.py`: ObjectRootMeta + Constant + BetaCoefficient
- `data_5_populate.py`: populate_from_phys24_lib (all 146 constants)
- `data_5_init.py`: init_data5() with constants only
- Self-test: count check, version test, search test, JSON export test

**Phase 2 (one session):**
- Add Representation, SolitonBoundary, R2Domain, R2Cancellation
- populate_boundaries, populate_R2_domains, populate_representations
- Self-test: full count, boundary traversal, domain search

**Phase 3 (one session):**
- Add Modulus, ExperimentResult, ResearchProgram
- populate_experiments (from today's 5 experiment scripts)
- populate_research_programs (from today's 3 research programs)
- Self-test: full database, cross-reference verification

**Phase 4 (one session):**
- Integration with diagram scripts (db objects as provenance sources)
- Integration with experiment scripts (results auto-populate)
- Export to JSON, HTML summary, and markdown catalog

---

## 16. The Goal

When DATA-5 is complete, a new session can:

```python
db = init_data5()
db.show_summary()

# "What do we know about dark matter?"
dm = db.find(tag="DM")

# "What are the open questions at the GUT boundary?"
gut = db.get("boundary.gut_unification_scale")
print(gut.open_questions)

# "Show me all Level 1 integers"
for obj in db.find_by_level(1):
    obj.show()

# "What changed between sessions?"
db.version_report()

# "Export everything for documentation"
export_json(db, "data5_snapshot.json")
```

The database IS the knowledge. The objects ARE the physics. The version chains ARE the history. The search IS the cross-reference. Everything in one place, queryable, exportable, versionable, composable.

---

*DATA-5 Library System Technical Specification v1.0. Two-layer object architecture (ObjectRootMeta + domain classes). Versioned constants with append-only chains. Composable objects with recursive search and JSON export. Python 3.8, low tech, mechanically simple. Wraps existing HOWL-PLATFORM-v1 libraries without replacing them. April 3, 2026.*

---

## Supporting Appendix Tables for: DATA-5 Library System Technical Specification

---

### TABLE D5.1: OBJECT TYPE REGISTRY

| obj_type | Class | Layer 2 Fields | Population Source | Phase |
|---|---|---|---|---|
| constant | Constant | value, versions, unit, level, digits, source, data4_id, uncertainty | phys24_lib.py (146 entries) | 1 |
| beta | BetaCoefficient | gauge_group, value, gauge_part, fermion_part, higgs_part, bsm_part | phys24_lib.py (N1-N9) + structure_lib | 1 |
| representation | Representation | su3_dim, su2_dim, Y, rep_type, db1, db2, db3, charges, S2, C2 | phys24_structure_lib.py | 2 |
| boundary | SolitonBoundary | scale_MeV, scale_fm, what_changes, forces_affected, known, couplings, above, below, open_questions | phys24_boundary_map_lib.py (19 entries) | 2 |
| domain | R2Domain | equation, coordinator_Z, precision, compute_fn | phys24_domain_lib.py (22 entries) | 2 |
| cancellation | R2Cancellation | formula, status, remains, precision | phys24_domain_lib.py (7+4 entries) | 2 |
| modulus | Modulus | value, level, origin, cancels_in | Modulus notebook (Tables MR.4-MR.7) | 3 |
| result | ExperimentResult | script, value, measured, miss_pct, status | 5 experiment scripts | 3 |
| program | ResearchProgram | thesis, status, scripts, kill_switches, connections | 3 research program docs | 3 |

9 object types. Each inherits only from ObjectRootMeta. No deeper hierarchy.

---

### TABLE D5.2: ObjectRootMeta FIELD REGISTRY (Layer 1 — All Objects)

| Field | Type | Required | Default | Purpose |
|---|---|---|---|---|
| obj_id | str | YES | — | Unique identifier, dot-separated namespace |
| obj_type | str | YES | — | One of the 9 types in Table D5.1 |
| name | str | YES | — | Human-readable label |
| tags | list[str] | no | [] | Search/filter terms |
| notes | str | no | "" | Freeform annotation |
| created_session | int or None | no | None | Session number when created |
| created_date | str or None | no | None | ISO date string |
| modified_session | int or None | no | None | Last modification session |
| modified_date | str or None | no | None | Last modification date |
| children | dict[str, obj] | no | {} | Composed child objects |

10 fields. Every object carries all 10. Layer 1 is identical across all types.

---

### TABLE D5.3: Constant FIELD REGISTRY (Layer 2)

| Field | Type | Required | Default | Purpose | Example |
|---|---|---|---|---|---|
| versions | list[Fraction] | YES (auto) | [initial_value] | Append-only value chain | [Fraction(137035999177, 10**9)] |
| version_sources | list[str] | YES (auto) | [source] | Source per version | ["CODATA 2022"] |
| version_sessions | list[int] | YES (auto) | [None] | Session per version | [4] |
| unit | str | no | "" | Physical unit | "dimensionless", "MeV", "m/s" |
| level | int or None | no | None | Modulus level (0,1,2,3) | 2 |
| digits | int or None | no | None | Source significant digits | 12 |
| source | str | no | "" | Publication source | "CODATA 2022" |
| data4_id | str or None | no | None | DATA-4 entry ID | "B1" |
| uncertainty | Fraction or None | no | None | Published uncertainty | Fraction(11, 10**9) |

9 Layer 2 fields. Properties: `.value` (latest), `.value_v0` (original), `.value_at(n)` (any version), `.current_version` (int), `.value_mpf()` (display).

---

### TABLE D5.4: BetaCoefficient FIELD REGISTRY (Layer 2)

| Field | Type | Required | Default | Purpose | Example |
|---|---|---|---|---|---|
| gauge_group | str | YES | — | "U1", "SU2", or "SU3" | "SU2" |
| value | Fraction | YES | — | Total beta coefficient | Fraction(-13, 6) |
| gauge_part | Fraction or None | no | None | Gauge boson contribution | Fraction(-22, 3) |
| fermion_part | Fraction or None | no | None | Fermion contribution (all gens) | Fraction(4, 1) |
| higgs_part | Fraction or None | no | None | Higgs contribution | Fraction(1, 6) |
| bsm_part | Fraction or None | no | None | BSM contribution (CD, etc.) | Fraction(1, 1) |

6 Layer 2 fields. Properties: `.numerator` (abs value of numerator), `.denominator`.

---

### TABLE D5.5: Representation FIELD REGISTRY (Layer 2)

| Field | Type | Required | Default | Purpose | Example |
|---|---|---|---|---|---|
| su3_dim | int | YES | — | SU(3) dimension | 3 |
| su2_dim | int | YES | — | SU(2) dimension | 2 |
| Y | Fraction | YES | — | Hypercharge | Fraction(1, 6) |
| rep_type | str | no | "chiral" | "chiral" or "vector-like" | "vector-like" |
| db1 | Fraction | auto | — | U(1) beta shift | Fraction(1, 15) |
| db2 | Fraction | auto | — | SU(2) beta shift | Fraction(1, 1) |
| db3 | Fraction | auto | — | SU(3) beta shift | Fraction(1, 3) |
| charges | tuple | auto | — | Electric charges of components | (Fraction(2,3), Fraction(-1,3)) |
| S2_R3 | Fraction | auto | — | SU(3) Dynkin index | Fraction(1, 2) |
| S2_R2 | Fraction | auto | — | SU(2) Dynkin index | Fraction(1, 2) |
| C2_R3 | Fraction | auto | — | SU(3) Casimir | Fraction(4, 3) |
| C2_R2 | Fraction | auto | — | SU(2) Casimir | Fraction(3, 4) |

12 Layer 2 fields. 4 required, 8 auto-computed by `make_rep()` from structure_lib. Property: `.rep_tuple` → (3, 2, 1/6), `.db` → (1/15, 1, 1/3).

---

### TABLE D5.6: SolitonBoundary FIELD REGISTRY (Layer 2)

| Field | Type | Required | Default | Purpose | Example |
|---|---|---|---|---|---|
| scale_MeV | Fraction or None | no | None | Energy scale | Fraction(911876, 10) |
| scale_fm | mpf or None | no | None | Distance scale | mpf("0.00216") |
| what_changes | str | no | "" | Description of rule change | "Three gauge couplings merge" |
| forces_affected | list[str] | no | [] | Force keys from FORCES dict | ["electromagnetic", "weak"] |
| known | bool | no | False | Measured (True) or theoretical | True |
| couplings | dict | no | {} | Coupling values at boundary | {"alpha_s": Fraction(1180, 10000)} |
| above | dict | no | {} | Properties above boundary | {"n_f": 6} |
| below | dict | no | {} | Properties below boundary | {"n_f": 5} |
| open_questions | list[str] | no | [] | Unresolved issues | ["What is M_VL exactly?"] |

9 Layer 2 fields. Boundaries are the most heterogeneous objects — some have scale_MeV, some have scale_fm, some have both, some have neither. The fat struct accommodates all variants.

---

### TABLE D5.7: OBJ_ID NAMESPACE CONVENTION

| Prefix | Object type | Pattern | Examples |
|---|---|---|---|
| const. | Constant | const.{short_name} | const.alpha_inv, const.m_e, const.c, const.R2 |
| beta. | BetaCoefficient | beta.{name} | beta.b1_SM, beta.b2_mod, beta.db3_VL |
| rep. | Representation | rep.{name} | rep.Q_L, rep.CD, rep.u_R |
| boundary. | SolitonBoundary | boundary.{scale_name} | boundary.planck, boundary.mz, boundary.confinement_upper |
| domain. | R2Domain | domain.{nn}_{name} | domain.01_pipe_flow, domain.10_wire_resistance |
| cancel. | R2Cancellation | cancel.{nn}_{name} | cancel.01_kj_x_rk, cancel.08_gap_ratio |
| modulus. | Modulus | modulus.{name} | modulus.R2, modulus.4_3_democracy, modulus.K_koide |
| result. | ExperimentResult | result.{script}.{finding} | result.beta_test.omega_dm, result.time.gps |
| program. | ResearchProgram | program.{name} | program.beta_unification, program.hubble_running |

All obj_ids are lowercase with dots and underscores only. No spaces, no special characters, no uppercase. This ensures reliable string matching in search.

---

### TABLE D5.8: TAG VOCABULARY

| Tag | Meaning | Used on |
|---|---|---|
| Level0 | Pure geometry constant | R2, R4, pi, e, sqrt2, Bessel zeros |
| Level1 | Group theory integer | Beta coefficients, Casimirs, Dynkin indices, gap ratios |
| Level2 | Measured parameter | alpha_inv, sin2_tW, alpha_s, masses |
| Level3 | Prediction / derived | alpha_s prediction, sin2_tW prediction, Koide m_tau |
| EM | Electromagnetic | alpha_inv, m_e, m_mu, e_charge, VP running |
| weak | Weak force | sin2_tW, M_W, M_Z, Gamma_Z |
| strong | Strong / QCD | alpha_s, m_c, m_b, m_t, confinement |
| gravity | Gravitational | Planck boundary, G_N references |
| SM | Standard Model | SM beta coefficients, SM particles |
| CD | Cabibbo Doublet | Modified betas, VL shifts, CD representation |
| SU2 | SU(2) related | b2_SM, b2_mod, SU(2) Casimirs |
| SU3 | SU(3) related | b3_SM, b3_mod, SU(3) Casimirs |
| U1 | U(1) related | b1_SM, b1_mod, hypercharges |
| R2 | R2 = pi/4 domain | All 22+ R2 equations, cancellations |
| SI | SI exact constant | c, h, e, k_B, N_A, dv_Cs, K_cd |
| exact | Exact by definition | SI constants, group theory Fractions |
| CODATA | CODATA source | alpha_inv, m_e, m_p, a_0, R_inf, ... |
| PDG | PDG source | alpha_s, sin2_tW, M_Z, quark masses |
| FLAG | FLAG lattice source | mc_ms, mb_mc, mu_md |
| coupling | Gauge coupling | alpha_inv, sin2_tW, alpha_s, G_F |
| mass | Particle mass | m_e, m_mu, m_tau, m_u, ..., m_t |
| ratio | Dimensionless ratio | mp_me, mmu_me, K_koide, gap ratios |
| boundary | Soliton boundary | All 19 boundary objects |
| domain | R2 domain | All 22 domain objects |
| cancellation | R2 cancellation | All 7+4 cancellation objects |
| quark | Quark related | m_u, m_d, m_s, m_c, m_b, m_t |
| lepton | Lepton related | m_e, m_mu, m_tau, K_koide |
| clock | Clock / process rate | dv_Cs, H_1S2S |
| DM | Dark matter | Omega_DM, DM/baryon, amplification |
| Hubble | Hubble tension | H0 measurements, running curve |
| Koide | Koide formula | K_koide, a2_lep, m_tau prediction |
| GUT | Grand unification | gap ratios, M_GUT, proton decay |

Tags are free-form strings. This table is the recommended vocabulary. Additional tags may be added as needed. Tags are always lowercase except for proper nouns (CODATA, PDG, FLAG, Koide, Hubble).

---

### TABLE D5.9: POPULATION MAP — phys24_lib.py CONSTANTS TO DATA-5 OBJECTS

| Section | DATA-4 IDs | Count | obj_id prefix | Level | Tags |
|---|---|---|---|---|---|
| A: SI fundamental | A1-A7 | 7 | const.c, const.h, const.e_charge, const.k_B, const.N_A, const.dv_Cs, const.K_cd | 0 | SI, exact, Level0 |
| B: CODATA measured | B1-B13 | 13 | const.alpha_inv, const.m_e, ... const.mu_0 | 2 | Level2, CODATA |
| C: Electroweak | C1-C6 | 6 | const.M_Z, const.Gamma_Z, ... const.G_F | 2 | Level2, EW, PDG |
| D: Quark/CKM | D1-D11 | 11 | const.m_u, const.m_d, ... const.mu_md | 2 | Level2, quark, PDG/FLAG |
| E: Nuclear | E1-E8 | 8 | const.m_n, const.mn_mp_diff, ... const.E_D | 2 | Level2, nuclear |
| F: Spectroscopy | F1 | 1 | const.H_1S2S | 2 | Level2, clock |
| G: Q335 analytical | G1-G31 | 31 | const.pi, const.e_euler, const.R2, ... const.E_3qtr | 0 | Level0, exact, Q335 |
| K: Mass ratios | K1-K8 | 8 | const.mmu_me, const.mtau_me, ... const.K_koide | 2 | Level2, ratio |
| L: CD parameters | L1-L2 | 3 | const.M_VL_lo, const.M_VL_hi, const.theta14 | — | CD, staged |
| N: GUT parameters | N1-N17 | 17 | (betas go to BetaCoefficient objects; others to Constant) | 1 | Level1, GUT |
| Koide derived | — | 3 | const.a2_lep, const.a2_down, const.a2_up | 2 | Level2, Koide |
| Named constants | — | 5 | const.CD_SU3, const.CD_SU2, const.CD_Y, const.casimir_gap, const.hbar | 1 | Level1, CD |
| **Total** | | **~113** | | | |

Plus ~33 derived quantities (inv_a1, inv_a2, inv_a3, gap_SM, gap_VL, gap_MSSM, gap_measured, alpha_em, b_ij_SM entries, etc.) for ~146 Constant objects total.

---

### TABLE D5.10: POPULATION MAP — BETA COEFFICIENTS TO BetaCoefficient OBJECTS

| obj_id | name | gauge_group | value | gauge | fermion | higgs | bsm | Tags |
|---|---|---|---|---|---|---|---|---|
| beta.b1_SM | b1 SM (U1) | U1 | 41/10 | 0 | 4 | 1/10 | 0 | Level1, U1, SM |
| beta.b2_SM | b2 SM (SU2) | SU2 | -19/6 | -22/3 | 4 | 1/6 | 0 | Level1, SU2, SM |
| beta.b3_SM | b3 SM (SU3) | SU3 | -7 | -11 | 4 | 0 | 0 | Level1, SU3, SM |
| beta.db1_VL | db1 CD (U1) | U1 | 1/15 | — | — | — | 1/15 | Level1, U1, CD |
| beta.db2_VL | db2 CD (SU2) | SU2 | 1 | — | — | — | 1 | Level1, SU2, CD |
| beta.db3_VL | db3 CD (SU3) | SU3 | 1/3 | — | — | — | 1/3 | Level1, SU3, CD |
| beta.b1_mod | b1 modified (U1) | U1 | 25/6 | 0 | 4 | 1/10 | 1/15 | Level1, U1, modified |
| beta.b2_mod | b2 modified (SU2) | SU2 | -13/6 | -22/3 | 4 | 1/6 | 1 | Level1, SU2, modified |
| beta.b3_mod | b3 modified (SU3) | SU3 | -20/3 | -11 | 4 | 0 | 1/3 | Level1, SU3, modified |

9 BetaCoefficient objects. Each carries the full decomposition.

---

### TABLE D5.11: POPULATION MAP — REPRESENTATIONS TO Representation OBJECTS

| obj_id | name | (SU3, SU2, Y) | type | db1 | db2 | db3 | charges | Tags |
|---|---|---|---|---|---|---|---|---|
| rep.Q_L | Left quark doublet | (3, 2, 1/6) | chiral | 1/15 | 1 | 2/3 | (2/3, -1/3) | SM, quark, SU2, SU3 |
| rep.u_R | Right up singlet | (3, 1, 2/3) | chiral | 8/15 | 0 | 1/3 | (2/3,) | SM, quark, SU3 |
| rep.d_R | Right down singlet | (3, 1, -1/3) | chiral | 2/15 | 0 | 1/3 | (-1/3,) | SM, quark, SU3 |
| rep.L_L | Left lepton doublet | (1, 2, -1/2) | chiral | 1/5 | 1/3 | 0 | (0, -1) | SM, lepton, SU2 |
| rep.e_R | Right electron singlet | (1, 1, -1) | chiral | 2/5 | 0 | 0 | (-1,) | SM, lepton |
| rep.CD | Cabibbo Doublet | (3, 2, 1/6) | vector-like | 1/15 | 1 | 1/3 | (2/3, -1/3) | CD, BSM, SU2, SU3 |
| rep.Higgs | Higgs doublet | (1, 2, 1/2) | scalar | 1/10 | 1/6 | 0 | (1, 0) | SM, scalar, EW |

7 Representation objects (5 SM fermions + CD + Higgs). Additional candidates (from PHYS-14 enumeration) can be added as needed.

---

### TABLE D5.12: POPULATION MAP — BOUNDARIES TO SolitonBoundary OBJECTS

| obj_id | name | scale_MeV | known | forces | Tags |
|---|---|---|---|---|---|
| boundary.planck | Planck scale | ~1.22×10¹⁹ GeV | No | gravity, unified | gravity, Level0 |
| boundary.gut | GUT unification | ~3.5×10¹⁵ GeV (est) | No | EM, weak, strong, unified | GUT, Level1 |
| boundary.cd_threshold | CD threshold | 1.5-6.0 TeV (window) | No | EM, weak, strong | CD, BSM |
| boundary.top | Top quark | 172570 MeV | Yes | strong | quark, mass |
| boundary.higgs | Higgs boson | 125200 MeV | Yes | EM, weak | scalar, EW |
| boundary.mz | Electroweak (M_Z) | 91187.6 MeV | Yes | EM, weak, strong | EW, reference |
| boundary.mw | W boson | 80369.2 MeV | Yes | weak | EW |
| boundary.bottom | Bottom quark | 4183 MeV | Yes | strong | quark, mass |
| boundary.tau | Tau lepton | 1776.86 MeV | Yes | EM | lepton, Koide |
| boundary.charm | Charm quark | 1273 MeV | Yes | strong | quark, mass |
| boundary.confinement_upper | Confinement (upper) | ~2000 MeV | No | strong | QCD, confinement |
| boundary.confinement_lower | Confinement (lower) | ~300 MeV | No | strong | QCD, confinement |
| boundary.strange | Strange quark | 93.5 MeV | Yes | strong | quark, mass |
| boundary.muon | Muon | 105.658 MeV | Yes | EM | lepton, VP |
| boundary.nuclear | Nuclear binding | ~8 MeV | Yes | strong | nuclear |
| boundary.electron | Electron | 0.51100 MeV | Yes | EM | lepton, VP |
| boundary.atomic | Atomic (Bohr) | — (distance only) | Yes | EM | atomic |
| boundary.molecular | Molecular | — (distance only) | Yes | EM | molecular |
| boundary.gravitational | Gravitational dominance | — (no sharp scale) | No | gravity, EM | gravity |

19 SolitonBoundary objects matching the existing BOUNDARY_STACK.

---

### TABLE D5.13: POPULATION MAP — R2 DOMAINS TO R2Domain OBJECTS

| obj_id | domain | equation | coordinator Z |
|---|---|---|---|
| domain.01_pipe_flow | Pipe flow | Q = R2*d²*v | velocity v |
| domain.02_drag | Drag force | F = ½ρv²R2d²Cd | drag coeff Cd |
| domain.03_orifice | Orifice flow | q = Cd*R2*d²*√(2ΔP/ρ) | discharge Cd |
| domain.04_capacitor | Capacitor | C = ε₀R2d²/t | permittivity ε |
| domain.05_poynting | Poynting flux | P = S*R2*d² | irradiance S |
| domain.06_antenna | Antenna aperture | A = η*R2*D² | efficiency η |
| domain.07_beam | Beam cross-section | A = R2*d² | none |
| domain.08_thermal | Thermal radiation | Q = εσT⁴R2d² | emissivity ε |
| domain.09_sound | Sound intensity | I = P/(16R2r²) | 1/r² spreading |
| domain.10_wire | Wire resistance | R = ρL/(R2d²) | resistivity ρ |
| domain.11_speaker | Speaker cone | Sd = R2*d²_eff | none |
| domain.12_fiber | Fiber mode | A_eff = R2*MFD² | mode confinement |
| domain.13_disc | Disc spot | A = R2*(1.22λ/NA)² | diffraction |
| domain.14_wafer | Wafer area | A = R2*D² | none |
| domain.15_gaussian | Gaussian beam | A = R2*w₀² | beam parameter |
| domain.16_poiseuille | Hagen-Poiseuille | Q = R2d⁴ΔP/(32μL) | viscosity μ |
| domain.17_implant | Ion implant | N = dose/√(8R2σ²)exp(..) | straggle σ |
| domain.18_helmholtz | Helmholtz resonance | f = (c/(8R2))√(R2d²/(lV)) | port geometry |
| domain.19_airy | Diffraction (Airy) | θ = j₁₁/(4R2)*λ/D | Bessel zero j₁₁ |
| domain.20_rayleigh | Rayleigh scattering | σ ~ (8R2/λ)⁴r⁶ | polarizability |
| domain.21_fspl | Free-space path loss | FSPL = (16R2d/λ)² | distance/wavelength |
| domain.22_rcs | Radar cross-section | σ = 16R2A²/λ² | plate area A |
| domain.23_coupling | Gauge coupling running | Δ(1/αᵢ) = bᵢL/(8R2) | beta coefficient bᵢ |

23 R2Domain objects (22 existing + 1 new from modulus notebook).

---

### TABLE D5.14: POPULATION MAP — R2 CANCELLATIONS TO R2Cancellation OBJECTS

| obj_id | name | status | formula | remains |
|---|---|---|---|---|
| cancel.01_kj_x_rk | K_J × R_K | CANCELS | (2e/h)(h/e²) | 2/e |
| cancel.02_g0_x_rk | G₀ × R_K | CANCELS | (2e²/h)(h/e²) | 2 |
| cancel.03_rydberg | Rydberg R∞ | CANCELS | α²m_ec/(2h) | via 2h = 16R₂ℏ |
| cancel.04_a0_alpha | a₀ × α | CANCELS | ℏ/(m_ec) | Compton/2π |
| cancel.05_hartree | Hartree energy | R2-FREE | m_ec²α² | no R₂ enters |
| cancel.06_phi0_rk | Φ₀²/R_K | REAPPEARS | h²/e² × e²/h | h |
| cancel.07_wire_rc | Wire R × Cap C | CANCELS | ρL/(R₂d²) × ε₀R₂d²/t | ρε₀L/t |
| cancel.08_gap_ratio | Gap ratio | CANCELS | (b₁−b₂)/(b₂−b₃) | pure integers |
| cancel.09_fermion_gap | Fermion gap | CANCELS | (4/3−4/3)/(4/3−4/3) | 0/0 (boson problem) |
| cancel.10_sin2_correction | sin²θ_W correction | CANCELS | 3/8 − 3/13 | 15/104 |
| cancel.11_omega_dm | Ω_DM product | CANCELS | Ω_b × DM/baryon | 44/169 |

11 R2Cancellation objects (7 existing + 4 new from modulus notebook).

---

### TABLE D5.15: VERSION CHAIN EXAMPLES

| Constant | v0 (original) | v0 source | v1 (hypothetical) | v1 source | .value returns |
|---|---|---|---|---|---|
| const.alpha_inv | Fraction(137035999177, 10⁹) | CODATA 2022 | (not yet) | — | v0 |
| const.alpha_s | Fraction(1180, 10000) | PDG 2024 | Fraction(1181, 10000) | PDG 2026 (example) | v1 |
| const.m_tau | Fraction(177686, 100) | PDG 2024 | Fraction(177693, 100) | Belle II (example) | v1 |
| const.sin2_tW | Fraction(23122, 100000) | PDG 2024 | (not yet) | — | v0 |

The version chain is append-only. `.value` is always the latest. `.value_v0` is always the original. If v1 is wrong, add v2 — never modify or delete v0 or v1.

---

### TABLE D5.16: QUERY API REFERENCE

| Function | Arguments | Returns | Example |
|---|---|---|---|
| db.get(obj_id) | str | single object or None | db.get("const.alpha_inv") |
| db.find(tag, obj_type, name_contains) | optional str, str, str | list of objects | db.find(tag="SU2") |
| db.find_constants(tag) | optional str | list of Constant | db.find_constants(tag="coupling") |
| db.find_boundaries() | none | list of SolitonBoundary | db.find_boundaries() |
| db.find_by_level(level) | int | list of objects with .level | db.find_by_level(1) |
| db.count(obj_type) | optional str | int | db.count("constant") |
| db.show_all(obj_type, tag) | optional str, str | prints to stdout | db.show_all(obj_type="beta") |
| db.show_summary() | none | prints to stdout | db.show_summary() |
| db.version_report() | none | prints to stdout | db.version_report() |
| db.to_json() | none | JSON string | db.to_json() |
| db.to_dict() | none | nested dict | db.to_dict() |
| search(db, query) | DATA5, str | list of objects | search(db, "dark matter") |
| constants_at_level(db, level) | DATA5, int | list of Constant | constants_at_level(db, 2) |
| show_constants(db, tag) | DATA5, optional str | prints to stdout | show_constants(db, tag="EM") |
| show_boundaries(db, known_only) | DATA5, bool | prints to stdout | show_boundaries(db, True) |
| show_R2(db) | DATA5 | prints to stdout | show_R2(db) |
| show_cancellations(db, status) | DATA5, optional str | prints to stdout | show_cancellations(db, "CANCELS") |
| export_json(db, filename) | DATA5, str | writes file | export_json(db, "snapshot.json") |

17 query functions. All are one-liners. All return lists or print to stdout.

---

### TABLE D5.17: SELF-TEST CHECKLIST (BY PHASE)

| Phase | Test | Expected | Check type |
|---|---|---|---|
| 1 | ObjectRootMeta creates with all fields | obj_id, obj_type, name populated | chk_bool |
| 1 | Constant stores initial value as v0 | .value == .value_v0 == initial | chk_exact |
| 1 | Constant version chain grows on add_version | len(.versions) == 2 after one add | chk_bool |
| 1 | Constant .value returns latest version | .value == v1 after add_version | chk_exact |
| 1 | Constant .value_v0 returns original | .value_v0 == initial always | chk_exact |
| 1 | BetaCoefficient stores value and parts | .value == Fraction(-13, 6) | chk_exact |
| 1 | DATA5.add() populates flat index | db.get("const.alpha_inv") is not None | chk_bool |
| 1 | DATA5.find(tag=) returns correct set | len(db.find(tag="coupling")) >= 3 | chk_bool |
| 1 | DATA5.find(obj_type=) returns correct type | all .obj_type == "constant" | chk_bool |
| 1 | DATA5.count() matches expected | db.count("constant") == 146 | chk_bool |
| 1 | JSON export produces valid JSON | json.loads(db.to_json()) succeeds | chk_bool |
| 1 | JSON roundtrip preserves obj_id | parsed["children"]["const.alpha_inv"]["obj_id"] correct | chk_bool |
| 2 | Representation computes db1, db2, db3 | CD: (1/15, 1, 1/3) | chk_exact × 3 |
| 2 | SolitonBoundary stores scale and forces | M_Z boundary has correct scale | chk_exact |
| 2 | R2Domain stores equation and Z | 22+ domains loaded | chk_bool |
| 2 | R2Cancellation stores status | 11 cancellations loaded | chk_bool |
| 2 | Recursive find searches children | boundary with child coupling found | chk_bool |
| 2 | populate_boundaries loads 19 boundaries | db.count("boundary") == 19 | chk_bool |
| 3 | Modulus stores level and value | Level 0: R2 = pi/4 | chk_bool |
| 3 | ExperimentResult stores script and status | GPS result PASS | chk_bool |
| 3 | ResearchProgram stores thesis and scripts | Beta program has 16 scripts | chk_bool |
| 3 | Full database summary correct | db.count() matches total | chk_bool |
| 4 | Diagram provenance from db objects | prov() source traces to obj_id | chk_bool |
| 4 | Full JSON export | File written, readable, complete | chk_bool |

24 self-tests across 4 phases.

---

### TABLE D5.18: METHOD SUMMARY BY CLASS

| Class | Layer 1 (inherited) | Layer 2 (own) | Properties |
|---|---|---|---|
| ObjectRootMeta | add_child, get_child, find, to_dict, to_json, show | — | — |
| Constant | (all above) | add_version, value_at, value_mpf | .value, .value_v0, .current_version |
| BetaCoefficient | (all above) | — | .numerator, .denominator |
| Representation | (all above) | — | .rep_tuple, .db |
| SolitonBoundary | (all above) | add_coupling | — |
| R2Domain | (all above) | compute | — |
| R2Cancellation | (all above) | — | — |
| Modulus | (all above) | — | — |
| ExperimentResult | (all above) | — | — |
| ResearchProgram | (all above) | — | — |
| DATA5 | (all above) | add, get, find_constants, find_boundaries, find_by_level, count, show_all, show_summary, version_report | — |

11 classes. ObjectRootMeta provides 6 methods. DATA5 adds 8 database-level methods. Domain classes add 0-2 methods each. Total API surface: ~20 methods. Minimal.

---

### TABLE D5.19: IMPLEMENTATION FILE CONTENTS

| File | Classes | Functions | Lines (est.) | Phase |
|---|---|---|---|---|
| data_5_objects.py | ObjectRootMeta, Constant, BetaCoefficient, Representation, SolitonBoundary, R2Domain, R2Cancellation, Modulus, ExperimentResult, ResearchProgram, DATA5 | — | 400-500 | 1-2 |
| data_5_populate.py | — | populate_from_phys24_lib, populate_beta_coefficients, populate_boundaries, populate_R2_domains, populate_representations, populate_experiments, populate_research_programs | 500-700 | 1-3 |
| data_5_helpers.py | — | search, constants_at_level, show_constants, show_boundaries, show_R2, show_cancellations, export_json | 80-100 | 1 |
| data_5_init.py | — | init_data5 | 30-50 | 1 |
| data_5_test.py | — | self-test with 24 checks | 200-300 | 1-4 |
| **Total** | **11 classes** | **~15 functions** | **~1200-1650** | **4 phases** |

---

### TABLE D5.20: COMPATIBILITY MATRIX

| Existing Component | DATA-5 Relationship | Breaking Changes |
|---|---|---|
| phys24_lib.py | DATA-5 imports from it. No changes. | None |
| data_4_derivation_lib.py | DATA-5 imports from it for predictions. No changes. | None |
| phys24_structure_lib.py | Representation objects call make_rep(). No changes. | None |
| phys24_boundary_map_lib.py | Boundary objects populated from BOUNDARY_STACK. No changes. | None |
| phys24_domain_lib.py | Domain objects populated from R2_EQUATIONS. No changes. | None |
| phys24_hubble_lib.py | H0 measurements become Constant objects. No changes. | None |
| data_5_diagram_lib.py | Future: prov() sources can reference obj_id. No changes needed now. | None |
| All experiment scripts | Continue to use flat imports. No changes. | None |
| All diagram scripts | Continue to use flat imports. No changes. | None |
| `from phys24_lib import *` | Still works. DATA-5 is an additional layer. | None |

Zero breaking changes. DATA-5 wraps, does not replace.

---

*End of supporting tables. 20 tables covering: object types, field registries, namespace conventions, tag vocabulary, population maps, version chain examples, query API, self-test checklist, method summary, file contents, and compatibility matrix. Together with the technical specification, these tables provide a complete blueprint for implementing DATA-5 in any future session.*

