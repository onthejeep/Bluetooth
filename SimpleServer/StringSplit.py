'''
Created on Oct 26, 2013

@author: admshuyang
'''

from datetime import date, time, datetime;
import re

data = "2013-10-26 04:21:18.234567;Speedway-Euclide;['00:21:06:7D:22:24', '00:25:BF:F0:0D:19', 'F4:B7:E2:39:92:18']";

print len( data.split(';'));

print  data.split(';')[0];


current = datetime.strptime(data.split(';')[0], '%Y-%m-%d %H:%M:%S.%f');
print current.year, current.month;


addr =  data.split(';')[2];

print len(addr.split('\''));
print addr.split('\'')[1];
print addr.split('\'')[3];
print addr.split('\'')[5];




