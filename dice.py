import random 
# ● ┌ ─ ┐ │ └ ┘   uni code  to draw  Acsiii Art
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#Simple Dice Simulater to give a Total number of dice  
dice_art = {
    1: ("┌────────┐",
        "│        │",
        "│   ●    │",
        "│        │",
        "└────────┘"),
    2: ("┌────────┐",
        "│  ●     │",
        "│        │",
        "│      ● │",
        "└────────┘"),
    3: ("┌────────┐",
        "│  ●     │",
        "│    ●   │",
        "│      ● │",
        "└────────┘"),
    4: ("┌────────┐",
        "│  ●   ● │",
        "│        │",
        "│  ●   ● │",
        "└────────┘"),
    5: ("┌────────┐",
        "│  ●   ● │",
        "│    ●   │",
        "│  ●   ● │",
        "└────────┘"),
    6: ("┌────────┐",
        "│  ●   ● │",
        "│  ●   ● │",
        "│  ●   ● │",
        "└────────┘"),
}
dice=[]  #create a list for dice
total=0
num_of_dice = int(input("How many Dice?:"))
#random.randint(1,6)  Genrate a random number between 1 to 6
for die in range(num_of_dice):
    dice.append(random.randint(1,6) )

for die in range(num_of_dice):
   for line in dice_art.get(dice[die]):
        print(line)
        
# for printin dice in Horizontal we use bloop nested loop

#for line in range(5):
 #   for die in dice:
  #      print(dice_art.get(die)[line], end="")
    
  #  print()    



    
for die in dice:
    total += die
    
print(f"total: {total}")    
    

