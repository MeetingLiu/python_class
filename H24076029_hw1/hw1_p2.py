# let the user inputs the octave and pitch class
inp1=input("Input an octave: ")
inp2=input("Input a pitch class: ")

# convert the input strings of octave and pitch class to the floating numbers
octave=float(inp1)
pc=float(inp2)

o=octave-4 # assign the variable o to (octave-4)
m=pc-9 # assign the variable m to (pc-9)
F=440*2**(o+m/12) # assign F to an expression

# print out what the corresponding frequency is
print("The corresponding frequency= ", F)