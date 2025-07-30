# Description
Headsets by Logitech or Blue (which was purchased by Logitech) are having some trouble with the game.
# Problem
This is caused by a `limiter`option that is selected in ghub/blue control.
# Solution
Deactivate the limiter in ghub/blue control. If this software is not installed, their headset may behave as if these options are enabled.

You might expect unchecking the options for exclusive mode in `mmsys.cpl` to stop the behavior, but it apparently doesn't always. If that is the case, the user has to insstall ghub / blue control and then disable the feature.

![[Headset.png]]