import subprocess
import os
from elevate import elevate
DETACHED_PROCESS = 0x00000008
file = "lol.exe"
location = "C:\Windows\System32"
print(f"move \"{file}\" \"{location}\"")