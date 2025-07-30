# Description
Sometimes the performance of the game suffers from a pagefile that is not big enough. The pagefile is a space on a disk that can be used when the physical memory is full - so basically it's a reserve for the computer to use.

The game may crash unexpectedly if the page file is off, both at startup or randomly on missions as the game runs out of memory.

NOTE: Especially when the system doesn't have a lot of RAM to work with the pagefile becomes more important. Anyone below 16 GB should make absolutely sure to have a proper set up pagefile!
# How to set
1. Press `Win + R` to open the Run dialog.,
2. Type `sysdm.cpl` into the textbox and click OK.,
3. Click on the `Advanced` tab, and then the `Settings` button in the Performance section.,
4. Click on the `Advanced` tab in the Performance Options dialog.,
5. Ensure your Processor Scheduling is set to `Programs`.,
6. Click the `Change` button in the Virtual memory section.,
7. Ensure the checkbox at the top of the Virtual Memory dialog is selected: `Automatically manage paging file size for all drives`,
8. If you do not want automatic management, click the `Custom size` radio button, then ensure your page file size minimum value is `0.25 * RAM` and maximum value is `1 * RAM + 257MB`.

! If you have both an SSD and an HDD, place the page file on your HDD !
# Sources
- Microsoft Learn: Appropriate page file size (https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/how-to-determine-the-appropriate-page-file-size-for-64-bit-versions-of-windows)"