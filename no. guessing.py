#number guessing game
#thx laoming
import random
import readchar

key = "x"

while key != "\r":
 ans = random.randint(1,999) #answer
 small = 0  #small
 large = 1000 #large
 input1 = 0
 
 while input1 != ans:
     print("bigger than:",small,",smaller than", large)
     input1 = int(input())
     
     if input1 <= small or input1 >= large:
      print("error: input too large or too small")
     elif input1 < ans:
      small = input1
     elif input1 > ans:
      large = input1
 
 print("You win!")
 print("Answer is ",ans)
 key = readchar.readkey("Press Enter to exit")