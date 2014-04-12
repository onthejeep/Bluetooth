'''
Created on Oct 17, 2013

@author: shu
'''

import socket;
import ReadXML;

def main():
    
    #Predefined Variables
    backlog = 5;
    Configuration = ReadXML.ReadConfig('config-server.xml');
    Port = Configuration.GetNodeValue('Port');
    Host = Configuration.GetNodeValue('Host');
    Size = int(Configuration.GetNodeValue('Size'));
    
    #Bind by TCP and listen to a port
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
        try:
            client, address = s.accept();
            data = client.recv(Size);
            
            if data:
                print '{0}'.format(data);
                RecordFile.write('{0}\n'.format(data));
            else:
                client.close();
                del client;
                continue;
            
            del data;
            del address;
            
        except socket.gaierror:
            print socket.gaierror.message;
            client.close();
            del client;
    
    RecordFile.close();
    
    print 'exit the program...';


if __name__ == "__main__":
    main();