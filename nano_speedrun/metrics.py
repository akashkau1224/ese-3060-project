import re

def extract_metrics(filename):
    epochs = []
    val_losses = []
    train_times = []

    # Regex pattern to match the structure
    pattern = re.compile(
        r"step:(\d+)/\d+\s+val_loss:([\d.]+)\s+train_time:(\d+)ms"
    )

    with open(filename, "r") as f:
        for line in f:
            if "0 val_loss" in line:  # filter lines you care about
                match = pattern.search(line)
                if match:
                    epoch = int(match.group(1))
                    val_loss = float(match.group(2))
                    train_time = int(match.group(3))

                    epochs.append(epoch)
                    val_losses.append(val_loss)
                    train_times.append(train_time)

    return epochs, val_losses, train_times


epochs, val_losses_3_5_1, train_times_3_5_1 = extract_metrics("logs/individual_final_runs/3_5_final_run_first.txt")
print(f"Epoch List: {epochs}\n")
print(f"3.5 First Run:  val losses - {val_losses_3_5_1}, train times - {train_times_3_5_1}\n")

_, val_losses_3_5_2, train_times_3_5_2 = extract_metrics("logs/individual_final_runs/3_5_final_run_second.txt")
print(f"3.5 Second Run: val losses - {val_losses_3_5_2}, train times - {train_times_3_5_2}\n")

_, val_losses_3_5_3, train_times_3_5_3 = extract_metrics("logs/individual_final_runs/3_5_final_run_third.txt")
print(f"3.5 Third Run:  val losses - {val_losses_3_5_3}, train times - {train_times_3_5_3}\n")

_, val_losses_4_0_1, train_times_4_0_1 = extract_metrics("logs/individual_final_runs/4_0_final_run_first.txt")
print(f"4.0 First Run:  val losses - {val_losses_4_0_1}, train times - {train_times_4_0_1}\n")

_, val_losses_4_0_2, train_times_4_0_2 = extract_metrics("logs/individual_final_runs/4_0_final_run_second.txt")
print(f"4.0 Second Run: val losses - {val_losses_4_0_2}, train times - {train_times_4_0_2}\n")

_, val_losses_4_0_3, train_times_4_0_3 = extract_metrics("logs/individual_final_runs/4_0_final_run_third.txt")
print(f"4.0 Third Run:  val losses - {val_losses_4_0_3}, train times - {train_times_4_0_3}\n")
