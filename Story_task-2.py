answer_yes=["yes","Y","Yes","y"]
answer_no=["No","N","n","no"]
print("""
Welcome,Let's Start the Adventure
you wake up in your bedrooom in the middle of night.you heard a loud noise outside the house.you have two choices to stay in the room or check what the sound might be
about.will you go out of your room(Yes/No)
""")
ans_1=input(">>")
if ans_1 in answer_yes:
    print("\n you exits the room silently and reaches the main hall.In the main hall,she finds a strabge but cute doll on the floor.It doesn't belong to you.will you pick up the teddy(Yes/No)\n")
    ans_2=input(">>")
    if ans_2 in answer_yes:
        print("""
        the moment you picked the doll it started talking!It tells that you are in danger as there is a monster in your househas captured your parents as well!
        But the doll told you not to get scared.It will help you tobeat the monster!you have killed the monster with the help pf doll.
        congracts.you won the game!
        """)
    elif ans_2 in answer_no:
        print("you decided not to pick the doll and went back to your room")
    else:
        print("you have entered the wrong input.Good Bye!")
elif ans_1 in answer_no:
    print("you decided to stay in the room.will you go to your elders.(Yes/NO)")
    
    ans_3=input(">>")
    if ans_3 in answer_yes:
        print("you can sleep with your parents without any fear")
    elif ans_3 in answer_no:
        print("The monster may come to your room and kills you.Game over!")
    else:
        print(" you have entered the wrong input.Good Bye!")
else:
    print("you have entered the wrong input.Goog Bye!")
    




