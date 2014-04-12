'''
Created on Oct 17, 2013

@author: shu
'''

import socket;
import ReadXML;
import threading;
import thread;
import datetime;
import time;
import SaveRawFile;
from multiprocessing import Process, Queue;

def ParseReceivedData(queue):
    
    #===========================================================================
    # Shared Memory
    #===========================================================================
    #Stations =  StationManage();
    
    #Predefined Variables
    Message = None;
    
    while True:
        if not queue.empty():
            Message = queue.get();
            #Stations.NewMacComing_RawData(Message);
        else:
            pass;

class ThreadServerCreation(threading.Thread):
    
    def __init__(self, host, port, size, queue):
        threading.Thread.__init__(self);
    
        self.Host = host;
        self.Port = port;
        self.Size = size;
        self.RecordFile = SaveRawFile.SaveRaw();
        self.Queue = queue;
        
        #Bind by UDP and listen to a port
        self.S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
        
        self.S.bind((self.Host,int(self.Port)));
        print 'start listening...';
        
    def run(self):
       
        while True:
            try:
                data, address = self.S.recvfrom(self.Size);
                
                if data:
                    print '{0}'.format(data);
                    #self.Queue.put(data);
                    
                    self.RecordFile.WriteMAC(data);
                else:
                    continue;
                
                del data;
                del address;
                
            except socket.gaierror:
                print socket.gaierror.message;
                print 'exit the thread...'
    

def MonitorThreadLive(thread, host, port, size, queue):
    
    CurrentMontiorThread = thread;
    
    while True:
        if not CurrentMontiorThread.is_alive():
            print 'not alive at ' + str(datetime.datetime.now());
            ThreadNew = ThreadServerCreation(host, port, size, queue);
            ThreadNew.start();
            
            CurrentMontiorThread =   ThreadNew;
        
        time.sleep(2);
        
def main():
    
    #Predefined Variables
    Configuration = ReadXML.ReadConfig('config-server.xml');
    Port = int(Configuration.GetNodeValue('Port'));
    Host = Configuration.GetNodeValue('Host');
    Size = int(Configuration.GetNodeValue('Size'));
    
    #Put the received MAC in a queue
    ReceivedData = Queue();
    
    #Create a Process to parse the data in the queue
    #ReceivedDataProcess = Process(target = ParseReceivedData, args = (ReceivedData,));
    #ReceivedDataProcess.start();
    
    try:
        ServerThread = ThreadServerCreation(Host, Port, Size, ReceivedData);
        ServerThread.start();
        thread.start_new_thread(MonitorThreadLive, (ServerThread, Host, Port, Size, ReceivedData,));
    except:
        print "Error: unable to start thread"; 
    
    while True:
        pass;

if __name__ == "__main__":
    main();
    
    
    
    