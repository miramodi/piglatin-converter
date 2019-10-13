
continuegame = "yes"

while (continuegame == "yes"):
    user_input = input("enter word to convert to pig latin ")
    
    vowels = ("aeiou")
    firstletter = user_input[0]
    if firstletter in vowels:
        user_input = user_input+"yay"
        
    else:
        user_input = user_input[1:]
        user_input = user_input+firstletter+"ay"
            
    print(user_input)
    continuegame = input("do you want to play again? ")
    
    if continuegame == "no" :
        print ("thanks for playing")
