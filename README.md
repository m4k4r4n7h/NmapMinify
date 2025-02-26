# Nmap Guide

This python file help users to understand and learn the fundamental flags used in nmap to scan a network.
These flags will be automatically added by the script once the actual objective of the scan is known.
---------------------------------------------------------------------------------------------------------
# Nmap Flags for Penetration Testers
-------------------------------------
| Flag             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `-sS`            | TCP SYN scan                                                                 |
| `-sT`            | TCP connect scan                                                             |
| `-sU`            | UDP scan                                                                     |
| `-sA`            | TCP ACK scan                                                                 |
| `-sW`            | TCP window scan                                                              |
| `-sM`            | TCP Maimon scan                                                              |
| `-sN`            | TCP scan without flags (TCP null scan)                                       |
| `-sF`            | TCP FIN scan                                                                 |
| `-sX`            | TCP Xmas scan                                                                |
| `-sI`            | Idle scan                                                                    |
| `-sP`            | Ping scan (host discovery only)                                              |
| `-sL`            | List scan (just list targets)                                                |
| `-sR`            | RPC scan                                                                     |
| `-O`             | OS detection                                                                 |
| `-A`             | Aggressive scan (OS, version, script, and traceroute)                        |
| `-v`             | Verbose output                                                               |
| `-vv`            | More verbose output                                                          |
| `-d`             | Debugging output                                                             |
| `-p`             | Scan specific ports                                                          |
| `-p-`            | Scan all 65535 ports                                                          |
| `-T`             | Timing template (0-5, 0 is slowest, 5 is fastest)                            |
| `-t`             | Scan delay (in milliseconds)                                                 |
| `-Pn`            | Treat all hosts as online (skip host discovery)                              |
| `-n`             | No DNS resolution                                                             |
| `-R`             | Reverse DNS resolution                                                        |
| `-iL`            | Input from a file of target hosts                                            |
| `-oN`            | Output to normal text file                                                   |
| `-oX`            | Output to XML file                                                           |
| `-oG`            | Output to grepable format file                                               |
| `-oA`            | Output in all formats (normal, XML, and grepable)                            |
| `-p-`            | Scan all ports (1-65535)                                                     |
| `-P0`            | Treat hosts as online, no ping scan                                          |
| `-T4`            | Timing template for faster scans (default is T3)                             |
| `-p`             | Specify port(s) to scan                                                      |
| `--top-ports`    | Scan top N most common ports                                                 |
| `--exclude`      | Exclude hosts from scan                                                      |
| `--exclude-ports`| Exclude specific ports from scan                                             |
| `-6`             | Enable IPv6 scanning                                                         |
| `-d`             | Enable debugging                                                              |
| `-sC`            | Default script scan (runs default Nmap scripts)                               |
| `-p-`            | Scan all ports from 1 to 65535                                               |
| `-sV`            | Version detection (service version info)                                      |
| `--version-all`  | Probe all possible service versions                                          |
| `--open`         | Show only open ports                                                          |
| `--unprivileged` | Scan without privileges (i.e. no raw packets)                                 |
| `-A`             | Enable OS detection, version detection, script scanning, and traceroute       |
| `--traceroute`   | Trace the network path to each host                                          |
| `--script`       | Specify which script(s) to run                                               |
| `--script-args`  | Specify arguments for scripts                                                |
| `--script-trace` | Show script trace output                                                     |
| `-e`             | Specify the network interface to use for scanning                             |
| `-f`             | Fragment packets                                                              |
| `--dns-servers`  | Use specific DNS servers during resolution                                    |
| `-S`             | Specify source IP address for scanning                                       |
| `--spoof-mac`    | Spoof MAC address                                                             |
| `--source-port`  | Use a specific source port for scanning                                       |
