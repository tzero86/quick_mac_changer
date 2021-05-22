#!/usr/bin/env python
import os
import re
import subprocess
import sys
import generate_mac
import netifaces
from netifaces import interfaces, ifaddresses
from colorama import Fore, Back

# GLOBALS
f_blue = Fore.BLUE
f_white = Fore.WHITE
f_yellow = Fore.YELLOW
f_red = Fore.RED
f_green = Fore.GREEN
f_cyan = Fore.CYAN
rst = Fore.RESET


def welcome():
    print(f_red + f"""


    ████████▄     ▄▄▄▄███▄▄▄▄    ▄████████ 
    ███    ███  ▄██▀▀▀███▀▀▀██▄ ███    ███ 
    ███    ███  ███   ███   ███ ███    █▀  
    ███    ███  ███   ███   ███ ███        
    ███    ███  ███   ███   ███ ███        
    ███    ███  ███   ███   ███ ███    █▄  
    ███  ▀ ███  ███   ███   ███ ███    ███ 
     ▀██████▀▄█  ▀█   ███   █▀  ████████▀  

                      ▀█{rst} Quick MAC Changer by {f_yellow}@tzero86 {f_red}█▀{rst}                                 
          """ + Fore.RESET)


# We generate a properly formatted random MAC Address using generate_mac module.
def menu():
    while True:
        welcome()
        check_root()
        list_interfaces()
        target_interface = str(
            input(f"{f_green}[Select Interface]{rst} Enter the name of the interface or press "
                  "CTRL+C to EXIT: "))
        if target_interface and target_interface.strip():
            new_address = str(input(f"{f_green}[Input MAC Address]{rst} Enter the MAC address or leave it blank to "
                                    "generate one automatically: " + rst))
            if new_address.strip() and re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$",
                                                new_address.lower()):
                change_mac(target_interface, new_address)
            else:
                print(f'{f_red}[ERROR] For some reason we did not like that MAC Address, generating a random one for '
                      f'you.{rst}')
                try:
                    change_mac(target_interface, get_random_mac_address())
                except:
                    print(f'{f_red}[ERROR] You MUST specify a valid interface name like  -> {f_cyan}wlan0{rst} '
                          f'or {f_cyan}enp4s0{rst}')
                    menu()
                break
        else:
            print(f'{f_red}[ERROR] You MUST specify an interface, for example -> wlan0 or enp4s0.{rst}')


# we need to list the network interfaces available in the system
def list_interfaces():
    print(f'{f_blue}[Working] Listing all available interfaces...{rst}')
    available_interfaces = interfaces()
    print(f"{f_green}[Available Interfaces Found] -> {f_cyan}{available_interfaces}{rst}")


# it gets the current MAC address assigned to the interface
def get_current_mac_address(target_interface):
    mac = netifaces.ifaddresses(target_interface)[netifaces.AF_LINK]
    print(
        f'{f_green}[Current MAC address] {f_cyan} interface: {target_interface} - MAC: {mac[0]["addr"]}{rst}')
    pass


# generates a random properly formatted MAC Address
def get_random_mac_address():
    return str(generate_mac.generate_mac.total_random())


def check_root():
    # At least on Manjaro we need to run it with sudo for it to work.
    # I also had to install net-tools to have ifconfig working.
    if not os.geteuid() == 0:
        sys.exit(f"{f_red}\n[ERROR] You Need to execute this script with Sudo/Root access!\n{rst}")


def change_mac(target_interface, new_address):
    print(f'{f_green}[Setting new MAC Address] Interface: {target_interface} | New MAC Address: {new_address} {rst}')
    get_current_mac_address(target_interface)
    # we call the subprocesses
    subprocess.call(f"ifconfig {target_interface} down", shell=True)
    subprocess.call(f"ifconfig {target_interface} hw ether {new_address}", shell=True)
    subprocess.call(f"ifconfig {target_interface} up", shell=True)
    subprocess.call("ifconfig", shell=True)
    get_current_mac_address(target_interface)
    print(f'\n{Back.LIGHTGREEN_EX}{Fore.BLACK}[SUCCESS]{rst}{Back.RESET} New MAC address {new_address} has been assigned to the target '
          f'interface {target_interface}{rst}')
    print(f'\n{f_green}[Bye] Thanks for using my shitty tool!{rst}')


if __name__ == "__main__":
    menu()
