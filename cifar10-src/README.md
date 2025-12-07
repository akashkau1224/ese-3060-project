# CIFAR-10 Training with Airbench94

## Files

- **`airbench94.py`**: Main training script. Trains ResNet on CIFAR-10 for 25 runs with optional AGC and custom learning rates.
- **`lr_sweep_analysis.ipynb`**: Jupyter notebook for analyzing learning rate sweep results and generating comparison visualizations.
- **`logs/`**: Directory containing training log files (auto-generated).

## Usage

### Basic Training
```bash
python airbench94.py
```

### With Adaptive Gradient Clipping
```bash
python airbench94.py --use_agc
```

### Custom Learning Rate
```bash
python airbench94.py --lr 23.0
```

### Combined Options
```bash
python airbench94.py --use_agc --lr 5.75
```

## Command-Line Arguments

- `--use_agc`: Enable Adaptive Gradient Clipping (default: False)
- `--agc_clip_factor FLOAT`: AGC clip factor (default: 10.0)
- `--lr FLOAT`: Learning rate per 1024 examples (default: 11.5)

## Output

- **Console**: Real-time training metrics table
- **Log Files**: Saved to `logs/` directory with format `airbench94_log_{agc|default}_{lr}.txt`

Each log file contains:
1. Configuration (AGC usage, learning rate)
2. Summary statistics (mean/std accuracy and time across 25 runs)
3. Detailed per-epoch training logs for all runs

## Requirements

- PyTorch, torchvision
- CUDA-capable GPU (recommended)
- pandas, matplotlib, jupyter (for analysis notebook)
