import unittest
import Navigation.prod.Fix as Fix
import datetime
import math
import xml.etree.ElementTree as ET
import nltk

def __init__(logFile):
     functionName = "Fix.__init__: "
try :
    logFile= open("C:\\Users\\homeindia\\Desktop\\Log.txt")
    if len(logFile) > 1:
		logFile = open(logFile, "a+")
		logFile.write('LOG 	:', datetime.datetime.now(),' Log file','\t')
    logFile.close()
except IOError:
    print('file cannot be created or appended for whatever', logFile)
	
def setSightingFile(sightingFile):
	try :
		if len(logFile) > 1:
			logFile.write('LOG	:', datetime.datetime.now(),' Sighting file','\t')
			logFile.write('LOG  :', datetime.datetime.today(),' Start of sighting file : sightings.xml')
			fix = ET.Element("fix")
			sighting = ET.SubElement(fix, "sighting")
			ET.SubElement=(sighting,"body").text= "Pollux"
			ET.SubElement=(sighting,"date").text= "2016-04-14"
			ET.SubElement=(sighting,"time").text= "23:50:14"
			ET.SubElement=(sighting,"observation").text= "015d04.9"
			ET.SubElement=(sighting,"height").text= "6.0"
			ET.SubElement=(sighting,"temperature").text= "72"
			ET.SubElement=(sighting,"pressure").text= "1010"
			ET.SubElement=(sighting,"horizon").text= "Artificial"
			sighting1 = ET.SubElement(fix, "sighting")
			ET.SubElement=(sighting1,"body").text= "Sirius"
			ET.SubElement=(sighting1,"date").text= "2017-04-17"
			ET.SubElement=(sighting1,"time").text= "09:30:30"
			ET.SubElement=(sighting1,"observation").text= "045d15.2"
			ET.SubElement=(sighting1,"height").text= "6.0"
			ET.SubElement=(sighting1,"temperature").text= "71"
			ET.SubElement=(sighting1,"pressure").text= "1010"
			ET.SubElement=(sighting1,"horizon").text= "Natural"
			tree = ET.ElementTree(fix)
			tree.write('/git/SoftwareProcess/SoftwareProcess/Navigation/test/sightings.xml')
			logFile.write('LOG	:', datetime.datetime.utcnow(),body, date, time, observation)
			logFile.write('LOG  :', datetime.datetime.today(),' End of sighting file : sightings.xml')
			logFile.close()
	except IOError:
		print('file cannot be created or appended for whatever', sightingFile)

def setAriesFile(ariesFile):
	tree = ET.parse('/git/SoftwareProcess/SoftwareProcess/Navigation/test/sightings.xml')
	try :
		ariesFile= open("/git/SoftwareProcess/SoftwareProcess/Navigation/test/ariesFile.txt","a+")
		if len(ariesFile) > 1:
			logFile.write('LOG	:', datetime.datetime.now(),' Aries file','\t')
		for sighting in root.findall('sighting'):
			date = sighting.find('date').text
			time = sighting.find('time').text
			observation = sighting.find('observation').text
		ariesFile.write('LOG	:', datetime.datetime.utcnow(),date,'\t')
		ariesFile.write('LOG	:', datetime.datetime.utcnow(),time,'\t')
		ariesFile.write('LOG	:', datetime.datetime.utcnow(),observation,'\n')
		ariesFile.close()
	except IOError:
		print('The file name is invalid. ', ariesFile)

def setStarFile(starFile):
	approximateLatitude = "0d0.0"
	tree = ET.parse('/git/SoftwareProcess/SoftwareProcess/Navigation/test/sightings.xml')
	try :
		starFile= open("/git/SoftwareProcess/SoftwareProcess/Navigation/test/starFile.txt","a+")
		if len(starFile) > 1:
			starFile.write('LOG 	:', datetime.datetime.now(),' Star file','\t')
		for sighting in root.findall('sighting'):
			body = sighting.find('body').text
			date = sighting.find('date').text
			observation = sighting.find('observation').text
		starFile.write('LOG	:', datetime.datetime.utcnow(),body,'\t')
		starFile.write(date,'\t')
		starFile.write(observation,'\t')
		starFile.write(approximateLatitude,'\n')
		starFile.close()
	except IOError:
		print('file cannot be created or appended for whatever', starFile)

