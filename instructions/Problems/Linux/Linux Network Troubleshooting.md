# Description
This guide is meant to help resolving network problems with Linux as they are done a little different in comparison to Windows.

WARNING! This section is still very WIP
# DNS
Use this as help: https://cyberpanel.net/blog/flush-dns-on-linux
## Check DNS
To see if a DNS query returns positive, it is a good idea to use the `dig`command (Domain Information Groper) in the Terminal. if it finds something, it will return detailed information about domain name queries and the DNS records associated with the domain.

May want to check these:
* akamaihd.net
* playfabapi.com
* steamcontent.com
* steamstatic.com
* steamusercontent.com

1. Open the Terminal with `[CTRL] + [Alt] + [T]`
2. Type in `dig akamaihd.net`
	1. Alternatively, in order to get a raw DNS query result, the user can type in `nslookup akamaihd.net`
	2. The command "Host" is also possible: `host akamaihd.net`
3. It should return information now.
## Flush DNS
1. Open the Terminal with `[CTRL] + [Alt] + [T]`
2. We now want to clear the DNS cache and renew it with data.
	1. Type in `systemd-resolve --flush-caches` 
	2. Some distros may instead use `sudo resolvectl flush-caches`
	3. Older distros instaed use `sudo systemctl restart dnsmasq`
3. Sometimes it's enough to simply restart the networking service with `sudo rndc flush`
	1. You can restart the network manager and clear DNS via `sudo systemctl restart network-manager`
## Manually Setting DNS
1. Open the Terminal
2. Type in `sudo nano /etc/resolv.conf`
3. Then append `nameserver 8.8.8.8` - this can be done with the desired DNS server, such as CloudFlare.
# IP adress
* Release IP adress with `sudo dhclient -r`
* Renew lease with  `sudo dhclient`
## Check local Network
Getting information about the local network can be a bit more convoluted compared to Windows.
### arp-scan
One of the methods to check your local network under Linux is to use arp-scan - another common way would be `nmap`. arp-scan cannot cross layer 3 boundaries - which means it is limited to your subnet. In a normal household this would be sufficient to detect the devices that are communicating in your local Network.

1. Open the Terminal, type in `arp-scan`
2. Accept the package that has to be installed. Once it is done it will probably return an Error - don't worry, nothing's broken.
3. Type in `ifconfig` - This will return the network adapters names. The first entry should be the network adapter.
4. Type in `sudo arp-scan --interface=eth0 --localnet` - replace "eth0" with the name of the network adapter
5. You should now be able to see all active devices in the local network.