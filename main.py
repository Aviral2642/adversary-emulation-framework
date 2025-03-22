import argparse
from core.scheduler import Scheduler
from core.logger import setup_logger
import yaml

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="Adversary Emulation Framework")
    parser.add_argument("--playbook", required=True, help="Path to playbook YAML file")
    parser.add_argument("--mode", choices=["real"], required=True, help="Execution mode")
    args = parser.parse_args()

    setup_logger()
    config = load_config()

    scheduler = Scheduler(args.playbook, args.mode, config)
    scheduler.run()

if __name__ == "__main__":
    main()