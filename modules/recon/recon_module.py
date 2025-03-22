import subprocess

def run(mode, config):
    if mode == "real":
        result = subprocess.run(["whoami"], capture_output=True, text=True)
        with open("recon.log", "w") as f:
            f.write(result.stdout)