# Description
Both AMD and NVIDIA's latest GPU drivers appear to be causing crashes. NVIDIA's latest 57x.xx driver line, in particular, is also causing stuttering and blackscreens. Run the specific driver EXACTLY for your class of GPU below to avoid as many issues as possible.
# Overview

- Nvidia Non-5000 Series: [566.36](https://us.download.nvidia.com/Windows/566.36/566.36-desktop-win10-win11-64bit-international-dch-whql.exe "566.36     (https://us.download.nvidia.com/Windows/566.36/566.36-desktop-win10-win11-64bit-international-dch-whql.exe)"),
- AMD 5000-7000 Series: [24.12.1](https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-24-12-1.html "24.12.1     (https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-24-12-1.html)"),
- AMD Vega & Ryzen APU: [22.11.2](https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-22-11-2.html "22.11.2     (https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-22-11-2.html)") (See [[Can't dive against bugs]])
    - Without this driver, Vega/APU parts crash on drop.    
# Driver rollback
- If you are rolling back from a newer driver, download [DDU](https://www.wagnardsoft.com/content/Download-Display-Driver-Uninstaller-DDU-18113 "DDU     (https://www.wagnardsoft.com/content/Download-Display-Driver-Uninstaller-DDU-18113)") and perform a clean install.
# Clear Shader Cache
**IMPORTANT:** After changing your driver be sure to delete your `shader_cache` folder at: `%APPDATA%\Arrowhead\Helldivers2`