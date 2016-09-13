from math import sqrt, acos, degrees
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
