# PCTRM SPECIFICATION GAPS — LLM-COMPACT FORM
# Source: PCTRM Specification Gaps — Completion Document
# Format: pipe-delimited tables, ID refs
# Read order: structural_gaps → codata_targets → mechanism_clarifications → novel_predictions → checklists → derivation_phases → relationships → section_index → decode_legend

# structural_gaps(id|title|spec_location|what_missing|what_needed|falsification|priority)
SG1|Per-Hierarchy-Boundary Moduli|SS7,SS11|moduli catalog states "family pending"; no specific values declared|complete enumeration of moduli at each hierarchy boundary; one modulus per boundary determines mass scale; 12 boundaries minimum (e,μ,τ,u,d,s,c,b,t,W,Z,H); possibly fewer if generation structure shares moduli|each modulus produces specific mass prediction matching CODATA or wrong|critical — largest gap; entire mass sector blocked
SG2|Natural Units to SI Bridge|SS2,SS9|derivation chain from integer alphabet through substrate to SI units not stated; 2019 SI fixed 7 defining constants; spec has c=1 cell/tick only|explicit bridging: ℏ = one unit substrate action per tick; e = EM channel unit throughput quantum; k_B = tick-energy to temperature bridge; N_A = counting number pure integer; ΔνCs = ticks per Cs-133 hyperfine period (specific prediction); K_cd = human-perceptual outside scope|bridge produces consistent SI values across all CODATA or contradictions at specific points|high — no CODATA comparison possible without
SG3|Charge Quantization|SS6|EM channels listed but quantization of charge not committed; why e/3 quarks and e leptons not specified|channel structure forcing charge quantization; what produces 1/3 and 2/3 fractional quark charges; why lepton charges integer multiples; how channel forbids other values|produces exactly observed charge spectrum or fails|high — foundational to SM reduction
SG4|Color Charge and SU(3)|SS14|"gauge group from channel enumeration" claimed but explicit enumeration producing SU(3) not provided|channel-counting argument forcing exactly 3 color states; combination rules (color singlets for hadrons, confinement preventing isolated color)|forces exactly 3 colors with correct rules or doesn't|high — mechanism behind confinement
SG5|Spin from Dual-Geometry|SS7,SS13|coverage audit marks spin as C-PI; specific mechanism not stated; how dual-geometry produces half-integer vs integer spin|explicit connection spherical/toroidal sector → spin; toroidal wrapping (full vs half) could distinguish; must produce spin-0,1/2,1,3/2,2 with correct statistics|produces observed spin spectrum with BE/FD statistics or doesn't|high — foundational to QM and SM

# si_bridge_constants(id|constant|substrate_interpretation|status)
SIB1|c|1 cell/tick|already in spec
SIB2|ℏ|one unit substrate action per tick|implicit, needs explicit statement + SI bridge
SIB3|e|EM channel unit throughput quantum|needs bridge to SI coulombs
SIB4|k_B|tick-energy to temperature bridge|needs thermal channel connection to kelvins
SIB5|N_A|counting number, pure integer|no substrate interpretation needed; bridge must state
SIB6|ΔνCs|ticks per Cs-133 hyperfine period|specific prediction framework should make
SIB7|K_cd|human-perceptual quantity|outside substrate scope; bridge must state boundary

# codata_em(id|constant|symbol|status|derivation_path|blocked_on)
CE1|fine structure constant|α|priority downstream|hierarchy config via integer alphabet|—
CE2|fine structure constant inverse|α⁻¹ ≈ 137.036|priority downstream|must emerge as alphabet expression|CE1
CE3|elementary charge|e|pending SI bridge|channel unit throughput quantum|SG2
CE4|vacuum permittivity|ε₀|pending SI bridge|follows from α,e,ℏ,c|CE1,CE3
CE5|vacuum permeability|μ₀|pending SI bridge|follows from ε₀,c|CE4
CE6|impedance of free space|Z₀|derived|follows from μ₀,ε₀|CE5,CE4
CE7|Bohr magneton|μ_B|derived|follows from e,ℏ,m_e|CE3,CM1
CE8|nuclear magneton|μ_N|derived|follows from e,ℏ,m_p|CE3,CM4
# Key: α from integer alphabet is single most important EM derivation; everything cascades

