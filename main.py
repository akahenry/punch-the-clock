from os import name
import sys

from manager import Manager
from config import Config

Config()
manager = Manager(f"{Config.datapath}/{Config.datafilename}")

if len(sys.argv) == 1:
    print("You must use `enter` or `exit`")
else:
    if sys.argv[1] == "enter":
        manager.enter()
    elif sys.argv[1] == "exit":
        manager.exit()
    elif sys.argv[1] == "history":
        manager.history()

manager.close()
