'''
Created on Oct 26, 2013

@author: admshuyang
'''

from Connect2DB import *;

Cursor = Connect2MySQL.GetInisitance().cursor();

Cursor.execute('select * from trips');

for Row in Cursor.fetchall():
    print Row;