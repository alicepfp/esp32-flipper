import usocket as socket
import wifi_lib as wifi
import packet_lib as packet
import network
import binascii
import machine
import time
import _thread
import os

machine.freq(240000000)


class Common:
    def __init__(self):
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)
        self.sdcard = machine.SDCard(slot=3)  # sck=18, miso=19, mosi=23, cs=5
        self.vfs = os.VfsFat(self.sdcard)
        self.timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        os.mount(self.vfs, '/sd')


class NetScan(Common):
    def __init__(self):
        super().__init__()
        self.sta.active(True)

    def scanner(self, results):
        auth = {0: 'open', 1: 'WEP', 2: 'WPA-PSK', 3: 'WPA2-PSK', 4: 'WPA/WPA2-PSK'}
        visibility = {True: 'hidden', False: 'visible'}

        try:
            scanner = self.sta.scan()
            print('{} networks found'.format(len(scanner)))
            for i, w in enumerate(scanner):
                ssid = w[0].decode('utf-8')
                bssid = binascii.hexlify(w[1]).decode('utf-8')
                channel = w[2]
                rssi = w[3]
                authmode = auth.get(w[4], 'unknown')
                hidden = visibility.get(w[5], 'unknown')
                results = ("{:d}: SSID: {}, BSSID: {}, Channel: {}, RSSI: {}, Auth: {}, Visibility: {}".format(
                    i + 1, ssid, bssid, channel, rssi, authmode, hidden))
                print(results)
        except OSError as e:
            print("Error scanning networks: {}".format(e))
        
        self.sta.active(False)
        return results

    def saveinfo(self, results):
        try:
            with open('/sd/scanner_{}.txt'.format(self.timestr), 'w') as f:
                f.write(results)
        except OSError as e:
            print("Error saving file: {}".format(e))

class PacketSniffer(Common):
    def __init__(self, channel, sck, pck):
        super().__init__()
        self.channel = int(channel)
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pck = wifi.packet()
        self.sta.active(True)
        self.sta.config(channel=self.channel)
    
    def channel_hopper(self):
        while (True):
            for ch in range(1, 13):
                self.sta.config(channel=ch)
                print("Hopping to channel {}".format(ch))
                time.sleep(5)
    
    def probe_req(self, probe_req_res):
        self.sck.bind(("127.0.0.1", 20001))
        while (True):
            try:
                temp_packet = self.sck.recv(4096)
                mv = memoryview(temp_packet)
                self.pck.update(mv)
                if (self.pck.fc_type == wifi.TYPE_MANAGEMENT) and (self.pck.fc_sub == wifi.TYPE_MANAGEMENT_PROBE_REQUEST):
                    tags = self.pck.decode_tags()
                    packet_src = wifi.raw_to_hex(self.pck.addr2).decode('utf-8')
                    packet_dst = wifi.raw_to_hex(self.pck.addr1).decode('utf-8')
                    packet_bssid = wifi.raw_to_hex(self.pck.addr3).decode('utf-8')
                    try:
                        probe_ssid = tags[0][0].decode('utf-8')
                        probe_req_res = "{:d} Probe Request: {} > {}  {} '{}'".format(self.channel,packet_src,packet_dst,packet_bssid,probe_ssid)
                        print(probe_req_res)
                    except OSError as e:
                        print("Error in probe request: {}".format(e))
            except OSError as e:
                print("Error: {}".format(e ,temp_packet))
    
    def probe_resp(self, probe_resp_res):
        self.sck.bind(("127.0.0.1", 20001))
        while (True):
            try:
                temp_packet = self.sck.recv(4096)
                mv = memoryview(temp_packet)
                self.pck.update(mv)
                if (self.pck.fc_type == wifi.TYPE_MANAGEMENT) and (self.pck.fc_sub == wifi.TYPE_MANAGEMENT_PROBE_RESPONSE):
                    packet_src = wifi.raw_to_hex(self.pck.addr2).decode('utf-8')
                    packet_dst = wifi.raw_to_hex(self.pck.addr1).decode('utf-8')
                    packet_bssid = wifi.raw_to_hex(self.pck.addr3).decode('utf-8')
                    try:
                        probe_ssid = tags[0][0].decode('utf-8')
                        probe_resp_res = "{:d} Probe Response: {} > {}  {} '{}'".format(self.channel,packet_src,packet_dst,packet_bssid,probe_ssid)
                        print(probe_resp_res)
                    except OSError as e:
                        print("Error in probe response: {}".format(e))
            except OSError as e:
                print("Error: {}".format(e ,temp_packet))
        
    def sniffer(self, probe_req_res, probe_resp_res, results):
        print("Starting UDP listener thread to recieve wifi packets...")
        probe_req = _thread.start_new_thread(self.probe_req, (probe_req_res))
        probe_resp = _thread.start_new_thread(self.probe_resp, (probe_resp_res))
        results = (probe_req, probe_resp)
        
        print("Starting the sniffer....")
        print(results)
        self.sta.active(False)
        self.sta.sniffer(ch=self.channel)
        
        _thread.start_new_thread(self.channel_hopper, ())
        print("Channel hopping thread started...")
        
        return results
    
    def saveinfo(self, results):
        try:
            with open('/sd/sniffer_{}.txt'.format(self.timestr), 'w') as f:
                f.write(results)
        except OSError as e:
            print("Error saving file: {}".format(e))

class NetBruteforce(Common):
    def __init__(self, passwords, ssid):
        super().__init__()
        self.sta.active(True)
        self.passwords = []
        self.ssid = ''
    
    def passwordlist(self):
        try:
            with open('/sd/passwords.txt', 'r') as f:
                self.passwords = f.read().splitlines()
        except OSError as e:
            print("Error reading password list: {}".format(e))
    
    def bruteforce(self):
        pass

class NetJammer(Common):
    def __init__(self):
        super().__init__()
        self.sta.active(True)
    
    def jammer(self):
        pass
    