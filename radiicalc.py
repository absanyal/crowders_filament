import numpy as np
from numpy import pi

cell_x_len = 150
cell_y_len = 150
cell_z_len = 150

crowder_fraction = 0.3

crowder_radius = 5
monomer_radius = 2.5

vol = cell_x_len * cell_y_len * cell_z_len
# print("Volume of the cell:\n{} nm^3".format(vol))

crowder_effective_radius = crowder_radius * pow(2.0, 1.0/6.0)
# each_crowder_vol = 4.0/3.0 * pi * pow(crowder_effective_radius, 3)
each_crowder_vol = 4.0/3.0 * pi * pow(crowder_radius, 3)

# print("Effective radius of the crowder:\n{:.3} nm".format(crowder_effective_radius))
# print("Volume of each crowder:\n{:.3} nm^3".format(each_crowder_vol))

number_of_crowders = vol * crowder_fraction / each_crowder_vol
number_of_crowders = int(number_of_crowders)

print("--------------------")

print("Crowder fraction in the cell:\n{}".format(crowder_fraction))
print("Number of crowders in the cell:\n{}".format(number_of_crowders))

# print()
print("--------------------")
print("Interaction radii")
print("--------------------")

print("Monomer - Monomer, LJ/cut")
r_mm = (2 * monomer_radius) * pow(2.0, 1.0/6.0)
print("{:.3f} nm".format(r_mm))

print("Monomer - Crowder, LJ/cut")
r_mc = (monomer_radius + crowder_radius) * pow(2.0, 1.0/6.0)
print("{:.3f} nm".format(r_mc))

print("Crowder - Crowder, LJ/cut")
r_cc = (2 * crowder_radius) * pow(2.0, 1.0/6.0)
print("{:.3f} nm".format(r_cc))

print("--------------------")

print("Monomer - Wall, LJ126")
r_mw = monomer_radius * pow(2, 1/6)
print("{:.3f} nm".format(r_mw))

print("Crowder - Wall, LJ126")
r_cw = crowder_radius * pow(2, 1/6)
print("{:.3f} nm".format(r_cw))

print("--------------------")



