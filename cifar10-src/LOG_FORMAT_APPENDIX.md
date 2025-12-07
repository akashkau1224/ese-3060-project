# Appendix: Log File Format Explanation

## Log File Structure

Each training log file (`airbench94_log_{agc|default}_{lr}.txt`) contains three main sections:

### 1. Configuration Section
```
AGC Used: True/False
AGC Clip Factor: 10.0 (if AGC is enabled)
Learning Rate (per 1024 examples): 11.5
```
- Indicates whether Adaptive Gradient Clipping was used
- Shows the learning rate used for training

### 2. Summary Results
```
Mean Accuracy: 0.9249
Std Accuracy: 0.0077
Time Mean: 4.2437 seconds
Time Std: 2.3105 seconds
```
- **Mean Accuracy**: Average TTA validation accuracy across 25 runs
- **Std Accuracy**: Standard deviation of accuracy across runs
- **Time Mean**: Average total training time per run
- **Time Std**: Standard deviation of training times

### 3. Detailed Training Logs

Each row represents one epoch from one run:
```
|   run  | epoch | train_loss | train_acc | val_acc | tta_val_acc | total_time_seconds |
```

**Column Descriptions:**
- **run**: Run number (0-24, one per independent training)
- **epoch**: Epoch number (0-8) or 'eval' for final TTA evaluation
- **train_loss**: Training loss on the last batch of the epoch
- **train_acc**: Training accuracy on the last batch
- **val_acc**: Validation accuracy (without TTA)
- **tta_val_acc**: Validation accuracy with Test-Time Augmentation (only shown for 'eval' rows)
- **total_time_seconds**: Cumulative training time from start of run

**Notes:**
- Runs are separated by horizontal lines (`---`)
- The 'eval' row appears at the end of each run with TTA results
- Training may stop early if validation accuracy reaches 90%
