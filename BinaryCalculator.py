running = True  # difining true value for setting up infinite while loop until we stop it


while running: # run while loop until running == False
    num = int(input("Enter a number:",)) # Taking input of number need to converted to binary        
    
    # creating a flage which will tell input was negative while printing
    flag = 0
    if num<0:
        flag = "-"
    
    binary = [] # place where digits of binary get added
    
    while num>1 or num<-1: # Agar number 1 se bada hai to do operation and append binary digits in binary
        reminder = num%2
        binary.append(reminder)
        num = int(num/2) # number ko chota bana do to get another digit in binary
    
    finisher = num%2 # solving error of not getting last digit of binary
    binary.append(finisher)
    binary.reverse() # reversing the binary list as we append binary digits in reverse form
    
    # now finally formating binary number to look like number
    result = ""
    for value in binary:
        result = int(str(result) + str(value))
    
    # printing the binary number in terminal
    if flag == "-":
        print("-"+str(result))
    else:
        print(result)
    
    # if input is 00 exit while loop
    if num == 0:
        running = False
        print("Thanks for using BINARY CALCULATOR")