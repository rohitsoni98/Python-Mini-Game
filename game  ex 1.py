#snake water gun
from random import choice
p= 0
snake = 2
water = 3
gun = 4
you = 0
com = 0
print("let's start the game !.!.!.")
print("Here I present one of our childhood's most fav game Snake, water and gun")
print("s:Snake, w:Water, g:Gun")
while p < 7:
    a = str(input("choose any one of them s/w/g\n"))
    if a=="s":
        z = choice([water,gun])
        if snake*a == 6:
            print("you won")
            you = you+1
        else:
            print("you lose")
            com = com+1

    if a=="w":
        z = choice([snake,gun])
        if water*a == 6:
            print("you lose")
            com = com + 1
        else:
            print("you win")
            you = you + 1

    if a=="g":
        z = choice([snake,gun])

        if gun*a == 12:
                print("you lose")
                com = com + 1
        else:
                print("you win")
                you = you + 1

    p=p+1
print("game over")
print("ur score", you)
print("com score", com)
