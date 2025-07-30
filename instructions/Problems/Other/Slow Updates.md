# Description
Sometimes Updates take longer than an actualy reinstall, which can be bothersome to users.

This is tied to how a game is updated and also depends on the game itself. Games such as ARK and Payday 2 for example have slow update speeds since large parts of the games files need to be copied somewhere else before the update is applied. It's simply a matter of work that needs to be done; during an update files have to be unpacked and reorganized which is rather resource intensive and can be felt especially on slower Hardware. With a fresh install, this can take less time since there is less organizational stuff happening.
# Details
## Downloading and Updating
There is a BIG difference between downloading and updating. It's important to actually be sure you are on the same page. Are they actually downloading, or are files being patched?

* If download bytes are 0b/s, but disk activity is high, that is not an issue and it's not downloading because it is patching.
## Download Regions
Downloads are almost always very fast unless the internet connection is slow. Steam uses content delivery servers based on specified steam regions.

* If the actual download speed is slow, it is advisable to try a different steam region. Arrowhead can do nothing about the Steam CDN in the region being slow, but a different region may be faster.
## Drives
A LOT of users have poorly performing SSD's that were 'budget' options. These SSD's in particular can be REALLY slow performing updates. If you look in task manager and go to the performance tab, check the 'active time' of your disk. If it's 100%, you know its caused by your storage being slow.

1. Storage can be slow due to anti virus software constantly scanning as patching is performed. If you suspect this is the case, temporarily disable your anti virus.
2. Storage can be slow if it is almost full, the game needs ~110GB free for updating.
    - Having sufficient free space to perform the patch does not guarantee the game will patch quickly, just that it will eventually patch. If your SSD is over 50% full, you may experience slow updates due to your SSD not handling being nearly full well.,
3. STEAM can be slow if you have it installed on a slow SSD or HDD, even if you moved helldivers to different, fast, storage.

If your internet is fast, an uninstall then fresh install will be faster than patching the game. 
# Solutions
If your pc has a SSD and HDD and your game is taking longer to update because of disk usage, open `Task Manager` and see if your HDD is being used instead of your SSD, if yes then here is a work around to force it to use the SSD: [This Reddit post](https://www.reddit.com/r/Helldivers/comments/1kwt9hh/psa_to_steam_users_if_your_pc_has_an_ssd_and_hdd/ "This Reddit post (https://www.reddit.com/r/Helldivers/comments/1kwt9hh/psa_to_steam_users_if_your_pc_has_an_ssd_and_hdd/)") has associated pictures if you are unfamiliar with any of these files

1. Go to where Steam is installed and open the `steamapps` folder. Default installation folder in Windows `C:/Program Files (x86)\Steam\steamapps`
2. Look for the `libraryfolders.vdf` file and open it with Notepad
3. Then make note of the `C://steam` number for your SSD is usually `0` or `1` etc
4. Then go back into `steamapps` and look for the file `appmanifest_553850` this is the HD2 download instructions file, open it with notepad
5. Then look for code line `Stagingfolder` and change the number to your SSD, once done save and close
6. After you have done that, open `Steam` `settings` > `downloads` then press `Clear Caches`, this will restart steam and you will need to log in again. **Note:** clearing the caches WILL wipe any download progress on the patch so you have to restart it again.
7. After Steam restarts and you are logged back in it should now be using the SSD!





