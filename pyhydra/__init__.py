from .install import is_hydra_installed
from .core import *

# TODO also allow windows but just use wsl like cmon
from platform import system
if system() == "Windows":
    print("pyhydra does not support windows")
    print("exiting...")
    exit()

if not is_hydra_installed():
    print("hydra is not installed")
    if input("would you like to install it? (y/n)").lower() == "y":
        from .install import install_hydra
        install_hydra()
    else:
        print("exiting...")
        exit()