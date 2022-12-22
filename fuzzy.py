import numpy as np
import skfuzzy as fuzz

import base64


def defuzzified_result(speed, distance):
    # Generate universe variables
    x_speed = np.arange(0, 21, 1)
    x_distance = np.arange(0, 101, 10)
    x_power = np.arange(0, 11, 1)

    # Generate fuzzy membership functions
    speed_vlo = fuzz.trimf(x_speed, [0, 0, 4])
    speed_lo = fuzz.trimf(x_speed, [0, 4, 8])
    speed_op = fuzz.trimf(x_speed, [4, 8, 12])
    speed_hi = fuzz.trimf(x_speed, [8, 12, 16])
    speed_vhi = fuzz.trimf(x_speed, [12, 16, 20])

    dist_vcl = fuzz.trimf(x_distance, [0, 0, 30])
    dist_cl = fuzz.trimf(x_distance, [20, 40, 60])
    dist_dt = fuzz.trimf(x_distance, [50, 75, 100])

    power_vlo = fuzz.trimf(x_power, [0, 2, 4])
    power_lo = fuzz.trimf(x_power, [2, 4, 6])
    power_op = fuzz.trimf(x_power, [4, 6, 8])
    power_hi = fuzz.trimf(x_power, [6, 8, 10])
    power_vhi = fuzz.trimf(x_power, [8, 10, 10])

    speed_level_vlo = fuzz.interp_membership(x_speed, speed_vlo, speed)
    speed_level_lo = fuzz.interp_membership(x_speed, speed_lo, speed)
    speed_level_op = fuzz.interp_membership(x_speed, speed_op, speed)
    speed_level_hi = fuzz.interp_membership(x_speed, speed_hi, speed)
    speed_level_vhi = fuzz.interp_membership(x_speed, speed_vhi, speed)

    dist_very_close = fuzz.interp_membership(x_distance, dist_vcl, distance)
    dist_close = fuzz.interp_membership(x_distance, dist_cl, distance)
    dist_distant = fuzz.interp_membership(x_distance, dist_dt, distance)

    ##############################  RULES  #####################################

    # Speed / dist	v_close	close	distant
    # v_low	        p_op	p_hi	p_vhi
    # low	        p_lo	p_op	p_hi
    # opt	        p_vlo	p_lo	p_op
    # high	        p_vlo	p_lo	p_op
    # v_high	    p_vlo	p_vlo	p_lo

    # 1  IF speed_vlo AND distance_vcl THEN power_op
    # 2  IF speed_vlo AND distance_cl THEN power_hi
    # 3  IF speed_vlo AND distance_dt THEN power_vhi

    # 4  IF speed_lo AND distance_vcl THEN power_lo
    # 5  IF speed_lo AND distance_cl THEN power_op
    # 6  IF speed_lo AND distance_dt THEN power_hi

    # 7  IF speed_op AND distance_vcl THEN power_vlo
    # 8  IF speed_op AND distance_cl THEN power_lo
    # 9  IF speed_op AND distance_dt THEN power_op

    # 10 IF speed_hi AND distance_vcl THEN power_vlo
    # 11 IF speed_hi AND distance_cl THEN power_lo
    # 12 IF speed_hi AND distance_dt THEN power_op

    # 13 IF speed_vhi AND distance_vcl THEN power_vlo
    # 14 IF speed_vhi AND distance_cl THEN power_vlo
    # 15 IF speed_vhi AND distance_dt THEN power_lo

    # Power_vlo - Rules 7, 10, 13, 14
    r7 = np.fmin(speed_level_op, dist_very_close)
    r10 = np.fmin(speed_level_hi, dist_very_close)
    r13 = np.fmin(speed_level_vhi, dist_very_close)
    r14 = np.fmin(speed_level_vhi, dist_close)
    active_rule1 = np.fmax(r7, np.fmax(r10, np.fmax(r13, r14)))

    # Power_lo - Rules 4, 8, 11, 15
    r4 = np.fmin(speed_level_lo, dist_very_close)
    r8 = np.fmin(speed_level_op, dist_close)
    r11 = np.fmin(speed_level_hi, dist_close)
    r15 = np.fmin(speed_level_vhi, dist_distant)
    active_rule2 = np.fmax(r4, np.fmax(r8, np.fmax(r11, r15)))

    # Power_op - Rules 1, 5, 9, 12
    r1 = np.fmin(speed_level_vlo, dist_very_close)
    r5 = np.fmin(speed_level_lo, dist_close)
    r9 = np.fmin(speed_level_op, dist_distant)
    r12 = np.fmin(speed_level_hi, dist_distant)
    active_rule3 = np.fmax(r1, np.fmax(r5, np.fmax(r9, r12)))

    # Power_hi - Rules 2, 6
    r2 = np.fmin(speed_level_vlo, dist_close)
    r6 = np.fmin(speed_level_lo, dist_distant)
    active_rule4 = np.fmax(r2, r9)

    # Power_vhi - Rule 3
    active_rule5 = np.fmin(speed_level_vlo, dist_distant)

    power_activation_vlo = np.fmin(active_rule1, power_vlo)
    power_activation_lo = np.fmin(active_rule2,  power_lo)
    power_activation_op = np.fmin(active_rule3,  power_op)
    power_activation_hi = np.fmin(active_rule4,  power_hi)
    power_activation_vhi = np.fmin(active_rule5, power_vhi)

    power0 = np.zeros_like(x_power)

    # Aggregate all three output membership functions together
    aggregated = np.fmax(power_activation_vlo,
                         np.fmax(power_activation_lo,
                                 np.fmax(power_activation_op,
                                         np.fmax(power_activation_hi, power_activation_vhi))))

    # Calculate defuzzified result
    power = fuzz.defuzz(x_power, aggregated, 'centroid')
    power_activation = fuzz.interp_membership(
        x_power, aggregated, power)  # for plot
