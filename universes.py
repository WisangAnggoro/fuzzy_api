import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#############################################
# Module generates plots of each universe
#############################################

# Generate universe variables
x_speed = np.arange(0, 21, 1)
x_distance = np.arange(0, 101, 10)
x_power = np.arange(0, 11, 1)

# Generate fuzzy membership functions
speed_vlo = fuzz.trimf(x_speed, [0, 0, 4])
speed_lo  = fuzz.trimf(x_speed, [0, 4, 8])
speed_op  = fuzz.trimf(x_speed, [4, 8, 12])
speed_hi  = fuzz.trimf(x_speed, [8, 12, 16])
speed_vhi = fuzz.trimf(x_speed, [12, 16, 20])

dist_vcl = fuzz.trimf(x_distance, [0, 0, 30])
dist_cl = fuzz.trimf(x_distance, [20, 40, 60])
dist_dt = fuzz.trimf(x_distance, [50, 75, 100])

power_vlo = fuzz.trimf(x_power, [0, 2, 4])
power_lo  = fuzz.trimf(x_power, [2, 4, 6])
power_op  = fuzz.trimf(x_power, [4, 6, 8])
power_hi  = fuzz.trimf(x_power, [6, 8, 10])
power_vhi = fuzz.trimf(x_power, [8, 10, 10])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_speed, speed_vlo, 'm', linewidth=1.5, label='Bardzo wolno')
ax0.plot(x_speed, speed_lo , 'r', linewidth=1.5, label='Wolno')
ax0.plot(x_speed, speed_op , 'y', linewidth=1.5, label='Optymalnie')
ax0.plot(x_speed, speed_hi , 'c', linewidth=1.5, label='Szybko')
ax0.plot(x_speed, speed_vhi, 'g', linewidth=1.5, label='Bardzo szybko')
ax0.set_title('Predkosc')
ax0.legend()

ax1.plot(x_distance, dist_vcl , 'r', linewidth=1.5, label='Bardzo maly')
ax1.plot(x_distance, dist_cl , 'c', linewidth=1.5, label='Maly')
ax1.plot(x_distance, dist_dt, 'g', linewidth=1.5, label='Daleki')
ax1.set_title('Dystans')
ax1.legend()

ax2.plot(x_power, power_vlo, 'm', linewidth=1.5, label='Bardzo mala')
ax2.plot(x_power, power_lo , 'r', linewidth=1.5, label='Mala')
ax2.plot(x_power, power_op , 'y', linewidth=1.5, label='Umiarkowana')
ax2.plot(x_power, power_hi , 'c', linewidth=1.5, label='Duza')
ax2.plot(x_power, power_vhi, 'g', linewidth=1.5, label='Bardzo duza')
ax2.set_title('Moc')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
