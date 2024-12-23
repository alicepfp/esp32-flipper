import network
import binascii
import machine
import time
import os


class netscan:
    def __init__(self, wifi, sdcard, vfs):
        self.wifi = network.WLAN(network.WLAN.IF_STA)
        self.sdcard = machine.SDCard(slot=3) #sck=18, miso=19, mosi=23, cs=5
        self.vfs = os.VfsFat(sdcard)
        os.mount(vfs, '/sd')
        wifi.active(True)
    
    def scanner(self, wifi, scanner, results):
        auth = {'0': 'open', '1': 'WEP', '2': 'WPA-PSK', '3': 'WPA2-PSK', '4': 'WPA/WPA2-PSK'}
        visibility = {'True': 'hidden', 'False': 'visible'}
        bssid = binascii.hexlify('bssid')
        
        try:
            scanner = wifi.scan()
            print('{} networks found'.format(len(scanner)))
            for i, w in enumerate(scanner):
                results = '{}. SSID: {}, BSSID: {}, Channel: {}, RSSI: {}, Auth: {}, Visibility: {}'.format(i+1, w[0], bssid, w[2], w[3], auth[str(w[4])], visibility[str(w[5])])
                print(results)
        except OSError as error:
            print(error)
    
    def saveinfo(self, results):
        timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        
        try:
            with open('/sd/scanner_{}.txt'.format(timestr), 'w') as f:
                f.write(results)
        except OSError as error:
            print(error)

class wifi_sniffer:
    def __init__(self, wlan, channel, sdcard, vfs):
        pass
    

class wifi_bruteforce:
    def __init__(self):
        pass
    

a