# NanoGPT Speedrun Training
### FOR MORE DETAIL ABOUT THE LOGS GO TO THE LOG_FORMAT_APPENDIX.MD
## Files

- **`train_gpt_final.py`**: Main training script for GPT-2 model with Muon optimizer. Trains on FineWeb dataset with distributed data parallel training. Has extra element in GPTConfig to change the expansion factor for the particular run
- **`train_gpt.py`**: Base training script.
- **`train_gpt_small.py`**: Smaller variant of the training script using less iterations and a subset of the training data.
- **`train_gpt_longer.py`**: Extended training script with additional iterations. Additional logging included at a more frequent rate. Includes the function calculation at regular periods on the validation loss during training.
- **`train_gpt_function.py`**: Testing with a custon function to factor in training time and validation loss into one metric.
- **`train_gpt_initial.py`**: Initial version of the training script trained using the smaller subset of data.
- **`metrics.py`**: Utility script for extracting and analyzing metrics from log files.
- **`logs/`**: Directory containing training log files (auto-generated from scripts).

## Usage

### Basic Training (start in root then cd to nano_speedrun when running the function)
(It must be run from inside nano_speedrun because of how the paths are set up)

```bash
pip install -r requirements.txt
python cached_fineweb10B.py 9
cd nano_speedrun
torchrun --nproc_per_node=8 train_gpt_final.py
```

### Model Configuration

Edit the `GPTConfig` dataclass to modify model architecture:
- `expansion_factor`: MLP expansion factor (set to 3.5 but can make this 4.0 to see the baseline)
- 
## Output

- **Console**: Real-time training metrics (step, train_loss, val_loss, train_time)
- **Log Files**: Saved to `logs/` directory with format `{uuid}.txt`

Each log file may contain (FOR MORE DETAIL ABOUT THE LOGS GO TO THE LOG_FORMAT_APPENDIX.MD):
1. Full training script code (for reproducibility)
2. Hardware/software environment information (PyTorch version, CUDA version, nvidia-smi output)
3. Training metrics for each step:
   - Training loss
   - Validation loss (periodically)
   - Training time (cumulative and per-step average)
