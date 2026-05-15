# PHYS-56 COORDINATED FALSIFICATION PROGRAM — LLM-COMPACT FORM
# Source: HOWL-PHYS-56-2026 + Errata + Supporting Appendix Tables
# Format: pipe-delimited tables, ID refs
# Read order: standing_commitments → baseline_status → crossings → kill_switches → round1_tests → novel_predictions → integer_alphabet → errata → relationships → section_index → decode_legend

# standing_commitments(id|commitment|detail)
SC1|Parallel Isomorphism|reproduce SM+GR observables at measurement precision from substrate derivation; inherits standard open problems (Li-7, muon g-2 hadronic VP)
SC2|Integer Alphabet|all predictions from: primary {2,3,4,5,6,8,11,12,13,22,251,264}, secondary catalogued, transcendentals {π,β=π/4,K(k),E(k),e}, moduli {k₈₁=0.999994@167ppb, k₈₃=0.997130@25ppm, per-hierarchy pending}; CD adds b₁=25/6,b₂=-13/6,b₃=-20/3,k₁=3/5,Y=1/6,db(SU2,SU2)=15/4,sinθ₁₄=0.045
SC3|Hierarchy-Local Planck|Planck length/time are Earth-local; dimensionless ratios hierarchy-universal; c=1 cell/tick universal; dimensional quantities hierarchy-specific
SC4|Substrate Completeness|5 primitives (cell,tick,direction-conditional adjacency,remainder,channel) + quiver + 7-level soliton hierarchy = complete ontology; no additional primitives needed
SC5|Cross-Derivation Discipline|multiple independent paths, no common numerical seeds, converging at measurement precision; pre-registered; no post-hoc path selection
SC6|Round 1 Decisive|pre-registered precision thresholds apply; no post-hoc adjustment; no moving goalposts; P1/P2 failures trigger mechanism revision or retraction

# baseline_summary(id|metric|value)
BS1|derived values|53
BS2|measured inputs|13 (11 irreducible + 2 computed convenience: Δα_had, Δr_total)
BS3|surplus|+40 independent predictions
BS4|domains|8 + Koide (now connected)
BS5|crossings|12, all passing
BS6|experimental suites|21
BS7|individual comparisons|85+ of 90+ passing
BS8|PSLQ nulls|58+ (0 hits; retirement confirmed)
BS9|kill switches total|68 (64 + 4 future)
BS10|kill switches cleared|45 at stated precision
BS11|precision span|0.007 ppb to 6.5σ (SM-limited)

# measured_inputs(id|input|value|used_for|source)
MI1|a_e|0.00115965218059|QED chain anchor|Harvard Penning
MI2|m_e|0.51099895 MeV|R∞, reduced mass|CODATA
MI3|m_μ|105.6584 MeV|muon g-2, Koide|PDG
MI4|m_t|172570 MeV|ρ parameter|LHC
MI5|m_H|125200 MeV|EW corrections|LHC
MI6|M_Z|91187.6 MeV|reference scale|LEP
MI7|G_F|1.1663788e-5 GeV⁻²|M_W path B|PDG
MI8|Ω_DM|0.2607|cosmology chain|Planck 2018
MI9|H₀|67.4 km/s/Mpc|ρ_crit|Planck 2018
MI10|T_CMB|2.7255 K|n_γ|COBE
MI11|sinθ₁₄|0.045|CKM/CD mixing|CD parameter
MI12|Δα_had|0.02766|α(M_Z) running|computed convenience
MI13|Δr_total|0.03692|M_W path B|computed convenience

# derived_top20(id|rank|value_name|derived|measured|miss|domain)
DV1|1|θ_QCD|0|0|exact|QCD
DV2|2|N_gen|3|3|exact|EW
DV3|3|α⁻¹ vs Rb|137.035999207|137.035999206|0.007 ppb|QED
DV4|4|α⁻¹ vs CODATA|137.035999207|137.035999084|0.22 ppb|QED
DV5|5|a₀|5.2918e-11 m|5.2918e-11|0.22 ppb|QED
DV6|6|μ₀|1.2566e-6 N/A²|1.2566e-6|0.22 ppb|QED
DV7|7|R∞|10973731.563 m⁻¹|10973731.568|0.44 ppb|QED
DV8|8|f(1S-2S)|2.466061412e15 Hz|2.466061413e15|0.44 ppb|Spectroscopy
DV9|9|a_μ QED shift|—|—|0.22 ppb|Muon
DV10|10|sin²θ_W|0.231223|0.23122|12 ppm|GUT
DV11|11|Ω_Λ|0.68896|0.6889|8.5 ppm|Cosmo
DV12|12|Koide K|0.666666|0.666666|9.2 ppm|Mass
DV13|13|k₈₃|0.997130|—|25 ppm (3-path)|QED
DV14|14|V_us PDG|0.22501|0.22501|44 ppm|Flavor
DV15|15|m_τ Koide|1776.97 MeV|1776.86 MeV|62 ppm|Mass
DV16|16|k₈₁|0.999994|—|167 ppb (3-path)|QED
DV17|17|M_W path B|80354 MeV|80369 MeV|195 ppm|EW
DV18|18|V_ud 4×4|0.97347|0.97373|264 ppm|Flavor
DV19|19|Koide a²|1.99996|2.0|1850 ppm|Mass (torus)
DV20|20|Ω_b|0.04904|0.04900|727 ppm|Cosmo

