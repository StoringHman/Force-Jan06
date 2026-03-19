#python script that attempts to automatically prepare studio for old ui usage
#must be run <AFTER> launching studio from fj06

import os
import json
from tkinter import messagebox

STUDIO_FILE_PATH = os.path.expandvars(r"%localappdata%\Roblox Studio\RobloxStudioBeta.exe")
FFLAGS_DIR = os.path.expandvars(r"%localappdata%\Roblox Studio\ClientSettings")
FFLAGS_FILE_PATH = os.path.join(FFLAGS_DIR, "ClientAppSettings.json")

#CONFIG<<
patchEmergencyMessage = True #disable if you want the out of date error thingy
applyOldUIFlags = True #disable if you want the old build without the fflags that trigger the old ui
#>>CONFIG

#main stuff now
if patchEmergencyMessage == True:
    with open(STUDIO_FILE_PATH, "rb") as f:
        studioEXE = f.read()

    timesFoundV4 = studioEXE.count(b"StudioEmergencyMessageV4")
    if timesFoundV4 == 0:
         messagebox.showerror("Patch Failed", "File appears to be corrupt or has already been patched. If you are confident this is not the case, please make a issue on github.")
    else:
        studioEXE = studioEXE.replace(b"StudioEmergencyMessageV4", b"StudioEmergencyMessageV5")
        with open(STUDIO_FILE_PATH, "wb") as f:
            f.write(studioEXE)
        messagebox.showinfo("Patch Complete", "Studio exe patched successfully! You can now open it from %localappdata%/Roblox Studio/RobloxStudioBeta.exe")

if applyOldUIFlags == True:
    FFLAGS_TO_WRITE = {
        "FFlagEnableRibbonPlugin3": "false",
        "FFlagNewExplorer":"false",
        "FFlagNextGenStudioBetaFeature":"false",
        "FFlagKillOldExplorer3":"false"
    }
    if not os.path.exists(FFLAGS_DIR):
        os.makedirs(FFLAGS_DIR)

    with open(FFLAGS_FILE_PATH, "w") as f:
        json.dump(FFLAGS_TO_WRITE, f, indent=2)