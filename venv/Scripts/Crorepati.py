import random
import time

name = ""
QuestionBank_easy={}
AnswerBank_easy={}
QuestionBank_average = {}
AnswerBank_average = {}
QuestionBank_hard = {}
AnswerBank_hard = {}

QuestionBank_easy[0]="Which animal is known as the ‘Ship of the Desert?’"
AnswerBank_easy[0]=["Antelope","Camel","Dromedary","Addax",2]
QuestionBank_easy[1]="What is the top color in a rainbow?"
AnswerBank_easy[1]=["Violet","Blue","Red","Pink",3]
QuestionBank_easy[2]="Which festival is known as the ‘Festival of flowers’?"
AnswerBank_easy[2]=["Onam","Bihu","Holi","Diwali",1]
QuestionBank_easy[3]="Velocity of wind is measured by which device?"
AnswerBank_easy[3]=["speedometer","tachometer","anemometer","audiometer",3]
QuestionBank_easy[4]="What is the term used to describe money that flows into a country to take advantage of high rates of interest"
AnswerBank_easy[4]=["hot money","hard sector","hard currency","None of the above",1]
QuestionBank_easy[5]="Which is the world's largest international organisation and a successor to the League of Nations"
AnswerBank_easy[5]=["UNICEF","UNESCO","WHO","UNO",4]
QuestionBank_easy[6]="The three abundant elements in the earth's crust are aluminium, oxygen and silicon. The correct order of their abundance is"
AnswerBank_easy[6]=["oxygen, aluminium, silicon","aluminium, silicon, oxygen","oxygen, silicon, aluminium","silicon, oxygen, aluminium",3]
QuestionBank_easy[7]="When is the International Yoga Day celebrated?"
AnswerBank_easy[7]=["June 21","March 21","April 22","May 31",1]
QuestionBank_easy[8]="Which is the smallest planet in our solar system?"
AnswerBank_easy[8]=["Saturn","Pluto","Neptune","Uranus",2]
QuestionBank_easy[9]="Ataulfo, Alphonso and Keitt are varieties of what fruit?"
AnswerBank_easy[9]=["Apple","Mango","Orange","Cantaloupe",2]
QuestionBank_easy[10]="If you have cryophobia, what are you afraid of?"
AnswerBank_easy[10]=["Ice","Water","Spider","Pigeon",1]
QuestionBank_easy[11]="what do caterpillars turn into?"
AnswerBank_easy[11]=["Earthworm","Moth","Butterfly","Ladybird",3]
QuestionBank_easy[12]="What is Black Mamba?"
AnswerBank_easy[12]=["crocodile","rat","spider","snake",4]
QuestionBank_easy[13]="How many consonants are there in English?"
AnswerBank_easy[13]=["21","19","18","22",1]
QuestionBank_easy[14]="Which is largest island in the world?"
AnswerBank_easy[14]=["Madagascar","Borneo","New Guinea","Greenland",4]

QuestionBank_average[0]="What is the name of the biggest technology company in South Korea?"
AnswerBank_average[0]=["Whirlpool","LG","Samsung","Sony",3]
QuestionBank_average[1]="How many breaths does the human body take around daily?"
AnswerBank_average[1]=["19000","20000","21000","19500",2]
QuestionBank_average[2]="What is the world’s smallest bird?"
AnswerBank_average[2]=["crow","woodpecker","sparrow","Hummingbird",4]
QuestionBank_average[3]="What is the doll, Barbie’s, full name?"
AnswerBank_average[3]=["Barbara Millicent","Barbara Roberts","Barbara Jonas","Barbara Millicent Roberts",4]
QuestionBank_average[4]="What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton?"
AnswerBank_average[4]=["1910","1911","1912","1914",3]
QuestionBank_average[5]="Who wrote Macbeth?"
AnswerBank_average[5]=["Shakespeare","Noel Coward","Sarah Kane","J.B. Priestley",1]

