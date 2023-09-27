from .install import is_hydra_installed
from .core import *

from platform import system
if system() == "Windows":
    print("just use wsl please")

if not is_hydra_installed():
    raise Exception("hydra is not installed")