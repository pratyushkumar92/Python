index=0
while index<10:
    num = int(raw_input("Guess a number\n"))
    if num==5:
        print "Right guess\n"
        break
    elif num<5:
        print "Your number is less\n try again\n"
    else:
        print "Your number is greater\ntry again"
    index = index + 1
print "Your chances are over"