'''
Created on Oct 26, 2013

@author: admshuyang
'''

from xml.dom import minidom;

class ReadConfig:
    def __init__(self, configFile):
        self.__ConfigFile__ = configFile;
        self.__XmlDoc = minidom.parse(self.__ConfigFile__);
        pass;
    
    def GetNodeValue(self, tagName):
        NodeList = self.__XmlDoc.getElementsByTagName(tagName);
        return NodeList[0].firstChild.nodeValue;
