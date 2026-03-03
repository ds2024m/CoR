# Análise Estatística

Timestamp: 20260302_114700 | Seed: 456


## McNemar: Caption Standard vs Emotional (com correção Bonferroni)

| Configuração | N_A_better | N_B_better | N_total | p-valor | p-corrigido | Significativo |
|---|---|---|---|---|---|---|
| ('bart_mnli', 'blip2', 'emotional_nli') | 9 | 17 | 154 | 0.1686 | 1.0000 | Não |
| ('bart_mnli', 'blip2', 'standard_nli') | 12 | 22 | 154 | 0.1214 | 1.0000 | Não |
| ('bart_mnli', 'llava_next', 'emotional_nli') | 25 | 17 | 200 | 0.2800 | 1.0000 | Não |
| ('bart_mnli', 'llava_next', 'standard_nli') | 31 | 14 | 200 | 0.0161 | 0.3863 | Não |
| ('bart_mnli', 'paligemma2', 'emotional_nli') | 39 | 8 | 199 | 0.0000 | 0.0001 | Sim |
| ('bart_mnli', 'paligemma2', 'standard_nli') | 40 | 12 | 199 | 0.0001 | 0.0031 | Sim |
| ('bart_mnli', 'qwen2_vl', 'emotional_nli') | 21 | 33 | 200 | 0.1337 | 1.0000 | Não |
| ('bart_mnli', 'qwen2_vl', 'standard_nli') | 20 | 35 | 200 | 0.0581 | 1.0000 | Não |
| ('deberta_nli', 'blip2', 'emotional_nli') | 5 | 15 | 154 | 0.0414 | 0.9933 | Não |
| ('deberta_nli', 'blip2', 'standard_nli') | 15 | 16 | 154 | 1.0000 | 1.0000 | Não |
| ('deberta_nli', 'llava_next', 'emotional_nli') | 21 | 23 | 200 | 0.8804 | 1.0000 | Não |
| ('deberta_nli', 'llava_next', 'standard_nli') | 35 | 21 | 200 | 0.0814 | 1.0000 | Não |
| ('deberta_nli', 'paligemma2', 'emotional_nli') | 32 | 20 | 199 | 0.1263 | 1.0000 | Não |
| ('deberta_nli', 'paligemma2', 'standard_nli') | 15 | 12 | 199 | 0.7011 | 1.0000 | Não |
| ('deberta_nli', 'qwen2_vl', 'emotional_nli') | 19 | 33 | 200 | 0.0704 | 1.0000 | Não |
| ('deberta_nli', 'qwen2_vl', 'standard_nli') | 23 | 33 | 200 | 0.2288 | 1.0000 | Não |
| ('roberta_nli', 'blip2', 'emotional_nli') | 9 | 17 | 154 | 0.1686 | 1.0000 | Não |
| ('roberta_nli', 'blip2', 'standard_nli') | 13 | 20 | 154 | 0.2962 | 1.0000 | Não |
| ('roberta_nli', 'llava_next', 'emotional_nli') | 23 | 18 | 200 | 0.5327 | 1.0000 | Não |
| ('roberta_nli', 'llava_next', 'standard_nli') | 19 | 18 | 200 | 1.0000 | 1.0000 | Não |
| ('roberta_nli', 'paligemma2', 'emotional_nli') | 40 | 28 | 199 | 0.1818 | 1.0000 | Não |
| ('roberta_nli', 'paligemma2', 'standard_nli') | 39 | 29 | 199 | 0.2750 | 1.0000 | Não |
| ('roberta_nli', 'qwen2_vl', 'emotional_nli') | 20 | 30 | 200 | 0.2026 | 1.0000 | Não |
| ('roberta_nli', 'qwen2_vl', 'standard_nli') | 13 | 32 | 200 | 0.0066 | 0.1586 | Não |

## McNemar: NLI Template Standard vs Emotional (com correção Bonferroni)

| Configuração | N_A_better | N_B_better | N_total | p-valor | p-corrigido | Significativo |
|---|---|---|---|---|---|---|
| ('bart_mnli', 'blip2', 'emotional') | 33 | 49 | 338 | 0.0970 | 1.0000 | Não |
| ('bart_mnli', 'blip2', 'standard') | 13 | 23 | 154 | 0.1325 | 1.0000 | Não |
| ('bart_mnli', 'llava_next', 'emotional') | 8 | 11 | 200 | 0.6476 | 1.0000 | Não |
| ('bart_mnli', 'llava_next', 'standard') | 12 | 6 | 200 | 0.2379 | 1.0000 | Não |
| ('bart_mnli', 'paligemma2', 'standard') | 9 | 12 | 199 | 0.6636 | 1.0000 | Não |
| ('bart_mnli', 'qwen2_vl', 'emotional') | 8 | 5 | 200 | 0.5811 | 1.0000 | Não |
| ('bart_mnli', 'qwen2_vl', 'standard') | 7 | 7 | 200 | 1.0000 | 1.0000 | Não |
| ('deberta_nli', 'blip2', 'emotional') | 22 | 32 | 338 | 0.2203 | 1.0000 | Não |
| ('deberta_nli', 'blip2', 'standard') | 11 | 12 | 154 | 1.0000 | 1.0000 | Não |
| ('deberta_nli', 'llava_next', 'emotional') | 4 | 20 | 200 | 0.0015 | 0.0340 | Sim |
| ('deberta_nli', 'llava_next', 'standard') | 14 | 14 | 200 | 1.0000 | 1.0000 | Não |
| ('deberta_nli', 'paligemma2', 'emotional') | 1 | 0 | 203 | 1.0000 | 1.0000 | Não |
| ('deberta_nli', 'paligemma2', 'standard') | 11 | 19 | 199 | 0.2005 | 1.0000 | Não |
| ('deberta_nli', 'qwen2_vl', 'emotional') | 8 | 19 | 200 | 0.0522 | 1.0000 | Não |
| ('deberta_nli', 'qwen2_vl', 'standard') | 19 | 26 | 200 | 0.3713 | 1.0000 | Não |
| ('roberta_nli', 'blip2', 'emotional') | 15 | 25 | 338 | 0.1539 | 1.0000 | Não |
| ('roberta_nli', 'blip2', 'standard') | 9 | 10 | 154 | 1.0000 | 1.0000 | Não |
| ('roberta_nli', 'llava_next', 'emotional') | 4 | 2 | 200 | 0.6875 | 1.0000 | Não |
| ('roberta_nli', 'llava_next', 'standard') | 6 | 8 | 200 | 0.7905 | 1.0000 | Não |
| ('roberta_nli', 'paligemma2', 'standard') | 7 | 9 | 199 | 0.8036 | 1.0000 | Não |
| ('roberta_nli', 'qwen2_vl', 'emotional') | 10 | 11 | 200 | 1.0000 | 1.0000 | Não |
| ('roberta_nli', 'qwen2_vl', 'standard') | 6 | 16 | 200 | 0.0525 | 1.0000 | Não |