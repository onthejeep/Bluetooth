'''
Created on Oct 25, 2013

@author: admshuyang
'''

from StationManage import *;
#===============================================================================
# Unit Test
# 1. 00-FF-TT-EE-SS-RR
# 2. 00-FF-TT-EE-SS-WW
# 3. 00-FF-TT-EE-SS-GG
#===============================================================================

Stations = StationManage();

Stations.NewMacComing_RawData("""2013-10-26 04:21:18.186000;Speedway-Euclide;['00:21:06:7D:22:00', '00:25:BF:F0:0D:00', 'F4:B7:E2:39:92:00']""");
Stations.NewMacComing_RawData("""2013-10-26 04:21:18.186000;Speedway-Tucson;['00:21:06:7D:22:11', '00:25:BF:F0:0D:11', 'F4:B7:E2:39:92:11']""");

Stations.NewMacComing_RawData("""2013-10-26 04:22:18.186000;Speedway-Euclide;['00:21:06:7D:22:00']""");
Stations.NewMacComing_RawData("""2013-10-26 04:22:18.186000;Speedway-Tucson;['00:21:06:7D:22:11', '00:25:BF:F0:0D:00', 'F4:B7:E2:39:92:00']""");
Stations.NewMacComing_RawData("""2013-10-26 04:22:18.186000;Speedway-Oracal;['00:21:06:7D:22:22']""");

Stations.NewMacComing_RawData("""2013-10-26 04:23:18.186000;Speedway-Euclide;['00:21:06:7D:22:00']""");
Stations.NewMacComing_RawData("""2013-10-26 04:23:18.186000;Speedway-Tucson;['00:21:06:7D:22:11']""");
Stations.NewMacComing_RawData("""2013-10-26 04:23:18.186000;Speedway-Oracal;['00:21:06:7D:22:22', '00:25:BF:F0:0D:00', 'F4:B7:E2:39:92:00']""");

Stations.NewMacComing_RawData("""2013-10-26 04:24:18.186000;Speedway-Euclide;['00:21:06:7D:22:00']""");
Stations.NewMacComing_RawData("""2013-10-26 04:24:18.186000;Speedway-Tucson;['00:21:06:7D:22:11']""");
Stations.NewMacComing_RawData("""2013-10-26 04:24:18.186000;Speedway-Oracal;['00:21:06:7D:22:22']""");

Stations.NewMacComing_RawData("""2013-10-26 04:25:18.186000;Speedway-Euclide;['00:21:06:7D:22:00']""");
Stations.NewMacComing_RawData("""2013-10-26 04:25:18.186000;Speedway-Tucson;['00:21:06:7D:22:11']""");
Stations.NewMacComing_RawData("""2013-10-26 04:25:18.186000;Speedway-Oracal;['00:21:06:7D:22:22']""");



