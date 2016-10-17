import unittest
import Navigation.prod.Fix as Fix
import datetime
import xml.etree.ElementTree as ET

def Fix(logFile):
	logFile= open("log.txt","a")
    if(len(logFile)> 1):
	    logFile = open(logFile, "a+")
		logFile.write()
		logFile.close()
     else:
	    logFile = open(logFile, "a+")
		logFile.write()
		logFile.close()
	
def setSightingFile(sightingFile):
	logFile= open("log.txt","a+")
    if len(logFile) > 1:
     	return True
    else:
     	return False
	
def getSightings():
	approximateLatitude = "0d0.0"			
	approximateLongitude = "0d0.0"
		
	tree = ET.parse('sightings.xml')
	logFile= open("log.txt","a+")
    if len(logFile) > 1:
		logFile = open(logFile, "a+")
		logFile.write('LOG 	:', datetime.datetime.now(),' Start of log')
		logFile.write('LOG  :', datetime.datetime.today(),' Start of sighting file : sightings.xml')
	for sighting in root.findall('sighting'):
		body = sighting.find('body').text
		date = sighting.find('date').text
		time = sighting.find('time').text
		observation = sighting.find('observation').text
		height = sighting.find('height').text
		temperature = sighting.find('temperature').text
		pressure = sighting.find('pressure').text
		horizon = sighting.find('horizon').text
		observedAltitude = horizon
		logFile.write('LOG	:', datetime.datetime.utcnow(),body, date, time, observation)
		logFile.write('LOG  :', datetime.datetime.today(),' End of sighting file : sightings.xml')
	if observation in (natural) :
		dip = ( -0.97 * sqrt( height ) ) / 60
	else			
		dip = 0			
		refraction = ( -0.00452 * pressure ) / ( 273 + celsius( temperature ) ) / tangent( altitude )			
		adjustedAltitude = observedAltitude + dip + refraction 			
		round adjustedAltitude to the nearest 0.1 arc-minute
		logFile.close()
	return (approximateLatitude, approximateLongitude)
		