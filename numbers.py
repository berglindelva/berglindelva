#for loop that checks every positive two digit number and sees  whose square of the sum of its digits is equal to the number
for number in range(10,100):
    if ((number//10)+(number%10))**2==number:
        print(number)

#for loop that checks every numbers<100 with exactly 10 divisors and prints them out
for number in range (1,100):
    counter=0
    for j in range(1,number+1):
        if number%j==0:
            counter+=1
    if counter==10:
        print(number)
