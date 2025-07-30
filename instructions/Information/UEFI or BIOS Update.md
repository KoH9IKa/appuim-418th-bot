# Description
Although it doesn't have to lead to crashes, it is good practice to update the UEFI / BIOS to the latest stable version to ensure a smooth and stable experience. Newer Software can cause problems if the UEFI / BIOS is not updated.
## Microcode
Another reason are fixes for CPU microcode / AGESA which can only be obtained this way. This includes not only security updates but also other important fixes.

Both AMD and Intel had microcode/AGESA issues that lead to physical hardware failure. These issues can only be fixed through a BIOS update. AMD's 7000 series burning CPUs was due to a VSOC overvoltage issue, and Intel's 13th and 14th gen 100% failure rate issue is caused by an eTVB overvoltage issue (for more information, look up "vMin Shift").
# How to check
 1. Click Start Menu
2. Type "Powershell"
3. Right Click on Powershell and "Run as Administrator"
4. Paste the below text into the console:

`$motherboardInfo = @( [pscustomobject]@{ 'Motherboard Info' = 'Manufacturer: '+(Get-CimInstance -ClassName Win32_BaseBoard).Manufacturer.Trim(); 'UEFI Info' = 'SMBIOS Version: '+(Get-CimInstance -ClassName Win32_BIOS).SMBIOSBIOSVersion.Trim() },[pscustomobject]@{ 'Motherboard Info' = 'Product: '+(Get-CimInstance -ClassName Win32_BaseBoard).Product.Trim(); 'UEFI Info' = 'Manufacturer: '+(Get-CimInstance -ClassName Win32_BIOS).Manufacturer.Trim() }, [pscustomobject]@{ 'Motherboard Info' = ''; 'UEFI Info' = 'BIOS Version:'+(Get-CimInstance -ClassName Win32_BIOS).Name.Trim() } ); $motherboardInfo | Format-Table 'Motherboard Info', 'UEFI Info' -AutoSize`

The output should look like this:

![[PowerShell1.png]]

# Nvidia GPUs
Warning - if certain Nvidia GPUs are present, it is important to run a tool first before updating the UEFI, because otherwise the user might experience a blackscreen they can't get rid off.
## GeForce 40 Series
* RTX 4090
* RTX 4080
## GeForce 30 Series
* RTX 3090 Ti
* RTX 3080 Ti
* RTX 3060
## GeForce 10 Series
* GeForce GT 1030
* GeForce GTX 1050
* GTX 1050Ti
* GTX 1060
* GTX 1070
* GTX 1070Ti
* GTX 1080
* GTX 1080Ti
## GeForce 900 Series
* GeForce GTX 950
* GTX 950Ti
* GTX 960
* GTX 970
* GTX 980
* GTX 980Ti
## GeForce 700 Series
* GeForce GTX 745
* GTX 750
* GTX 750Ti (Just run the tool. It will tell you either way)
## Updates
* RTX 4090 & RTX 4080 update: [NVIDIA GPU UEFI Firmware Update Tool](https://nvidia.custhelp.com/app/answers/detail/a_id/5411/~/nvidia-gpu-uefi-firmware-update-tool "NVIDIA GPU UEFI Firmware Update Tool (https://nvidia.custhelp.com/app/answers/detail/a_id/5411/~/nvidia-gpu-uefi-firmware-update-tool)") 
* RTX 3090 Ti, RTX 3080 Ti, RTX 3060 update: [NVIDIA GPU Firmware Update Tool for DisplayID](https://nvidia.custhelp.com/app/answers/detail/a_id/5233/~/nvidia-gpu-firmware-update-tool-for-displayid "NVIDIA GPU Firmware Update Tool for DisplayID (https://nvidia.custhelp.com/app/answers/detail/a_id/5233/~/nvidia-gpu-firmware-update-tool-for-displayid)") 
* 700, 900 and 1000 series update: [NVIDIA Graphics Firmware Update Tool for DisplayPort 1.3 and 1.4 Displays](https://www.nvidia.com/en-us/drivers/nv-uefi-update-x64/ "NVIDIA Graphics Firmware Update Tool for DisplayPort 1.3 and 1.4 Displays (https://www.nvidia.com/en-us/drivers/nv-uefi-update-x64/)")