# Toy LLM Turn Plan

## Capacity

Last session: ~600-900 lines per turn actual. Doubling to ~1200-1800 lines per turn.

## Turn Plan

### Turn 1 — config.py + data.py + model.py (forward only)

- `examples/toy_llm/config.py` (~30 lines)
- `examples/toy_llm/data.py` (~80 lines)
- `examples/toy_llm/model.py` (~400 lines — init, embed, attention_block, ffn_block, forward, forward_last_logits, parameters, zero_grad — no backward yet)
- `examples/toy_llm/attention_backward.py` (~200 lines — softmax_backward, attention_mix_backward, score_backward, attention_backward)

~710 lines. Comfortable fit.

### Turn 2 — model.py backward + train.py + generate.py

- `examples/toy_llm/model.py` additions (~250 lines — backward_from_output, backward_from_last, forward_with_cache for capturing intermediates)
- `examples/toy_llm/train.py` (~150 lines — compute_loss, train_step, train_epoch, train)
- `examples/toy_llm/generate.py` (~120 lines — generate_ids, generate_text, generate_greedy, generate_top_k)

~520 lines. Room to spare, but backward through attention is tricky logic that benefits from space.

### Turn 3 — verify.py + inspect.py + run.py

- `examples/toy_llm/verify.py` (~300 lines — all 8 verification functions + verify_all)
- `examples/toy_llm/inspect.py` (~150 lines — print_parameters, print_attention_map, print_logits_and_probs, print_gradient_magnitudes, print_loss_trajectory, denominator_report)
- `examples/toy_llm/run.py` (~80 lines — main entry point)

~530 lines.

## Summary

| Turn | Files | Est. Lines |
|---|---|---|
| 1 | config.py, data.py, model.py (forward), attention_backward.py | ~710 |
| 2 | model.py (backward + cache), train.py, generate.py | ~520 |
| 3 | verify.py, inspect.py, run.py | ~530 |
| **Total** | **8 files** | **~1760** |

3 turns for the complete toy LLM.
