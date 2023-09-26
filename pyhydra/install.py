import subprocess

def is_hydra_installed():
    try:
        subprocess.check_output(["hydra"])
    except PermissionError:
        return False
    # hydra returns 255 if it is ran without any arguments (also with -h)
    except subprocess.CalledProcessError:
        return True
    return True