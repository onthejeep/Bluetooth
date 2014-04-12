'''
Created on Oct 17, 2013

@author: shu
'''

import socket;
import ReadXML;
from multiprocessing import Process, Queue;
from StationManage import StationManage;


def ParseReceivedData(queue):
    
    #===========================================================================
    # Shared Memory
    #===========================================================================
    Stations =  StationManage();
    
    #Predefined Variables
    Message = None;
    
    while True:
        if not queue.empty():
            Message = queue.get();
            Stations.NewMacComing_RawData(Message);
        else:
            pass;


def main():
    
    #Predefined Variables
    backlog = 5;
    Configuration = ReadXML.ReadConfig('config-server.xml');
    Port = Configuration.GetNodeValue('Port');
    Host = Configuration.GetNodeValue('Host');
    Size = int(Configuration.GetNodeValue('Size'));
    
    #Put the received MAC in a queue
    ReceivedData = Queue();
    
    #Create a Process to parse the data in the queue
    ReceivedDataProcess = Process(target = ParseReceivedData, args = (ReceivedData,));
    ReceivedDataProcess.start();
    
    #listen to a port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    s.bind((Host,int(Port)));
    s.listen(backlog);
    print 'start listening...';
    
    #==========================
    #Open a file to write
    try:
        RecordFile = open('RecordFile.txt', 'w+');
    except:
        print 'Could not open the file!';
    #==========================
        
    
    while True: 
        client, address = s.accept();
        
        data = client.recv(Size);
        
        if data:
            #print '{0}'.format(data);
            RecordFile.write('{0}\n'.format(data));
            ReceivedData.put(data);
            
        client.close();
        del data;
        del client;
        del address;
    
    RecordFile.close();
    
    print 'exit the program...';


if __name__ == "__main__":
    main();