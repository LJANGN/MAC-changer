Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
#!/usr/bin/env python

import optparse
# Allows to get arguments from user and parse and use them in the code

import subprocess

import re

#Creating a parser object that can handle user input using arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i",  "--interface",  dest="interface", help="Interface  to change its MAC address")
    parser.add_option("-m",  "--mac",  dest="new_mac", help="New  MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("I-]  Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-]  Please specify an interface, use --help for more info")
    return options

# This function can either be here, before the get_current_mac(interface) -function, or after it
def change_mac(interface, new_mac):
    print("[+] Changing MAC adress for "  + interface +  " to "  + new_mac)
    subprocess.call(["ifconfig", interface,  "down"])
    subprocess.call(["ifconfig", interface,  "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface,  "up"])

# Using a regular expression (regex) search from the "ifconfig" output to locate the MAC address in the text
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # implementing regular expression
    mac_address_search_result =  re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",  ifconfig_result)
    if  mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could  not  find MAC address")

#These 8 lines are the code for the actual main program!
options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current  MAC = "  + str(current_mac))
change_mac(options.interface, options.new_mac)
#This is same line as above. Its needed first to show the current MAC and then here to show the new MAC
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was succesfully changed to " + current_mac)
else: print("[-] MAC address did not get changed.")