# codata_mass(id|constant|symbol|status|blocked_on|notes)
CM1|electron mass|m_e|pending|SG1|per-hierarchy-boundary modulus
CM2|muon mass|m_μ|pending|SG1|per-hierarchy-boundary modulus
CM3|tau mass|m_τ|pending|SG1|per-hierarchy-boundary modulus
CM4|proton mass|m_p|pending|SG1|modulus + toroidal content (99%)
CM5|neutron mass|m_n|pending|CM4|m_p + mass difference derivation
CM6|up quark mass|m_u|pending|SG1|per-hierarchy-boundary modulus
CM7|down quark mass|m_d|pending|SG1|per-hierarchy-boundary modulus
CM8|strange quark mass|m_s|pending|SG1|per-hierarchy-boundary modulus
CM9|charm quark mass|m_c|pending|SG1|per-hierarchy-boundary modulus
CM10|bottom quark mass|m_b|pending|SG1|per-hierarchy-boundary modulus
CM11|top quark mass|m_t|pending|SG1|per-hierarchy-boundary modulus
CM12|W boson mass|M_W|pending|SG1|per-hierarchy-boundary modulus
CM13|Z boson mass|M_Z|pending|SG1|per-hierarchy-boundary modulus
CM14|Higgs boson mass|M_H|pending|SG1|per-hierarchy-boundary modulus
CM15|proton-electron mass ratio|m_p/m_e|pending|SG1|ratio may be derivable before absolute masses
CM16|muon-electron mass ratio|m_μ/m_e|pending|SG1|206.768... from hierarchy structure
CM17|neutron-proton mass difference|m_n-m_p|pending|CM4|channel arithmetic
# Note: dimensionless mass ratios derivable before SI bridge; productive intermediate step

# codata_electroweak(id|constant|symbol|status|derivation_path|gap_note)
CEW1|weak mixing angle|sin²θ_W|not listed in spec|channel type enumeration|should be explicit target in SS14
CEW2|Fermi coupling constant|G_F|not listed in spec|weak channel throughput at low energy|should be explicit target in SS14
CEW3|W boson width|Γ_W|downstream|weak channel decay arithmetic|—
CEW4|Z boson width|Γ_Z|downstream|weak channel decay arithmetic|—
CEW5|Higgs boson width|Γ_H|downstream|channel decay arithmetic|—

# codata_strong(id|constant|symbol|status|derivation_path|gap_note)
CS1|strong coupling constant|α_s(M_Z)|not explicitly listed|channel-coupling scaling at Z mass|should be high-priority target
CS2|QCD scale parameter|Λ_QCD|downstream|from α_s running|—
CS3|proton charge radius|r_p|downstream|toroidal content of proton channel structure|may resolve muonic hydrogen puzzle
CS4|proton magnetic moment|μ_p|downstream|toroidal sector at proton scale|—
CS5|neutron magnetic moment|μ_n|downstream|toroidal sector at neutron scale|—
CS6|pion mass|m_π|downstream|strong channel arithmetic|—
CS7|pion decay constant|f_π|downstream|strong channel decay|—

# codata_gravitational(id|constant|symbol|status|derivation_path|gap_note)
CG1|gravitational constant|G|not listed|hierarchy-local drain channel throughput|conspicuously absent; framework claims hierarchy-local not universal; predicted Earth-hierarchy value should be target
CG2|Planck mass|m_P|derived|follows from G,ℏ,c|—
CG3|Planck length|l_P|derived|= 1 cell in Earth hierarchy|—
CG4|Planck time|t_P|derived|= 1 tick in Earth hierarchy|—
CG5|Planck temperature|T_P|derived|follows from m_P,k_B|—

# codata_g2(id|constant|status|derivation_path|notes)
CG2A|electron g-2 (a_e)|high priority|dual-geometry: spherical π + toroidal elliptic|—
CG2B|muon g-2 (a_μ)|high priority|dual-geometry with 22 MeV crossover|current BNL/FNAL vs SM tension; framework may produce different prediction; novel-prediction opportunity
CG2C|tau g-2 (a_τ)|downstream|same decomposition at tau scale|—

