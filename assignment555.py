print ("positive two digit numbers whose square of the sum of its digits is equal to the number")
for number in range(10,100):
    if ((number//10)+(number%10))**2==number:
        print(number)


print("all positive numbers < 100 with exactly 10 divisors:")
for number in range (1,100):
    counter=0
    for j in range(1,number+1):
        if number%j==0:
            counter+=1
    if counter==10:
        print(number)
