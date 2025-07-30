# Description
The user can dive against bots and squids but any missions involving bugs instantly leads to crashing.
# Problem
The user uses a GPU based on AMD Vega. This can either be a GPU that actually is named Vega or certain Ryzen APU that have a Vega-based iGPU integrated.
# Fixes
The user needs to use Driver Version 22.11.2. (See [[GPU Drivers]])
## Steps
* Deinstall the Driver using the DDU - https://www.wagnardsoft.com/content/Download-Display-Driver-Uninstaller-DDU-18113
* Install Recommended Driver 22.11.2 - https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-22-11-2.html
* User has to deactivate GPU driver updates for the time being to avoid the error from occuring again.
# Affected models
## Ryzen APUs
### Ryzen 3
* PRO 2100GE
* 2200GE
* 2200G
* 2200U
* 2300U
* PRO 3200GE
* 3200GE
* PRO 3200G
* 3200U
* 3250C
* 3250U
* 3300U
* 3350U
* 4300GE
* 4300G
* (PRO) 7330U
### Ryzen 5
* 2400GE
* 2400G
* 2500U
* 2600H
* PRO 3350GE
* PRO 3350G
* PRO 3400GE
* 3400G
* PRO 3400G
* 3450U
* 3500U
* 3500C
* 3550H
* 3580U
* 4600GE
* 4600G
* 5600G
* 7430U
* (PRO) 7530U
### Ryzen 7
* 2700U
* 2800H
* 3700U
* 3700C
* 3750H
* 3780U
* 4700GE
* 4700G
* 5700G
* (PRO) 7730U
### Embedded Processors
* R1102G
* R1305G
* R1505G
* R1606G
* V1202B
* V1404I
* V1605B
* V1756B
* V1807B