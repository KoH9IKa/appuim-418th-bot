This is just an excerpt in case you wonder why we tell people to deactivate XMP or EXPO and why it leads to instabilities.
# Overview
As you know every RAM runs on certain standards, called JEDEC (https://en.wikipedia.org/wiki/JEDEC). This is basically saying "This RAM is this fast and has these timings", so it kinda defines how fast your RAM module is running. (Such as DDR5-4800)

Now aside from the JEDEC there are certain performance profiles available (XMP which was originally created by Intel and AMD EXPO). Depending on the profile this can be a quick and easy way to increase performance - you simply tell the RAM to use thise profile and it will try and run at the speeds defined in that XMP- or EXPO-Profile.

While that does sound easy - and it actually is - this also means a difference in terms of voltage that is applied. This can lead to certain problems, because not every mainboard will function with these settings and voltages applied. And that is also why you can look up compatible RAM on websites of Mainboards.
# Deactivating
If you don't activate XMP or EXPO, the RAM will use the JEDEC instead - so it will probably run a bit slower, but most likely more stable (this would also be the case if the Mainboard doesn't support either XMP or EXPO, because it wouldn't be able to read to profile).

And that can resolve the memory issues.
# Missmatched RAM
Missmatched RAM can also be another issue - even if your Mainboard allows for XMP and EXPO and works flawlessly, it's a whole different breed if you use different RAM kits. Even a single RAM module can cause problems, because the mainboard has to run all modules at the same speed and timings and that in of itself often leads to a lot of headache, which is why it is highly advised to only use the same kits on a single mainboard.