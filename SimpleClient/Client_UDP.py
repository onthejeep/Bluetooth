'''
Created on Oct 17, 2013

@author: shu
'''
import socket;
import time;
import datetime;
import threading;
import thread;
import bluetooth;
import ReadXML;
import os;
import signal;
import SaveRawFile;

class ThreadSendingData(threading.Thread):
    
    def __init__(self, location, host, port, rawFile):
        threading.Thread.__init__(self);
        
        self.Location = location;
        self.Host = host;
        self.Port = port;
        self.SaveFile = rawFile;
        
    def run(self):
        while (True):
            
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
            
            Nearby_address = bluetooth.discover_devices(duration = 3, lookup_names = False);
            
            MacData = '{0};{1};{2}'.format(datetime.datetime.now(), self.Location, Nearby_address);
            
            s.sendto(MacData, (self.Host, self.Port));
            #print '{0};{1}:{2}'.format(datetime.datetime.now(), self.Location, Nearby_address);
            self.SaveFile.WriteMAC(MacData);
            
            del Nearby_address;
        s.close();


def MonitorSendingThreadLive(thread, location, host, port, rawFile):
    
    CurrentMontiorThread = thread;
    
    while True:
        if not CurrentMontiorThread.is_alive():
            print 'not alive at ' + str(datetime.datetime.now());
        
            Thread1 = ThreadSendingData(location, host, int(port), rawFile);
            Thread1.start();
            CurrentMontiorThread = Thread1;
        time.sleep(2);
        

class RestartBluetoothApplet(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self);
        
        self.ProcessName_Short = 'bluetooth-applet';
        self.ProcessName_Long = None;
        
    def run(self):
            
        for line in os.popen("ps xa"):
            fields = line.split();
            pid = fields[0];
            self.ProcessName_Long = fields[4];
            
            if self.ProcessName_Long.find(self.ProcessName_Short) >= 0:
                os.kill(int(pid), signal.SIGILL);
            else:
                pass;
            
        time.sleep(1);
        #Restart the process
        try:
            result = os.system('bluetooth-applet');
            print result;
            
        except:
            print '''Couldn't restart Bluetooth-applet''';
            
            
def RestartBluetoothApplet_12Hours():
    while True:
        time.sleep(1 * 3600);
        #Thread1 = RestartBluetoothApplet();
        #Thread1.start();
        if (datetime.datetime.now().hour == 3):
            os.system('echo uapwd2012 | sudo -S shutdown -r now');
        
        if (datetime.datetime.now().hour == 5):
            os.system('echo uapwd2012 | sudo -S ntpdate 166.89.240.5');
		if (datetime.datetime.now().hour == 11):
            os.system('echo uapwd2012 | sudo -S ntpdate 166.89.240.5');
		if (datetime.datetime.now().hour == 16):
            os.system('echo uapwd2012 | sudo -S ntpdate 166.89.240.5');
        
        #del Thread1;

def MonitorRestartThreadLive(thread):
    
    CurrentMontiorThread = thread;
    
    while True:
        if not CurrentMontiorThread.is_alive():
            print 'not alive at ' + str(datetime.datetime.now());
            
            Thread2 = RestartBluetoothApplet();
            Thread2.start();
            CurrentMontiorThread = Thread2;
        time.sleep(2);
       
def main():   
    try:
        
        Configuration = ReadXML.ReadConfig('config-client.xml');
        Location = Configuration.GetNodeValue('Location');
        Host = Configuration.GetNodeValue('Host');
        Port = Configuration.GetNodeValue('Port');
        
        RawFile = SaveRawFile.SaveRaw();
        
        Thread1 = ThreadSendingData(Location, Host, int(Port), RawFile);
        Thread1.start();
        thread.start_new_thread(MonitorSendingThreadLive, (Thread1, Location, Host, int(Port), RawFile,));
        
        #=======================================================================
        # Thread2 = RestartBluetoothApplet();
        # Thread2.start();
        #=======================================================================
        thread.start_new_thread(RestartBluetoothApplet_12Hours,());
        
    except:
        print "Error: unable to start thread"
    
    while 1:
        pass;

if __name__ == "__main__":
    main();
