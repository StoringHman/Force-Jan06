<hr/>

<p align="center">
  <img width="256" height="256" src="https://raw.githubusercontent.com/StoringHman/Force-Jan06/master/ProjectSrc/Resources/Logo.png"><h1 align=center>Force-Jan06<br/>(RSMM By: MaximumADHD)</h1>
  
</p>

<hr/>

# notice
You are now no longer able to use this version of Studio. Trying to connect to published games will throw an error.

# how to use
Very simple, there are two use cases.
If you want this for the old studio UI (which I am assuming most people who use this are using it for), you will need the latest .exe file from releases and (optionally, as you can do it manually) the .py file for patching it.

If you want this just to use old studio for some reason I guess, you will need to follow the same steps but inside the patcher UI disable FFlags.


If you want to do this manually without the .py file, first install the studio build and then add all FFlags into %localappdata%/Roblox Studio/ClientSettings/ClientAppSettings.json.

Then for manually patching the file to remove the out of date reinstall error, see https://github.com/MaximumADHD/Roblox-Studio-Mod-Manager/issues/239#issuecomment-3868394613

# stuff
hi so basically this is just the latest studio mod manager but the compiled exe now targets my own roblox client tracker repo that tells studio mod manager the string for the latest build version is the jan06 one, the actual repo has nothing changed aside from visual stuff and forcing the target version to 0.713. you can do this yourself by making your own client tracker repo and editing it, or just downloading the compiled exe from releases. YOU WILL STILL NEED TO APPLY OLD FIXES TO THE STUDIO EXE WHEN COMPELTE! THIS INCLUDES FFLAGS!

IF YOU DO WANT TO COMPILE SOMETHING LIKE THIS YOURSELF:
you will need the source of the latest rsmm repo and roblox-deploy-history repo
you will need a fork of roblox-client-tracker on github

(roblox-deploy-history is used in compiling rsmm)
i personally compiled with visual studio

# What is this?


The **Roblox Studio Mod Manager** is an open-source alternative bootstrapper for Roblox Studio. It is intended for power users who want to make experimental changes/tweaks to Roblox Studio without those changes being overwritten, and experiment with new features of Roblox Studio before the general public.

# Features
* File overrides are sustained between updates.
* Updates are applied incrementally to a single directory.
* A fast flag editor, allowing you to toggle new unstable features.
* Support for launching from the website, and from saved _RBXL_ files.
* File updates from Roblox's deployment servers are only applied where needed.
* Runs and installs in a separate directory, 100% independent of Roblox Studio's bootstrapper.

# ANTI-VIRUS DISCLAIMER

If you have an anti-virus program installed, there's a non-zero chance it may flag this program as malicious, due to this application being misdiagnosed as a trojan horse.<br/>

It was flagged as such because it downloads builds of Roblox Studio from a remote location and executes them on your PC. Since anti-virus programs can't distinguish whether this is malicious or not, it chooses to take no chances and assume it is malicious.<br/>

I've attempted to get this cleared several times, but haven't had any luck so far. I may need to get the application signed by a proper certificate authority, which will cost me some money to do.<br/>

In the meantime, you can try this workaround from boatbomber if you'd still like to use it:
https://twitter.com/BoatbomberRBLX/status/1347262909915738113

# Downloads

The latest version can be found on the ***Releases*** page of this repository:<br/>
https://github.com/MaximumADHD/Roblox-Studio-Mod-Manager/releases

You can also download the latest committed versions here:
* <a href="https://github.com/MaximumADHD/Roblox-Studio-Mod-Manager/raw/main/RobloxStudioModManager.exe">Download (.exe)</a></h1>
* <a href="https://github.com/MaximumADHD/Roblox-Studio-Mod-Manager/archive/main.zip">Download (.zip)</a>
