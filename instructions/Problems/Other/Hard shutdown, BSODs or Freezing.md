In case the computer is shutting down hard (turning itself fully off), showing a BSOD or is Freezing to the point where the reset button has to be pressed, the underlying issue is probably more significant.
# BSOD
Blue Screens of Death (BSOD for short) can be cause by driver issues but can also be a prevalent indicator that something with the hardware has gone terribly wrong. Even a lack of sufficient power can potentially lead to a bluescreen. It's advised to look into the Windows Event Manager and check the Logs there.
# Problems
The cause for such events can pretty much be attributed to three things:

1. Thermal problems - the Hardware heated up so much it had to shutdown in order to prevent damage
2. Power - The device simply didn't get enough power and when it tried to draw in more than it could things simply went down the drain
3. Damage - Something in the device is broken and triggers one of these events.

Especially Laptop users tend to run into heat issues.
## Windows Event Viewer
The Windows Event Viewer is a good way of diagnosing what's going on, albeit it cannot tell everything that could be the issue. A Kernel Event ID 41 would be just saying that the device shutdown improper, but not why - but other Events may and they can be looked up to see what the cause may be.

To open up the Event Viewer, do the following:
1. Press `[Win] + [R]` or open the search bar
2. Type in `eventvwr.msc`

And then direct the user to Windows logs.
### WHEA errors
One thing to look out for when suspecting hardware damage is the so called "WHEA" - Windows Hardware Error Architecture, a tool to handle Hardware Errors that exists since Vista SP1. 

Usually when Windows gives out a WHEA error that means something is terribly awry. This typically results in a BSOD with the error code WHEA_UNCORRECTABLE_ERROR. Causes for this are usually fualty hardware, but can also be caused by driver conflicts, missing Windows updates and even overclocking.
## Temperature problems
When a devices sensors detect rising heat in the hardware then they will automatically start to throttle in order to reduce heat buildup. However there is only so much a device can do; neglect of the device (not cleaning out dust or reapplying thermal paste) will result in very high temperatures.

It is suggested to take care of heating issues first and foremost. Some users may be brave enough to use ThrottleStop to circumvent this but that can lead to hardware damage and is not suggested - it could potentially turn a power supply into a fire hazard in the worst of circumstances.