QuestionBank_average[6]="Which of the following is the first calculating device?"
AnswerBank_average[6]=["Pascaline","Abacus","Turing Machine","Calculator",2]
QuestionBank_average[7]="Which of the following is also called translator?"
AnswerBank_average[7]=["Data representation","MS DOS","Language Processor","Kernel",3]
QuestionBank_average[8]="How the quality of printer is measured?"
AnswerBank_average[8]=["Alphabet per strike","Words per Inch","Strike per Inch","Dots per Inch",4]
QuestionBank_average[9]="IC chips used in computers are usually made of:"
AnswerBank_average[9]=["Lead","Silicon","Chromium","Gold",2]
QuestionBank_average[10]="What type of process creates a smaller file that is faster to transfer over the internet?"
AnswerBank_average[10]=["Compression","Fragmentation","Encapsulation","None",1]
QuestionBank_average[11]="Which is a wind instrument?"
AnswerBank_average[11]=["Shehnai","Sitar","Pakhawaj","Mridangam",1]
QuestionBank_average[12]="The lowest range of musical note is referred to as"
AnswerBank_average[12]=["Treble","Soprano","Alto","Bass",4]
QuestionBank_average[13]="Which of the following musical instruments is of Indian origin?"
AnswerBank_average[13]=["Drums","guitar","Flute","Piano",3]
QuestionBank_average[14]="Who is the author of 3 little pigs?"
AnswerBank_average[14]=["Charles Dickens","Rudyard Kipling","James Halliwell","Nora Robberts",3]
QuestionBank_hard[0]="What is Prince William's full name?"
AnswerBank_hard[0]=["William Arthur Philip Louis Windsor","William Philip Louis Windsor","William Philip Louis Windsor","William Arthur Philip Louis",1]
QuestionBank_hard[1]="Who designed the Eiffel Tower?"
AnswerBank_hard[1]=["Emrald Eiffel","Jonas Eiffel","Gustave Eiffel","Gasto Eiffel",3]
QuestionBank_hard[2]="Switzerland is made up of how many cantons?"
AnswerBank_hard[2]=["22","26","21","27",2]
QuestionBank_hard[3]="Where is the oldest tree in the world?"
AnswerBank_hard[3]=["California","Sydney","New York","Mexico",1]
QuestionBank_hard[4]="How many tombs are there in the Valley of the Kings in Egypt?"
AnswerBank_hard[4]=["61","65","63","62",3]
QuestionBank_hard[5]="What do you call a group of bears?"
AnswerBank_hard[5]=["pandemonium","troop","yoke","sloth",4]
QuestionBank_hard[6]="What’s the maximum score you can achieve in 10-pin bowling?"
AnswerBank_hard[6]=["200","270","299","300",4]
QuestionBank_hard[7]="'Moonshine' was a slang term for which type of beverage?"
AnswerBank_hard[7]=["Juice","Coffee","Alcohol","Tea",3]
QuestionBank_hard[8]="Tom Cruise is an outspoken member of which religion?"
AnswerBank_hard[8]=["Pentecoastal","Scientology","Adonism","Arkeon",2]
QuestionBank_hard[9]="What is the largest moon of Saturn called?"
AnswerBank_hard[9]=["Titan","Rhea","Mimas","Tethys",1]

