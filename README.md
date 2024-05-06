# Uncovering the Latency Divide: Exploring the Performance of Embedding Model on GPU vs CPU with ONNX


##### Embedding Model : BGE-large-en-1.5
##### VM used for this experiment : g4dn.xlarge (AWS EC2)

| Tokens Length |  GPU (sec) | CPU (sec) | ONNX cpu (sec) | ONNX GPU (sec) |
| --- | --- | --- | --- | --- |
| 1134 | 0.25 | 1.62 | 0.57 | 0.33 |
| 362 | 0.07 | 1.16 | 0.35 | 0.02 |
| 125 | 0.03 | 0.51 | 0.23 | 0.01 |
| 10 | 0.01 | 0.2 | 0.11 | 0.01 |
| 383 | 0.07 | 1.21 | 0.52 | 0.03 |
| 278 | 0.05 | 0.9 | 0.34 | 0.02 |
| 208 | 0.04 | 0.7 | 0.23 | 0.02 |
| 10 | 0.01 | 0.2 | 0.11 | 0.009 |
| 408 | 0.07 | 1.25 | 0.52 | 0.03 |
| 367 | 0.07 | 1.15 | 0.35 | 0.02 |
| 235 | 0.04 | 0.78 | 0.23 | 0.02 |
| 10 | 0.01 | 0.2 | 0.11 | 0.02 |
| 417 | 0.09 | 1.39 | 0.52 | 0.03 |
| 10 | 0.01 | 0.2 | 0.11 | 0.009 |
| 388 | 0.07 | 1.2 | 0.52 | 0.02 |

![Embedding Experiment](/img/embedding_chart.png)
