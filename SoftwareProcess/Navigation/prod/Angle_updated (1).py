from math import sqrt, acos, degrees
import Navigation.prod.Angle as Angle
import Navigation.prod.Fix as Fix
#Import axis and degrees packages. 
pow_n = float(2)
def print_angles():
	prec = 4
	#assumes direction along y axis
	current_x = round(float(input("initial x: ")), prec)
	current_y = round(float(input("and y: ")), prec)
	current_v = round(float(input("velocity: ")), prec)
	#angle will be calculated from origin (0,0)
	#unit vector with no magnitude
	src_x = float(0)
	src_y = float(0)
	src_z = float(1)
	u_v = sqrt(pow(src_x,pow_n) + pow(src_y,pow_n) + pow(src_z,pow_n))
# Calculating Angles based on input values.  
	angle = calc_angle((calc_dot(src_x, src_y, src_z, current_x, current_y, current_v)), u_v, (sqrt_vec(current_x, current_y, current_v)))
	angle_min = float(-1)
	angle_max = float(90)
# checking the Angle with max angle and min angles. If angle is is greater than max angle then print out of bounds other wise Print origin.  
	if angle > angle_max:
		print("input out of bounds.")
	else:
		print("origin: (" + str(src_x) + "," + str(src_y) + "," + str(src_z) + ")")
	while angle > angle_min and angle < angle_max:
		rel_x = current_x
		rel_y = current_y
		rel_z = current_v
		dot = calc_dot(src_x, src_y, src_z, current_x, current_y, current_v)
		n_v = sqrt_vec(current_x, current_y, current_v)
# Calculating actual angle and velacity and It will return Degrees and Priting the angles.  
		angle_actual = calc_angle(dot, u_v, n_v)
		angle = round(angle_actual, 1)
		print("-" * 36)
		print("translated: \tx \ty \tz")
		print("\t ( " + str(rel_x) + ",\t" + str(rel_y) + ",\t" + str(rel_z) + " )")
		print("\t sqrt vector \t" + str(round(n_v, prec)))
		print("\t angle (deg) \t" + str(angle) + " \t\tactual: " + str(angle_actual))
		current_x = round(n_v, prec)
	return
def calc_dot(src_x, src_y, src_z, rel_x, rel_y, rel_z):
	return float((src_x*rel_x) + (src_y*rel_y) + (src_z*rel_z))
def sqrt_vec(x, y, z):
	return sqrt(pow(float(x),pow_n) + pow(float(y),pow_n) + pow(float(z),pow_n))
def calc_angle(inner_pdct, v_pdct1, v_pdct2):
	return degrees(acos(float(inner_pdct)/(float(v_pdct1)*float(v_pdct2))))
if __name__ == "__main__":
	import sys
	print_angles()

# ---------- constructor ----------					
# Instantiate angles					
angle1 = Angle.Angle()					
angle2 = Angle.Angle()					
angle3 = Angle.Angle()					
angle4 = Angle.Angle()					

# ---------- set ----------					
angle1Degrees = angle1.setDegreesAndMinutes("45d0.0")   #angle1Degrees should be 45.0					
angle2Degrees = angle2.setDegrees(degrees=-19.5)        #angle2Degrees should be 340.5					
angle3Degrees = angle3.setDegreesAndMinutes("0d30.0")   #angle3Degrees should be 0.5					

# Attempts to set an invalid value should result					
# in a ValueError exception bearing a diagnostic message					
try:					
    invalidAngle = angle2.setDegreesAndMinutes("")					
except ValueError as raisedException:					
    diagnosticString = raisedException.args[0]					

# ---------- add ----------					
# Add angle2 to angle1; save result in angle1; return result as degrees					
# 45d0 + 340d30 = 385d30 = 25d30 = 25.5 degrees					
addedDegrees1 = angle1.add(angle2)  #addedDegress1 should be 45d0 + 340d30 = 385d30 = 25d30 = 25.5 					
# Add angle3 to angle2; save result in angle2; return result as degrees					
addedDegrees3 = angle2.add(angle3)  #addedDegrees should be 340d30 + 0d30 = 340d60 = 341d0 = 341.0					

# Attempts to pass a parm that is not an instance of Angle					
# should result in a ValueError exception bearing a diagnostic message.					
try:					
    angle1.add("42d0")					
except ValueError as raisedException:					
    diagnosticString = raisedException.args[0]					
	
# ---------- subtract ----------					
# Subtract angle1 from angle4; save result in angle4; return result as degrees					
subtractedDegrees = angle4.subtract(angle1) #subtracted degrees should be 0d0 - 25d30 = -25d30 = 334d30= 334.5					
	
# Attempts to pass a parm that is not an instance of Angle					
# should result in a ValueError exception bearing a diagnostic message.					
try:					
    angle1.subtract(0)					
except ValueError as raisedException:					
    diagnosticString = raisedException.args[0]					
	
# ---------- compare ----------					
# Compare angle2 to angle1.  Return -1 if angle1 is less than angle2,					
# +1 if angle1 is greater than angle2					
# 0 if angle1 is equal to angle2					
angle1.setDegrees(45.0)					
angle2.setDegrees(45.1)					
result = angle1.compare(angle2) #result should be -1					

# Attempts to pass a parm that is not an instance of Angle					
# should result in a ValueError exception bearing a diagnostic message					
try:					
    angle1.compare(42.0)					
except ValueError as raisedException:					
    diagnosticString = raisedException.args[0]					
	
# ---------- getString ----------					
angle1String = angle1.getString()   #angle1String should be "45d0.0"					
angle2String = angle2.getString()   #angle2String should be "45d6.0"					
angle3.setDegrees(45.123)					
angle3String = angle3.getString()   #angle3String should be "45d7.4"					
	
# ---------- getDegrees ----------					
angle1Degrees = angle1.getDegrees()   #angle1String should be 45.0					
angle2Degress = angle2.getDegrees()   #angle2String should be 45.1					
angle3Degrees = angle3.getDegrees()   #angle3String should be 45.1

# ---------- constructor ----------		
theFix = Fix.Fix()		
theFix.setSightingFile("sightings.xml")		
approximatePosition = theFix.getSightings()				