# domain_summary(id|domain|values|best|worst|status)
DS1|QED|6|0.007 ppb|0.44 ppb|complete anchor
DS2|Electroweak|15|195 ppm|0.84%|mature
DS3|GUT|10|12 ppm|43.7%|active
DS4|Cosmology|6|0.15%|0.73%|complete
DS5|Nuclear|5|0.12σ|2.96× (Li-7)|standard problem
DS6|Muon|3|0.22 ppb|6.5σ (SM-limited)|SM-limited
DS7|Flavor|4|214 ppm|0.83σ|complete
DS8|Spectroscopy|1|0.44 ppb|0.44 ppb|extensible
DS9|Koide|2|exact|62 ppm|newly connected

# crossings(id|num|from_to|bridge|precision|tests)
CR1|1|Trap→QED|5-loop + Newton|0.22 ppb|QED perturbation
CR2|2|QED→Atomic|SI formulas|0.22-0.44 ppb|SI 2019 definitions
CR3|3|Atomic→Spectroscopy(H)|R∞ scaling|0.44 ppb|bound-state QED
CR4|4|QED→Muon|m_μ/m_e|0.22 ppb|lepton universality
CR5|5|Gauge→GUT|two-loop RGE|0.064% gap|CD beta coefficients
CR6|6|GUT→EW coupling|backward run|12 ppm|unification boundary
CR7|7|Gauge→EW mass(A)|Weinberg+ρ|402 ppm|sin²θ_W→M_W
CR8|8|Gauge→EW mass(B)|Sirlin+Δr|195 ppm|G_F→M_W
CR9|9|EW→Z widths|fermion couplings|0.58%|α_s+sin²θ_W
CR10|10|Gauge→Cosmology|(22/13)π|725 ppm|integer ratio×π
CR11|11|Cosmo→Nuclear(H)|BBN fitting|0.12σ|η→BBN reactions
CR12|12|Gauge→Flavor|4×4 CKM|0.83σ|CD mixing angle
# Hydrogen at crossings 3 and 11: same element, completely different physics paths

# koide_connection(id|aspect|detail)
KD1|R₃/R₂|= 2/3 exact; filling fraction ratio (2D→3D packing efficiency)
KD2|a²=2|torus surface dimension at 0.0019% miss (2.0000 vs 1.99996)
KD3|boson K|~1/3 in spherical limit (a=0); confirms lepton form as toroidal emergence
KD4|four-loop correction|computed; convergent series
KD5|critical modulus|k where K(k)=π found; elliptic structure
KD6|implication|Koide atoll connected; amplitude derives from substrate primitive; lepton generation structure is toroidal emergence from integer alphabet

# cd_evidence(id|line|domain|result|falsifier)
CD1|gap ratio 38/27|group theory|exact fraction (only CD matches)|different rep gives 38/27
CD2|CKM deficit|flavor|0.83σ (θ₁₄=0.045 predicts V_ud correction)|V_ud resolves to zero
CD3|α_s one-loop|GUT|8.74% miss (known one-loop limitation)|—
CD4|two-loop gap|GUT|0.027 (218× better than SM)|gap grows at 3-loop
CD5|sin²θ_W prediction|GUT|12 ppm|FCC-ee shift>0.1%

# coupling_collapse(id|quantity|before|after|change)
CC1|sin²θ_W|measured input|derived 12 ppm|input→output
CC2|α_s|measured input|derived 0.33%|input→output
CC3|α_em|measured|measured|anchor unchanged
CC4|coupling inputs|3|1|two freed

