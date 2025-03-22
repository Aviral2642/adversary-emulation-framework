# Adversary Emulation Framework

**Adversary Emulation Framework (AEF)** is a fully functional red team toolkit designed to simulate real-world cyber threat behavior using the MITRE ATT&CK framework. This tool enables security professionals to evaluate and improve the resilience of their infrastructure by emulating threat actor tactics, techniques, and procedures (TTPs) in a controlled environment.

---

## 🚀 Features

- 🎯 **Realistic Attack Simulation**  
  Execute real emulation playbooks based on APT groups like APT29, FIN7, and more.

- 🧠 **Modular Architecture**  
  Easily extend and plug in new TTPs, playbooks, or custom logic through Python modules.

- 📖 **MITRE ATT&CK Mapped**  
  All playbooks and modules are mapped to MITRE ATT&CK tactics and techniques.

- ⚙️ **Real and Safe Modes**  
  Run modules in `--mode safe` for simulation or `--mode real` to perform real (but contained) actions.

- 📝 **Detailed Logging**  
  Track executions, results, and any failures via structured logging for audit and analysis.

---

## 📂 Project Structure

```
adversary-emulation-framework/
│
├── core/                   # Core engine: executor, scheduler, logger
├── modules/                # Attack modules (e.g., recon, privilege escalation, etc.)
├── playbooks/              # YAML playbooks for threat actor simulations
├── config/                 # Configuration files (e.g., config.yaml)
├── docs/                   # Documentation and usage guidelines
├── main.py                 # Entry point to the framework
├── requirements.txt        # Python dependencies
└── install.sh              # Setup and environment installation script
```

---

## 🛠️ Installation

```bash
git clone https://github.com/Aviral2642/adversary-emulation-framework.git
cd adversary-emulation-framework
chmod +x install.sh
./install.sh
```

---

## 🧪 Usage

Run a specific threat emulation playbook in real or safe mode:

```bash
python main.py --playbook playbooks/apt29.yml --mode real
```

Options:
- `--playbook`: Path to the YAML playbook (e.g., APT29, FIN7)
- `--mode`: `real` to execute real actions, or `safe` to simulate

---

## 📘 Example Playbooks

| Playbook | Description |
|----------|-------------|
| `apt29.yml` | Emulates the APT29 threat group using MITRE-mapped techniques |
| `fin7.yml`  | Simulates FIN7 behavior with persistence, lateral movement, and more |
| `custom-threat.yml` | Create your own attack chain with custom modules |

---

## 📚 Documentation

Check out the [docs/](docs/) folder for:

- `README.md`: Overview and setup
- `usage.md`: CLI options and use cases
- `ATTACK-matrix.md`: List of implemented MITRE ATT&CK techniques

---

## 🧩 Contributing

We welcome PRs and suggestions! Please open an issue or a discussion before submitting major changes.

---

## ⚠️ Disclaimer

This tool is intended **for educational and authorized red team use only**. Do not use this framework against systems you do not own or have explicit permission to test.

---

## 📄 License

MIT License © 2025 [Aviral Srivastava](https://github.com/Aviral2642)