# codata_mixing(id|constant|status|derivation_path|gap_note)
MX1|CKM V_us|claimed 9/40|integer channel ratio|needs derivation
MX2|CKM V_cb|claimed 1/24|integer channel ratio|needs derivation
MX3|CKM V_ub|not listed|integer channel ratio|should be target
MX4|CKM V_td|not listed|integer channel ratio|should be target
MX5|CKM V_ts|not listed|integer channel ratio|should be target
MX6|CKM V_tb|not listed|integer channel ratio|should be target
MX7|CKM V_ud|not listed|unitarity from V_us,V_ub|consistency check
MX8|CKM V_cs|not listed|unitarity|consistency check
MX9|CKM V_cd|not listed|unitarity|consistency check
MX10|Jarlskog invariant J|not listed|CP violation magnitude from CKM|should be target
MX11|PMNS θ₁₂|high priority|weak channel arithmetic|neutrino mixing
MX12|PMNS θ₂₃|high priority|weak channel arithmetic|neutrino mixing
MX13|PMNS θ₁₃|high priority|weak channel arithmetic|neutrino mixing
MX14|PMNS δ_CP|not listed|neutrino CP phase|should be target
MX15|neutrino Δm²₂₁|not listed|channel arithmetic|should be explicit target
MX16|neutrino Δm²₃₂|not listed|channel arithmetic|should be explicit target
# Gap: full CKM = 9 elements (4 independent + unitarity); spec claims 2; all 9 should be targets
# Gap: PMNS needs all params including δ_CP and Majorana phases if neutrinos are Majorana
# Gap: neutrino Dirac/Majorana commitment needed

# codata_cosmo(id|constant|status|value|gap_note)
CC1|Ω_b|derived|13/264|complete
CC2|Ω_DM|derived|π/12|complete
CC3|Ω_Λ|derived|(251-22π)/264|complete
CC4|DM/baryon ratio|derived|22π/13|complete
CC5|baryon-to-photon ratio η|derived|—|complete
CC6|H₀ absolute value|not derived|12/11 ratio only|absolute value should be target
CC7|CMB temperature T₀|not listed|—|2.7255 K should be derivable from early-universe + expansion
CC8|scalar spectral index n_s|not listed|—|high-precision CMB measurement; should predict
CC9|tensor-to-scalar ratio r|not listed|—|primordial GW amplitude
CC10|optical depth τ|not listed|—|downstream
CC11|age of universe|not listed|—|follows from H₀ + expansion history
CC12|N_eff|derived|2.71|10.9% miss vs standard 3.044; tension — commit as prediction or state as known issue
CC13|primordial He-4 Y_p|derived|—|1.5% miss
CC14|primordial D/H|derived|—|0.14% miss
CC15|primordial Li-7|tension reproduced|—|resolution pending
CC16|σ₈|not listed|—|downstream from structure formation
CC17|primordial He-3|not listed|—|derivation needed
CC18|primordial Li-6|not listed|—|derivation needed

# codata_nuclear(id|constant|status|derivation_path|gap_note)
CN1|deuteron mass|not listed|nuclear channel arithmetic|significant precision data not targeted
CN2|deuteron binding energy|not listed|strong residual channel|—
CN3|triton mass|not listed|nuclear channel arithmetic|—
CN4|helion mass|not listed|nuclear channel arithmetic|—
CN5|alpha particle mass|not listed|nuclear channel arithmetic|—
CN6|nuclear magnetic moments|not listed|toroidal sector content|—
CN7|deuteron magnetic moment|not listed|toroidal sector|—
CN8|nuclear charge radii|not listed|channel structure|—
CN9|semi-empirical mass formula coefficients|not listed|strong channel averaging|—
CN10|magic numbers (2,8,20,28,50,82,126)|not listed|channel closure at nuclear scale|integers; natural fit for alphabet; should be listed

# codata_qed_precision(id|constant|status|derivation_path|notes)
CQ1|Lamb shift (H 2S-2P)|C-PI in audit|toroidal QED contribution|—
CQ2|hydrogen 1S-2S transition|not listed|atomic scale derivation|measured to 15 sig figs; ultimate precision test
CQ3|hydrogen hyperfine splitting|not listed|toroidal magnetic interaction|—
CQ4|positronium ground state hyperfine|not listed|pure QED system|—
CQ5|muonium hyperfine splitting|not listed|QED + muon mass|—
CQ6|Rydberg constant R_∞|not listed|follows from α,m_e,c,ℏ|cascades from fundamentals
CQ7|Bohr radius a₀|not listed|follows from α,m_e,ℏ|cascades
CQ8|classical electron radius r_e|not listed|follows from α,m_e,c,ℏ|cascades
CQ9|electron Compton wavelength|not listed|follows from m_e,ℏ,c|cascades
CQ10|Thomson cross section|not listed|follows from r_e|cascades

