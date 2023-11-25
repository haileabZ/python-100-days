
import random


def random_celebrity():
    celebrities = [
        {"name": "Ronaldo", "role": "football player", "country": "portugal", "followers": 500000000},
        {"name": "Shakira", "role": "musician", "country": "colombia", "followers": 415000000}
      ]
    return random.choice(celebrities)

def compare(num1,num2):
    prompt=input("Who has more followers? Type 'A' or 'B' ")
    if prompt.strip().upper() == "A" and num1 > num2:
        return True
    if prompt.strip().upper() == "B" and num1 < num2:
        return True
    return  False



def printer(celeb1,celeb2):
    print(f"Compare A: {celeb1['name']} , {celeb1['role']} , from  {celeb1['country']}")
    vs="""
         _     __
        | |   / /----
        | |  / / ___/
        | | / (___ )
        |____/____(__)
        """
    print(vs)
    print(f"Against B: {celeb2['name']} , {celeb2['role']} , from  {celeb2['country']}")
count=0
while True:
    celeb1=random_celebrity()
    celeb2=random_celebrity()
    if celeb1 != celeb2:
        printer(celeb1,celeb2)
        value=compare(celeb1["followers"], celeb2["followers"])
        if value == True:
            count+=1
            print(f"you got it! current score: {count}")
        else:
            print(f"You lose! your score: {count}")
            break
