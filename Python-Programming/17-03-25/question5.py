#  Take input of 3 variables : 1) Weather {option: i] Rainy ii]Clear} 2) DayShift {option: i]Morning  ii] Afternoon iii] Night } 3) Emergency {option: i]True ii] False}
#    if ambulance:  Allow fast passage
#       Heavy Traffic: Adjusting Signals for Smooth Flow
#       Peak hour Mode 
#       Low Traffic mode : Light on sensor mode 
weather = int(input("Please chose One Index from below:\n\t\t1)Rainy\n\t\t2)Clear\nEnter your Choice: "))
day_shift = int(input("Please chose One Index from below:\n\t\t1)Morning\n\t\t2)AfterNoon\n\t\t3)Night\n Enter your Choice: "))
emergency = int(input("Please chose One Index from below:\n\t\t1)True\n\t\t2)False\nEnter Your Choice: "))
print(f'Your Weather is {weather} Shift {day_shift} and Emergency status is {emergency}')
if(emergency):
    print("Allow Fast Passage")
elif(weather==1 and day_shift==1):
    print("Heavy Traffic Mode: Adjusting Signals for Smooth Flow")
elif(weather==1 and day_shift==2):
    print("Peak-Hour Traffic Mode")
elif(weather==1 and day_shift==3):
    print("Low Traffic mode : Light on sensor mode")
elif(weather==2 and day_shift==1):
    print("Low Traffic mode : Light on sensor mode")
elif(weather==2 and day_shift==2):
    print("Heavy Traffic Mode: Adjusting Signals for Smooth Flow")
elif(weather==2 and day_shift==3):
    print("Peak-Hour Traffic Mode")