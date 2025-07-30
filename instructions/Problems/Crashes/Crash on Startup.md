# Description
These are solutions for crashes that occur upon starting the game.
# Solutions
1. If you haven't rebooted your PC, reboot your PC.,
2. If you are on [[Windows 11 24H2 Gaming Fix|Windows 11 24H2]] with a NVIDIA GPU, be sure to install the June Gaming Fix Patch released by Microsoft, KB5058499. It specifically addresses game startup hangs and crashes.
3. Error: `0x44415441` Remove all [[Mods]].
    - Hellbomb script options `[Q]`+`[C]`+`[S]`, in this order, **then verify game files** in steam, to remove mods fully.,
4. If no mods were ever used before, delete the `helldivers2` folder at `%appdata%\arrowhead`.
    - Hellbomb script option `[C]`,
5. Make sure your [[Set Pagefile|page file]] is enabled on at least one disk either `System Managed` or with a minimum value of `0.25 * RAM` and a maximum value of `1 * RAM + 257MB`.
    - This is an absolute MUST if you have 16GB or less RAM.
    - The game may crash unexpectedly if your page file is off, both at startup or randomly on missions as you run out of memory.
6. Make sure you are on one of the suggested [[GPU Drivers|video drivers]]:
7. [[Reinstall GameGuard]].
    - Hellbomb script option `[G]`
8. [[Reinstall Visual C++ Redistributables]]
    - Hellbomb script option `[U]`, then Reboot, then option `[I]`.,
9. Set your High Performance GPU in Windows
    - Hellbomb script option `[P]` and follow the on-screen steps.,
# See also
* [[Hellbomb Script]]