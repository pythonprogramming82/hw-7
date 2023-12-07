import pickle
import random
import os

class Quise:
    list = []
    questions = []
    def __init__(self, quise, answer):
        self.quise = quise
        self.answer = answer

    def __str__(self):
        return f"{self.quise}"


    def pick(self):
        pickled = pickle.dumps(self)
        file = open("quiz.pk", 'ab')
        file.write(pickled)
        file.close()
        file = open("quiz.pk", 'a')
        file.write('\n')
        file.close()


    def take_exam(self):
        score = 0
        for _ in range(5):
            question = random.choice(Quise.list)
            print(question)
            answer = input("pleas enter your answer: ")
            os.system("cls" if os.name == "nt" else "clear")
            result = self.check_answer(answer)
            score += result
            print("your score is: ", score)
    
       
    def check_answer(self, answer):
        if answer == self.answer:
            print("your answer is true +10")
            return 10
        else:
            print("your answer is false -3")
            return -3
        

    @staticmethod
    def read_text():
        file = open("quiz.pk", "rb")
        Quise.unpickle_text(file.readlines())
        file.close()


    @staticmethod
    def unpickle_text(file):
            for x in file:
                unpickle = pickle.loads(x)
                Quise.list.append(unpickle)


obj = Quise("is your name kosar?", "true")
obj_1 = Quise("is your fname is teymoori?", "True")
obj_2 = Quise("is your age is 20?", "True")
obj_3 = Quise("is your name marsa?", "False")
obj_4 = Quise("is your fname is hassani?", "False")
obj_5 = Quise("is your age is 19?", "False")
obj_6 = Quise("are you a man?", "false")
obj_7 = Quise("are you a woman?", "true")
obj.pick()
obj_1.pick()
obj_2.pick()
obj_3.pick()
obj_4.pick()
obj_5.pick()
obj_6.pick()
obj_7.pick()
Quise.read_text()


while True:
    choice = input("pleas choice the number\n1)start...\n2)new-Question...\n3)show-the-score...\n4)Exit...\nyour number: ")

    if choice == "1":
        for x in Quise.list:
            print(x)


    elif choice == "2":
        new_Question = input("pleas enter the new Question: ")
        Quise.list.append(new_Question)
    
    
    elif choice == "3":
        obj.take_exam()

    else:
        print("Exit...")
        break