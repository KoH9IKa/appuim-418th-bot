# Description
Sometimes the System Data is damaged and that in turn can cause crashes and other problems. To fix this the user can attempt to repair it via the Command prompt.
# How to
1. Go to search bar and search "command prompt" or "CMD"
2. Right click on it and click "**Run as Administrator**"
3. Type in exactly (it must include the spaces and slashes, it won't break anything if you don't, it just won't run the command):  "sfc /scannow"
4. Once this has concluded, run these afterwards in order:
	1. `dism /online /cleanup-image /scanhealth`
	2. `dism /online /cleanup-image /checkhealth`
	3. `dism /online /cleanup-image /restorehealth`
5. This process takes some time and will hang about 62.8% when running the restore health command. No worries, just let it run and it'll do its thing.
6. Restart the computer

If this fix can't repair Windows, the OS may have to be reinstalled. It however cannot fix a faulty drive.