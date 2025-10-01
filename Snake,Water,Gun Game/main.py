# 1 = snake
# 0 = Water
# -1 = Gun
import random

def game():
    try:
        print("WELCOME TO THE GAME:SNAKE WATER GUN")
        while True:
            

            computer= random.choice([1, 0, -1])

            yourchoice=input("Enter Your Choice :")
            youDict ={"S":1,"W":0,"G":-1,"E":2}
            you=youDict[yourchoice.capitalize()]

            rev={1:"Snake",0:"Water",-1:"Gun",2:"Exit"}
            print(f"YOU Enter {rev[you]} And Computer Enter {rev[computer]}")

            if you==2:
                break
            else:
                if computer==you:
                    print("Its a Draw ")

                elif computer==1 and you==0:
                    print("Computer Wins")

                elif computer==1 and you==-1:
                    print("You Win")

                elif computer==0 and you==1:
                    print("You Win")

                elif computer==0 and you==-1:
                    print("Computer Wins")

                elif computer==-1 and you==1:
                    print("Computer Wins")

                elif computer==-1 and you==0:
                    print("You Win")
    except KeyError:
        print("Pls enter S:snake,W:water,G:gun,E:Exit")

if __name__=="__main__":
    game()

    