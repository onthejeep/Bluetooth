'''
Created on Oct 17, 2013

@author: admshuyang
'''


import socket;
import time;
import random;
import threading;
             
class ThreadSendingData(threading.Thread):
    
    def __init__(self, host, port):
        threading.Thread.__init__(self);
        
        self.host = host;
        self.port = port;
        
    def run(self):
        while (True):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            s.connect((self.host, self.port));
            s.send('{0}; {1}'.format(random.random(), time.ctime(time.time())));
            s.close();
            
            time.sleep(3);
        
try:
    ThreadList = [];
     
    for i in range(10):
        Single = ThreadSendingData("localhost", 50000);
        ThreadList.append(Single);
        
    for i in range(10):
        ThreadList[i].start();
    
    #===========================================================================
    # Thread1 = ThreadSendingData("localhost", 50000);
    # Thread1.start();
    #===========================================================================
except:
   print "Error: unable to start thread"

while 1:
   pass;
