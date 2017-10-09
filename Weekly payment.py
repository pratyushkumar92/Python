hourly_pay=int(raw_input("Enter hourly payment"))
hours_week=int(raw_input("Enter hours per week"))
weeklypay=hourly_pay*hours_week
if weeklypay>400:
    print "You can afford to live alone"
else:
    print "You are unable to live alone"