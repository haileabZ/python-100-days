
from random import choice

def deal_card():
    card_numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return choice(card_numbers)

user_cards=[]
computer_cards=[]
is_game_over=False


def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        print("It's Draw!")
    elif calculate_score(computer_cards) == 0:
        print("You lose!")
    elif calculate_score(user_cards) == 0:
        print("You Won!")
    elif user_score > 21:
        print("You lose!")
    elif computer_score > 21:
        print("You win!")
    elif computer_score > user_score:
        print("You Lose!")
    else:
        print("You win!")

def printer():
    print(f"Your cards: {user_cards}")
    print(f"computer first card: {computer_cards[0]}")

def play_again ():
        global is_game_over
        for i in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        while not is_game_over:
            printer()
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over=True
            else:
                while True:
                  prompt=input("Do you want to draw another card(y or n)")
                  if prompt.isalpha() and len(prompt)==1:
                      break
                if prompt.strip().upper() == "Y":
                    user_cards.append(deal_card())
                else:
                    is_game_over=True

        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score=calculate_score(computer_cards)
        print(f"Your final cards: {user_cards}  score: {calculate_score(user_cards)}")
        print(f"computer final cards: {computer_cards}")
        compare(calculate_score(user_cards),calculate_score(computer_cards))


while True:
  wanna_play=input("Do you want to play the game (y or n)")
  if wanna_play.strip().upper() == "Y":
      play_again()