# kill_switches(id|name|spec_ref|precision|status|notes)
# K1-K22: Substrate baseline (PHYS-55)
K1|Koide K=2/3 geometric|§XIV,§VII|9.2 ppm|CLEARED|giga_remainder + koide_r3r2
K2|DM/baryon=22π/13|§XV.C|725 ppm|CLEARED|—
K3|V_us=9/40|§XIV.F|44 ppm|CLEARED|—
K4|V_cb=1/24|§XIV.F|0.37%|CLEARED|—
K5|generation democracy 4/3|§XIV.C|exact|CLEARED|—
K6|bridge identity|§XV.E|300 ppm|CLEARED|0.03% best
K7|Ω_Λ=(251-22π)/264|§XV.A|85 ppm|CLEARED|8.5 ppm best
K8|Ω_DM=π/12|§XV.A|1σ Planck|CLEARED|0.42%
K9|Ω_b=13/264|§XV.A|1σ Planck|CLEARED|727 ppm
K10|H₀ tension=12/11|§XV.D|10⁻³|CLEARED|0.67%
K11|flatness ΣΩ=1|§XV.A|exact|CLEARED|—
K12|Lorentz invariance|§XI.G|5-digit|CLEARED|relativity exp
K13|k₈₁ three-path|§VII.E|sub-ppm|CLEARED|167 ppb
K14|k₈₃ three-path|§VII.E|sub-ppm|CLEARED|25 ppm
K15|A₄ magnitude|§VII,§XIV.G|magnitude|CLEARED|—
K16|1/r² gravity|§XII.E|structural|CLEARED|—
K17|PSLQ retirement|meta|58+ nulls|CLEARED|—
K18|Laporta β⁰|§VII|24/24 null|CLEARED|—
K19|cosmic partition closure|§XV.A|exact|CLEARED|—
K20|(m_μ/m_e)²=42753|§VII.D,§XI.C|structural|CLEARED|—
K21|4-loop toroidal dominance|§VII.D|2304×|CLEARED|—
K22|cross-derivation meta|meta|multi-path|ACTIVE|governance rule
# K23-K42: Master spec mechanisms
K23|GPS time dilation|§IX.D|10⁻¹⁰|PARTIAL|0.35%
K24|Pound-Rebka|§IX.D|10⁻³|CLEARED|624 ppm
K25|Hill sphere|§VIII.D|structural|CLEARED|—
K26|Mercury perihelion|§XII.F|10⁻³|CLEARED|2781 ppb
K27|Shapiro delay γ=1|§XII.F|10⁻⁵|CLEARED|—
K28|Hulse-Taylor Pdot|§XII.K|10⁻⁴|CLEARED|42 ppm
K29|solar redshift|§XII.F|10⁻⁴|CLEARED|16 ppm
K30|muon dilated lifetime|§XI.G|10⁻³|CLEARED|442 ppm
K31|SR Minkowski signature|§XI.G|5-digit|CLEARED|—
K32|galactic rotation|§XV.J|10⁻²|CLEARED|toroidal DM
K33|dwarf DM/vis pattern|§XV.I|10⁻²|CLEARED|—
K34|Tully-Fisher v⁴|§XV.J|exact|CLEARED|16.0
K35|frame dragging galactic|§XII.F|10⁻¹|CLEARED|2e-13
K36|amplification (44/13)π(c/v)²|§XV.J|exact|CLEARED|—
K37|α⁻¹ QED forward|§XIV.G|10⁻⁹|CLEARED|3 ppb
K38|sin²θ_W from CD|§XIV.D|12 ppm|CLEARED|—
K39|α_s from CD|§XIV.D|10⁻³|CLEARED|3257 ppm/0.33%
K40|gauge coupling running|§XIV.D|4-digit|CLEARED|—
K41|GUT scale|§XIV.D|10⁻²|CLEARED|log₁₀ 15.54-15.61
K42|proton decay consistency|§XIV|Super-K bound|CLEARED|—
# K43-K56: Additional integration
K43|hydrogen 1S-2S|§XIV.G|10⁻¹⁵|CLEARED|0.44 ppb
K44|Koide universality 9 apps|§XIV|10⁻⁴-10⁻²|CLEARED|—
K45|Chandrasekhar 15π/8|§XII|10⁻²|CLEARED|0.93%
K46|Planck length/time consistency|§IX|10⁻⁸|CLEARED|14.8/102.6 ppb
K47|c=l_P/t_P|§IX.B,§X.C|exact|CLEARED|9-digit
K48|BBN η|§XV.G|10⁻²|CLEARED|0.24%
K49|BBN He-3|§XV.G|10⁻¹|CLEARED|0.36σ
K50|BBN Li-7|§XV.G|—|OPEN|standard BBN problem not PCTRM-specific
K51|coordinate decomposition|§VIII|classification|CLEARED|18/18
K52|R² universality|§IV,§VI|exact|CLEARED|30-digit
K53|BCS gap ratio 1.764|DATA-7|10⁻⁵|CLEARED|13 ppm
K54|Bell correlation|§XIII.F|10⁻³ CHSH|UNTESTED|Round 1 T1
K55|factor-of-2 light bending|§XII.F|10⁻³|UNTESTED|Round 1 T2
K56|direct-detection null|§XII.H|null all sensitivities|PRE-REGISTERED|Round 1 T3
# K57-K64: PHYS-40/CD integration
K57|CD evidence consistency|§XIV.D|5 lines pass|CLEARED|—
K58|coupling sector collapse|§XIV.D|12 ppm+0.33%|CLEARED|—
K59|surplus +40|meta|40 predictions|CLEARED|—
K60|Koide a²=2 torus|§XIV|0.002%|CLEARED|koide_r3r2
K61|12 crossings network|§XIV,§XV|all 12 pass|CLEARED|—
K62|hydrogen dual-domain|§XIV,§XV|QED 0.44ppb + BBN 0.12σ|CLEARED|crossings 3+11
K63|k₁ bug precedent|meta|bug-caught|CLEARED|DATA-6 diagnostic
K64|Casimir from quiver|§IV|10⁻⁶|UNTESTED|Round 1 T4
# K65-K68: Future pre-registered
K65|LHC Run 3 VL quark|CD|2024-2029|PRE-REGISTERED|VL<1.5TeV→CD fails
K66|Hyper-K proton decay|GUT|2027-2037|PRE-REGISTERED|τ_p>10³⁶yr→M_GUT fails
K67|FCC-ee sin²θ_W|CD two-loop|2040s|PRE-REGISTERED|shift>0.1% from 0.23122→fails
K68|CMD-3 vs lattice a_μ|hadronic VP|ongoing|PRE-REGISTERED|changes a_μ(SM) by >2σ

# kill_switch_summary(id|status|count)
KSS1|CLEARED at stated precision|45
KSS2|PARTIAL|3 (K23 GPS, K39 α_s, K41 GUT)
KSS3|UNTESTED Round 1|3 (K54,K55,K64)
KSS4|PRE-REGISTERED|5 (K56,K65-K68)
KSS5|OPEN standard problem|1 (K50 Li-7)
KSS6|ACTIVE meta|1 (K22)
KSS7|total|68