# mechanism_clarifications(id|title|what_missing|what_needed|falsification)
MC1|Neutrino Mass Structure|no commitment on Dirac/Majorana; no absolute masses; no mass ordering; no sterile neutrino position|explicit commitments on each; channel structure should force one option per question|neutrinoless double beta decay tests Majorana; JUNO/DUNE test ordering
MC2|Strong CP and θ Parameter|θ=0 discussed but not formally committed; ground state argument needs rigor|explicit: θ=0 from substrate ground state; consequence: no axion; state as commitment|axion detection falsifies
MC3|Proton Lifetime|soliton framework doesn't commit to eternal stability vs eventual decay|explicit commitment: stable or unstable with lifetime|Hyper-Kamiokande
MC4|Baryon Asymmetry Mechanism|listed "downstream"; Sakharov conditions need substrate equivalents|specific channel dynamics in early universe producing asymmetry|—
MC5|Vacuum Energy / CC Problem|BBN output shows 3.94e+54 ratio vs standard 10¹²²; type-error argument discussed but not committed|explicit: does framework dissolve CC problem? what does 10⁵⁴ ratio represent?|—

# novel_predictions(id|prediction|pctrm_value|sm_consensus|testable_by|status)
NP1|N_eff|2.71 (current)|3.044|CMB Stage-4|commit as prediction or state as known issue
NP2|strong CP θ|exactly 0 structurally|0 observed mechanism unknown|axion searches (null predicted)|needs formal commitment
NP3|proton stability|commit needed|SM: stable; GUTs: ~10³⁴ yr|Hyper-Kamiokande|needs commitment
NP4|H₀ tension|12/11 structural ratio|unknown resolution|future precision measurements|partially derived
NP5|muon g-2|dual-geometry prediction pending|SM: tension with experiment|Fermilab/J-PARC comparison|pending derivation
NP6|G variability|hierarchy-local not universal|universal constant|precision G measurements at L1/L2|pending derivation
NP7|dark matter|not particles; toroidal-flow Higgs response|particles (WIMPs, axions etc)|direct detection (null predicted)|committed
NP8|neutrino nature|commit needed|unknown|neutrinoless double beta decay|needs commitment

# novel_precision(id|quantity|why_pctrm_may_exceed_sm|status)
NPR1|G|explains measurement scatter; may predict value more precisely than experiments agree|pending derivation
NPR2|proton radius|dual-geometry may resolve muonic hydrogen puzzle|pending derivation
NPR3|Li-7 abundance|BBN reproduces standard tension; may identify resolution path|tension confirmed resolution pending
NPR4|Y_p primordial helium|1.5% miss may improve with refined BBN chain|derivation refinement

# checklist_fundamental(id|item|status)
CKF1|α|pending
CKF2|α_s(M_Z)|pending
CKF3|sin²θ_W|pending
CKF4|G_F|pending
CKF5|G|pending
CKF6|m_e|pending
CKF7|m_μ|pending
CKF8|m_τ|pending
CKF9|m_u|pending
CKF10|m_d|pending
CKF11|m_s|pending
CKF12|m_c|pending
CKF13|m_b|pending
CKF14|m_t|pending
CKF15|M_W|pending
CKF16|M_Z|pending
CKF17|M_H|pending
CKF18|CKM matrix (4 independent)|pending
CKF19|PMNS matrix (6 independent)|pending
CKF20|neutrino Δm² (2)|pending
CKF21|θ strong CP|pending commitment
CKF22|Λ cosmological|pending

# checklist_cosmo(id|item|status)
CKC1|Ω_b|done: 13/264
CKC2|Ω_DM|done: π/12
CKC3|Ω_Λ|done: (251-22π)/264
CKC4|DM/baryon ratio|done: 22π/13
CKC5|baryon-to-photon ratio η|done
CKC6|H₀ absolute|pending
CKC7|CMB temperature T₀|pending
CKC8|n_s|pending
CKC9|r tensor-to-scalar|pending
CKC10|optical depth τ|pending
CKC11|age of universe|pending
CKC12|N_eff|done: 2.71 (tension 10.9% vs 3.044)

