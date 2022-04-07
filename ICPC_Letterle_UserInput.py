def letterle():

  letterle = input('Enter the 5 letter combination: ').upper()
  mydict={}
  for letter in letterle:
    if(letter in mydict):
      mydict[letter]+=1
    else:
      mydict[letter]=1

  #USER GETS 7 guesses
  for i in range(7):
    print("\nTry", str(i+1) + ":")
    feedback = ["X","X","X","X","X"]
    tempdict={}
    #USER GUESS
    guess = input().upper()

    #Correct guess
    if guess == letterle:
      print('GGGGG')
      return "\nWINNER"

    #PRINT FEEDBACK
    for i in range(5):     
      if guess[i] == letterle[i]:
        feedback[i] = "G"
        if(guess[i] in tempdict):
          tempdict[guess[i]]+=1
        else:
          tempdict[guess[i]]=1
    for i in range(5):
      if guess[i] == letterle[i]:
        continue
      if(guess[i] in tempdict):
          tempdict[guess[i]]+=1
      else:
          tempdict[guess[i]]=1
      if (guess[i] in letterle and tempdict[guess[i]]<=mydict[guess[i]] ):
        feedback[i] = "Y"

    print("".join(feedback))

  return "LOSER"

print(letterle())