#!/bin/bash

# 1. Setup temporary file
cp manuscript.md manuscript_fixed.md

# 2. Basic cleanup: Remove Variation Selector and leading spaces that break Pandoc
sed -i 's/\xEF\xB8\x8F//g' manuscript_fixed.md
sed -i 's/^    //g' manuscript_fixed.md
sed -i 's/```//g' manuscript_fixed.md

# 3. Consolidated Symbol Replacement (Unicode to LaTeX Math)
# This uses $...$ for everything to ensure the X symbol (times) renders as a glyph
sed -i -e 's/π/ $\\pi$ /g' \
       -e 's/μ/ $\\mu$ /g' \
       -e 's/ν/ $\\nu$ /g' \
       -e 's/ρ/ $\\rho$ /g' \
       -e 's/Λ/ $\\Lambda$ /g' \
       -e 's/𝕋/ $\\mathbb{T}$ /g' \
       -e 's/ℝ/ $\\mathbb{R}$ /g' \
       -e 's/ℚ/ $\\mathbb{Q}$ /g' \
       -e 's/ℤ/ $\\mathbb{Z}$ /g' \
       -e 's/ℕ/ $\\mathbb{N}$ /g' \
       -e 's/×/ $\\times$ /g' \
       -e 's/✗/ $\\times$ /g' \
       -e 's/✓/ $\\checkmark$ /g' \
       -e 's/±/ $\\pm$ /g' \
       -e 's/⟨/ $\\langle$ /g' \
       -e 's/⟩/ $\\rangle$ /g' \
       -e 's/ₖ/$_k$ /g' \
       -e 's/ᵢ/$_i$ /g' \
       -e 's/ₙ/$_n$ /g' \
       -e 's/ₗ/$_l$ /g' \
       -e 's/ₜ/$_t$ /g' \
       -e 's/ₚ/$_p$ /g' \
       -e 's/𝒯/ $\\mathcal{T}$ /g' \
       -e 's/ₘ/$_m$ /g' \
       -e 's/ⱼ/$_j$ /g' \
       -e 's/ᵈ/$^d$ /g' \
       -e 's/☉/ $\\odot$ /g' \
       -e 's/ö/\\text{ö}/g' \
       -e 's/ー/ $\\text{ー}$ /g' \
       -e 's/⚠/\\textbf{!}/g' manuscript_fixed.md

# # 4. Fix double-wrapping and clean up math markers
# # If a symbol was already in math mode, we might have created $$symbol$$. This fixes it.
# sed -i 's/\$\$/$ /g' manuscript_fixed.md

# 5. Fix list formatting: Force a newline before any hyphen preceded by text
sed -i 's/\([[:alnum:]\)]\)- /\1\n- /g' manuscript_fixed.md

# Double Space - Only if line does not start with |
sed -i '/^|/!{/^$/d;G}' manuscript_fixed.md

# 6. Run Pandoc
# Added amssymb and amsmath to ensure symbols like \checkmark and \times are recognized
pandoc manuscript_fixed.md -o !manuscript.pdf \
  --pdf-engine=xelatex \
  --from markdown+tex_math_dollars \
  --citeproc \
  --bibliography=../../../references.bib \
  --metadata link-citations=true \
  --metadata title="CKS-DWDM-6-2026" \
  -V mainfont="FreeSerif" \
  -V monofont="FreeMono" \
  -V "title:" \
  -V header-includes="\usepackage{amssymb,amsmath}" \
  -V header-includes="\usepackage{silence}\WarningFilter{latex}{Command \underbar has changed}\WarningFilter{latex}{Command \underline has changed}" \
  -V header-includes="\usepackage{sectsty}\sectionfont{\centering}" \
  -V header-includes="\usepackage{float}" \
  -V header-includes="\makeatletter\def\fps@figure{H}\makeatother" \
  --lua-filter=../../../_template/diagram-generator.lua \
  --lua-filter=../../../_template/columns.lua \
  --metadata nocite='@*' \
  --csl=../../../pass-through.csl \
  -V colorlinks=true \
  -V linkcolor=blue

# 7. Clean up
rm manuscript_fixed.md