# round1_tests(id|priority|name|mechanism|paths|precision|kill_switch|status)
T1|P1|Bell correlation|§XIII.F channel-sharing|3: channel-merger projection; β² exponent counting Born rule; Tsirelson 2√2 alphabet|10⁻³ CHSH|K54|untested
T2|P1|factor-of-2 light bending|§XII.F toroidal|3: radial+tangential drain decomp; probe-scale toroidal at photon wavelength; Shapiro cross-check|10⁻³|K55|untested
T3|P1|direct-detection null|§XII.H no-particle DM|3: no-particle commitment; 22π/13 flow-based@725ppm; cross-scale toroidal|null all sensitivities|K56|pre-registered
T4|P1|Casimir from quiver|§IV|2: substrate quiver boundary; standard QED compare|10⁻⁶|K64|untested
T5|P1|complex amplitude from dual-geometry|§XIII.M|3: substrate spherical(magnitude)+toroidal(phase); standard QM; Feynman path integral|10⁻³|new K69|untested
T6|P2|A₄ four-path Harvard|§VII.D,§XIV.G|4: layer1+layer2 sum; -(13/8)K(k₈₁)/π; KE k=0.9 C83b; linear combo topology|10⁻¹²|K15 refine|pending
T7|P2|M_W from derived sin²θ_W|§XIV cascade|2: ew_oneloop_v1 with derived sin²θ_W; path B G_F+Δr@195ppm|200 ppm|K58 cascade|pending
T8|P2|G_F derivation|§XIV cascade|2: forward from derived M_W+sin²θ_W; cross-check measured|200-500 ppm|cascade|pending; converts G_F input→output
T9|P2|sin²θ_eff from M_W|§XIV cascade|2: on-shell→effective conversion; measured check 0.23153|10⁻³|cascade|pending
T10|P2|τ_p for Hyper-K|§XIV GUT|2: M_GUT=10¹⁵·⁶¹ + α_GUT⁻¹=42.135; Super-K bound check|10³⁴-10³⁶ yr|K66|pending
T11|P3|Lamb shift 1057 MHz|§VI.D,§XIV.G|2: substrate quiver+atomic; standard QED compare|10⁻⁶|—|pending
T12|P3|neutron half-life 10.2 min|§VI.C weak|2: weak channel+CKM V_ud; standard EW|10⁻³|—|pending
T13|P3|water bond angle 104.5°|§VI.C molecular|2: molecular orbital substrate; alphabet expression|10⁻³|—|pending
T14|P3|deuteron binding 2.224 MeV|§VI.C strong residual|2: multi-nucleon channel; alphabet expression|10⁻⁵|—|pending
T15|P3|BBN Li-7 extension|§XV.G|2: standard BBN+substrate corrections; alphabet Li-7 specific|10⁻²|K50 resolution|open research
T16|P4|cross-scale c VLBI|§IX.B,§X.C|2: substrate arithmetic identity; VLBI constraint 10⁻²⁰|10⁻²⁰|K38 refine|pending
T17|P4|fermion mass hierarchy|§XIV.L|3: lepton democracy+boundary modulus; Koide R₃/R₂ mass ratios; CKM alphabet quark hierarchy|CODATA/PDG|K1,K2|pending
T18|P4|Bullet Cluster displacement|§XII.H|2: structural flow calc; lensing observation|10⁻² offset|K35|pending
T19|P4|cosmic horizon consistency|§XV.M|2: substrate universal soliton; CMB+redshift check|10⁻²|—|pending
T20|P4|black hole thermodynamics|§XII.J|3: boundary arithmetic S=A/4; Hawking T from boundary; evaporation τ∝M³|structural|—|pending
T21|P5|LHC Run 3 VL quark|CD|1: no VL<1.5TeV|>1.5 TeV|K65|pre-registered 2024-2029
T22|P5|FCC-ee sin²θ_W|CD two-loop|1: 0.231223 consistency|10⁻⁵|K67|pre-registered 2040s
T23|P5|vacuum stability CD|§XIV CD Yukawa|2: CD-modified RGE; m_H=125.2 check|10⁻²|—|pending
T24|P5|additional spectroscopy|§XIV.G|2: D 1S-2S, He⁺ 1S-2S, H-D isotope shift|sub-ppb|K43 extend|pending
T25|P5|complete BSM scan|§XIV.D|10: systematic elimination remaining candidates|38/27 exact or ruled out|K57 refine|pending

# success_criteria(id|outcome|p1_req|p2_req|p3_5_req|verdict)
SUC1|full success|all 5 pass at stated precision|≥4 pass|≤2 fail|framework validated
SUC2|partial success|all pass|mixed|mixed|primary mechanism validated
SUC3|specific failure|any fail|—|—|mechanism retracts/revises
SUC4|framework failure|multiple fail|multiple fail|—|substantial retraction

# test_dependencies(id|test|depends_on|reason)
TD1|T6|Round 0+ validated moduli k₈₁,k₈₃|foundation
TD2|T7|T6 + CD two-loop K58|cascade
TD3|T8|T7 M_W derivation|cascade
TD4|T9|T7+T8|cascade
TD5|T10|CD coupling running|GUT scale
TD6|T11|§IV quiver specification|atomic coupling
TD7|T12|§VI weak channel spec|weak channel
TD8|T13|§VI molecular channel|molecular
TD9|T14|§VI strong residual spec|nuclear
TD10|T20|§XII.J Hawking mechanism|BH
TD11|T1-T5|independent of each other|can run parallel

