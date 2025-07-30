In order to provide help to others, it is essential to gather information about the users system. While commonly attributed to be more tech-savy, with the rise of more user friendly distributions and the Steam Deck you will inevitably run into users who may have installed Linux but who are not too well-versed in its usage.

This article is meant as a help to gather information and to provide an overview of commands you can use in the Terminal (`[CTRL] + [ALT] + [T]`) in order to gather information. Some of these commands require users to download and install packages - there is nothing scary about that, nor is it unsafe or convoluted. It's a simple yes or no and then Linux will do its thing.

Also if the user needs to clear the Terminal of all current information, they can simply type in `clear` to clear it instead of opening a new terminal window.
# General System Information
While lots of Distributions have GUIs with System Info Tabs, sometimes this can be tricky to access or there may be a different reason why a user can't access it. In any case you can always ask them to run commands in the Terminal.
## inxi
The quickest and easiest way to find information about a system, would be the `inxi`command. It shows the CPU, Kernel, Uptime, Memory and a bit more.
![[inxiTerminal.png]]
## dmidecode utility
Despite not being installed in all Distros by default, the `dmidecode` utility is very usable and provides indepth information. 

It can be installed with `$ sudo dnf install -y dmidecode`

You can then use `dmidecode -t` to filter.
# Show CPU Information
While you can utilize the [[Hellbomb Script]] or CPU-Z as a quick way, you can also use the command `lscpu`to provide a summery of the CPUs capabilities, the model information, as well as number of cores, speeds, flags, and security mitigations applied.

It is also possible to use the command with different opteions. Two examples would be `-p` to print specific fields or `-j` for JSON output.
![[lscpuTerminal.png]]
# Show Disk Information
One of the easiest ways to show disk information would be `lsblk` as that will show discs and partitions. 
![[lsblk.png]]
## Partitions
In the picture above you can see three discs - `sda`, `sdb` and `sdc`. `sda` is the main disc that houses Linux and contains three partitions, `sda1`, `sda2` and `sda3`.

These paritions are separated due to how Linux is built and critical in their existence; deleting them will very likely make the OS unusable (maybe with the exception of the Home partition, but still, better be safe than sorry).

Please keep in mind that some Distros work differently and therefore can sometimes look differently or have different names.
### Boot partition
One of the partitions that should never be deleted (and make sure to have enough space!) is the boot parition. This critical component usually houses the kernel, initial RAM disk (also known as "`initrd`") and the bootloader, such as GRUB.
### EFI partition
The EFI system partition (also known as "ESP") is also critical and used by the UEFI firmware to boot operation system. This partition also stores boot loaders, applications and drivers which can be accessed by the UEFI firmware during the boot process. As you can guess, it's also absolutely critical.
### Home partition
Finally there is a separate home parition in Linux where the OS stores user data, such as documents, settings and personal files. If you ask yourself why the separation exists, it's simple: if you ever need to update or reinstall the OS, the User Data will not be altered.
# Show RAM information
In order to receive information about RAM, you can simply use the command `free`. Please note that the option `-m` makes it a bit more readable.
![[freeTerminal.png]]
As you can see above, you can see the overall RAM in the system and how much is used. You also see "swap".
## Swap partition
Swap isn't RAM in your system but a dedicated partition on the hard drives that can be used as virtual memory when the physical memory is full - so basically the equivalent to Windows' [[Set Pagefile|pagefile]]. 
## RAM via dmidecode
Now `free` might be good for a quick overview, but we can't really read a lot of information out of that. in order to get more information, we can install an extra package (in case it is not installed by default with the Distribution) that is called `dmidecode`. This will give us lots of information about hardware and firmware components.

It can be installed with `$ sudo dnf install -y dmidecode`

In order to run dmidecode to give us information specific about RAM, we need to run it with the option `-t` to filter the output and specify `memory`.  So the command will be `$ sudo dmidecode -t memory`.
![[dmidecodeTerminal.png]]
This filter will give us output for the mainboard and its maximum capacity, DIMM-slots (used and unused), RAM manufacturer, Speed, Voltage, etc.
# Show BIOS information
The utility `dmidecode` can also be used to display BIOS information without having to get into the BIOS / UEFI screen at the start of the system. 

Enter `sudo dmidecode -t bios`.
![[dmidecodeBIOS.png]]
This way you can easily discern if a BIOS update is necessary. You can find out the Mainboards name by typing in `sudo dmidecode -t baseboard`.
# Show USB information
The easiest and quickest way to see all currently connected (available!) USB devices would be the `lsusb` utility. Please note that not all distributions include this utility by default, so the user would have to install the `usbutils` package in order to access it.

`$ sudo dnf install -y usbutils`

Once the user has done that, they can simply type in `lsusb` to receive information.
![[lsusbTerminal.png]]
# Show PCI Information
You can also show information about PCI devices via the terminal. Like the `usbutils` case, the distro of the user may not include it by default, so it would have to be installed via the `pciutils` package.

`$ sudo dnf install -y pciutils`

And then they simply use the `lspci` command to show PCI information.

If you need to, you can also use the `-v` option to get a more detailed output and the `-k`option lists the Linux kernel module in use by the device. You can also use `-s` if you want filter specific devices based on their ID.
![[lspci.png]]
# Show System information
In case you ever need to look up a manufacturer, you can also use `dmidecode` to find out System Information.

For this we simply type in `sudo dmidecode -t system`.
![[dmidecodeSystem.png]]
# Show GPU Information
Now GPU information is a bit bigger and allows for a lot more information.
## Vulkan utilities
One of the best and easiest ways to show information would be to use `vulkan-tools`. This package may have to be installed if it isn't included by default by the distribution.

`install vulkan-tools` is the command to do so. Once it is installed, the user can then use `vulkaninfo --summary`:
![[vulkaninfo.png]]
This will list not only information about Vulkan itself, but also about the GPU, the currently used driver and many other things - so it's quick and easy to gather information.
## Driver Information
The following commands are specific and not all that informative but should work without having to install additional utility packages and can give a small overview.
### Check video drivers in use
If you want to check out what Video Drivers are currently in use, you can use this command: 

`lspci -n -n -k | grep -A 2 -e VGA -e 3D`
![[lspciDriverInfo 2.png]]
### Check active GPU driver
If you want to check which GPU driver is currently active you can also use this command: 
`glxinfo | grep -e OpenGL.vendor -e OpenGL.renderer`
![[glxinfoGPUDriver.png]]
### List available and default GPU
If you just want to check which GPUs are available, you can use this command:
`switcherooctl list`
![[switcherooCTL.png]]