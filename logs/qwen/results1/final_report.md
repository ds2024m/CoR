# Emotion Recognition Experiment - Final Report

**Experiment ID:** 1experimentoadicionalv13_20260203_152518
**Start Time:** 2026-02-03 15:25:18.093692
**Duration:** 0:52:58.814941

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
- **direct**: Direct inference with single prompt
- **cot_single**: Chain-of-Thought in single turn
- **cot_multiturn_generic**: Chain-of-Thought in multiple generic turns (SINGLE-AGENT BASELINE, NO specialization)
- **cor**: Chain-of-Responsibility with specialized agents (Face, Body, Context, Synthesizer)
- **cor_ablation_without_face**: CoR without Face Analyzer (Body → Context → Synthesizer)

## Results Summary

### Classification Performance
| Model | Method | Accuracy | F1-Macro | F1-Weighted | N Valid |
|-------|--------|----------|----------|-------------|---------|
| qwen | direct | 0.5549 | 0.4318 | 0.4786 | 164/200 |
| qwen | cot_single | 0.5260 | 0.4297 | 0.4556 | 173/200 |
| qwen | cot_multiturn_generic | 0.2550 | 0.1730 | 0.1804 | 200/200 |
| qwen | cor | 0.5650 | 0.4881 | 0.5065 | 200/200 |
| qwen | cor_ablation_without_face | 0.5500 | 0.5015 | 0.5113 | 200/200 |

### Specialization Analysis: CoR vs CoT Multi-Turn Generic
This analysis isolates the effect of **agent specialization** vs **just multi-turn reasoning**.


**qwen:**
- Agreement Rate: 0.410 (82/200)
- CoR Accuracy: 0.565
- CoT Generic Accuracy: 0.255
- Accuracy Difference (CoR - CoT): 0.310
- Specialization Benefit: POSITIVE
- Time Ratio (CoR/CoT): 1.44x
- Token Ratio (CoR/CoT): 0.63x

## Files Generated
- `experiment_config.json`
- `results/metrics/classification_metrics.json`
- `results/metrics/comparison_table.csv`
- `results/metrics/specialization_analysis.json`
- `results/metrics/efficiency_metrics.json`
- `final_report.md`
