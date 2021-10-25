c=int(input("Enter temperature in celcius: "))
f=(c*1.8+32)
assert(f<=32), "It is freezing"
print("Temperature in Farenheit= ",f)