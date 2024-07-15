from pyats import aetest

class test_case(aetest.Testcase):
    @aetest.setup
    def initial_setup(self):
        self.output={}
        self.output={'AP6849.92F9.8930': {'AP-Model': 'CW9163E-B',
                      'Country-Code': 'US',
                      'Ethernet-MAC': '6849.92f9.8930',
                      'IP-Address': '192.165.8.139',
                      'Location': 'default location',
                      'Radio-MAC': 'ecf4.0c4f.3360',
                      'Regulatory-Domain': '-B',
                      'Slots': '3',
                      'State': 'Registered'},
 'APA4B2.3904.1F0C': {'AP-Model': 'C9130AXI-B',
                      'Country-Code': 'US',
                      'Ethernet-MAC': 'a4b2.3904.1f0c',
                      'IP-Address': '192.165.3.119',
                      'Location': 'default location',
                      'Radio-MAC': '2c57.4156.9000',
                      'Regulatory-Domain': '-B',
                      'Slots': '3',
                      'State': 'Registered'},
 'APBC26.C7A3.1970': {'AP-Model': 'AIR-AP3802E-B-K9',
                      'Country-Code': 'US',
                      'Ethernet-MAC': 'bc26.c7a3.1970',
                      'IP-Address': '192.165.7.199',
                      'Location': 'default location',
                      'Radio-MAC': '00b7.7166.bea0',
                      'Regulatory-Domain': '-B',
                      'Slots': '2',
                      'State': 'Registered'}}
    @aetest.test
    def verify_ap_details(self):
        for apname,ap_details in self.output.items():
            print(f"AP NAME: {apname}")
            print(f"AP Slots: {ap_details['Slots']}")
            print(f"AP model: {ap_details['AP-Model']}")
            print(f"Ethernet MAC: {ap_details['Ethernet-MAC']}")
            print(f"Country Code: {ap_details['Country-Code']}")
            print(f"Regulatory Domain: {ap_details['Regulatory-Domain']}")
            print(f"IP-Address: {ap_details['IP-Address']}")
            print(f"State: {ap_details['State']}")
            print(f"Location: {ap_details['Location']}")
            print()

    @aetest.test
    def verify_status(self):
        for apname,ap_details in self.output.items():
            State= ap_details['State']
            assert State == 'Registered',f"test failed for {apname} due to improper state"

if __name__=='__main__':
    result=aetest.main()
    print(result)
