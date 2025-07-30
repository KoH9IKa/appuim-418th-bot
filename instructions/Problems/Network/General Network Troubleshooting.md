# Description
For general Network problems it is advised to follow these steps. Problems can arise from a huge variety of issues, be it DNS or NAT related.
# Solutions
Start by doing things inside your control like checking network settings, if you haven't already turn off your router for 5-6 minutes before turning it back on again.
## ipconfig
Reset your local network adapter settings via command prompt by running these commands in order:
* `ipconfig /release`
* `ipconfig /renew`
* `ipconfig /flushdns`
## Double NAT check
Run option `[T]` in [bob's hellbomb script](https://github.com/helldivers2fixes/HellbombScript "bob's hellbomb script (https://github.com/helldivers2fixes/HellbombScript)") to check for Dual NAT
## DNS errors
`Windows` + `R` and run `ncpa.cpl`

* Option A: Use Cloudflare DNS Servers
	* Right-click your NIC >> Properties and click `Properties` on the `Internet Protocol Version 4` section.
	* Try setting an IPv4 DNS as suggested in the script `1.1.1.1` is what's suggested [CloudFlare DNS](https://developers.cloudflare.com/1.1.1.1/ip-addresses/ "CloudFlare DNS (https://developers.cloudflare.com/1.1.1.1/ip-addresses/)") or alternatively `8.8.8.8` which is Googles
	* If you want or require secondary DNS addresses see below:
		* Secondary IPv4 Cloudflare `1.0.0.1`
		* Secondary IPv4 Google `8.8.4.4`
		* Right-click your NIC >> Properties and click `Properties` on the `Internet Protocol Version 6` section (will need to scroll down). Try setting an IPv6 DNS as suggested in the script `2606:4700:4700::1111` is what's suggested [CloudFlare DNS](https://developers.cloudflare.com/1.1.1.1/ip-addresses/ "CloudFlare DNS (https://developers.cloudflare.com/1.1.1.1/ip-addresses/)") or alternatively `2001:4860:4860::8888` which is Googles
	* If you want or require secondary DNS addresses see below:
		* Secondary IPv6 Cloudflare `2606:4700:4700::1001`
		* Secondary IPv6 Google `2001:4860:4860::8844` See if that fixes it.
* Option B: Disable IPv6
	* Disable IPv6 on your network adapter by unchecking Internet Protocol Version 6 and see if that fixes it. If it does, you can just do this before you play the game, but it usually fixes other connection issues in other applications as well.

After changing any DNS settings run `ipconfig /flushdns` in Command Prompt, or Restart your device.
# Other Problems
Another cause for the inability to connect to other players is a possible [[Version Missmatch]].
# Other Suggestions
In general it is better to use wired connections than wireless as they are more stable and faster.