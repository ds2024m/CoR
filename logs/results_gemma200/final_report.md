# Emotion Recognition Experiment - Final Report

**Experiment:** results_gemma200
**Start Time:** 2026-02-05 13:51:46.546357
**Duration:** 9:55:27.542059

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
- **gemma**

## Methods Tested
- **direct**: Direct inference with single prompt
- **cot_single**: Chain-of-Thought in single turn
- **cot_multiturn_generic**: Chain-of-Thought in multiple generic turns (SINGLE-AGENT BASELINE, NO specialization)
- **cor**: Chain-of-Responsibility with specialized agents (Face, Body, Context, Synthesizer)
- **cor_ablation_normal**: CoR with normal order using ablation method
- **cor_ablation_without_face**: CoR without Facial Analyzer (Body → Context → Synthesizer)
- **cor_ablation_without_body**: CoR without Body Analyzer (Face → Context → Synthesizer)
- **cor_ablation_without_context**: CoR without Context Analyzer (Face → Body → Synthesizer)

## Results Summary

### Classification Performance
| Model | Method | Accuracy | F1-Macro | F1-Weighted | N Valid |
|-------|--------|----------|----------|-------------|---------|
| gemma | direct | 0.6985 | 0.6952 | 0.6941 | 199/200 |
| gemma | cot_single | 0.6250 | 0.6082 | 0.6124 | 200/200 |
| gemma | cot_multiturn_generic | 0.6150 | 0.5968 | 0.6021 | 200/200 |
| gemma | cor | 0.6500 | 0.6330 | 0.6370 | 200/200 |
| gemma | cor_ablation_normal | 0.6500 | 0.6330 | 0.6370 | 200/200 |
| gemma | cor_ablation_without_face | 0.6400 | 0.6239 | 0.6281 | 200/200 |
| gemma | cor_ablation_without_body | 0.6400 | 0.6272 | 0.6322 | 200/200 |
| gemma | cor_ablation_without_context | 0.6200 | 0.6004 | 0.6073 | 200/200 |

### Specialization Analysis: CoR vs CoT Multi-Turn Generic
This analysis isolates the effect of agent specialization vs just multi-turn reasoning.


**gemma:**
- Agreement Rate: 0.805 (161/200)
- CoR Accuracy: 0.650
- CoT Generic Accuracy: 0.615
- Accuracy Difference (CoR - CoT): 0.035
- Time Ratio (CoR/CoT): 1.09x
- Token Ratio (CoR/CoT): 0.56x

## Files Generated
- `experiment_config.json`
- `results/metrics/classification_metrics.json`
- `results/metrics/comparison_table.csv`
- `results/metrics/specialization_analysis.json`
- `results/metrics/efficiency_metrics.json`
- `final_report.md`
