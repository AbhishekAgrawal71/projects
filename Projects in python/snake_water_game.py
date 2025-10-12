data={1:"snake",
      2:"water",
      3:"gun"}
while(1):
    for i in data.items():
        print(i)
    player1=float(input("player 1 enter your choice : "))
    if((player1 ==1) or (player1 ==2) or (player1 ==3)):
        print(f"player1 selected {data.get(player1)}")
    else:
        print("Wrong selection select number from the list given :")
        continue
    player2=float(input("player 2 enter your choice : "))
    player2=int(player2)
    if((player2 ==1) or (player2 ==2) or (player2 ==3)):
        print(f"player2 selected {data.get(player2)}")
    else:
        print("Wrong selection select number from the list given :")
        continue
    if(player1==1 and player2==2):
        print("player1 beats player2 means (snake drinks water )")
        break
    elif(player1==1 and player2==3):
        print("player2 beats player1 means (gun kills snake )")
        break
    elif(player1==2 and player2==1):
        print("player2 beats player1 means (snake drinks water )")
        break
    elif(player1==2 and player2==3):
        print("player1 beats player2 means (water drowns gun )")
        break
    elif(player1==3 and player2==1):
        print("player1 beats player2 means (gun kills snake )")
        break
    elif(player1==3 and player2==2):
        print("player2 beats player1 means (water drowns gun )")
        break
    else:
        print("Draw")
    