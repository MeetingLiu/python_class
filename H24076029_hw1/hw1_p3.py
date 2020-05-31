# let the user input the velocity
inp1=input("Input velocity: ")
# convert the input string of velocity to the floating number
v=float(inp1)
# assign the variable c to 299792458
c=299792458
# assign the percentage of light speed to v/c
Percentage_of_light_speed=v/c
# assign r to an expression
r=1/(1-v**2/c**2)**0.5

# assign the travel time to each place to (its values of delta td)/r
Travel_time_to_Alpha_Centauri=4.3/r
Travel_time_to_Barnard_s__Star=6.0/r
Travel_time_to_Betelgeuse=309/r
Travel_time_to_Andromeda_Galaxy=2000000/r

# print out what the percentage of light speed is
## keep six significant digits after the decimal point
print("Percentage of light speed = ",'%f' % Percentage_of_light_speed)
# print out how much time do the astronauts spend on traveling to Alpha Centauri, Barnard's Star, Betelgeuse, Andromeda Galaxy
## keep six significant digits after the decimal point
print("Travel time to Alpha Centauri = ",'%f' % Travel_time_to_Alpha_Centauri)
print("Travel time to Barnard's Star = ",'%f' % Travel_time_to_Barnard_s__Star)
print("Travel time to Betelgeuse (in the Milky Way) = ",'%f' % Travel_time_to_Betelgeuse)
print("Travel time to Andromeda Galaxy (closest galaxy) = ",'%f' % Travel_time_to_Andromeda_Galaxy)

