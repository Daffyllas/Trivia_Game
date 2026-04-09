import random 
points = 0

questions = [
    "What is the capital of Japan?\n1. Tokyo\n2. Seoul\n3. Beijing\n4. Bangkok",
    
    "Who discovered gravity?\n1. Albert Einstein\n2. Isaac Newton\n3. Galileo Galilei\n4. Nikola Tesla",
    
    "Which planet is known as the Red Planet?\n1. Venus\n2. Mars\n3. Jupiter\n4. Saturn",
    
    "How many continents are there on Earth?\n1. 5\n2. 6\n3. 7\n4. 8",
    
    "What is the chemical symbol for water?\n1. O2\n2. CO2\n3. H2O\n4. HO2",
    
    "Which animal is known as the king of the jungle?\n1. Elephant\n2. Tiger\n3. Lion\n4. Cheetah",
    
    "How many sides does a hexagon have?\n1. 4\n2. 5\n3. 6\n4. 8",
    
    "Who painted the Starry Night?\n1. Pablo Picasso\n2. Leonardo da Vinci\n3. Vincent van Gogh\n4. Claude Monet",
    
    "What is the capital of Canada?\n1. Toronto\n2. Vancouver\n3. Ottawa\n4. Montreal",
    
    "Which is the longest river in the world?\n1. Amazon River\n2. Nile River\n3. Mississippi River\n4. Yangtze River",

    "What is the smallest bone in the human body?\n1. Stapes\n2. Femur\n3. Tibia\n4. Radius",

    "Which element has the chemical symbol 'Fe'?\n1. Iron\n2. Fluorine\n3. Francium\n4. Phosphorus",

    "Who was the first woman to fly solo across the Atlantic Ocean?\n1. Amelia Earhart\n2. Bessie Coleman\n3. Jacqueline Cochran\n4. Sally Ride",

    "In what year did the Titanic sink?\n1. 1908\n2. 1910\n3. 1912\n4. 1915",

    "What is the hardest natural substance on Earth?\n1. Gold\n2. Diamond\n3. Iron\n4. Platinum",

    "Which language has the most native speakers in the world?\n1. Spanish\n2. Mandarin Chinese\n3. English\n4. Hindi",

    "What is the longest bone in the human body?\n1. Femur\n2. Tibia\n3. Fibula\n4. Radius",

    "What is the smallest country in the world by land area?\n1. Vatican City\n2. Monaco\n3. Nauru\n4. San Marino",

    "Which animal can hold its breath the longest underwater?\n1. Whale\n2. Dolphin\n3. Elephant Seal\n4. Turtle",

    "In what year did World War I begin?\n1. 1912\n2. 1914\n3. 1916\n4. 1918",

    "What is the chemical symbol for gold?\n1. Ag\n2. Au\n3. Pb\n4. Fe",

    "Which planet is closest to the Sun?\n1. Earth\n2. Venus\n3. Mercury\n4. Mars",

    "Who wrote the play 'Romeo and Juliet'?\n1. William Shakespeare\n2. Charles Dickens\n3. George Orwell\n4. Mark Twain",

    "Which country invented pizza?\n1. Greece\n2. Italy\n3. France\n4. United States",

    "What is the longest river in the world?\n1. Nile\n2. Amazon\n3. Yangtze\n4. Mississippi",

    "What is the largest ocean on Earth?\n1. Atlantic Ocean\n2. Indian Ocean\n3. Arctic Ocean\n4. Pacific Ocean",

    "What does DNA stand for?\n1. Deoxyribonucleic Acid\n2. Dioxyribonuclear Acid\n3. Diatomic Nitrogen Acid\n4. Deoxyribonuclear Acid",

    "Who was the first man to step on the Moon?\n1. Neil Armstrong\n2. Buzz Aldrin\n3. Yuri Gagarin\n4. Alan Shepard",

    "Which country is known as the Land of the Rising Sun?\n1. China\n2. Japan\n3. South Korea\n4. Thailand",

    "What is the capital of Australia?\n1. Sydney\n2. Melbourne\n3. Canberra\n4. Brisbane"
]

answers = {questions[0] : 1 ,
           questions[1] : 2,
           questions[2] : 2,
           questions[3] : 3,
           questions[4] : 3,
           questions[5] : 3,
           questions[6] : 3,
           questions[7] : 3,
           questions[8] : 3,
           questions[9] : 2,
           questions[10] : 1 ,
           questions[11] : 1,
           questions[12] : 1,
           questions[13] : 3,
           questions[14] : 2,
           questions[15] : 2,
           questions[16] : 1,
           questions[17] : 1,
           questions[18] : 3,
           questions[19] : 2,
           questions[20] : 2,
           questions[21] : 3,
           questions[22] : 1,
           questions[23] : 2,
           questions[24] : 2,
           questions[25] : 4,
           questions[26] : 1,
           questions[27] : 1,
           questions[28] : 2,
           questions[29] : 3}






def generate_questions() :
    global questions
    question = random.choice(questions)
    print(question)
    questions.remove(question)
    
    return question


def win_check(question):
    global points
    while True :
        player_answer = input("Pick the correct answer (1-4) : ")
        if player_answer.isdigit() :
            player_answer = int(player_answer)
            if player_answer >= 1 and player_answer <= 4 :
                
                if player_answer == answers[question] :
                    print("You guessed right\n---------------\n")
                    points += 1
                    break
                else :
                    print("Wrong answer\n----------------\n")
                    print(f"The correct answer is {answers[question]}\n---------------\n")
                    break    
            else : 
                print("Insert a number 1-4")        
        else :
            print("Insert a valid answer (1-4)")



def check_score():
    
    score_input = input("Wright score to check your score").lower()
    if score_input == "score : ":
        print(f"Your score is {points}\n----------------\n")






while len(questions) > 0 :
    
    selected_question = generate_questions()
    win_check(selected_question)
    if len(questions) == 20 :
        check_score()


else :
    print(f"The game ended!!!!Your score is {points}")    
