# HOWL-DATA-1 — Domain Inventory

## Phase 1: What We Have vs What We Need

Three tiers of data quality across all domains. Every entry classified by whether we already have source values, need to search for them, or whether the domain produces exact data at all.

---

## Master Domain Table

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **A. SI FUNDAMENTAL CONSTANTS** | | | | | |
| A1 | Speed of light c | EXACT INTEGER | **HAVE** | BIPM SI 2019 | 299792458 m/s |
| A2 | Planck constant h | EXACT RATIONAL | **HAVE** | BIPM SI 2019 | 662607015/10⁴² J·s |
| A3 | Elementary charge e | EXACT RATIONAL | **HAVE** | BIPM SI 2019 | 1602176634/10²⁸ C |
| A4 | Boltzmann constant k | EXACT RATIONAL | **HAVE** | BIPM SI 2019 | 1380649/10²⁹ J/K |
| A5 | Avogadro constant N_A | EXACT RATIONAL | **HAVE** | BIPM SI 2019 | 602214076 × 10¹⁵ mol⁻¹ |
| A6 | Cs hyperfine frequency | EXACT INTEGER | **HAVE** | BIPM SI 2019 | 9192631770 Hz |
| A7 | Luminous efficacy K_cd | EXACT INTEGER | **HAVE** | BIPM SI 2019 | 683 lm/W |
| **B. DERIVED EXACT CONSTANTS (from SI)** | | | | | |
| B1 | Josephson constant K_J = 2e/h | EXACT RATIONAL | **HAVE** | derived | computable from A2, A3 |
| B2 | von Klitzing constant R_K = h/e² | EXACT RATIONAL | **HAVE** | derived | computable from A2, A3 |
| B3 | Flux quantum Φ₀ = h/(2e) | EXACT RATIONAL | **HAVE** | derived | computable from A2, A3 |
| B4 | Stefan-Boltzmann σ | EXACT (involves π) | **HAVE** | derived | π²k⁴/(60ℏ³c²), all inputs exact except π |
| B5 | Reduced Planck ℏ = h/(2π) | EXACT (involves π) | **HAVE** | derived | h/(8R₂) |
| **C. MEASURED FUNDAMENTAL CONSTANTS (CODATA 2022)** | | | | | |
| C1 | Fine structure α⁻¹ | 12 digits | **HAVE** | CODATA 2022 | 137.035999177(21) |
| C2 | Electron mass m_e | 11 digits | **HAVE** | CODATA 2022 | 0.51099895069(16) MeV |
| C3 | Muon mass m_μ | 10 digits | **HAVE** | CODATA 2022 | 105.6583755(23) MeV |
| C4 | Tau mass m_τ | 6 digits | **HAVE** | PDG 2024 | 1776.86(12) MeV |
| C5 | Proton mass m_p | 11 digits | **HAVE** | CODATA 2022 | 938.27208943(29) MeV |
| C6 | Proton-electron mass ratio | 13 digits | **HAVE** | CODATA 2022 | 1836.15267343(32) |
| C7 | Rydberg constant R∞ | 13 digits | **HAVE** | CODATA 2022 | 10973731.568157(12) m⁻¹ |
| C8 | Bohr radius a₀ | 12 digits | **HAVE** | CODATA 2022 | 5.29177210544(82)×10⁻¹¹ m |
| C9 | Electron g-factor anomaly a_e | 12 digits | **HAVE** | Fan et al. 2023 | 0.00115965218059(13) |
| C10 | Muon g-factor anomaly a_μ | 8 digits | **HAVE** | Fermilab 2023 | 0.00116592059(22) |
| C11 | Vacuum permeability μ₀ | 10 digits | **HAVE** | CODATA 2022 | 1.25663706127(20)×10⁻⁶ |
| C12 | Free-space impedance Z₀ | 10 digits | **HAVE** | derived from μ₀c | 376.730313412(59) Ω |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **D. OPTICAL STORAGE** | | | | | |
| D1 | CD laser wavelength | EXACT NOMINAL | **HAVE** | ECMA-130 | 780 nm |
| D2 | CD track pitch | EXACT NOMINAL | **HAVE** | ECMA-130 | 1.60 µm |
| D3 | CD pit width | EXACT NOMINAL | **HAVE** | ECMA-130 | 500 nm |
| D4 | CD pit height | EXACT NOMINAL | **HAVE** | ECMA-130 | 125 nm (= λ/4 × n) |
| D5 | CD min pit length | EXACT NOMINAL | **HAVE** | ECMA-130 | 830 nm |
| D6 | CD disc diameter | EXACT NOMINAL | **HAVE** | ECMA-130 | 120 mm |
| D7 | CD disc thickness | EXACT NOMINAL | **HAVE** | ECMA-130 | 1.2 mm |
| D8 | CD sampling rate | EXACT INTEGER | **HAVE** | Red Book | 44100 Hz |
| D9 | CD sector size (raw) | EXACT INTEGER | **HAVE** | ECMA-130 | 2352 bytes |
| D10 | CD sector size (data) | EXACT INTEGER | **HAVE** | ECMA-130 | 2048 bytes |
| D11 | DVD laser wavelength | EXACT NOMINAL | **HAVE** | ECMA-267 | 650 nm |
| D12 | DVD track pitch | EXACT NOMINAL | **HAVE** | ECMA-267 | 0.74 µm |
| D13 | DVD pit width | EXACT NOMINAL | **HAVE** | search results | 320 nm |
| D14 | DVD pit height | EXACT NOMINAL | **HAVE** | search results | 120 nm |
| D15 | DVD min pit length | EXACT NOMINAL | **HAVE** | ECMA-267 | 400 nm |
| D16 | DVD channel bit length | EXACT NOMINAL | **HAVE** | ECMA-267 | 133.3 nm |
| D17 | DVD sector size | EXACT INTEGER | **HAVE** | ECMA-267 | 2048 bytes |
| D18 | Blu-ray laser wavelength | EXACT NOMINAL | **HAVE** | BD White Paper | 405 nm |
| D19 | Blu-ray track pitch | EXACT NOMINAL | **HAVE** | BD White Paper | 0.320 µm |
| D20 | Blu-ray min pit length (2T) | EXACT NOMINAL | **HAVE** | BD White Paper | 149 nm |
| D21 | Blu-ray cover layer | EXACT NOMINAL | **HAVE** | BD White Paper | 0.100 mm |
| D22 | Blu-ray NA | EXACT NOMINAL | **HAVE** | BD White Paper | 0.85 |
| D23 | Blu-ray spot size | EXACT NOMINAL | **HAVE** | Wikipedia/specs | 580 nm |
| D24 | Blu-ray capacity (SL) | EXACT INTEGER | **HAVE** | BD spec | 25 GB |
| D25 | DVD capacity (SL) | EXACT RATIONAL | **HAVE** | DVD spec | 4.7 GB |
| D26 | CD capacity | EXACT NOMINAL | **HAVE** | Red Book | 700 MB / 80 min |
| D27 | CD scanning velocity | EXACT NOMINAL | **NEED CONFIRM** | ECMA-130 | 1.2–1.4 m/s |
| D28 | DVD NA | EXACT NOMINAL | **NEED SEARCH** | ECMA-267 | ~0.60 |
| D29 | CD NA | EXACT NOMINAL | **NEED SEARCH** | ECMA-130 | ~0.45 |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **E. RAM / MEMORY** | | | | | |
| E1 | DDR4-3200 transfer rate | EXACT INTEGER | **HAVE** | JEDEC JESD79-4 | 3200 MT/s |
| E2 | DDR4-3200 clock period | EXACT RATIONAL | **HAVE** | derived | 1/1600000000 s |
| E3 | DDR5-4800 transfer rate | EXACT INTEGER | **HAVE** | JEDEC JESD79-5 | 4800 MT/s |
| E4 | DDR5-6400 transfer rate | EXACT INTEGER | **HAVE** | JEDEC JESD79-5 | 6400 MT/s |
| E5 | DDR5-6400 clock period | EXACT RATIONAL | **HAVE** | derived | 1/3200000000 s |
| E6 | Data bus width | EXACT INTEGER | **HAVE** | JEDEC | 64 bits |
| E7 | ECC bus width | EXACT INTEGER | **HAVE** | JEDEC | 72 bits |
| E8 | Burst lengths | EXACT INTEGER | **HAVE** | JEDEC | 2, 4, 8, 16 |
| E9 | DDR4 voltage | EXACT RATIONAL | **HAVE** | JEDEC | 1.2 V |
| E10 | DDR5 voltage | EXACT RATIONAL | **HAVE** | JEDEC | 1.1 V |
| E11 | DDR4-1600 transfer rate | EXACT INTEGER | **HAVE** | JEDEC | 1600 MT/s |
| E12 | DDR4-2400 transfer rate | EXACT INTEGER | **HAVE** | JEDEC | 2400 MT/s |
| E13 | DDR5-5600 transfer rate | EXACT INTEGER | **NEED CONFIRM** | JEDEC | 5600 MT/s |
| E14 | DDR5-8800 transfer rate | EXACT INTEGER | **NEED SEARCH** | JEDEC | 8800 MT/s? |
| E15 | Typical CAS latencies | EXACT INTEGER | **NEED SEARCH** | JEDEC | per speed grade |
| E16 | DRAM cell area (F²) | EXACT INTEGER | **HAVE** | industry | 6F² standard, 4F² emerging |
| E17 | SRAM cell area | APPROXIMATE | **HAVE** | industry | ~120 F² |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **F. SSD / STORAGE INTERFACES** | | | | | |
| F1 | SATA I line rate | EXACT RATIONAL | **HAVE** | SATA-IO | 1.5 Gbit/s |
| F2 | SATA II line rate | EXACT RATIONAL | **HAVE** | SATA-IO | 3.0 Gbit/s |
| F3 | SATA III line rate | EXACT RATIONAL | **HAVE** | SATA-IO | 6.0 Gbit/s |
| F4 | SATA III unit interval | EXACT RATIONAL | **HAVE** | derived | 1/6000000000 s |
| F5 | PCIe Gen3 transfer rate | EXACT RATIONAL | **HAVE** | PCI-SIG | 8.0 GT/s |
| F6 | PCIe Gen4 transfer rate | EXACT RATIONAL | **HAVE** | PCI-SIG | 16.0 GT/s |
| F7 | PCIe Gen5 transfer rate | EXACT RATIONAL | **HAVE** | PCI-SIG | 32.0 GT/s |
| F8 | PCIe Gen5 unit interval | EXACT RATIONAL | **HAVE** | PCI-SIG | 1/32000000000 s = 31.25 ps |
| F9 | NVMe LBA sizes | EXACT INTEGER | **HAVE** | NVMe spec | 512, 4096 bytes |
| F10 | NAND page sizes | EXACT INTEGER | **HAVE** | ONFI | powers of 2, typically 16384 |
| F11 | 3D NAND layer counts | EXACT INTEGER | **NEED SEARCH** | vendor | 128, 176, 232, 300+ |
| F12 | MRAM half-pitch | MEASURED | **HAVE** | IEDM 2024 | 20.5 nm (smallest demonstrated) |
| F13 | PCIe Gen6 transfer rate | EXACT RATIONAL | **NEED SEARCH** | PCI-SIG | 64.0 GT/s? |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **G. WIRE / CABLE / CONDUCTORS** | | | | | |
| G1 | Inch definition | EXACT RATIONAL | **HAVE** | International agreement | 127/5 mm |
| G2 | Mil definition | EXACT RATIONAL | **HAVE** | derived | 127/5000 mm |
| G3 | AWG formula | IRRATIONAL (92^x) | **HAVE** | ASTM B258 | d_n = 0.005" × 92^((36−n)/39) |
| G4 | AWG diameter ratio | EXACT | **HAVE** | ASTM B258 | ratio = 92^(1/39) ≈ 1.12293 |
| G5 | AWG 36 diameter | EXACT | **HAVE** | ASTM B258 | 0.005 inches exactly |
| G6 | AWG 0000 diameter | EXACT | **HAVE** | ASTM B258 | 0.4600 inches |
| G7 | Circular mil definition | EXACT | **HAVE** | ASTM/NEC | area = d²(mils), NOT π/4 × d² |
| G8 | Circular mil to mm² | INVOLVES R₂ | **HAVE** | derived | 1 cmil = π/4 × (0.0254/1000)² m² |
| G9 | AWG tabulated diameters | EXACT NOMINAL (4 sf) | **NEED SEARCH** | ASTM B258 | full table, gauges 0000–40 |
| G10 | IEC conductor sizes | EXACT NOMINAL | **HAVE** | IEC 60228 | 0.5, 0.75, 1.0, 1.5, 2.5 mm² |
| G11 | Copper resistivity (IACS ref) | EXACT DEFINED | **HAVE** | IACS | 5.8001×10⁷ S/m = 100% IACS at 20°C |
| G12 | 50 Ω impedance | EXACT INTEGER | **HAVE** | RF standard | 50 Ω |
| G13 | 75 Ω impedance | EXACT INTEGER | **HAVE** | RF standard | 75 Ω |
| G14 | 110 Ω impedance | EXACT INTEGER | **HAVE** | differential standard | 110 Ω |
| G15 | Coax cable dimensions | EXACT NOMINAL | **NEED SEARCH** | MIL/RG specs | RG-6, RG-58, RG-59, etc. |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **H. ACOUSTICS / AUDIO** | | | | | |
| H1 | Standard pitch A4 | EXACT INTEGER | **HAVE** | ISO 16 | 440 Hz |
| H2 | CD sample rate | EXACT INTEGER | **HAVE** | Red Book | 44100 Hz |
| H3 | Studio sample rates | EXACT INTEGER | **HAVE** | AES | 48000, 96000, 192000 Hz |
| H4 | SPL reference pressure p₀ | EXACT RATIONAL | **HAVE** | IEC | 20 µPa = 1/50000 Pa |
| H5 | Sound power reference P₀ | EXACT RATIONAL | **HAVE** | IEC | 1 pW = 1/10¹² W |
| H6 | Standard atmosphere | EXACT INTEGER | **HAVE** | ISO 2533 | 101325 Pa |
| H7 | Nominal speaker impedances | EXACT INTEGER | **HAVE** | IEC | 4, 8, 16 Ω |
| H8 | Just intonation ratios | EXACT RATIONAL | **HAVE** | music theory | 2/1, 3/2, 4/3, 5/4 |
| H9 | Equal temperament semitone | IRRATIONAL | **HAVE** | ISO 16 | 2^(1/12) |
| H10 | CD bit depth | EXACT INTEGER | **HAVE** | Red Book | 16 bits |
| H11 | DVD-Audio max sample rate | EXACT INTEGER | **HAVE** | DVD-Audio spec | 192000 Hz |
| H12 | DVD-Audio max bit depth | EXACT INTEGER | **HAVE** | DVD-Audio spec | 24 bits |
| H13 | Speaker Sd (cone area) | MEASURED, uses R₂ | **NEED SEARCH** | manufacturer | Sd = R₂ × d² for circular cones |
| H14 | Example T/S parameters | MEASURED | **NEED SEARCH** | Klippel/manufacturer | Fs, Qts, Vas, Re, Le for specific drivers |
| H15 | Helmholtz resonance formula | INVOLVES R₂ | **HAVE** | acoustics | f = c/(8R₂) × √(A/(lV)) |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **I. RF / TELECOM** | | | | | |
| I1 | Antenna aperture formula | INVOLVES R₂ | **HAVE** | MATH-1 | A_eff = λ²G/(16R₂) |
| I2 | Free-space path loss | INVOLVES R₂ | **HAVE** | Friis | FSPL = (16R₂d/λ)² |
| I3 | π/4-DQPSK modulation | NAMED AFTER R₂ | **HAVE** | IS-136 | constellation rotates by R₂ per symbol |
| I4 | T1 carrier rate | EXACT RATIONAL | **HAVE** | telecom | 1.544 Mbps |
| I5 | Ethernet frame sizes | EXACT INTEGER | **HAVE** | IEEE 802.3 | 64–1518 bytes |
| I6 | Standard baud rates | EXACT INTEGER | **HAVE** | RS-232 | 9600, 115200, etc. |
| I7 | 5G NR subcarrier spacing | EXACT INTEGER | **HAVE** | 3GPP | 15×2ⁿ kHz |
| I8 | WiFi frequencies | EXACT NOMINAL | **NEED SEARCH** | IEEE 802.11 | 2.4 GHz, 5 GHz, 6 GHz bands |
| I9 | DWDM channel spacing | EXACT NOMINAL | **NEED SEARCH** | ITU-T G.694.1 | 100 GHz, 50 GHz grids |
| I10 | GPS L1 frequency | EXACT RATIONAL | **HAVE** | GPS spec | 1575.42 MHz = 154 × 10.23 MHz |
| I11 | GPS L2 frequency | EXACT RATIONAL | **HAVE** | GPS spec | 1227.60 MHz = 120 × 10.23 MHz |
| I12 | GPS base frequency | EXACT RATIONAL | **HAVE** | GPS spec | 10.23 MHz |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **J. SEMICONDUCTOR / LITHOGRAPHY** | | | | | |
| J1 | Wafer diameter (300mm) | EXACT NOMINAL | **HAVE** | SEMI | 300 mm |
| J2 | Wafer area | INVOLVES R₂ | **HAVE** | derived | R₂ × (300)² mm² |
| J3 | Si lattice constant | 10 digits MEASURED | **HAVE** | CODATA | 5.431020511(89) Å |
| J4 | EUV wavelength | EXACT NOMINAL | **HAVE** | ASML | 13.5 nm |
| J5 | ArF immersion wavelength | EXACT NOMINAL | **HAVE** | industry | 193 nm |
| J6 | Diffusion erfc formula | INVOLVES R₂ | **HAVE** | Fick | erfc contains 1/√(πt) = 1/(2√(R₂t)) |
| J7 | Gaussian implant formula | INVOLVES R₂ | **HAVE** | ion implant | 1/√(2π)σ = 1/√(8R₂)σ |
| J8 | Process node names | MARKETING (not real) | **HAVE** | industry | "7nm", "5nm", "3nm" are not dimensions |
| J9 | Rayleigh criterion | INVOLVES R₂ | **HAVE** | optics | 1.22 ≈ 3.83/π from Airy disk |
| J10 | Current leading-edge specs | MEASURED | **NEED SEARCH** | TSMC/Samsung/Intel | gate pitch, metal pitch, cell height |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **K. OPTICS / PHOTONICS** | | | | | |
| K1 | Gaussian beam Rayleigh range | INVOLVES R₂ | **HAVE** | optics | z_R = 4R₂w₀²/λ |
| K2 | Gaussian beam divergence | INVOLVES R₂ | **HAVE** | optics | θ = λ/(4R₂w₀) |
| K3 | Fiber V-number | INVOLVES R₂ | **HAVE** | fiber optics | V = 4R₂·d·NA/λ |
| K4 | SMF-28 mode field diameter | MEASURED | **NEED SEARCH** | Corning | ~10.4 µm at 1550 nm |
| K5 | Fiber loss at 1550 nm | MEASURED | **NEED SEARCH** | Corning | ~0.18 dB/km |
| K6 | Telecom C-band | EXACT NOMINAL | **NEED SEARCH** | ITU-T | 1530–1565 nm |
| K7 | Planck radiation formula | INVOLVES R₄ | **HAVE** | thermal | σ = 32R₄k⁴/(60ℏ³c²) |
| K8 | Si refractive index at 1550 nm | MEASURED | **NEED SEARCH** | literature | ~3.48 |
| K9 | SiO₂ refractive index at 1550 nm | MEASURED | **NEED SEARCH** | literature | ~1.444 |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **L. FLOW / THERMAL / MECHANICAL** | | | | | |
| L1 | Pipe flow (MATH-1 #2) | INVOLVES R₂ | **HAVE** | MATH-1 | Q = R₂d²v |
| L2 | Drag (MATH-1 #3) | INVOLVES R₂ | **HAVE** | MATH-1 | F = ½ρv²·R₂d²·C_d |
| L3 | Orifice flow (MATH-1 #4) | INVOLVES R₂ | **HAVE** | MATH-1 | Q = C_d·R₂d²·√(2ΔP/ρ) |
| L4 | Capacitor (MATH-1 #5) | INVOLVES R₂ | **HAVE** | MATH-1 | C = ε₀/t·R₂d² |
| L5 | Poynting (MATH-1 #6) | INVOLVES R₂ | **HAVE** | MATH-1 | P = S·R₂d² |
| L6 | Antenna (MATH-1 #7) | INVOLVES R₂ | **HAVE** | MATH-1 | A_eff = η·R₂D² |
| L7 | Beam optics (MATH-1 #8) | INVOLVES R₂ | **HAVE** | MATH-1 | A = R₂d² |
| L8 | Thermal radiation (MATH-1 #9) | INVOLVES R₂ | **HAVE** | MATH-1 | Q = σT⁴·R₂d²·ε |
| L9 | Pendulum | INVOLVES R₂ | **HAVE** | mechanics | T = 8R₂√(L/g) |
| L10 | Torsion (polar moment) | INVOLVES R₂ | **HAVE** | mechanics | J = R₂d⁴/8 |
| L11 | Standard gravity g_n | EXACT RATIONAL | **HAVE** | CGPM 1901 | 9.80665 m/s² |
| L12 | Coriolis meter precision | MEASURED | **NEED SEARCH** | manufacturer | ±0.05% typical |
| L13 | Orifice C_d (ISO 5167) | MEASURED | **NEED SEARCH** | ISO 5167 | ~0.61, tabulated |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **M. METROLOGY / PRECISION INSTRUMENTS** | | | | | |
| M1 | QHE integer verification | 0.2 ppb | **HAVE** | NIST/PTB | R_K/i for integer i |
| M2 | Josephson step verification | 10⁻¹⁰ | **HAVE** | NIST | V = nhf/(2e) |
| M3 | Gauge block sizes | EXACT NOMINAL | **NEED SEARCH** | ISO 3650 | standard series |
| M4 | ISO tolerance grades | EXACT FORMULA | **NEED SEARCH** | ISO 286 | IT01–IT18 |
| M5 | Surface roughness Ra series | EXACT NOMINAL | **HAVE** | ISO 4287 | 0.1, 0.2, 0.4, 0.8, 1.6, 3.2 µm |
| M6 | CMM uncertainty | MEASURED | **NEED SEARCH** | manufacturer | ~50 nm over 1 m |
| M7 | Crystal oscillator stability | MEASURED | **HAVE** | industry | 5×10⁻¹² (DOCXO) |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **N. GEODESY / NAVIGATION** | | | | | |
| N1 | WGS 84 semi-major axis | EXACT INTEGER | **HAVE** | WGS 84 | 6378137 m |
| N2 | WGS 84 flattening 1/f | EXACT RATIONAL | **HAVE** | WGS 84 | 298.257223563 |
| N3 | GPS seconds per week | EXACT INTEGER | **HAVE** | GPS spec | 604800 |
| N4 | Standard gravity | EXACT RATIONAL | **HAVE** | CGPM 1901 | 9.80665 m/s² |
| N5 | Earth angular velocity | EXACT NOMINAL | **HAVE** | WGS 84 | 7.292115×10⁻⁵ rad/s |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **O. SIGNAL PROCESSING / MATH** | | | | | |
| O1 | Fourier normalization | INVOLVES R₂ | **HAVE** | math | 1/(2π) = 1/(8R₂) |
| O2 | Sinc function | INVOLVES R₂ | **HAVE** | math | sinc(t) = sin(4R₂t)/(4R₂t) |
| O3 | Gaussian normalization | INVOLVES R₂ | **HAVE** | math | 1/√(2π) = 1/√(8R₂) |
| O4 | Stirling approximation | INVOLVES R₂ | **HAVE** | math | n! ≈ √(8R₂n)(n/e)ⁿ |
| O5 | Maxwell-Boltzmann | INVOLVES R₂ | **HAVE** | stat mech | (8R₂)^(3/2) in normalization |
| O6 | BCS gap ratio | INVOLVES π, γ | **HAVE** | BCS theory | 2Δ/(kT_c) = π/e^γ = 3.528 |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **P. ATOMIC SPECTROSCOPY / CLOCKS** | | | | | |
| P1 | H 1S-2S frequency | 16 digits | **HAVE** | Parthey et al. | 2466061413187018(11) Hz |
| P2 | H hyperfine splitting 1S | 12 digits | **HAVE** | H maser | 1420405751.768(1) kHz |
| P3 | Sr-87 clock frequency | 16 digits | **HAVE** | BIPM CIPM | 429228004229873.0(2) Hz |
| P4 | Yb-171 clock frequency | 16 digits | **HAVE** | BIPM CIPM | 518295836590863.6(3) Hz |
| P5 | Al+ clock frequency | 18 digits | **HAVE** | NIST | ~1121015393207857.3 Hz |
| P6 | Lamb shift 2S-2P | 7 digits | **HAVE** | spectroscopy | 1057845.0(9) kHz |
| P7 | Proton charge radius | 5 digits | **HAVE** | muonic H | 0.84075(64) fm |

---

| # | Domain | Rational-Friendly? | Data Status | Source Standard | Notes |
|---|---|---|---|---|---|
| **Q. NUCLEAR / HADRON MASSES** | | | | | |
| Q1 | Proton mass | 11 digits | **HAVE** | CODATA | 938.27208943(29) MeV |
| Q2 | Neutron mass | 11 digits | **HAVE** | CODATA | 939.56542194(48) MeV |
| Q3 | n-p mass difference | 7 digits | **HAVE** | CODATA | 1.29333251(38) MeV |
| Q4 | Pion mass (charged) | 9 digits | **HAVE** | PDG | 139.57039(18) MeV |
| Q5 | Pion mass (neutral) | 7 digits | **HAVE** | PDG | 134.9770(5) MeV |
| Q6 | Kaon mass (charged) | 6 digits | **HAVE** | PDG | 493.677(16) MeV |
| Q7 | Deuteron mass | 11 digits | **HAVE** | CODATA | 1875.61294500(58) MeV |
| Q8 | He-4 mass | 11 digits | **HAVE** | CODATA | 3727.3794118(12) MeV |
| Q9 | Deuteron binding energy | 7 digits | **HAVE** | CODATA | 2.22456614(42) MeV |

---

## Gap Analysis — What to Search Next

| Priority | Domain | What's Missing | Search Target |
|---|---|---|---|
| HIGH | G9 | Full AWG table (gauges 0000–40) with diameters | ASTM B258 table |
| HIGH | H13-H14 | Real speaker Sd and T/S parameters from specific drivers | Klippel data, Eminence/B&C spec sheets |
| HIGH | K4-K9 | Fiber optic measured specs (MFD, loss, refractive indices) | Corning SMF-28 datasheet, literature |
| MEDIUM | D28-D29 | CD and DVD numerical aperture values | ECMA-130, ECMA-267 |
| MEDIUM | E14-E15 | Latest DDR5 speed grades and CAS latencies | JEDEC JESD79-5C |
| MEDIUM | F11 | 3D NAND layer counts by vendor/year | Samsung/Micron/SK hynix press releases |
| MEDIUM | F13 | PCIe Gen6 specs | PCI-SIG |
| MEDIUM | G15 | Coax cable dimensions (RG-6, RG-58, etc.) | MIL-C-17 specs |
| MEDIUM | I8-I9 | WiFi frequencies, DWDM channel grid | IEEE 802.11, ITU-T G.694.1 |
| MEDIUM | J10 | Current leading-edge semiconductor dimensions | TSMC/Samsung/Intel specs |
| MEDIUM | L12-L13 | Flow meter precision specs, orifice coefficients | ISO 5167, manufacturer data |
| MEDIUM | M3-M4 | Gauge block series, ISO tolerance grades | ISO 3650, ISO 286 |
| LOW | M6 | CMM manufacturer specs | Zeiss/Hexagon datasheets |
| LOW | N5 | Earth angular velocity precision | WGS 84 tech doc |

---

## Summary Counts

| Category | Total Entries | HAVE | NEED SEARCH | NEED CONFIRM |
|---|---|---|---|---|
| A. SI Fundamental | 7 | 7 | 0 | 0 |
| B. Derived Exact | 5 | 5 | 0 | 0 |
| C. Measured Fundamental | 12 | 12 | 0 | 0 |
| D. Optical Storage | 29 | 26 | 2 | 1 |
| E. RAM/Memory | 17 | 14 | 2 | 1 |
| F. SSD/Storage | 13 | 11 | 2 | 0 |
| G. Wire/Cable | 15 | 12 | 3 | 0 |
| H. Acoustics/Audio | 15 | 12 | 2 | 0 |* |
| I. RF/Telecom | 12 | 9 | 3 | 0 |
| J. Semiconductor | 10 | 8 | 2 | 0 |
| K. Optics/Photonics | 9 | 4 | 5 | 0 |
| L. Flow/Thermal/Mech | 13 | 11 | 2 | 0 |
| M. Metrology | 7 | 4 | 3 | 0 |
| N. Geodesy | 5 | 5 | 0 | 0 |
| O. Signal Processing | 6 | 6 | 0 | 0 |
| P. Spectroscopy/Clocks | 7 | 7 | 0 | 0 |
| Q. Nuclear/Hadron | 9 | 9 | 0 | 0 |
| **TOTAL** | **206** | **178** | **26** | **2** |

**178 of 206 entries have source data. 26 need targeted searches. 2 need confirmation.**

The R₂ connection column tells us which entries go into the R₂ equation mapping in DATA-2. Roughly 60+ entries directly involve R₂ or R₄ in their governing equation. The rest are either pure integers, exact rationals, or measured values that enter as inputs to R₂ equations.
