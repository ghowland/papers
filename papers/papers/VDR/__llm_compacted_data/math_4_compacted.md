# MATH-4 UNIVERSAL POWER-OF-TWO BASIS — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → cf_origin → basis_constants → verification → arithmetic → compression → qed_application → falsification → limitations → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Shared power-of-two denominator|all 22 constants as single integers over 2³³⁵; addition/subtraction reduces to integer add/sub on numerators; no LCD computation
P2|Representation change not new math|same constants, same precision, same sub-Planck threshold as MATH-2; contribution is encoding optimization for linear combinations
P3|CF origin|87/32 is 5th convergent of e, best rational approximation with denominator ≤ 32; 32=2⁵; extending to 2³³⁵ provides 100-digit precision for entire basis
P4|Complementary to MATH-2|MATH-2 pairs for single-constant high-precision work; Q335 basis for multi-constant linear combinations (physics formulas)
P5|Minimal universal exponent|n=335 is minimal: at n=334 Catalan's G fails at position 101; at n=335 all 22 constants pass 100-digit verification

# cf_convergents(id|index|cf_coeff|p|q|decimal|error_ppm|power_of_two)
CF0|0|2|2|1|2.000|264241|2⁰
CF1|1|1|3|1|3.000|103638|no
CF2|2|2|8|3|2.667|18988|no
CF3|3|1|11|4|2.750|11668|2²
CF4|4|1|19|7|2.714|1470|no
CF5|5|4|87|32|2.71875|172|2⁵
CF6|6|1|106|39|2.71795|123|no
CF7|7|1|193|71|2.71831|10.3|no
CF8|8|6|1264|465|2.71828|0.83|no
# CF pattern: e = [2; 1, 2k, 1] repeating for k=1,2,3,...
# Three power-of-two convergents: CF0(2⁰), CF3(2²), CF5(2⁵); no further in first 25 convergents
# 87/32 is the last and best power-of-two convergent at human-readable scale

# projection_math(id|aspect|detail)
PM1|Rounding error bound|projecting x onto nearest p/2ⁿ: error ≤ 2⁻⁽ⁿ⁺¹⁾
PM2|100-digit requirement|2⁻⁽ⁿ⁺¹⁾ < 10⁻¹⁰⁰ → n > 100·log₂(10)−1 ≈ 331.2
PM3|Sub-1 constants|ln(2)≈0.693 needs extra bit; empirically n=335 covers all 22
PM4|Sub-Planck threshold|rounding error 2⁻³³⁶ ≈ 10⁻¹⁰¹·²; Planck length ≈ 10⁻³⁵; ratio = 10⁻⁶⁶; first divergent digit is 66 orders of magnitude below Planck length

