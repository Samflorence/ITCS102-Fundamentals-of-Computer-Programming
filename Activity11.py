#ask user to input temperature outside 
#conditions as follow 
# 0 to negative temperature --- below freezing 
# 1 to 15 - Extreme Cold temperatures
# 16 to 30 - Cold Temperature 
# 31 to 38 - Lukewarm Temperature 
# 39 to 42 - Warm Temperature
# 43 to 50 - Hot Temperature 
# 51 to 60 - Extremly Hot Temperature 
# 61 and above - Burning Temperature 

temp = eval(input("Input temperature outside -->"))

if temp <= 0:
		print("Temperature is considered Below freezing")
elif temp >= 1 and temp <= 15:
		print("Temperature is considered extremly cold")
elif temp >= 16 and temp <= 30:
		print("Temperature is considered cold")
elif temp >= 31 and temp <= 38:
		print("Temperature is considered lukewarm")
elif temp >= 39 and temp <= 42:
		print("Temperature is considered warm")
elif temp >= 43 and temp <= 50:
		print("Temperature is considered hot")
elif temp >= 51 and temp <= 60:
		print("Temperature is considered extremly hot")
elif temp >= 61:
		print("Temperature is considered Burning")

else:
	print("invalid temperature")