# checklist_qed(id|item|status)
CKQ1|a_e electron g-2|pending
CKQ2|a_μ muon g-2|pending
CKQ3|H 1S-2S transition|pending
CKQ4|H hyperfine splitting|pending
CKQ5|Lamb shift|pending
CKQ6|Rydberg R_∞|pending

# checklist_nuclear(id|item|status)
CKN1|proton charge radius r_p|pending
CKN2|proton magnetic moment μ_p|pending
CKN3|neutron magnetic moment μ_n|pending
CKN4|deuteron binding energy|pending
CKN5|nuclear magic numbers|pending
CKN6|pion mass m_π|pending
CKN7|pion decay constant f_π|pending
CKN8|neutron lifetime τ_n|pending

# checklist_bbn(id|item|status)
CKB1|D/H|done: 0.14% miss
CKB2|Y_p He-4|done: 1.5% miss
CKB3|He-3|pending
CKB4|Li-7|tension reproduced
CKB5|Li-6|pending

# checklist_structural(id|item|status)
CKS1|per-hierarchy-boundary moduli|pending: SG1
CKS2|natural-to-SI bridge|pending: SG2
CKS3|charge quantization mechanism|pending: SG3
CKS4|color charge / SU(3) derivation|pending: SG4
CKS5|spin from dual-geometry|pending: SG5
CKS6|neutrino Dirac/Majorana|pending: MC1

# checklist_novel(id|item|status)
CKV1|no axion (θ=0 structural)|pending commitment
CKV2|no DM particles|committed
CKV3|G hierarchy-local prediction|pending derivation
CKV4|N_eff commitment|pending: 2.71 or revised
CKV5|proton stability|pending commitment
CKV6|neutrino mass ordering|pending commitment
CKV7|muon g-2 dual-geometry|pending derivation
CKV8|proton radius dual-geometry|pending derivation

# derivation_phases(id|phase|title|items|unblocks)
DP1|1|Unblock mass sector|SG1 per-hierarchy moduli; m_e from alphabet; all mass ratios; Koide K=2/3|entire mass sector CM1-CM17
DP2|2|Unblock electroweak|α from alphabet; sin²θ_W; G_F; W,Z,H masses|CE1-CE8,CEW1-CEW5
DP3|3|Unblock strong sector|α_s(M_Z); m_π,f_π; r_p; nuclear magnetic moments|CS1-CS7
DP4|4|Complete mixing matrices|full CKM (9 elements); full PMNS (all params); Δm²; CP magnitudes|MX1-MX16
DP5|5|Precision QED|a_e,a_μ dual-geometry; Lamb shift; H 1S-2S|CG2A-CG2C,CQ1-CQ10
DP6|6|Gravitational sector|G from hierarchy config; H₀ absolute; age of universe|CG1-CG5,CC6,CC11
DP7|7|Cosmological precision|T₀; n_s; complete BBN (He-3,Li-6)|CC7-CC18
DP8|8|Novel predictions|pre-register all NP1-NP8; identify additional; design experimental tests|CKV1-CKV8
DP9|9|SI bridge and publication|complete dimensional bridge; full CODATA table; all derivations in integer-alphabet-only Python|SG2,SIB1-SIB7

# completion_criterion(id|criterion)
COMP1|every checklist item derived with integer-alphabet-only Python matching CODATA to measurement precision, or committed with falsification condition
COMP2|every structural commitment in SG1-SG5 specified with explicit values
COMP3|every novel prediction NP1-NP8 pre-registered with falsification conditions
COMP4|SI bridge produces consistent dimensional values across all derived quantities
COMP5|full CODATA table generatable from single execution of derivation chain from integer alphabet with no external inputs

