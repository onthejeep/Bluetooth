'''
Created on Nov 7, 2013

@author: admshuyang
'''

import Connect2DB;
import re;
import datetime;
import os;

def NewMacComing_RawData(data, connection2DB):
        StringSplit = data.split(';');
        DetectedTimeString = StringSplit[0];
        
        Year_Month = DetectedTimeString.split('-');
        Year = Year_Month[0];
        Month = Year_Month[1];
        
        Location = StringSplit[1];
        MacString = StringSplit[2].split('\'');
        
        for i in range((len(MacString)-1)/2):
            #print MacString[2 * i + 1];
            connection2DB.InsertIndividualMAC(Year, Month, MacString[2 * i + 1], Location, DetectedTimeString, None);
            

Start_Year = 2014;
Start_Month = 1;
Start_Date = 1;
End_Year = 2014;
End_Month = 2;
End_Date = 6;

StartTime = datetime.datetime(Start_Year, Start_Month, Start_Date);
EndTime = datetime.datetime(End_Year, End_Month, End_Date);

TempTime = StartTime;

Connect2DB = Connect2DB.MacData2MySQL();

# try to create a new table using the initial information
Connect2DB.CreateNewTable('{0:04d}'.format(Start_Year), '{0:02d}'.format(Start_Month));

# import the data each day (from [Start_Year,Start_Month] to [End_Year, End_Date] )
while TempTime <= EndTime:
    Year = TempTime.year;
    Month = TempTime.month;
    Date = TempTime.day;
    
    for hour in range(24):     
        FileName = 'E:\\MAC_Data\\{0:04d}\\{0:04d}_{1:02d}\\{0:04d}_{1:02d}_{2:02d}\\{0:04d}_{1:02d}_{2:02d}_{3:02d}.txt'.format(Year, Month, Date, hour);
        
        if (os.path.exists(FileName) == False):
            continue;
        
        RawFile = open(FileName, 'r');
        
        for line in RawFile:
            NewMacComing_RawData(line, Connect2DB);
            
        print(FileName);
    
    Month_Previous = TempTime.month;
    TempTime = TempTime + datetime.timedelta(days = 1);
    Month_Next = TempTime.month;
    
    if(Month_Previous != Month_Next):
        Connect2DB.CreateNewTable('{0:04d}'.format(TempTime.year), '{0:02d}'.format(TempTime.month));
    