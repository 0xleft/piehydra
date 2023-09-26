from .install import is_hydra_installed
from .core import *

# TODO also allow windows but just use wsl like cmon
from platform import system
if system() == "Windows":
    print("pyhydra does not support windows")
    print("exiting...")
    exit()

if not is_hydra_installed():
    raise Exception("hydra is not installed")