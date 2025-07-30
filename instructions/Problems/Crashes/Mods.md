# Description
Mods currently cause crash on load with error code `0x44415441`. They can also partly function and break other things, such as sound, icons, textures, etc.

As there is no official mod support expect every patch to break mods, and as mods are not officially supported AH will not be changing how updates are done to stop this happening after updates/patches. If there are any remnants it will still crash. 
# Solutions
It's important to not just disable them but hard purge them from from the system with bobs [[Hellbomb Script]] Option `[H]` to detect mods then `[Q]` to delete mods detected as well as options `[C]` + `[S]` to clear your Local HD2 Data and Reset Steam (note this will not remove any progress or affect other games)

After this you want to **Verify Files**.

If any mods are left after this the below is the Manual Method to clear up any remaining mods from the system.
## HD2MM
If the user is using HD2MM:

Click `Settings` and then `Hard Purge` Clear the local data for HD2MM (usually `%appdata%/helldivers2modmanager`) **If using Vortex:** `Uninstall` the mods and click `Purge` Click `Settings` and check where the mod storage folder is and delete it (usually `%appdata%/vortex/helldivers2/mods`) Clear the `%appdata%/Arrowhead/Helldivers2` folder

After this you want to **Verify Files**,

If the mods were shoddily designed and replaced any original files in the `Data` or `Bin` directory folders in the Steam install location you will need to delete the whole Data and/or Bin folders and **Verify Files** to redownload the 25gb (`Data` folder only) or ALL game files (`Data` & `Bin`) which should be larger around 92-96gb