# novel_predictions(id|prediction|mechanism|expected|precision|testable_by|kill_switch)
NP1|direct-detection null|§XII.H no-particle DM|no WIMP at any sensitivity|all current+next-gen|LZ,XENONnT,PandaX|K56
NP2|tau anomalous moment|§XI.C,§VII.D|(m_τ/m_e)² toroidal amplification ≈10⁷|10⁻⁹|future tau g-2|—
NP3|Hawking spectrum|§XII.J|substrate boundary dynamics|future|—|—
NP4|Hyper-K proton decay|M_GUT=10¹⁵·⁶¹|τ_p in sensitivity window 10³⁴-10³⁶ yr|—|Hyper-K 2027-2037|K66
NP5|FCC-ee sin²θ_W|two-loop 0.231223|within 10⁻⁵|10⁻⁵|FCC-ee 2040s|K67
NP6|LHC Run 3 VL quark|CD mass bound|no VL<1.5 TeV|—|LHC 2024-2029|K65
NP7|cosmic c-invariance|§IX.B,§X.C|constant at VLBI|10⁻²⁰|VLBI|—
NP8|Casimir from substrate|§IV quiver|force derivation from boundary|10⁻⁶|precision Casimir|K64
NP9|primordial GW|§XII.K|channel activity patterns|—|CMB polarization|—
NP10|Bullet Cluster offset|§XII.H|specific displacement magnitude|10⁻²|lensing|—
NP11|no new particles commitment|—|no DM particles; no new fermions beyond SM+CD VL quark; no axions|—|ongoing|K56,K65

# future_falsification(id|experiment|timeline|measures|prediction|kill_threshold)
FF1|LHC Run 3|2024-2029|VL quark search|no VL<1.5TeV|observed<1.5TeV→K65
FF2|Hyper-K|2027-2037|τ_p to 10³⁵ yr|M_GUT=10¹⁵·⁶¹|τ_p>10³⁶→K66
FF3|FCC-ee|2040s|sin²θ_W to 10⁻⁵|0.231223|shift>0.1%→K67
FF4|CMD-3 vs lattice|ongoing|hadronic VP|SM-consistent|changes a_μ by >2σ→K68
FF5|new a_e|~2027|a_e to 0.05 ppb|0.00115965218|shifts α by >0.5ppb
FF6|improved V_ud|ongoing|β-decay+radiative|CKM deficit 0.83σ|deficit→0→CD sinθ₁₄ fails
FF7|LZ/XENONnT/PandaX|ongoing|DM particle search|no particle|any WIMP→K56
FF8|future τ g-2|post-2040|a_τ|toroidal amplification|deviation>predicted

# integer_primary_usage(id|integer|mechanisms)
IP1|2|loop doubling, spatial pairs, 2π, Koide a²=2 torus surface
IP2|3|generations, colors, SU(3), R₃/R₂ numerator
IP3|4|Minkowski, β=π/4, db democracy denominator
IP4|6|proton lattice 3π/2=6β, CD b-coefficient denominators
IP5|8|L1 circumference, 8 gluons, 2π/β
IP6|11|Yang-Mills β₁, H₀ ratio denominator
IP7|12|Ω_DM=π/12, H₀ ratio 12/11
IP8|13|Ω_b=13/264, 22π/13, A₄=-(13/8)K/π, b₂(CD)=-13/6
IP9|22|Yang-Mills doubling, Ω_Λ
IP10|251|closure constant Ω_Λ=(251-22π)/264
IP11|264|cosmic denominator 8·3·11

# cd_integers(id|value|source|usage)
CDI1|25/6|b₁(CD)|U(1) modified beta
CDI2|-13/6|b₂(CD)|SU(2) modified beta
CDI3|-20/3|b₃(CD)|SU(3) modified beta
CDI4|3/5|k₁ normalization|GUT U(1) (k₁ bug precedent)
CDI5|1/6|Y(CD)|CD hypercharge
CDI6|15/4|db(SU2,SU2)|two-loop shift
CDI7|199/50|b_ij(U1,U1) SM|two-loop matrix
CDI8|38/27|gap ratio CD|(b₁-b₂)/(b₂-b₃) exact
CDI9|218/115|gap ratio SM|(b₁-b₂)/(b₂-b₃) SM comparison
CDI10|9/40|V_us|=3²/(8·5)
CDI11|1/24|V_cb|=1/(8·3)
CDI12|1/264|V_ub|=1/(8·3·11)

# koide_universality(id|application|particles|K|nearest_rational|miss)
KU1|lepton primary|e,μ,τ|0.66666|2/3|9.2 ppm
KU2|baryon triplet|p,n,Λ|0.3339|1/3|0.17%
KU3|Σ triplet|Σ⁺,Σ⁰,Σ⁻|0.333334|1/3|1.9 ppb
KU4|strange-hyperons|Σ,Ξ,Ω|0.3351|1/3|0.52%
KU5|pseudoscalar|π,K,η|0.358|3/8|4.75%
KU6|charmed|π,K,D|0.419|3/7|2.2%
KU7|vector|ρ,K*,φ|0.334|1/3|0.31%
KU8|Υ states|1S,2S,3S|0.3334|1/3|0.035%
KU9|bosons|W,Z,H|0.336|1/3|0.90%

