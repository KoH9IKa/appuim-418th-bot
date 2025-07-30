# Description
Proton Errors are Linux (and therefore also SteamDeck) specific errors that come from the currently used Proton Version. These Errors can be very unspecific and encompass a range of strange errors. That can be:
*  [[Texture errors]]
* Escape Key causes CTDs
* [[Gameguard Error 114]]
## Explanation
Proton is a compatibility layer that translates Windows API calls, such as Direct3D 11 and Direct3D 12, into Vulkan. So any of these errors can be, to make it overly simple, attributed to translation errors.
## Creating Logs
If it's unclear what the problem with Proton is, the user can always add the Launch Option `PROTON_LOG=1 %command%` which allows Proton to write a log where it will give infromation about what's wrong.

Here is an explanation from ProtonDB:

![[ProtonLog.png]]
# Solutions
The user should change their Proton Version. They do so by right clicking the game in Steam, go to Properties and then Compatibility. There they can change their Proton Versions.

Note that there is no definitive Proton Version any user can use; two users can use the same Proton Version and while one has a flawless experience, the other could experience issues, so testing is in order.
# See Also
For tipps and experiences by other users, check ProtonDB: https://www.protondb.com/app/553850