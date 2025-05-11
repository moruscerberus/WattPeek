# ⚡ WattPeek – CPU & GPU Power Usage (Windows + Linux)

A lightweight Python app that displays a transparent, real-time overlay showing your system’s **CPU power (estimated)** and **NVIDIA GPU power (actual via NVML)**.

Works on **Windows** and **Linux** using `psutil`, `tkinter`, and `pynvml`.

---

## 🔧 Features

- ✅ Real-time **CPU power estimation**
- ✅ Accurate **NVIDIA GPU power** (via NVML)
- ✅ Transparent always-on-top overlay (using `tkinter`)
- ✅ Cross-platform: **Windows & Linux**

---

## 🚀 Setup Instructions

### 🖥️ Windows

1. **Install Python 3.8+**  
   👉 [Download Python](https://www.python.org/downloads/)

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment (Windows)**
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ensure NVIDIA GPU drivers are installed**

6. **Run the app**
   ```bash
   python main.py
   ```

---

### 🐧 Linux

1. **Install Python 3 and Tkinter**

   **Debian/Ubuntu**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk
   ```

   **Arch Linux**
   ```bash
   sudo pacman -S python tk
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment (Linux)**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install NVIDIA drivers (if using an NVIDIA GPU)**
   ```bash
   sudo apt install nvidia-driver-535
   ```

   Or verify installation with:
   ```bash
   nvidia-smi
   ```

6. **Run the app**
   ```bash
   python3 main.py
   ```

---

## 📝 Notes

- If no NVIDIA GPU is detected or NVML is unavailable, the overlay will still run and display `GPU: 0.0W`.
- CPU power is **estimated based on CPU load**, not measured directly.
- Native support for AMD GPUs and actual CPU power readings (via RAPL) is planned for future versions.

---

## 📦 Requirements

Contents of `requirements.txt`:

```
psutil>=5.9.0
nvidia-ml-py3>=7.352.0
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🛠️ License

MIT – Use, modify, and share freely.