# r2_universality(id|domain|result|precision)
R2U1|electrical|RC product exact cancellation|30-digit exact
R2U2|QED|K_J×R_K=2/e|exact
R2U3|fluid|vena contracta π/(π+2)=0.611|exact
R2U4|superconductor|BCS gap ratio 1.764|13 ppm
R2U5|engineering|AWG 12 resistance 5.208 mΩ/m|range
R2U6|optical|Blu-ray spot size 0.581 μm|range

# gr_panel(id|test|predicted|measured|miss|status)
GR1|Mercury perihelion|42.9800"|42.9799"|2781 ppb|CLEARED
GR2|solar redshift|636.31"|636.3"|16 ppm|CLEARED
GR3|Pound-Rebka|2.458e-15|2.46e-15|624 ppm|CLEARED
GR4|Hulse-Taylor Pdot|0.999958|1.0|42 ppm|CLEARED
GR5|Cassini Shapiro γ|1.0|1.00000|10⁻⁵|CLEARED
GR6|SN Ia stretch|2.0|2.0|exact|CLEARED
GR7|muon lifetime|6.437e-5 s|6.44e-5 s|442 ppm|CLEARED
GR8|GPA gyroscope|4.25e-10|4.36e-10|2.47%|refinement needed
GR9|GPS net shift|3.85e-5|3.864e-5|0.35%|CLEARED (tolerance)

# galactic_dm(id|check|predicted|measured|status)
GDM1|DM/baryon|5.3165 (22π/13)|5.3204|CLEARED 725 ppm
GDM2|amplification|44/13 exact|3.385|CLEARED exact
GDM3|frame dragging|2e-13 negligible|~0|CLEARED
GDM4|virial ratio|2.81|consistent|PASS
GDM5|Tully-Fisher v⁴|16.0 exact|16.0|CLEARED
GDM6|Draco DM/vis|186|~180|CLEARED
GDM7|Segue1 DM/vis|3824|~3800|CLEARED
GDM8|Fornax DM/vis|8.0|~8|CLEARED

# experimental_suites(id|suite|category|checks|pass|status)
EX1|pctrm_b_round_0|substrate baseline|16|15|15/16
EX2|toroidal_dm_v0|galactic flow DM|8|7|7/8+1INFO
EX3|laporta_toroidal_v0|β⁰ classify|6|6|6/6
EX4|laporta_attack3_v0|modulus consistency|8|8|sub-ppm 3-path
EX5|laporta_pslq_v0|PSLQ null|17|17 NULL|all null
EX6|laporta_muon_electron_v0|mass scaling|structural|2304×|validated
EX7|qed_alpha_extraction_v0|α ppb|22|22|3 ppb
EX8|laporta_a4_decomposition_v0|A₄ sensitivity|27|structural|25 ppb/unit
EX9|hydrogen_1s2s_v0|H 1S-2S|18|4+2+3|0.44 ppb
EX10|clock_reading_decomposition|coordinates|18|18|18/18
EX11|bbn_extended_v0|BBN|34|4+Li-7+3|standard
EX12|giga_remainder_test_v0|multi-domain|127|~90%|comprehensive
EX13|gr_time_dilation_v0|GR panel|18|7+1+10|7/8
EX14|cosmology_chain_v0|partition|5|1+4|closure exact
EX15|relativity_v0|SR|6|6|6/6
EX16|sin2_from_two_loop_v0|Weinberg|6|4+2|12 ppm
EX17|bridge_ew_cosmo_v0|EW-cosmo|10|2+6+2|tree-level gaps
EX18|proton_decay_v0|GUT scale|2|2|2/2
EX19|whatif_scan_v0|framework consistency|6|consistent|confirmed
EX20|r2_universality_v0|R² cancellation|6|6|6/6 DATA-7
EX21|koide_r3r2_v0|Koide geometric|8|6+2|6/6+2INFO

# precision_ledger(id|level|examples|count)
PL1|exact structural|β=π/4, flatness=1, c=c_SI, R²(30-digit), K_J×R_K=2/e, vena contracta=π/(π+2), R₃/R₂=2/3|10+
PL2|sub-ppb ≤1|k₈₁(167ppb), H 1S-2S(0.44ppb), α⁻¹ vs Rb(0.007ppb), α⁻¹ vs CODATA(0.22ppb)|6
PL3|1-100 ppb|α⁻¹ QED(3ppb), Mercury(2781ppb), Planck time/length(~100ppb)|5+
PL4|1-100 ppm|Ω_Λ(8.5), sin²θ_W(12), Koide(9.2), k₈₃(25), V_us(44), solar redshift(16), m_τ(62), Pound-Rebka(624), DM/baryon(725), Ω_b(727)|10+
PL5|100ppm-1%|M_W(195ppm), V_ud(264ppm), a²=2(1850ppm), α_s(0.33%), V_cb(0.37%), Chandrasekhar(0.93%)|10+
PL6|1-10%|Ω_DM(0.42%), H₀(0.67%), α_s 1-loop(8.74%), Γ_Z tree(6.35%)|5+
PL7|known standard issues|Li-7(196% BBN), muon g-2(6.5σ hadronic VP), GPA(2.47%)|3

