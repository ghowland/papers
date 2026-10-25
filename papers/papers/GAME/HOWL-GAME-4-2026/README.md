# Op Cost Analysis of Player-Facing Tool Selection Interfaces in Simulation Games

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

No standard unit exists for measuring the cost of player actions in game user interfaces. Design discussions rely on subjective preference, playtester sentiment, or A/B testing without a shared unit of measurement. This paper applies the op — the universal unit of information under action, defined in HOWL-INFO-14-2026 — to the specific domain of tool selection interfaces in simulation games. The op counts every discrete cognitive and physical action a player must perform to complete a task. Six domain-specific op categories are defined (look-at, read, scan, hover, move, click), each with fixed counting rules calibrated to game UI patterns. A library of compound actions provides pre-computed op costs for common UI interactions. Twelve benchmark tasks provide a standardized measurement surface for cross-game comparison. Measurements are taken across six commercial titles in two genres: colony simulation (Oxygen Not Included, Dwarf Fortress Steam Edition, RimWorld) and grand strategy (Europa Universalis IV, Crusader Kings III, Total War: Warhammer III). Results show that text-labeled hierarchical menus with keyboard acceleration produce the lowest combined new-player and expert interaction cost. Icon-only hierarchies produce the lowest expert cost but the highest new-player cost. Persistent icon grids produce the lowest within-category switching cost but the highest regression vulnerability. The framework makes these tradeoffs quantifiable, reproducible, and falsifiable.

---

## Howland Archive Context

This publication is part of the **Howland Archive**, a collection of research spanning information theory, computational architecture, physics, and philosophy. All work unified by axiomatic methodology: derive complex systems from minimal constraint sets with zero free parameters.

### Series Position

**Prerequisites:** None (foundation paper)

---

**Methodology Principles:**

1. **Maximum Constraints:** Start with minimal axioms
2. **Necessary Derivation:** All results follow logically from axioms
3. **Extreme Falsifiability:** Clear failure conditions
4. **Working Implementations:** Build it, don't just theorize
5. **Measured Results:** Empirical validation where possible

---

## Repository Contents

```
zenodo_package/
├── manuscript.md              # Main paper
├── README.md                  # This file
└── zenodo.json                # Zenodo metadata
```


---

## Citation
If you use this work in a pedagogical or research context, please cite:

```bibtex
@article{ HOWL-GAME-4-2026,
  title={ Op Cost Analysis of Player-Facing Tool Selection Interfaces in Simulation Games },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.23647485},
  url = {https://zenodo.org/record/23647485},
  note={Howland Archive: HOWL-GAME-4-2026. Prerequisites: None (foundation paper) }
}
```
---
