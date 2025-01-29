lower= int(input("Eneter a lower range: "))
upper= int(input("Enetr a higher range: "))

print("The prime numbers between your lower and upper range are: ")

for num in range(lower,upper +1):
    if num>1:
        for i in range (2, num):
            if(num% i)==0:
                break
        else:
            print(num)
