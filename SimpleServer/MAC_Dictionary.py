'''
Created on Oct 25, 2013

@author: admshuyang
'''

from Connect2DB import *;
from StationManage import *;


class StartEndNode:
    def __init__(self, mac, database):
        self.Mac = mac;
        self.PreviousTime = None;
        self.PreviousLocation = None;
        
        self.NextTime = None;
        self.NextLocation = None;
        
        self.__DataInsert__ = database;
        pass;
    
    def Update(self, currentLocation, currentTime):
        
        if (currentLocation is self.NextLocation):
            self.NextTime = currentTime;
        else: # if the currentLocation is not equal to NextLocation
            
            #===================================================================
            # push next to previous
            #===================================================================
            self.__PushNext2Prev__(currentLocation, currentTime);
            
            #===================================================================
            # store the trip (mac, previousLocation[startLocation], previousTime[startTime], NextLocation[endLocation], NextTime[endTime]) in MySQL
            #===================================================================
            if(self.PreviousLocation is not None):
                self.__DataInsert__.InsertTrip(self.Mac, self.PreviousLocation, self.PreviousTime, self.NextLocation, self.NextTime);
            
    
    def __PushNext2Prev__(self, currentLocation, currentTime):
        self.PreviousLocation = self.NextLocation;
        self.PreviousTime = self.NextTime;
        
        self.NextLocation = currentLocation;
        self.NextTime = currentTime;
    
    #only used to test    
    def Print(self):
        print 'PreviousTime: {0};    PreviousLocation: {1};    NextTime:{2};    NextLocation:{3}'.format(self.PreviousTime, self.PreviousLocation, self.NextTime, self.NextLocation);
            
class ManageMac:
    
    def __init__(self):
        self.MacAddr = dict();
        self.__DataInsert__ = MacData2MySQL();
        
    def NewMacComing(self, newMac, currentLocation, currentTime):
        
        if (self.MacAddr.has_key(newMac)):
            self.MacAddr[newMac].Update(currentLocation, currentTime);
        else:
            self.MacAddr[newMac] = StartEndNode(newMac, self.__DataInsert__);
            self.MacAddr[newMac].Update(currentLocation, currentTime);
        
    #2013-10-26 04:21:18.186000;Speedway-Euclide;['00:21:06:7D:22:24', '00:25:BF:F0:0D:19', 'F4:B7:E2:39:92:18']
    def NewMacComing_RawData(self, data):
        StringSplit = data.split(';');
        CurrentTime = StringSplit[0];
        Location = StringSplit[1];
        MacString = StringSplit[2].split('\'');
        
        for i in range((len(MacString)-1)/2):
            #MacList.append(MacString[2*i+1]);
            self.NewMacComing(MacString[2*i+1], Location, CurrentTime);
            
        
        
        


        
