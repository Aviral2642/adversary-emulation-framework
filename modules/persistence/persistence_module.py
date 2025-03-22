def run(mode, config):
    if mode == "real":
        with open("/tmp/.malicious", "w") as f:
            f.write("This is a simulated persistence backdoor.")