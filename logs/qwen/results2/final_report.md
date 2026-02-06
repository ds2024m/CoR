# Emotion Recognition Experiment - Final Report

**Experiment ID:** 1experimentoadicionalv13_20260203_174356
**Start Time:** 2026-02-03 17:43:56.941998
**Duration:** 1:28:35.014663

## Dataset Summary
- **Total Samples:** 200
- **Emotion Distribution:**
  - neutral: 37 samples (18.5%)
  - fear: 28 samples (14.0%)
  - sadness: 30 samples (15.0%)
  - joy: 37 samples (18.5%)
  - anger: 39 samples (19.5%)
  - surprise: 29 samples (14.5%)

## Models Tested
- **qwen**

## Methods Tested
- **cor**: Chain-of-Responsibility with specialized agents (Face, Body, Context, Synthesizer)
- **cor_ablation_normal**: CoR with normal order using ablation method
- **cor_ablation_without_face**: CoR without Face Analyzer (Body → Context → Synthesizer)
- **cor_ablation_without_body**: CoR without Body Analyzer (Face → Context → Synthesizer)
- **cor_ablation_without_context**: CoR without Context Analyzer (Face → Body → Synthesizer)

## Results Summary

### Classification Performance
| Model | Method | Accuracy | F1-Macro | F1-Weighted | N Valid |
|-------|--------|----------|----------|-------------|---------|
| qwen | cor | 0.5650 | 0.4881 | 0.5065 | 200/200 |
| qwen | cor_ablation_normal | 0.5650 | 0.4881 | 0.5065 | 200/200 |
| qwen | cor_ablation_without_face | 0.5500 | 0.5015 | 0.5113 | 200/200 |
| qwen | cor_ablation_without_body | 0.5550 | 0.4979 | 0.5094 | 200/200 |
| qwen | cor_ablation_without_context | 0.5050 | 0.4299 | 0.4495 | 200/200 |

## Files Generated
- `experiment_config.json`
- `results/metrics/classification_metrics.json`
- `results/metrics/comparison_table.csv`
- `results/metrics/efficiency_metrics.json`
- `final_report.md`
