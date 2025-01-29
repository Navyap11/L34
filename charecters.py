word= input("Enetr your own word: ")
charecter= input("Enter the charecter you would like to check: ")
i=0
count=0

while(i<len(word)):
    if(word[i] == charecter):
        count= count+1
    i= i+1

print("The total number of times ",charecter," has happened= ", count, " amount of times")