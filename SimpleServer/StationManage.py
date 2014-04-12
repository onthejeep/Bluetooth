'''
Created on Oct 31, 2013

@author: admshuyang
'''

from MAC_Dictionary import *;


class Station:
    
    def __init__(self, manageMac):
        self.Location = None;
        self.UpdateTime = None;
        self.MacAddr = dict();
        self.Update_Clear = 0;
        self.__CycleInterval__ = 2;# if a Mac has not been updated for 2*10.24 seconds, send this Mac out
        self.__ManageMac__ = manageMac;
        self.__DeletedItemList__ = [];
        
    def Print(self):
        for item in self.MacAddr:
            print item, self.MacAddr[item];
        print '\n\n\n';
        
    def NewMacComing(self, CurrentTime, Location, MacString):
        
        #2013-10-26 04:21:18.186000;Speedway-Euclide;['00:21:06:7D:22:24', '00:25:BF:F0:0D:19', 'F4:B7:E2:39:92:18']
        #=======================================================================
        # StringSplit = data.split(';');
        # CurrentTime = StringSplit[0];
        # Location = StringSplit[1];
        # MacString = StringSplit[2].split('\'');
        #=======================================================================
        
        self.Location = Location;
        self.UpdateTime = CurrentTime;
        
        #if the new data is coming, the old Mac will be set as "not be found" by default
        for item in self.MacAddr:
            self.MacAddr[item][1] += 1;
        
        for i in range((len(MacString)-1)/2):
            Mac = MacString[2*i+1];
            
            if(self.MacAddr.has_key(Mac)):
                # if there is an existing Mac, set it as zero, which means the Mac is still at this station
                self.MacAddr[Mac][0] = CurrentTime;
                self.MacAddr[Mac][1] = 0;
            else:
                self.MacAddr[Mac] = [CurrentTime, 0];
                
        for item in self.MacAddr:
            # if the times we found equals to self.__CycleInterval__, send it out, and delete it
            if(self.MacAddr[item][1] is self.__CycleInterval__):
                self.__ManageMac__.NewMacComing(item, self.Location, self.MacAddr[item][0]);
                self.__DeletedItemList__.append(item);
                
        for item in self.__DeletedItemList__:
            del self.MacAddr[item];
            
        del self.__DeletedItemList__;
        self.__DeletedItemList__ = [];
        
        #Test
        self.Print();
        
class StationManage:
    def __init__(self):
        self.__ManageMac__ = ManageMac();
        self.__Stations__ = dict();
        
    def NewMacComing_RawData(self, data):
        #2013-10-26 04:21:18.186000;Speedway-Euclide;['00:21:06:7D:22:24', '00:25:BF:F0:0D:19', 'F4:B7:E2:39:92:18']
        StringSplit = data.split(';');
        CurrentTime = StringSplit[0];
        Location = StringSplit[1];
        MacString = StringSplit[2].split('\'');
        
        if(self.__Stations__.has_key(Location)):
            pass;
        else:
            self.__Stations__[Location] = Station(self.__ManageMac__);
            
        self.__Stations__[Location].NewMacComing(CurrentTime, Location, MacString);
                











            