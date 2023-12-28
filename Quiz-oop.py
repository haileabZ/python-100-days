
questions=[{"question":"abiy ahmed is current ethiopian prime minster.","answer":"true"},
           {"question":"ethiopia is the largest country in africa.","answer":"false"},
           {"question":"KM is not the greater M.","answer":"false"},
           {"question":"einstein is physician.","answer":"true"}
           ]
count=0
class Quiz:
    def __init__(self,question):
        self.question=question["question"]
        self.answer=question["answer"]

    def display(self):
        global count
        prompt=input(self.question+" (true/false)")
        if prompt.lower() == self.answer:
            count += 1
            print(f"You got it! score:{count}/{len(questions)}")

        else:
            print(f"you lose it! score:{count}/{len(questions)}")
            print("correct answer is",self.answer)




for question in questions:
    quiz1=Quiz(question)
    quiz1.display()