# Agregação Multi-Seed

Seeds: [42, 123, 456]

| classifier_name   | caption_model   | prompt_type   | nli_template_type   |   acc_mean |   acc_std |   f1_mean |   f1_std |   mcc_mean |   mcc_std |   n_seeds |
|:------------------|:----------------|:--------------|:--------------------|-----------:|----------:|----------:|---------:|-----------:|----------:|----------:|
| bart_mnli         | blip2           | emotional     | emotional_nli       |   0.45122  |         0 | 0.438328  |        0 |  0.353347  |         0 |         3 |
| bart_mnli         | llava_next      | standard      | standard_nli        |   0.44     |         0 | 0.407544  |        0 |  0.349371  |         0 |         3 |
| bart_mnli         | qwen2_vl        | emotional     | standard_nli        |   0.43     |         0 | 0.410271  |        0 |  0.331024  |         0 |         3 |
| bart_mnli         | blip2           | standard      | emotional_nli       |   0.409091 |         0 | 0.400461  |        0 |  0.31933   |         0 |         3 |
| bart_mnli         | llava_next      | standard      | emotional_nli       |   0.41     |         0 | 0.377491  |        0 |  0.314145  |         0 |         3 |
| bart_mnli         | qwen2_vl        | emotional     | emotional_nli       |   0.415    |         0 | 0.406092  |        0 |  0.313261  |         0 |         3 |
| bart_mnli         | blip2           | emotional     | standard_nli        |   0.402439 |         0 | 0.403388  |        0 |  0.301143  |         0 |         3 |
| deberta_nli       | qwen2_vl        | emotional     | emotional_nli       |   0.395    |         0 | 0.378957  |        0 |  0.295119  |         0 |         3 |
| deberta_nli       | llava_next      | emotional     | emotional_nli       |   0.395    |         0 | 0.351393  |        0 |  0.294142  |         0 |         3 |
| deberta_nli       | llava_next      | standard      | standard_nli        |   0.385    |         0 | 0.360419  |        0 |  0.283635  |         0 |         3 |
| deberta_nli       | llava_next      | standard      | emotional_nli       |   0.385    |         0 | 0.340784  |        0 |  0.279879  |         0 |         3 |
| deberta_nli       | blip2           | emotional     | emotional_nli       |   0.373984 |         0 | 0.345556  |        0 |  0.271632  |         0 |         3 |
| roberta_nli       | qwen2_vl        | emotional     | emotional_nli       |   0.375    |         0 | 0.357038  |        0 |  0.271488  |         0 |         3 |
| roberta_nli       | qwen2_vl        | emotional     | standard_nli        |   0.37     |         0 | 0.344722  |        0 |  0.267697  |         0 |         3 |
| bart_mnli         | qwen2_vl        | standard      | emotional_nli       |   0.355    |         0 | 0.346434  |        0 |  0.265009  |         0 |         3 |
| bart_mnli         | llava_next      | emotional     | emotional_nli       |   0.37     |         0 | 0.341732  |        0 |  0.263412  |         0 |         3 |
| roberta_nli       | blip2           | emotional     | emotional_nli       |   0.373984 |         0 | 0.325885  |        0 |  0.260604  |         0 |         3 |
| bart_mnli         | qwen2_vl        | standard      | standard_nli        |   0.355    |         0 | 0.342532  |        0 |  0.256171  |         0 |         3 |
| roberta_nli       | llava_next      | standard      | emotional_nli       |   0.36     |         0 | 0.310015  |        0 |  0.255341  |         0 |         3 |
| roberta_nli       | llava_next      | standard      | standard_nli        |   0.35     |         0 | 0.301431  |        0 |  0.24561   |         0 |         3 |
| bart_mnli         | llava_next      | emotional     | standard_nli        |   0.355    |         0 | 0.322945  |        0 |  0.243255  |         0 |         3 |
| roberta_nli       | llava_next      | emotional     | standard_nli        |   0.345    |         0 | 0.301787  |        0 |  0.23763   |         0 |         3 |
| bart_mnli         | blip2           | standard      | standard_nli        |   0.344156 |         0 | 0.3503    |        0 |  0.232965  |         0 |         3 |
| deberta_nli       | blip2           | emotional     | standard_nli        |   0.333333 |         0 | 0.338171  |        0 |  0.232136  |         0 |         3 |
| deberta_nli       | qwen2_vl        | emotional     | standard_nli        |   0.34     |         0 | 0.329366  |        0 |  0.22901   |         0 |         3 |
| roberta_nli       | blip2           | emotional     | standard_nli        |   0.349593 |         0 | 0.316839  |        0 |  0.22833   |         0 |         3 |
| bart_mnli         | paligemma2      | standard      | emotional_nli       |   0.316583 |         0 | 0.268572  |        0 |  0.224722  |         0 |         3 |
| roberta_nli       | llava_next      | emotional     | emotional_nli       |   0.335    |         0 | 0.293123  |        0 |  0.219525  |         0 |         3 |
| roberta_nli       | qwen2_vl        | standard      | emotional_nli       |   0.325    |         0 | 0.291643  |        0 |  0.217481  |         0 |         3 |
| deberta_nli       | qwen2_vl        | standard      | emotional_nli       |   0.325    |         0 | 0.288112  |        0 |  0.213235  |         0 |         3 |
| deberta_nli       | blip2           | standard      | emotional_nli       |   0.311688 |         0 | 0.296152  |        0 |  0.210042  |         0 |         3 |
| deberta_nli       | blip2           | standard      | standard_nli        |   0.305195 |         0 | 0.31236   |        0 |  0.199064  |         0 |         3 |
| deberta_nli       | llava_next      | emotional     | standard_nli        |   0.315    |         0 | 0.288126  |        0 |  0.194098  |         0 |         3 |
| bart_mnli         | paligemma2      | standard      | standard_nli        |   0.301508 |         0 | 0.274478  |        0 |  0.193784  |         0 |         3 |
| roberta_nli       | blip2           | standard      | emotional_nli       |   0.285714 |         0 | 0.251929  |        0 |  0.174612  |         0 |         3 |
| deberta_nli       | qwen2_vl        | standard      | standard_nli        |   0.29     |         0 | 0.256682  |        0 |  0.165394  |         0 |         3 |
| roberta_nli       | blip2           | standard      | standard_nli        |   0.279221 |         0 | 0.264062  |        0 |  0.159626  |         0 |         3 |
| roberta_nli       | qwen2_vl        | standard      | standard_nli        |   0.275    |         0 | 0.217905  |        0 |  0.155609  |         0 |         3 |
| deberta_nli       | paligemma2      | standard      | emotional_nli       |   0.221106 |         0 | 0.146359  |        0 |  0.0792224 |         0 |         3 |
| roberta_nli       | paligemma2      | standard      | emotional_nli       |   0.221106 |         0 | 0.143955  |        0 |  0.0780539 |         0 |         3 |
| roberta_nli       | paligemma2      | standard      | standard_nli        |   0.211055 |         0 | 0.127571  |        0 |  0.0661662 |         0 |         3 |
| deberta_nli       | paligemma2      | standard      | standard_nli        |   0.180905 |         0 | 0.128703  |        0 |  0.0256649 |         0 |         3 |
| deberta_nli       | paligemma2      | emotional     | standard_nli        |   0.164179 |         0 | 0.0470085 |        0 |  0         |         0 |         3 |
| bart_mnli         | paligemma2      | emotional     | standard_nli        |   0.159204 |         0 | 0.0457797 |        0 | -0.0547735 |         0 |         3 |
| roberta_nli       | paligemma2      | emotional     | emotional_nli       |   0.159204 |         0 | 0.0457797 |        0 | -0.055046  |         0 |         3 |
| roberta_nli       | paligemma2      | emotional     | standard_nli        |   0.159204 |         0 | 0.0457797 |        0 | -0.055046  |         0 |         3 |
| bart_mnli         | paligemma2      | emotional     | emotional_nli       |   0.159204 |         0 | 0.0457797 |        0 | -0.055046  |         0 |         3 |
| deberta_nli       | paligemma2      | emotional     | emotional_nli       |   0.159204 |         0 | 0.0457797 |        0 | -0.055046  |         0 |         3 |