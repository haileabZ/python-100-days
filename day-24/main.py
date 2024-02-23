


text = """ Dear [name]

 you are invited to my birthday this monday.

 Hope you can make it!

 Seni"""

with open("input/names/invited_names.txt", "r") as file:
     names = file.readlines()

for line in names:
     name = line.rstrip().strip()
     letter = text.replace("[name]", name)
     with open(f"output/readyToSend/letter_for_{name}.txt","w") as f:
         f.write(letter)

