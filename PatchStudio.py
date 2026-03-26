import os
import json

import subprocess
import tempfile
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

STUDIO_FILE_PATH = os.path.expandvars(r"%localappdata%\Roblox Studio\RobloxStudioBeta.exe")
FFLAGS_DIR = os.path.expandvars(r"%localappdata%\Roblox Studio\ClientSettings")
FFLAGS_FILE_PATH = os.path.join(FFLAGS_DIR, "ClientAppSettings.json")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Old Studio Patcher")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        #changed now so that config is done via checkboxes in the ui
        self.patchEmergencyMessage = tk.BooleanVar(value=True)
        self.applyOldUIFlags = tk.BooleanVar(value=True)

        tk.Label(self, text="Old Studio Patcher\n", font=("Comic Sans MS", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 245))
        tk.Label(self, text="USE THIS AFTER INSTALLING WITH THE MOD MANAGER!!", font=("Comic Sans MS", 12)).grid(row=0, column=0, columnspan=2, pady=(0, 210))
        tk.Label(self, text="Targets %localappdata%/Roblox Studio/", font=("Comic Sans MS", 10)).grid(row=0, column=0, columnspan=2, pady=(0, 165))

        #couldn't REALLY figure out a libraryless solution for this, so ill use tk with base64
        LOGO_BASE64 = "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"
        self.photo = tk.PhotoImage(data=LOGO_BASE64)
        tk.Label(self, image=self.photo).grid(row=0, column=0, columnspan=2, pady=(0, 0))

        ttk.Checkbutton(self, text="Disable Reinstall error", variable=self.patchEmergencyMessage).grid(row=1, column=0, sticky="w")
        ttk.Checkbutton(self, text="Apply/update old UI FFlags", variable=self.applyOldUIFlags).grid(row=2, column=0, sticky="w")

        ttk.Separator(self, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)

        self.log = tk.Text(self, height=8, width=50, state="disabled", bg="#000000", fg="#ffffff", font=("Consolas", 9), relief="flat")
        self.log.grid(row=5, column=0, columnspan=2, pady=(0, 10))

        self.run_btn = ttk.Button(self, text="Apply", command=self.run)
        self.run_btn.grid(row=6, column=0, columnspan=2, pady=(0, 5))
        self.launch_btn = ttk.Button(self, text="Launch Studio", command=self.launchStudio)
        self.launch_btn.grid(row=7, column=0, columnspan=2, pady=(0, 5))
        self.github_btn = ttk.Button(self, text="Github", command=self.openGithub)
        self.github_btn.grid(row=8, column=0, columnspan=2)

    def log_msg(self, msg):
        self.log.configure(state="normal")
        self.log.insert("end", msg + "\n")
        self.log.configure(state="disabled")
        self.log.see("end")
        self.update()

    def openGithub(self):
        webbrowser.open("https://github.com/StoringHman/Force-Jan06")
    
    #AI DISCLOSURE: I used AI to write this function as no matter what I did to open Studio, it would crash the moment this script finished.
    #There was NO way I was figuring this out as I did some research and nothing even came close to this solution.
    def launchStudio(self):
        import ctypes
        import ctypes.wintypes
        self.log_msg("Attempting Studio Launch.")

        kernel32 = ctypes.windll.kernel32
        
        # Find explorer.exe pid to use as fake parent
        explorer_pid = None
        import subprocess
        result = subprocess.check_output("tasklist /FI \"IMAGENAME eq explorer.exe\" /FO CSV /NH", shell=True).decode()
        for line in result.strip().split("\n"):
            if "explorer.exe" in line:
                explorer_pid = int(line.split(",")[1].strip().strip('"'))
                break

        if not explorer_pid:
            self.log_msg("Could not find explorer.exe, aborting.")
            return

        PROCESS_ALL_ACCESS = 0x1F0FFF
        EXTENDED_STARTUPINFO_PRESENT = 0x00080000
        PROC_THREAD_ATTRIBUTE_PARENT_PROCESS = 0x00020000

        class STARTUPINFOEX(ctypes.Structure):
            _fields_ = [
                ("StartupInfo", ctypes.c_byte * 104),
                ("lpAttributeList", ctypes.c_void_p)
            ]

        h_parent = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, explorer_pid)

        attr_list_size = ctypes.c_size_t(0)
        kernel32.InitializeProcThreadAttributeList(None, 1, 0, ctypes.byref(attr_list_size))
        attr_list = ctypes.create_string_buffer(attr_list_size.value)
        kernel32.InitializeProcThreadAttributeList(attr_list, 1, 0, ctypes.byref(attr_list_size))

        h_parent_ptr = ctypes.c_void_p(h_parent)
        kernel32.UpdateProcThreadAttribute(
            attr_list, 0,
            PROC_THREAD_ATTRIBUTE_PARENT_PROCESS,
            ctypes.byref(h_parent_ptr),
            ctypes.sizeof(h_parent_ptr),
            None, None
        )

        si = STARTUPINFOEX()
        ctypes.memset(ctypes.byref(si), 0, ctypes.sizeof(si))
        si.StartupInfo[0] = ctypes.sizeof(si)  # cb field
        si.lpAttributeList = ctypes.cast(attr_list, ctypes.c_void_p).value

        pi = ctypes.create_string_buffer(32)  # PROCESS_INFORMATION

        result = kernel32.CreateProcessW(
            STUDIO_FILE_PATH,   # lpApplicationName
            None,               # lpCommandLine
            None,               # lpProcessAttributes
            None,               # lpThreadAttributes
            False,              # bInheritHandles
            EXTENDED_STARTUPINFO_PRESENT,  # dwCreationFlags
            None,               # lpEnvironment
            os.path.dirname(STUDIO_FILE_PATH),  # lpCurrentDirectory
            ctypes.byref(si),   # lpStartupInfo
            pi                  # lpProcessInformation
        )

        kernel32.CloseHandle(h_parent)

        if result:
            self.log_msg("Studio launched. You can close this window.")
            self.destroy()
        else:
            err = kernel32.GetLastError()
            self.log_msg(f"Launch failed. Error code: {err}")

        self.run_btn.configure(state="normal")

    def run(self):
        self.run_btn.configure(state="disabled")
        updateFFlags = False

        if self.patchEmergencyMessage.get():
            if not os.path.exists(STUDIO_FILE_PATH):
                self.log_msg("PATCH FAILED: Studio doesn't exist? Make sure to run this AFTER using fj06.\n")
                self.run_btn.configure(state="normal")
                return
            with open(STUDIO_FILE_PATH, "rb") as f:
                studioEXE = f.read()

            if studioEXE.count(b"StudioEmergencyMessageV4") == 0:
                self.log_msg("PATCH FAILED: File appears to be corrupt or has already been patched. If you are confident this is not the case, please make a issue on github.\n")

            else:
                studioEXE = studioEXE.replace(b"StudioEmergencyMessageV4", b"StudioEmergencyMessageV5")
                with open(STUDIO_FILE_PATH, "wb") as f:
                    f.write(studioEXE)
                self.log_msg("PATCH COMPLETE: Studio exe patched successfully! You can now open it from %localappdata%/Roblox Studio/RobloxStudioBeta.exe\n")

        if self.applyOldUIFlags.get() or updateFFlags:
            FFLAGS_TO_WRITE = {
                "FFlagEnableRibbonPlugin3": "false",
                "FFlagNewExplorer": "false",
                "FFlagNextGenStudioBetaFeature": "false",
                "FFlagKillOldExplorer3": "false",
                "FFlagAdvancedCommandBar6": "false"
            }
            self.log_msg("Checking for ClientSettings dir\n")
            if not os.path.exists(FFLAGS_DIR):
                self.log_msg("NF: Making ClientSettingd dir\n")
                os.makedirs(FFLAGS_DIR)
            with open(FFLAGS_FILE_PATH, "w") as f:
                self.log_msg("ClientSettings dir found, writing to ClientAppSettings.json\n")
                json.dump(FFLAGS_TO_WRITE, f, indent=2)
            self.log_msg("Wrote FFlags to ClientAppSettings.json\n")

        self.log_msg("Finished, if something went wrong copy the above and make a github issue.")

        self.run_btn.configure(state="normal")

if __name__ == "__main__":
    app = App()
    app.mainloop()