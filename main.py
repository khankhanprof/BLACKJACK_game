import random
def deal_cards():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,comp_score):
  if user_score==comp_score:
    return "draw"
  elif user_score==0:
    return "BlackJack! you win"
  elif comp_score==0:
    return "dealer BlackJack! lose"
  elif user_score>21:
    return "went overboard,you lose"
  elif comp_score>21:
    return "dealer went overboard,you win"
  elif user_score>comp_score:
    return "  you win"
  else:
    return "you lose"
   
user_card=[]
comp_card=[]
for i in range(0,2):
    user_card.append(deal_cards())
    comp_card.append(deal_cards())
 
def play():
  is_game_over=False
  while not is_game_over:
    user_score=calculate_score(user_card)
    comp_score=calculate_score(comp_card)
    print(f"user cards:{user_card},user score:{user_score}")
    print(f"comp's first card:{comp_card[0]}")
    if comp_score==0 or user_score==0 or user_score>21:
      is_game_over==True
    else:
      unitappend=input("do you want to take another card:\'y\' for yes,\'n\' for no=")
      if unitappend=='y':
        user_card.append(deal_cards())
      else:
        is_game_over=True
    
  while comp_score != 0 and comp_score<17:
    comp_card.append(deal_cards())
    comp_score=calculate_score(comp_card)

  print(f"   Your final hand: {user_card}, final score: {user_score}")
  print(f"   Computer's final hand: {comp_card}, final score: {comp_score}")
  print(compare(user_score, comp_score))



user=input("press yes if you want to play , else press no ")
if user=='yes':
  play()





