
                                                            ████████▄     ▄▄▄▄███▄▄▄▄    ▄████████
                                                            ███    ███  ▄██▀▀▀███▀▀▀██▄ ███    ███
                                                            ███    ███  ███   ███   ███ ███    █▀  
                                                            ███    ███  ███   ███   ███ ███        
                                                            ███    ███  ███   ███   ███ ███        
                                                            ███    ███  ███   ███   ███ ███    █▄  
                                                            ███  ▀ ███  ███   ███   ███ ███    ███ 
                                                             ▀██████▀▄█  ▀█   ███   █▀  ████████▀  
                                                        
                                                             ▀█ Quick MAC Changer by @tzero86█▀


QMC is a super simple and rather silly utility to quickly change the MAC Address of a given interface. It supports both user entered MAC Addresses and automatically generated one following the correct format for the values. It can also be executed from the commandline.


## Installation 

1. Clone the repository: `git clone https://github.com/tzero86/quick_mac_changer.git`
2. Install prerequisites: `pip3 install -r requirements.txt`

Execute by running: `sudo python3 qmc.py`

## Usage
![](https://i.imgur.com/ci01dBz.png)

As you can probably have guessed from the image above, QMC is very simple to use. It will automatically detect and list the available Network Interfaces. That way you can quickly Specify which interface you want the MAC address getting changed for and get it done in seconds.


## Commandline Usage

This tool also supports getting called from the commandline, see the help for details. 
![](https://i.imgur.com/bqw2MF0.png)

Simply run: `sudo python3 qmc.py -h` to see the options you can specify.

For Example if you want to change the MAC Address of WLAN0, run:
``bash
sudo python3 qmc.py -i wlan0 -m 00:11:22:33:44:55
``

You can also run -l to list all the interfaces from the commandline:
List Interfaces: `sudo python3 qmc.py -l`


> **Note**: This tool requires running it as root/sudo.


That's all for now...

@tzero86