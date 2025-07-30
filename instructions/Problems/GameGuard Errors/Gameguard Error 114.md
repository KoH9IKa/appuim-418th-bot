# Description
The Game doesn't start due to GameGuard. The user receives error message 114.

For further information, check https://gameguardfaq.nprotect.com/eng/con_01.html
# Possible Solutions
* [[General Network Troubleshooting]] (Try a simple ipconfig /flushdns first)
* Linux: [[Proton Error]] (Need to Switch Proton Versions)
* In some Mainboards the [[UEFI or BIOS Update]] seems to cause Error 114. This is especially tricky when updating Intel Mainboards for CPUs of the 13th or 14th Generation as the update for Microcode 0x12F is essential to avoid the degradation issue caused by the vMin Shift.
	* Hardware longevity should be prioritized above playing Helldivers 2 - if a beta UEFI is available that contains 0x12F, it could potentially fix that problem without exposing the hardware.
	* For all non 13th- or 14th generation Mainboards reverting to an older UEFI isnt as critical and can be recommended.
	* Especially GigaByte boards are affected by this error and even HP Laptops without the 0x12F fix can suffer the same problem. Repeated retries can sometimes be used to get into the game regardless - even if it takes 20 tries.
* Disabling SecureBoot can cause GameGuard errors. However it is required for Win11 to be enabled and some Linux Distros support it - some don't. Testing is in order.
* [[Reinstall GameGuard]] (fastest with [[Hellbomb Script]])
# See Also
* [[GameGuard Error List]]