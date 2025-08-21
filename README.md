
# Hyprfindr

**Hyprfindr** is a small Python utility that lets you **search and display your Hyprland keybinds** via the terminal or as desktop notifications.
It parses your `~/.config/hypr/hyprland.conf`, resolves `$variables`, and formats the keybinds for quick lookup.

<img width="2240" height="1400" alt="2025-08-21-202243_hyprshot" src="https://github.com/user-attachments/assets/dc718ae1-60eb-4435-85fd-7b7b76f6cc0c" />

[![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square\&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

---

## 🚀 Getting Started

### 📦 Install via AUR

Hyprfindr is available on the **Arch User Repository (AUR)**. If you’re using an AUR helper like `yay` or `paru`:

```bash
yay -S hyprfindr
```

This will fetch the PKGBUILD, build the package, and install it for you.

---

### 🛠 Build from source (custom install)

If you want to build manually or use the latest Git version:

1. **Clone the repository**

```bash
git clone https://github.com/fwtwoo/hyprfindr.git
cd hyprfindr
```

2. **Install dependencies**

```bash
sudo pacman -S python zenity
```

3. **Run directly**

```bash
python hyprfindr.py firefox
```

4. *(Optional)* Install to `/usr/local/bin` for global access:

```bash
sudo install -Dm755 hyprfindr.py /usr/local/bin/hyprfindr
```

### ⚙️ Usage

```
usage: hyprfindr [-h] [--version] NAME

Search and display Hyprland keybinds via CLI and your notification daemon.

positional arguments:
  NAME        Search keybinds by application/command name, or by a key within a key combination.

options:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```
---

### ✅ Requirements

* Python 3
* `zenity` (for desktop notifications)
* Hyprland (for keybinds)

---

### 📄 License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.

---
