task=input("What Task do you wish to use?: ")  #asks for which task to look at
if task=='1':  #desplays task one
  binary=input("Plase enter a binary number: ")  #asks for a binary number
  decimal=0  #varible for the decimal equivalent
  impossible='false'  #varible used to see if the number is a binary number
  for number in range(len(binary)):
    if binary[number]=='1':  #goes through all values in the binary number to see if they are a 1
        decimal+=2**(len(binary)-number-1)  #adds to the total 2 to the power of the leght of the binary number minus 1 minus their posision.
    elif binary[number]!='0':  #if the number in that posision is also not a 0 then the number is not binary
        impossible='true'
  if impossible=='true':  #if the number is not binary diusplay the flollowing message
    print("The value given is not a binary number.")
  else:
    print("That binary number in decimal is",decimal)  #states what the number is in decimal
if task=='2':  #shows task two
  sentance=input("Plase write a sentance where each word is seperated by question marks:\n")
    # asks for a scentance where instead of spaces there are question marks
  if sentance.count('?')==0:  #if there are no question marks as required state that there are none
    print("There are no question marks like previously asked.")
  else:
    print(sentance.replace('?', ' '))  #replace the question marks with spaces
    print("There are",sentance.count('?')+1,"words in the sentance")  #states how many words there are in the given sentance