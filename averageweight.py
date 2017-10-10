w1=int(raw_input("Enter First person weight"))
w2=int(raw_input("Enter second person weight"))
w3=int(raw_input("Enter third person weight"))
w4=int(raw_input("Enter fourth person weight"))
w5=int(raw_input("Enter fifth person weight"))
w6=int(raw_input("Enter sixth person weight"))
w7=int(raw_input("Enter seventh person weight"))
w8=int(raw_input("Enter eighth person weight"))
w9=int(raw_input("Enter ninth person weight"))
w10=int(raw_input("Enter tenth person weight"))
w11=int(raw_input("Enter eleventh person weight"))
average=(w1+w2+w3+w4+w5+w6+w7+w8+w9+w10+w11)/11
print "Average weight of 11 person is",average
if average%5==0:
    print "Average age is multiple of 5"
else:
    print "Average age is not a multiple of 8"