# basis_constants(id|name|numerator_over_2_335|p_digits|p_bits)
BC1|π|219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314|102|337
BC2|e|190258044782769202588129925521314757831284456026137946619894798297742927086075833929023100244479638112|102|337
BC3|ln(2)|48514773537953331556699584584828624926234404478840896710102416707062925979128257345653169777835518667|101|335
BC4|√2|98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506|101|336
BC5|φ|113249472467736168604496750010842101773570690275806888818880481552730738076053012711350611809151189412|102|336
BC6|π²|690793580147337726804277647484346770338921354138994508002872352435529393755796399964695383625668575976|102|339
BC7|π³|2170192036537868242782341740347526814570179266657980009466902575842216583318830559778528157446001240080|103|340
BC8|π⁴|6817859358866439017122533696289105276559442547141782759070845808348090383725467935335488832685124730326|103|342
BC9|eᵖ|1619663895456875537109657111692739211478931048048038025064408441944407978010684548404551575192727763397|103|340
BC10|ln²(2)|33627878493336594620147550513544307026418133133387860405002917547734923457242850195041264715469792904|101|334
BC11|ln⁴(2)|16156615573798633249523359538243246008210686364818713716124360467773572086286920210666548222826014086|101|333
BC12|ln(3)|76894096788635086096158790585166115140009649181250777410832538562395270797691729322128736655820466233|101|336
BC13|ln(5)|112647815694871799155432631259623524245586803429977893615314774516410370135500048646041895614334987799|102|336
BC14|ln(10)|161162589232825130712132215844452149171821207908818790325417191223473296114628305991695065392170506466|102|337
BC15|√3|121229740294912895234576661752159696642961157181742464717663915473198765686797807393142352785809790154|102|336
BC16|√5|156506921742415955629073428753920319855839958763030979672136303700342980177725995879548801953564656455|102|337
BC17|√7|185181487127092153770432076884133468631121666203542492409943031514633653137939942068870811445311050320|102|337
BC18|ζ(2)|115132263357889621134046274580724461723153559023165751333812058739254898959299399994115897270944762663|102|336
BC19|ζ(3)|84134394645319852071522700710261177454128732241134555234516209978359598548186272768450592529361881680|101|336
BC20|ζ(5)|72576671487518636549061590533542457287978428544763113598602740326685645428855657003519154452098433211|101|336
BC21|Li₄(1/2)|36219406486600619537883622883703292936779255100080725994962678520983767482244581297270363585520219319|101|335
BC22|Catalan G|64110285111693582641294563817927086726382757371148180987419195376360958765615024299223500526530512841|101|335
# All 22 verified against mpmath at 100 decimal digits by string comparison. All match.
# All numerators are 100-103 digit integers, bit-widths 333-342.

# arithmetic_properties(id|operation|mechanism|precision_impact)
AR1|Addition/subtraction of two constants|(p₁ ± p₂) / 2³³⁵; single integer add/sub|at most ±1 rounding residual from individual projections
AR2|Multiplication by integer k|(k · p_C) / 2³³⁵|exact
AR3|Multiplication by power-of-two rational a/2ᵐ|(a · p_C) / 2³³⁵⁺ᵐ or (a · p_C) >> m over 2³³⁵|exact
AR4|Multiplication by rational r/s (s has odd factors)|approach A: carry as r·p_C / (s·2³³⁵) with odd factor explicit (exact); approach B: round(r·p_C/s) / 2³³⁵ (loses ≤1 ULP)|A preserves exactness; B stays below 100-digit floor
AR5|Multiplication of two basis constants|product has denominator 2⁶⁷⁰; project back to 2³³⁵ by right-shifting 335 bits + rounding|loses precision below 100-digit floor; or precompute as separate basis entry
AR6|Algebraic identity residuals|p(π²) − 6·p(ζ(2)) = −2 (not 0)|bounded by #terms × individual rounding error; far below 100-digit floor

# compression(id|constant|math2_digits|q335_digits|ratio)
CM1|π|1107|102|10.9×
CM2|π²|2213|102|21.7×
CM3|π³|3319|103|32.2×
CM4|π⁴|4425|103|43.0×
CM5|e|233|102|2.3×
CM6|ln(2)|426|101|4.2×
CM7|√2|784|101|7.8×
CM8|√3|586|102|5.7×
CM9|√5|429|102|4.2×
CM10|√7|842|102|8.3×
CM11|φ|856|102|8.4×
CM12|ζ(2)|2213|102|21.7×
CM13|ζ(3)|618|101|6.1×
CM14|Li₄(1/2)|618|101|6.1×
CM15|Catalan G|1714|101|17.0×
CM16|eᵖ|131868|103|1280×
# Total MATH-2: ~20000 digits for 22 constants
# Total Q335: 2238 digits + exponent 335
# Compression most dramatic for composed constants (denominator explosion eliminated)

# qed_application(id|aspect|detail)
QA1|A₂ formula|A₂ = 197/144 + π²/12 + 3ζ(3)/4 − (π²/2)·ln(2)
QA2|Odd content|denominators 144=2⁴·3², 12=2²·3, 4=2², 2=2¹; odd content is 3²=9; composite denominator 9·2³³⁵
QA3|Computation|each term = small rational coefficient × basis integer; accumulate; shared 2³³⁵ factor common throughout
QA4|Verification|result matches MATH-2 Fraction computation from PHYS-5 at 100 digits

