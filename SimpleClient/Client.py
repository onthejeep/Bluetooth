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

class ThreadSendingData(threading.Thread):
    
    def __init__(self, location, host, port):
        threading.Thread.__init__(self);
        
        self.Location = location;
        self.Host = host;
        self.Port = port;
        
        self.S = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.S.connect((self.Host, self.Port));
        
    def run(self):
        while (True):
            #===================================================================
            # TCP
            #===================================================================
            
            
            
            #Nearby_address = bluetooth.discover_devices(duration = 8, lookup_names = True);
            
            #Test=================
            # print '{0};{1};{2}'.format(datetime.datetime.now(), self.Location, Nearby_address);
            #=====================
            
            self.S.send('send some strings......');
            #s.send('{0};{1};{2}'.format(datetime.datetime.now(), self.Location, Nearby_address));
            #self.S.close();
            
            #del Nearby_address;
            #del s;
            
            time.sleep(2);

##### A function to monitor the thread
def MonitorThreadLive(thread):
    
    CurrentMontiorThread = thread;
    
    while True:
        if not CurrentMontiorThread.is_alive():
            print 'not alive at ' + str(datetime.datetime.now());
            
            Configuration = ReadXML.ReadConfig('config-client.xml');
            Location = Configuration.GetNodeValue('Location');
            Port = Configuration.GetNodeValue('Port');
            Host = Configuration.GetNodeValue('Host');
        
            Thread1 = ThreadSendingData(Location, Host, int(Port));
            Thread1.start();
            CurrentMontiorThread = Thread1;
        time.sleep(1);

def main():   
    try:        
        Configuration = ReadXML.ReadConfig('config-client.xml');
        Location = Configuration.GetNodeValue('Location');
        Host = Configuration.GetNodeValue('Host');
        Port = Configuration.GetNodeValue('Port');
        
        Thread1 = ThreadSendingData(Location, Host, int(Port));
        Thread1.start();
        thread.start_new_thread(MonitorThreadLive, (Thread1,));
        
    except:
        print "Error: unable to start thread";
    
    while 1:
        pass;

if __name__ == "__main__":
    main();