# relationships(from|rel|to)
SG1|blocks|CM1,CM2,CM3,CM4,CM6,CM7,CM8,CM9,CM10,CM11,CM12,CM13,CM14
SG1|blocks|DP1
SG2|blocks|CE3,CE4,CE5
SG2|blocks|DP9
SG3|prerequisite_of|SG4
SG4|prerequisite_of|CS1
SG5|prerequisite_of|MX11,MX12,MX13
CE1|cascades_to|CE2,CE4,CE5,CE6,CE7,CE8,CQ6,CQ7,CQ8,CQ9,CQ10
CM1|cascades_to|CE7,CQ6,CQ7,CQ8,CQ9
CM4|cascades_to|CM5,CE8
CM15|derivable_before|SG2
CM16|derivable_before|SG2
MX1|unitarity_check_with|MX3,MX7
MX2|unitarity_check_with|MX5,MX8
CC12|tension_with|3.044 standard
CC13|tension|1.5% miss
CC14|tension|0.14% miss
NP1|tests_via|CMB Stage-4
NP2|tests_via|axion searches
NP3|tests_via|Hyper-Kamiokande
NP5|tests_via|Fermilab/J-PARC
NP6|tests_via|L1/L2 G measurements
NP7|tests_via|direct detection null
NP8|tests_via|neutrinoless double beta
MC1|requires_commitment_in|SS6,SS13
MC2|requires_commitment_in|SS14
MC3|requires_commitment_in|SS5
MC4|requires_commitment_in|SS15
MC5|requires_commitment_in|SS15
DP1|prerequisite_of|DP2
DP2|prerequisite_of|DP3
DP3|prerequisite_of|DP4
DP4|prerequisite_of|DP5
DP5|prerequisite_of|DP6
DP6|prerequisite_of|DP7
DP7|prerequisite_of|DP8
DP8|prerequisite_of|DP9
COMP1|requires|DP1,DP2,DP3,DP4,DP5,DP6,DP7
COMP2|requires|SG1,SG2,SG3,SG4,SG5
COMP3|requires|NP1,NP2,NP3,NP4,NP5,NP6,NP7,NP8
COMP4|requires|SG2,DP9
COMP5|requires|COMP1,COMP2,COMP3,COMP4

# section_index(source_section|title|ids)
I|Structural Commitments Pending|SG1,SG2,SG3,SG4,SG5,SIB1-SIB7
II.1|EM Constants|CE1-CE8
II.2|Mass Constants|CM1-CM17
II.3|Electroweak Constants|CEW1-CEW5
II.4|Strong Constants|CS1-CS7
II.5|Gravitational Constants|CG1-CG5
II.6|Anomalous Magnetic Moments|CG2A-CG2C
II.7|Mixing Matrix Elements|MX1-MX16
II.8|Cosmological Parameters|CC1-CC18
II.9|Nuclear and Hadronic|CN1-CN10
II.10|Precision QED Tests|CQ1-CQ10
III|Mechanism Clarifications|MC1-MC5
IV|Novel Predictions|NP1-NP8,NPR1-NPR4
V|Structural Completeness Checklists|CKF1-CKF22,CKC1-CKC12,CKQ1-CKQ6,CKN1-CKN8,CKB1-CKB5,CKS1-CKS6,CKV1-CKV8
VI|Derivation Priority Ordering|DP1-DP9
VII|Completion Criterion|COMP1-COMP5

# decode_legend
# Format: pipe-delimited tables with ID cross-references
# ID prefixes: SG=structural_gap, SIB=si_bridge_constant, CE=codata_em, CM=codata_mass, CEW=codata_electroweak, CS=codata_strong, CG=codata_gravitational, CG2x=codata_g2, MX=mixing_matrix, CC=codata_cosmo, CN=codata_nuclear, CQ=codata_qed_precision, MC=mechanism_clarification, NP=novel_prediction, NPR=novel_precision, CKF=checklist_fundamental, CKC=checklist_cosmo, CKQ=checklist_qed, CKN=checklist_nuclear, CKB=checklist_bbn, CKS=checklist_structural, CKV=checklist_novel, DP=derivation_phase, COMP=completion_criterion
# SS* references point to spec_sections in prior compact doc (PCTRM Master+Coverage)
# Status values: pending | downstream | done | not listed | claimed | C-PI | tension | critical
# Priority: critical | high | medium | low
# Checklist status: pending | done | done with tension | pending commitment | pending derivation
# Derivation phase ordering: DP1→DP2→...→DP9 strict prerequisite chain; each unblocks downstream
# Blocked_on: ID of item that must be resolved first
# Tension: numerical mismatch between derived value and observation/standard; stated with percentage
# rel_types: blocks | cascades_to | prerequisite_of | derivable_before | unitarity_check_with | tension_with | tests_via | requires_commitment_in | requires