# falsification(id|criterion)
F1|Any numerator in basis divided by 2³³⁵ must produce 100-digit decimal matching mpmath evaluation; reproducible with Python + mpmath
F2|QED coefficient or physical quantity via Q335 must agree with MATH-2 Fraction computation at 100 digits
F3|If constant from MATH-3+ cannot be projected onto 2³³⁵ grid at 100 digits, basis is incomplete (extension is mechanical: compute MATH-2 pair and project)

# limitations(id|limitation|detail)
LM1|100-digit precision ceiling|for higher precision increase exponent proportionally: ~3.32 bits per decimal digit; 200 digits → ~2⁶⁶⁸
LM2|Basis not exhaustive|higher ζ values, higher polylogarithms, complete elliptic integrals from MATH-3 not yet included; extension mechanical
LM3|Product of two basis constants|produces denominator 2⁶⁷⁰; must project back or precompute as separate entry
LM4|Odd-denominator rationals|require hybrid approach (explicit odd factor or projection with ≤1 ULP loss)
LM5|Algebraic identity residuals|exact identities hold only approximately; residuals bounded and below precision floor

# relationships(from|rel|to)
P1|enables|AR1,AR2,AR3
P2|clarifies|P4
P3|motivates|P1,P5,CF5
P4|distinguishes|P1(Q335 for combinations) vs MATH-2(for single-constant precision)
P5|determined_by|BC1-BC22
CF5|motivates|P3
PM1|bounds|PM4
PM2|determines|P5
BC1-BC22|verified_by|F1
BC6|equals_approx|BC18(p(π²)−6·p(ζ(2))=−2; AR6)
AR1|used_in|QA1-QA4
AR4|used_in|QA2
AR5|limited_by|LM3
CM1-CM16|demonstrates|P1(denominator explosion eliminated)
CM16|most_dramatic|1280×(eᵖ composed constant)
QA4|validates|P2,F2
F1|validates|BC1-BC22
LM1|extensible_via|increasing exponent
LM2|extensible_via|MATH-3 projection

# section_index(section|title|ids)
I|Abstract|P1,P2,P3
II.1|The Observation|P3,CF5
II.2|Convergent Table|CF0-CF8
II.3|Power-of-Two Convergents|CF0,CF3,CF5
II.4|The Extension|PM1-PM4,P5
III|Precision Threshold|PM4
IV|Complete Basis|BC1-BC22
V.1|Exact Operations|AR1,AR2,AR3
V.2|Hybrid Operations|AR4,AR5
V.3|QED Case|QA1-QA4
VI|Compression|CM1-CM16
VII|Relationship to MATH-2/3|P2,P4
VIII|Application A₂|QA1-QA4
IX|Falsification|F1-F3
X|Limitations|LM1-LM5

# decode_legend
id_prefixes: P=principle, CF=cf_convergent, PM=projection_math, BC=basis_constant, AR=arithmetic_property, CM=compression, QA=qed_application, F=falsification, LM=limitation
rel_types: enables|clarifies|motivates|distinguishes|determined_by|verified_by|equals_approx|used_in|limited_by|demonstrates|most_dramatic|validates|extensible_via|bounds|determines
q335: shared denominator 2³³⁵ for all 22 constants; each constant stored as single integer numerator
verification: all 22 constants verified against mpmath at 100 decimal digits by string comparison
storage: 2238 total numerator digits + exponent 335 (vs ~20000 digits for MATH-2 pairs)
precision: 100 decimal digits; rounding error ≤ 2⁻³³⁶ ≈ 10⁻¹⁰¹·²; 10⁶⁶ × below Planck length
exponent_scaling: ~3.32 bits per additional decimal digit of precision
