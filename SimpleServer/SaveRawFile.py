'''
Created on Nov 6, 2013

@author: shu
'''


import datetime;
import os;

class SaveRaw:
    def __init__(self):
        self.File = None;
        self.Hour = None;
        
        self.StationFiles = dict();
        
    def WriteMAC(self, data):
        CurrentTime = datetime.datetime.now();
        
        Year = CurrentTime.year;
        Month = CurrentTime.month;
        Date = CurrentTime.day;
        Hour = CurrentTime.hour;
        
        DirectoryPath = 'MAC_Data/{0:04d}/{0:04d}_{1:02d}/{0:04d}_{1:02d}_{2:02d}'.format(Year, Month, Date);
        
        if (self.Hour is not Hour):
            self.Hour = Hour;
        
            FileName = '{0:04d}_{1:02d}_{2:02d}_{3:02d}.txt'.format(Year, Month, Date, Hour);
            FilePath = '{0}/{1}'.format(DirectoryPath, FileName);
            
            if (os.path.exists(path = DirectoryPath)):
                pass;
            else:
                os.makedirs(name = DirectoryPath);
                
            if (self.File is None):pass;
            else: self.File.close();
            
            self.File = open(FilePath, 'a');

        self.File.write(data + '\n');
        
    def WriteMAC_ServerSide(self, data):
        CurrentTime = datetime.datetime.now();
        
        Year = CurrentTime.year;
        Month = CurrentTime.month;
        Date = CurrentTime.day;
        Hour = CurrentTime.hour;
        
        Location = data.split(';')[1];
        
        DirectoryPath = 'MAC_Data/{0}/{1:04d}/{1:04d}_{2:02d}/{1:04d}_{2:02d}_{3:02d}'.format(Location, Year, Month, Date);
        
        if (self.Hour is not Hour):
            self.Hour = Hour;
        
            FileName = '{0:04d}_{1:02d}_{2:02d}_{3:02d}.txt'.format(Year, Month, Date, Hour);
            FilePath = '{0}/{1}'.format(DirectoryPath, FileName);
            
            if (os.path.exists(path = DirectoryPath)):
                pass;
            else:
                os.makedirs(name = DirectoryPath);
                
            if (not self.StationFiles.has_key(Location)):pass;
            else: self.StationFiles[Location].close();
            
            print FilePath;
            self.StationFiles[Location] = open(FilePath, 'a');

        self.StationFiles[Location].write(data + '\n');
        
        
    