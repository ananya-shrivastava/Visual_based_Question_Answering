import sys
import csv
import pyttsx3

with open("/home/ubuntu/Documents/deep_learning/visual_question_answering-master/test/questions.csv") as f1:
    reader1 = csv.reader(f1)
    my_list1 = [row[-1] for row in reader1]
    print("The question is "+my_list1[1])
    engine1 = pyttsx3.init()
    engine1.say("The question is "+my_list1[1])
    engine1.runAndWait()


with open("/home/ubuntu/Documents/deep_learning/visual_question_answering-master/test/results.csv") as f:
    reader = csv.reader(f)
    my_list = [row[-1] for row in reader]
    print("The answer is "+my_list[1])
    engine = pyttsx3.init()
    engine.say("The answer is "+my_list[1])
    engine.runAndWait()
    
