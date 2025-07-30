# Description
Antivirus Software reports that the game contains a Thermida Q Trojan.
# Problem
The Antivirus Software falsely flags game data. The game was packed with Thermida to obfuscate and make it harder to reverse-engineer the game code. Malware devs use the same packer to make it harder to detect their malware.

Helldivers 2 does **not** contain any trojans or other malware.
# Solution
While the easiest solution would be to deactivate antivirus software, this is not recommended as it makes the users device more susceptible to actual malware.

It is better for the user to set up exclusions within their antivirus software so it does not falsely flag the files.

1. `$drive:$steam_library_path/steamapps/commom/Helldivers`
2. `$drive:$steam_library_path/steamppps/downloading`