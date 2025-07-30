# Description
These are fixes if the user experiences Crashes to Desktop (CTD).
# Solutions
1. Remove all [[Mods]].
2. Delete the `shader_cache` folder at `%appdata%\arrowhead\helldivers2`
3. Ensure your motherboard [[UEFI or BIOS Update|UEFI/BIOS]] is up to date.  
    - This is doubly important for Intel 13th/14th gen CPUs.   
4. Remove any and all overclocking/undervolting.  
    - This includes features such as PBO, Intel 200s Boost, ASUS Multicore Enhancement,  [[Memory Issues|XMP/EXPO/DOCP]], and factory GPU overclocks.
    - Many 6000 and 7000 series AMD GPUs require a negative core clock offset to achieve stability. We suggest starting at -200MHz.,
5. Make sure you are **specifically** on one of the suggested [[GPU Drivers]]
    - NVIDIA: 566.36, AMD RDNA: 24.12.1, AMD VEGA: 22.11.2.
6. Uninstall/Install Fresh your Microsoft [[Reinstall Visual C++ Redistributables|Visual C++ Redistributable packages]].
    - Hellbomb script option `[U]`, then Reboot, then option `[I]`.,
    - For manual steps ask for the `vcreinstall` tag
7. Make sure your [[Set Pagefile|page file]] is enabled on at least one disk either `System Managed` or with a minimum value of `0.25 * RAM` and a maximum value of `1 * RAM + 257MB`.
    - This is an absolute MUST if you have 16GB or less RAM.,
    - The game may crash unexpectedly if your page file is off, both at startup or randomly on missions as you run out of memory.,
8. Run bobthebuilder's [[Hellbomb Script]]
	1. Option `[H]` to check for known problematic software.
	2. The script can also tell you your motherboard model, bios version, memory speed, and GPU driver version to provide clarity about 2/3/4.
	3. Note option `[H]` performs diagnostics and the output must be acted on by the user, it does not perform corrective actions.