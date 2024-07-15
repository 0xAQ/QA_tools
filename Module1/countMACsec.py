from scapy.all import rdpcap
import os

def count_macsec_packets(pcap_file):

    # Check if the PCAP file exists
    if not os.path.isfile(pcap_file):
        print("File does not exist")
        return

    # Read packets from the PCAP file
    packets = rdpcap(pcap_file)

    # MACsec packet filter
    MACSEC_ETHER_TYPE = 0x88E5

    #MACsec packet count
    count = 0

    # Iterating over each packet
    for packet in packets:
        # Checking if the packet is an Ethernet packet and has the MACsec 
        if packet.haslayer('Ether') and packet.type == MACSEC_ETHER_TYPE:
            count += 1

    # Print the total number of MACsec packets
    print("Number of MACsec packets: ", count)

    return count

#location of pcap file
pcap_file_path = '/home/aaquil/MACsec.pcap'
#function call
count_macsec_packets(pcap_file_path)

