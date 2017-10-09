index=0
while index<10:
    num = int(raw_input("Guess a number\n"))
    if num==5:
        print "Right guess\n"
        break
    else:
        print "Wrong guess\n"
    index = index + 1
print "Your chances are over"

