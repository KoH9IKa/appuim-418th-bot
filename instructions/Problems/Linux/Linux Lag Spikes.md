# Description
The game suffers from stutters / lag spikes.
# Problem
Currently there is a known bug in Steam that causes these spikes.  For info see this post on [Gaming on Linux](https://www.gamingonlinux.com/2025/05/upcoming-steam-update-should-fix-lag-spikes-on-linux-when-the-steam-overlay-is-disabled/ "Gaming on Linux (https://www.gamingonlinux.com/2025/05/upcoming-steam-update-should-fix-lag-spikes-on-linux-when-the-steam-overlay-is-disabled/)")
# Solutions
There are two possible workarounds:
* Launch with `LD_PRELOAD="" %command%`
* Temporarily reenable the Overlay until Steam has released a fix.