# cross_derivation_examples(id|target|paths|convergence|status)
XD1|Ω_Λ=(251-22π)/264|4 paths: alphabet direct; substrate; giga_remainder; flatness closure|8.5-85 ppm|CLEARED
XD2|DM/baryon=22π/13|5 paths: alphabet; substrate; galactic flow; multi-domain; BBN|725 ppm|CLEARED
XD3|α⁻¹ QED forward|4 paths: CODATA; Cs recoil; Rb recoil; forward A₂-A₅+a_e→α⁻¹|3-4 ppb|CLEARED
XD4|hydrogen 1S-2S|3 paths: MPQ 2020; CODATA Rydberg; substrate atomic|0.44 ppb|CLEARED
XD5|bridge identity|3 paths: forward |A₄|(α/π)⁴·3·(M_Z/m_e)²; alphabet 22π/13; Round 0 substrate|0.03%|CLEARED
XD6|Koide K=2/3|3 paths: lepton formula; R₃/R₂ filling fraction; a²=2 torus|9.2 ppm|CLEARED

# topology_moduli(id|modulus|value|source|validation|spread)
TM1|k₀|0|spherical limit|exact|—
TM2|k₈₁|0.999994|Laporta 81 (3-path)|sub-ppm|167 ppb
TM3|k₈₃|0.997130|Laporta 83 (3-path)|sub-ppm|25 ppm
TM4|k(A₃)|~0.99|3-loop|magnitude|—
TM5|k(A₄)|~0.995|4-loop|magnitude|—
TM6|k(cosmic)|TBD|cosmic toroidal|pending|—
TM7|k(nucleon)|TBD|nuclear toroidal|pending|—
TM8|k(per-boundary)|TBD|per-hierarchy family|Q10 pending|—

# program_trajectory(id|stage|inputs|derived|surplus|advance)
PT1|PHYS-9|2|4|+2|QED chain only
PT2|PHYS-37|12|17|+5|five domains
PT3|PHYS-38|15|38|+23|seven domains
PT4|PHYS-39|15|48|+33|two-loop GUT
PT5|PHYS-40 (current)|13|53|+40|sin²θ_W,α_s derived; coupling collapse
PT6|after EW cascade T7-T9|11|57|+46|M_W,G_F,sin²θ_eff derived
PT7|after Round 1|10|67+|+57+|comprehensive

# dead_ends(id|attempt|runs|outcome)
DE1|Hubble VP|3|N_VP=0.71<1, killed
DE2|sin²θ_W iterative|1(100 iter)|diverged to 10²¹
DE3|sin²θ_W algebraic|1|0.43 at M_GUT=10³²
DE4|sin²θ_W self-consistent|1|L=0 trivial degenerate
DE5|α(M_Z) VP running|1|128.93 (0.76% miss)
DE6|EW wrong root|1|M_W=43704 MeV
DE7|EW wrong Δr|2|Γ_Z 9-11% miss
DE8|k₁=5/3 inverted|2|M_GUT=10⁴⁵
DE9|Bohr model 1S-2S|2|30 GHz miss

# errata(id|type|issue|correction)
ER1|structural|test dependency relationships not numbered clearly against T1-T25|T1-T5 independent parallel; T6-T10 cascading (T7→T6, T8→T7, T9→T7+T8); T11-T15 depend on spec sections; T16-T20 independent mechanisms; T21-T25 external timelines
ER2|structural|K-switch summary says 45 CLEARED but recount shows ~53+ validated|revise to "53+ validated at stated precision or structural level" with explicit audit
ER3|content|α_s K39 precision target 10⁻³ but match is 3257 ppm (exceeds 1000 ppm)|K39 target should be 10⁻² not 10⁻³; or status PARTIAL at 3257 ppm
ER4|content|M_GUT varies: 15.54 (proton decay 1-loop) vs 15.61 (CD two-loop)|state both explicitly: 1-loop=10¹⁵·⁵⁴, two-loop=10¹⁵·⁶¹
ER5|content|derived count 53 but domain sum = 52 (difference of 1)|verify per-domain and adjust; likely Koide count 3 not 2
ER6|content|K62 "0.12σ" unexplained|0.12σ = cosmology→nuclear hydrogen consistency at crossing #11
ER7|gap|T5 complex amplitude paths underspecified|Path 1: spherical→magnitude + toroidal K(k) periodicity→phase = Ae^(iφ); Path 3: Mach-Zehnder predict interference@10⁻³
ER8|gap|T1 Bell CHSH 10⁻³ not detailed|substrate predicts S=2√2 at optimal angles; within 0.003 of 2.8284
ER9|gap|T20 BH thermodynamics paths vague|need explicit derivation chains from substrate primitives
ER10|gap|T3 direct-detection "convergence" ambiguous for null prediction|success = flow mechanism validated + no WIMP at any sensitivity

# not_in_scope(id|item)
NS1|BBN Li-7 problem (standard BBN)
NS2|muon g-2 hadronic VP dispute (CMD-3 vs lattice)
NS3|consciousness
NS4|free will
NS5|deep "why" of specific integers
NS6|origin of substrate itself
NS7|multiverse / other substrates