def play_game(name):
    answers = []
    currentearnings = 0
    highscore = 0
    lifeline = 3
    list1 = []
    list2 = []
    list3 = []
    roundprize = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    file = open("scoreboard.txt","a")
    print("All the best",name,",the game begins after 2 seconds")
    time.sleep(2)
    round=1
    while True:
        if(round<=5):
            k = random.randint(0, 14)
            if k not in list1:
                list1.append(k)
                print("Round",round,"Current Earnings:",currentearnings,"$   Round Prize:",roundprize[round-1],"$   lifelines left",lifeline)
                time.sleep(1)
                print("Question",round,".",QuestionBank_easy.get(k))
                time.sleep(1)
                answers = AnswerBank_easy.get(k)
                print("1.",answers[0])
                print("2.",answers[1])
                print("3.",answers[2])
                print("4.",answers[3])
                time.sleep(1)
                print("Enter your choice, 1. Answer the question 2. Choose lifeline 3. Walk away with earnings")
                choice = int(input())
                if(choice==1):
                    print("Choose your option")
                    answer = int(input())
                    if(answer==answers[4]):
                        print("Yor answer is correct")
                        currentearnings = currentearnings+roundprize[round-1];
                        highscore = currentearnings
                        round=round+1
                        time.sleep(1)
                    else:
                        print(name,"your answer is wrong, you lost the game before first checkpoint")
                        str1=name+" "+str(0)+"\n"
                        file.write(str1)
                        time.sleep(2)
                        exit(1)

                if (choice==2):
                    if(lifeline>0):
                        lifeline = lifeline-1
                        print(name,"You lost a lifeline, now you are left with",lifeline)
                        print("You are still in the same round, you will be presented with a new question")
                        time.sleep(1)
                if(choice==3):
                    print("Thankyou for playing the game",name)
                    print("Your earnings till now is",currentearnings,"$, which will be credited soon.")
                    str1 = name+" "+str(highscore)+"\n"
                    file.write(str1)
                    time.sleep(2)
                    exit(1)
        else:
            break

    time.sleep(1)
    while True:
        if(round>=6 and round<=10):
            k = random.randint(0, 14)
            if k not in list2:
                list2.append(k)
                print("Round", round, "Current Earnings:", currentearnings, "$   Round Prize", roundprize[round - 1],"$   lifelines left",lifeline)
                time.sleep(1)
                print("Question", round, ".", QuestionBank_average.get(k))
                time.sleep(1)
                answers = AnswerBank_average.get(k)
                print("1.", answers[0])
                print("2.", answers[1])
                print("3.", answers[2])
                print("4.", answers[3])
                time.sleep(1)
                print("Enter your choice, 1. Answer the question 2. Choose lifeline 3. Walk away with earnings")
                choice = int(input())
                if (choice == 1):
                    print("Choose your option")
                    answer = int(input())
                    print("Confirm your option by typing yes, if you want to change your option, type no")
                    confirm = input()
                    if(confirm=="no"):
                        print("Choose your option again, this is your last chance")
                        answer = int(input())
                        if (answer == answers[4]):
                            print("Yor answer is correct")
                            currentearnings = currentearnings + roundprize[round - 1];
                            highscore = currentearnings
                            round = round + 1
                            time.sleep(1)
                        else:
                            print("Your answer is wrong,",name,"but you won 1000$, which was your first checkpoint")
                            str1 = name+" "+str(1000)+"\n"
                            file.write(str1)
                            time.sleep(2)
                            exit(1)
                    if(confirm=="yes"):
                        if (answer == answers[4]):
                            print("Yor answer is correct")
                            currentearnings = currentearnings + roundprize[round - 1];
                            highscore = currentearnings
                            round = round + 1
                            time.sleep(1)
                        else:
                            print("Your answer is wrong,",name,"but you won 1000$, which was your first checkpoint")
                            str1 = name+" "+str(1000)+"\n"
                            file.write(str1)
                            time.sleep(2)
                            exit(1)


                if (choice == 2):
                    if (lifeline > 0):
                        lifeline = lifeline - 1
                        print(name, "You lost a lifeline, now you are left with", lifeline)
                        print("You are still in the same round, you will be presented with a new question")
                        time.sleep(1)

                if (choice == 3):
                    print("Thankyou for playing the game",name)
                    print("Your earnings till now is", currentearnings, "$, which will be credited soon.")
                    str1 = name+" "+str(highscore)+"\n"
                    file.write(str1)
                    time.sleep(2)
                    exit(1)

        else:
            break

    time.sleep(1)
    while True:
        if(round>=11 and round<=15):
            k = random.randint(0, 9)
            if k not in list3:
                list3.append(k)
                print("Round", round, "Current Earnings:", currentearnings, "$   Round Prize", roundprize[round - 1], "$    lifelines left",lifeline)
                time.sleep(1)
                print("Question", round, ".", QuestionBank_hard.get(k))
                time.sleep(1)
                answers = AnswerBank_hard.get(k)
                print("1.", answers[0])
                print("2.", answers[1])
                print("3.", answers[2])
                print("4.", answers[3])
                time.sleep(1)
                print("Enter your choice, 1. Answer the question 2. Choose lifeline 3. Walk away with earnings")
                choice = int(input())
                if (choice == 1):
                    print("Choose your option")
                    answer = int(input())
                    print("Confirm your option by typing yes, if you want to change your option, type no")
                    confirm = input()
                    if (confirm == "no"):
                        print("Choose your option again, this is your last chance")
                        answer = int(input())
                        if (answer == answers[4]):
                            print("Yor answer is correct")
                            currentearnings = currentearnings + roundprize[round - 1];
                            highscore = currentearnings
                            round = round + 1
                            time.sleep(1)
                        else:
                            print("Yor answer is wrong,",name,"but you won 32000$, which was your second checkpoint")
                            str1 = name+" "+str(32000)+"\n"
                            file.write(str1)
                            time.sleep(2)
                            exit(1)
                    if (confirm == "yes"):
                        if (answer == answers[4]):
                            print("Yor answer is correct")
                            currentearnings = currentearnings + roundprize[round - 1];
                            highscore = currentearnings
                            round = round + 1
                            time.sleep(1)
                        else:
                            print("Yor answer is wrong,",name,"but you won 32000$, which was your second checkpoint")
                            str1 = name+" "+str(32000)+"\n"
                            file.write(str1)
                            time.sleep(2)
                            exit(1)

                if (choice == 2):
                    if (lifeline > 0):
                        lifeline = lifeline - 1
                        print(name,"You lost a lifeline, now you are left with",lifeline)
                        print("You are still in the same round, you will be presented with a new question")
                        time.sleep(1)

                if (choice == 3):
                    print("Thankyou for playing the game",name)
                    print("Your earnings till now is", currentearnings, "$, which will be credited soon.")
                    str1 = name+" "+str(highscore)+"\n"
                    file.write(str1)
                    time.sleep(2)
                    exit(1)
        else:
            str1 = name+" "+str(highscore)+"\n"
            file.write(str1)
            print("Congratulations",name,",you are now a millionaire, you will be credited with 1000000$")
            break

    file.close()

def get_high_score():
    file = open("scoreboard.txt", "r")
    print(file.read())

def take_input():
    print("enter choice")
    print("a) Play game")
    print("b) View high score")
    print("c) Quit game")
    print("Type 'a' to play game, 'b' to view high score, 'c' to quit")
    choice = input()
    if(choice=='a'):
        name = input("Enter your name")
        play_game(name)
    if(choice=='c'):
        print("Thankyou")
    if(choice=='b'):
        get_high_score()
take_input()

