# Logs
Trials for data models are recorded here.

### Data
718887 battles; Absolute trophy diff < 1000; Trophy data scaled;

### ANN
- Trial 1:
    - Hidden Layers:
        - 1: `neurons=144`, `activation="relu"`, `kernel_regularizer=L1(0.0001)`
        - 2: `neurons=144`, `activation="relu"`, `kernel_regularizer=L1(0.0001)`
        - 3: (Output): `activation="sigmoid"`, `kernel_regularizer=L1(0.0001)`
    - Optimizer: `SGD`, `learning_rate=0.0025`, `momentum=0.95`, `nesterov=True`
    - Training: `batch_size=64`
    - **Results: Stopped at `31/512` epochs; Validation Accuracy is `0.583`**
- Trial 2:
    - Hidden Layers
        - 1: `neurons=144`, `activation="relu"`, `kernel_regularizer=L1(0.0001)`, `kernel_initializer="he_uniform"`
        - 2: `neurons=144`, `activation="relu"`, `kernel_regularizer=L1(0.0001)`, `kernel_initializer="he_uniform"`
        - 3: (Output): `activation="sigmoid"`, `kernel_regularizer=L1(0.0001)`
    - Optimizer: `Adam`, `learning_rate=0.00025`
    - Training: `batch_size=128`
    - **Results: Stopped at `85/512` epochs' Validation Accuracy is `0.592`**

