import os

def run(mode, config):
    if mode == "real":
        os.system("sudo -n true || echo 'Insufficient privileges for sudo'")