def getSightingsgetSightings(assumedLatitude, assumedLongitude):
	try :
		tree = ET.parse('/git/SoftwareProcess/SoftwareProcess/Navigation/test/sightings.xml')
		logFile= open("/git/SoftwareProcess/SoftwareProcess/Navigation/test/log.txt","a+")
		if len(logFile) > 1:
			logFile = open(logFile, "a+")
			logFile.write('LOG 	:', datetime.datetime.now(),' Log file :','\t')
			logFile.write('/git/SoftwareProcess/SoftwareProcess/Navigation/test/log.txt','\n')
			logFile.write('LOG 	:', datetime.datetime.now(),' Sighting file :','\t')
			logFile.write('/git/SoftwareProcess/SoftwareProcess/Navigation/test/sightingss.xml','\n')
			logFile.write('LOG 	:', datetime.datetime.now(),' Aries file :','\t')
			logFile.write('/git/SoftwareProcess/SoftwareProcess/Navigation/test/aries.txt','\n')
			logFile.write('LOG 	:', datetime.datetime.now(),' Star file :','\t')
			logFile.write('/git/SoftwareProcess/SoftwareProcess/Navigation/test/star.txt','\n')
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
				hour = time[0:2]
				minitues = time[3:5]
				LHS = hour * 15 + minitues * 15			
				GHA = "60"
				geographicPositionLatitude = ( LHS + GHA ) / 360
				geographicPositionLongitude = ( LHS + GHA ) / 360
				adjustedgeographicPositionLatitude = round (geographicPositionLatitude,1)
				adjustedgeographicPositionLongitude = round (geographicPositionLongitude,1)
       /* if observation in (natural):
		    dip = ( -0.97 * sqrt( height ) ) / 60
        else			
		    dip = 0			
		 	refraction = ( -0.00452 * pressure ) / ( 273 + celsius( temperature ) ) / tangent( altitude )			
			adjustedAltitude = observedAltitude + dip + refraction 			
			round (adjustedAltitude,1)
			LHA = geographicPositionLongitude  -  assumedLongitude
			correctedAltitude = arcsin(	(sin(geographicPositionLatitude) * sin(assumedLatitude))  +	(cos(geographicPositionLatitude) * cos(assumedLatitude) * cos(LHA)))			
            distanceAdjustment = (adjustedAltitude - correctedAltitude) rounded to the nearest whole arc-minutes.
			azimuthAdjustment  = arccos((sin(geographicPositionLatitude) - sin(assumedLatitude) * sin(distanceAdjustment))/(cos(assumedLatitude) * cos(distanceAdjustment)))			
            approximateLatitude =  assumedLatitude + (sum (distanceAdjustmenti * cos(azimuthAdjustmenti)) for each sighting i)/60			
            approximateLongitude =  assumedLongitude + (sum (distanceAdjustmenti * sin(azimuthAdjustmenti)) for each sighting i)/60	
			logFile.write('LOG	:', datetime.datetime.utcnow(),body,'\t',date,'\t',time,'\t',adjustedAltitude,'\t',geographicPositionLatitude,'\t',geographicPositionLongitude,'\t',assumedLatitude,'\t',assumedLongitude,'\t',azimuthAdjustment,'\t',distanceAdjustment,'\n')
			logFile.write('LOG  :', datetime.datetime.today(),' Sighting errors : ' error,'\n')
			logFile.write('LOG  :', datetime.datetime.today(),' Approximate latitude: ' approximateLatitude,'\t',' Approximate longitude: ' approximateLongitude)
 			logFile.close()
	except IOError:
	print('file cannot be created or appended for whatever', logFile)	
	return (approximateLatitude, approximateLongitude)

