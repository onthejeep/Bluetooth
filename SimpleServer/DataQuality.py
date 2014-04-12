'''
Created on Nov 25, 2013

@author: admshuyang
'''
import ReadXML;
import os;
import time;
import datetime;


class DataSumamryStatistics:
    def __init__(self):
        self.PerHour = [0] * 24;
        self.PerDay = 0;
        
    def Summation(self):
        self.PerDay = sum(self.PerHour);

class DataQuality:
    def __init__(self):
        self.Stations = dict();
        pass;
    
    def ReadStations(self):
        #Predefined Variables
        Configuration = ReadXML.ReadConfig('config-server.xml');
        StationList = Configuration.GetNodeValues('Station');
        
        for station in StationList:
            self.Stations[station] = DataSumamryStatistics();
        
    def ReadSingleFile(self, fullPath):
        FileName = os.path.basename(fullPath);
        Hour = int(FileName[11:13]);
        File = open(fullPath, 'r');
        for line in File:
            self.Stations[line.split(';')[1]].PerHour[Hour] +=1;
        
        File.close();
        
    def ReadFile(self, year, month, day):
        Path = '{0}/{1}/{2}/{3}'.format('MAC_Data', year, '{0:4d}_{1:2d}'.format(year, month), '{0:4d}_{1:2d}_{2:2d}'.format(year, month, day));
        
        for dataFile in os.listdir(Path):
                if dataFile.endswith(".txt"):
                    FullPath = '{0}/{1}'.format(Path, dataFile);
                    self.ReadSingleFile(FullPath);
        
            
    def PrintSummary(self):
        
        #----the first line
        print 'Time of day,';
        for station in self.Stations:
            print station, ',';
        print '\n';
        #----the first line
        
        for i in range(24):
            print i, ',';
            for station in self.Stations.keys():
                print self.Stations[station].PerHour[i], ',';
            print '\n';
            
        #----the last line
        print 'Daily,';
        for station in self.Stations.keys():
            print self.Stations[station].PerDay, ',';
        print '\n';
        #----the last line
        
    def Print2File(self, fileName):
        File = open(fileName, 'w');
        
        #----the first line
        File.write('Time of day,');
        for station in self.Stations.keys():
            File.write('{0},'.format(station));
        File.write('\n');
        #----the first line
        
        for i in range(24):
            File.write('{0},'.format(i));
            for station in self.Stations.keys():
                File.write('{0},'.format(self.Stations[station].PerHour[i]));
                self.Stations[station].Summation();
            File.write('\n');
        
        
        #----the last line
        File.write('Daily,');
        for station in self.Stations.keys():
            File.write('{0},'.format(self.Stations[station].PerDay));
        File.write('\n');
        #----the last line
        
        File.close();
    
    def GetSummary(self, year, month, day):
        SummaryFile = 'DataSummary/{0}_{1}_{2}.csv'.format(year, month, day);
        self.ReadStations();
        self.ReadFile(year, month,day);
        self.Print2File(SummaryFile);
        
    def Exec(self):
        time.sleep(1 * 3600);
        
        CurrentTime = datetime.datetime.now();
        Yesterday = CurrentTime + datetime.timedelta(days = -1);
        Year = Yesterday.year;
        Month = Yesterday.month;
        Day = Yesterday.day;
        
        if (CurrentTime.hour == 8):
            self.GetSummary(Year, Month, Day);
        


Summary = DataQuality();
#Summary.GetSummary(2013, 11, 23);
Summary.Exec();
        