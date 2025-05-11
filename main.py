import os
import ctypes
import tkinter as tk
import psutil
import time
import threading
from pynvml import (
    nvmlInit,
    nvmlDeviceGetHandleByIndex,
    nvmlDeviceGetPowerUsage,
    nvmlShutdown,
)

# Manually load NVIDIA's NVML library
try:
    ctypes.CDLL(r"C:\Windows\System32\nvml.dll")
    nvmlInit()
    gpu_handle = nvmlDeviceGetHandleByIndex(0)  # First GPU
    nvml_available = True
except Exception as e:
    print(f"[Warning] NVML not available: {e}")
    nvml_available = False

def get_gpu_power():
    if not nvml_available:
        return 0.0
    try:
        power_mw = nvmlDeviceGetPowerUsage(gpu_handle)
        return power_mw / 1000  # Convert milliwatts to watts
    except:
        return 0.0

def get_cpu_power_estimate():
    # Estimate CPU power based on usage percentage
    cpu_usage = psutil.cpu_percent(interval=0.1)
    base_power = 15  # Typical idle CPU power
    max_power = 65   # Typical max CPU power
    return base_power + (cpu_usage / 100) * (max_power - base_power)

# --- GUI Overlay Setup ---
root = tk.Tk()
root.overrideredirect(True)             # Remove window border
root.attributes("-topmost", True)       # Always on top
root.attributes("-alpha", 0.8)          # Transparency
root.configure(bg='black')              # Background color

label = tk.Label(
    root,
    text="Loading...",
    fg='lime',
    bg='black',
    font=("Consolas", 14)
)
label.pack()
root.geometry("+20+20")  # Position on screen

def update_overlay():
    while True:
        cpu_watts = get_cpu_power_estimate()
        gpu_watts = get_gpu_power()
        total = cpu_watts + gpu_watts
        text = f"CPU: {cpu_watts:.1f}W\nGPU: {gpu_watts:.1f}W\nTotal: {total:.1f}W"
        label.config(text=text)
        time.sleep(1)

# Background thread for updating values
threading.Thread(target=update_overlay, daemon=True).start()

# Start GUI
root.mainloop()

# Clean up (only reached if GUI is closed)
if nvml_available:
    nvmlShutdown()
