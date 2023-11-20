
while True:
     key=input("enter the key,(key <27)")
     if (key.isdigit() and int(key)<27):
         key=int(key)
         letters=list(chr(i) for i in range(65,91))
         correspondig_letters=letters[key:]+letters[0:key]
         break



def encrypt(word):
    encrypted=""
    for char in word:
       encrypted+=correspondig_letters[letters.index(char)]
    print(encrypted)

def main():
    while True:
      word=input("enter the word to be encrypted")
      if word.isalpha():
          encrypt(word.upper())
          prompt=int(input("do you want to continue encryption? say 1 to yes or 0 to no"))
          if prompt==1:
              if __name__=="__main__":
                 main()
          else:
              print("thanks for using our product")
          break


if __name__=="__main__":
    main()


