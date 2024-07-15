import re

def parser(output):
    # Define the regular expression pattern to match each line of the output
    pattern = re.compile(r'(\S+)\s+(\S+)\s+\S+\s+(\S+)\s+(\S+)\s+(\S+)')

    # Iterate over each line of the output, skipping the first header line
    for line in output.splitlines()[1:]:
        match = pattern.match(line)
        if match:
            interface, ip_address, method, status, protocol = match.groups()
            yield {
                interface: {
                    "IP-Address": ip_address,
                    "Method": method,
                    "Status": status,
                    "Protocol": protocol
                }   
            }

output = """Interface             IP-Address      OK? Method Status        Protocol
FastEthernet0/0       15.0.15.1       YES manual up            up
FastEthernet0/1       10.0.12.1       YES manual up            up
FastEthernet0/2       10.0.13.1       YES manual up            up
FastEthernet0/3       unassigned      YES unset  up            down
Loopback0             10.1.1.1        YES manual up            up
Loopback100           100.0.0.1       YES manual up            up
"""

# call parser function
ethernet_interface = {}
for dicts in parser(output):
    ethernet_interface.update(dicts)

#print the dictonary in correct format
print("{")
for interface, details in ethernet_interface.items():
    print(f"  \"{interface}\": {{")
    for key, value in details.items():
        print(f"    \"{key}\": \"{value}\",")
    print("  },")
print("}")