# relationships(from|rel|to)
SC1|constrains|K1-K64
SC2|constrains|DV1-DV20
SC5|governs|K22
SC6|governs|SUC1-SUC4
MI1|anchors|DS1
MI2|anchors|DS1
MI6|anchors|DS2
CR3|validates_at|DV8
CR11|validates_at|DS5
CR3|shares_element_with|CR11
K1|validated_by|KD1,KD2
K6|validated_by|XD5
K7|validated_by|XD1
K13|validated_by|TM2
K14|validated_by|TM3
K38|validated_by|CD5,CC1
K58|validated_by|CC1,CC2
K60|validated_by|KD2
K54|tested_by|T1
K55|tested_by|T2
K56|tested_by|T3
K64|tested_by|T4
K65|tested_by|T21
K66|tested_by|T10
K67|tested_by|T22
T7|depends_on|T6
T8|depends_on|T7
T9|depends_on|T7,T8
T10|depends_on|K58
T11|depends_on|SS4
T12|depends_on|SS6
T13|depends_on|SS6
T14|depends_on|SS6
T20|depends_on|SS12
CD1|selects|CDI8
CD5|predicts|DV10
CC1|cascades_to|CC2
CC2|cascades_to|CC3
PT5|current_state|BS1-BS11
NP1|tests_via|FF7
NP4|tests_via|FF2
NP5|tests_via|FF3
NP6|tests_via|FF1
KD1|derives|K1
KD2|connects|KD6
XD1|validates|K7
XD3|validates|K37
XD4|validates|K43
XD6|validates|K1

# section_index(source_section|title|ids)
PHYS56|I Abstract|BS1-BS11,SC6
PHYS56|II Standing Commitments|SC1-SC6
PHYS56|III.A Experimental Suite|EX1-EX21
PHYS56|III.B Koide Connection|KD1-KD6
PHYS56|III.C Derivation Map|DV1-DV20,DS1-DS9
PHYS56|III.D 13 Inputs|MI1-MI13
PHYS56|III.E 12 Crossings|CR1-CR12
PHYS56|III.F Coupling Collapse|CC1-CC4,CD1-CD5
PHYS56|III.G CD Evidence|CD1-CD5
PHYS56|III.H Precision Ledger|PL1-PL7
PHYS56|III.I PSLQ Retirement|BS8
PHYS56|IV Cross-Derivation|XD1-XD6,SC5
PHYS56|V Kill Switches|K1-K68,KSS1-KSS7
PHYS56|VI Round 1 Tests|T1-T25,SUC1-SUC4,TD1-TD11
PHYS56|VII Integer Alphabet|IP1-IP11,CDI1-CDI12
PHYS56|VIII Methodology|DE1-DE9,SC5,SC6
PHYS56|IX Novel Predictions|NP1-NP11
PHYS56|X Companion Commitments|SC1,GR1-GR9,GDM1-GDM8
PHYS56|XI Success Matrix|SUC1-SUC4,FF1-FF8
PHYS56|XII Framework Commitment|SC6,NS1-NS7,PT1-PT7
PHYS56|Errata|ER1-ER10
PHYS56|App A Kill Switch Catalog|K1-K68
PHYS56|App B Experimental Suites|EX1-EX21
PHYS56|App C Derivation Map|MI1-MI13,DV1-DV20,DS1-DS9,CR1-CR12,CD1-CD5,CC1-CC4
PHYS56|App D Round 1 Tests|T1-T25,SUC1-SUC4,TD1-TD11
PHYS56|App E Integer Alphabet|IP1-IP11,CDI1-CDI12,KD1-KD6,TM1-TM8
PHYS56|App F Precision Ledger|PL1-PL7
PHYS56|App G Cross-Derivation|XD1-XD6
PHYS56|App H PSLQ Null Registry|BS8
PHYS56|App I GR Panel + Galactic DM|GR1-GR9,GDM1-GDM8
PHYS56|App J Future Falsification|FF1-FF8,NP1-NP11
PHYS56|App K Spec→Kill Switch Map|K1-K68
PHYS56|App L Commitment Statement|SC1-SC6,SUC1-SUC4,NS1-NS7
PHYS56|App M I/O Accounting|PT1-PT7
PHYS56|App N Dead Ends|DE1-DE9
PHYS56|App O Epistemic Structure|PL1-PL7,XD1-XD6
PHYS56|App P Summary|BS1-BS11,KSS1-KSS7

# decode_legend
# Format: pipe-delimited tables with ID cross-references
# ID prefixes: SC=standing_commitment, BS=baseline_summary, MI=measured_input, DV=derived_value, DS=domain_summary, CR=crossing, KD=koide_connection, CD=cd_evidence, CC=coupling_collapse, K=kill_switch, KSS=kill_switch_summary, T=round1_test, SUC=success_criterion, TD=test_dependency, NP=novel_prediction, FF=future_falsification, IP=integer_primary, CDI=cd_integer, KU=koide_universality, R2U=r2_universality, GR=gr_panel, GDM=galactic_dm, EX=experimental_suite, PL=precision_ledger, XD=cross_derivation, TM=topology_modulus, PT=program_trajectory, DE=dead_end, ER=erratum, NS=not_in_scope
# SS* references point to master spec sections in prior compact doc
# Kill switch status: CLEARED|PARTIAL|UNTESTED|PRE-REGISTERED|OPEN|ACTIVE
# Test priority: P1(mechanism validation)|P2(cascade+refinement)|P3(systematic coverage)|P4(cross-scale)|P5(CD validation+future)
# Success outcomes: full_success|partial_success|specific_failure|framework_failure
# Precision notation: ppb=parts per billion, ppm=parts per million, σ=standard deviations from measurement
# Cross-derivation: multiple independent paths with no common numerical seeds converging at measurement precision
# Surplus = derived_values - measured_inputs = independent testable predictions
# Errata types: structural|content|gap
# rel_types: constrains|governs|anchors|validates_at|shares_element_with|validated_by|tested_by|depends_on|selects|predicts|cascades_to|current_state|tests_via|derives|connects
