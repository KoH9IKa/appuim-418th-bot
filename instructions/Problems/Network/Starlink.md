# Description
Starlink has known connectivity issues if playing wired on an UTR-211 modem. According to bob "It's a reproducible issue where IPv6 addresses randomly don't get properly passed through the switch in the UTR-211 modem."
# Solution
There are three different methods that can be tried to fix the problem.
1. If you're **wired** into a **router** that is **then connected** to the Starlink **modem**, set your router IPv6 mode to `autoconfigure` instead of `autodetect`
2. Play on wireless with no other changes
3. Disable IPv6 on your network adapter by unchecking Internet Protocol Version 6 and see if that fixes it. If it does, you can just do this before you play the game, but it usually fixes other connection issues in other applications as well.
	1. Remember that this can be an intermittent issue, so it _may_ work _sometimes_ with IPv6. 