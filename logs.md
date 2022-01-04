# Logs
Trials for data models are recorded here.

### Data
718887 battles; Absolute trophy diff < 1000; Trophy data scaled;

### MLP
- Trial 1:
    - Layers: 2x144
    - Optimizer: `SGD`, `lr=0.0025`, `momentum=0.95`, `nesterov=True`
    - Training: `batch_size=64`
    - **Results: Stopped at `31/512` epochs; Validation Accuracy is `0.583`**
