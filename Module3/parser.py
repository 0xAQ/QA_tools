import re

def parser(output):
    # Define the regular expression pattern to match each line of the output
    pattern = re.compile(r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+\s+\S+)\s')

    # Iterate over each line of the output, skipping the first header line
    for line in output.splitlines()[3:]:
        match = pattern.match(line)
        if match:
            ap , slots, model, ether, radio,  cc, rd, ip_address, state, location= match.groups()
            yield {
                ap: {
                    "Slots":slots,
                    "AP-Model":model,
                    "Ethernet-MAC":ether,
                    "Radio-MAC":radio,
                    "Country-Code":cc,
                    "Regulatory-Domain":rd,
                    "IP-Address": ip_address,
                    "State": state,
                    "Location": location
                }
            }

def print_dict():
    print("{")
    for ap, details in ethernet_interface.items():
        print(f"  \"{ap}\": {{")
        for key, value in details.items():
            print(f"    \"{key}\": \"{value}\",")
        print("  },")
    print("}")

output = """
AP Name                 Slots               AP Model               Ethernet MAC        Radio MAC         CC   RD    IP Address        State        Location
-------------------------------------------------------------------------------------------------------------------------------------------------------------
APBC26.C7A3.1970          2               AIR-AP3802E-B-K9       bc26.c7a3.1970     00b7.7166.bea0      US   -B   192.165.7.199     Registered   default location                
APA4B2.3904.1F0C          3                 C9130AXI-B           a4b2.3904.1f0c     2c57.4156.9000      US   -B   192.165.3.119     Registered   default location                
AP6849.92F9.8930          3                 CW9163E-B            6849.92f9.8930     ecf4.0c4f.3360      US   -B   192.165.8.139     Registered   default location    
"""

# call parser function
ethernet_interface = {}
for dicts in parser(output):
    ethernet_interface.update(dicts)

print_dict()

