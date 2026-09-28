import random
# dictionary of questions and answers
questions = {

    1: {"question": "What is the only mammal capable of true flight?", "answer": "Bat", "category": "Science"},
    2: {"question": "Which planet is known as the Red Planet?", "answer": "Mars", "category": "Science"},
    3: {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean", "category": "Geography"},
    4: {"question": "How many bones do sharks have in their bodies?", "answer": "Zero", "category": "Science"},
    5: {"question": "Which country is home to the kangaroo?", "answer": "Australia", "category": "Geography"},
    6: {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond", "category": "Science"},
    7: {"question": "Which fruit is known for being the smelliest in the world?", "answer": "Durian", "category": "Food"},
    8: {"question": "What is the capital city of Japan?", "answer": "Tokyo", "category": "Geography"},
    9: {"question": "How many elements are there in the periodic table?", "answer": "118", "category": "Science"},
    10: {"question": "Which company created the iPhone?", "answer": "Apple", "category": "Technology"},
    11: {"question": "What is the name of the dynamic tracking system used in tennis to review decisions?", "answer": "Hawk-Eye", "category": "Sports"},
    12: {"question": "In what year did the Titanic sink?", "answer": "1912", "category": "History"},
    13: {"question": "What is the national animal of Scotland?", "answer": "Unicorn", "category": "General"},
    14: {"question": "Which artist painted the Mona Lisa?", "answer": "Leonardo da Vinci", "category": "Art"},
    15: {"question": "What is the primary ingredient in guacamole?", "answer": "Avocado", "category": "Food"},
    16: {"question": "How many days are in a leap year?", "answer": "366", "category": "General"},
    17: {"question": "What language has the most words?", "answer": "English", "category": "Language"},
    18: {"question": "What is the chemical symbol for gold?", "answer": "Au", "category": "Science"},
    19: {"question": "Which country invented tea?", "answer": "China", "category": "History"},
    20: {"question": "How many hearts does an octopus have?", "answer": "3", "category": "Science"},
    21: {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest", "category": "Geography"},
    22: {"question": "Which instrument has 88 keys?", "answer": "Piano", "category": "Music"},
    23: {"question": "What is the smallest country in the world?", "answer": "Vatican City", "category": "Geography"},
    24: {"question": "How many colors are there in a rainbow?", "answer": "7", "category": "General"},
    25: {"question": "What is the most spoken native language in the world?", "answer": "Mandarin Chinese", "category": "Language"},
    26: {"question": "Which animal is known as the Ship of the Desert?", "answer": "Camel", "category": "General"},
    27: {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare", "category": "Literature"},
    28: {"question": "What is the capital of Australia?", "answer": "Canberra", "category": "Geography"},
    29: {"question": "What pigment gives leaves their green color?", "answer": "Chlorophyll", "category": "Science"},
    30: {"question": "Which cartoon character lives in a pineapple under the sea?", "answer": "SpongeBob SquarePants", "category": "Entertainment"},
    31: {"question": "What is the main gas found in the air we breathe?", "answer": "Nitrogen", "category": "Science"},
    32: {"question": "How many players are on a soccer field for one team?", "answer": "11", "category": "Sports"},
    33: {"question": "Which country is famous for the pyramids?", "answer": "Egypt", "category": "Geography"},
    34: {"question": "What is the currency used in the United Kingdom?", "answer": "Pound sterling", "category": "Finance"},
    35: {"question": "Who was the first person to walk on the moon?", "answer": "Neil Armstrong", "category": "History"},
    36: {"question": "What is the name of the wizarding school in Harry Potter?", "answer": "Hogwarts", "category": "Literature"},
    37: {"question": "Which operating system uses a green robot as its mascot?", "answer": "Android", "category": "Technology"},
    38: {"question": "What is the standard dynamic resolution of a Full HD monitor?", "answer": "1920x1080", "category": "Technology"},
    39: {"question": "How many sides does a stop sign have?", "answer": "8", "category": "General"},
    40: {"question": "What is the largest mammal in the world?", "answer": "Blue whale", "category": "Science"},
    41: {"question": "Which food never expires and can last for thousands of years?", "answer": "Honey", "category": "Food"},
    42: {"question": "What is the square root of 144?", "answer": "12", "category": "Math"},
    43: {"question": "Which ancient civilization built the Colosseum?", "answer": "Romans", "category": "History"},
    44: {"question": "What is the capital of Canada?", "answer": "Ottawa", "category": "Geography"},
    45: {"question": "How many teeth does an adult human normally have?", "answer": "32", "category": "Science"},
    46: {"question": "Which popular video game is made entirely of blocks?", "answer": "Minecraft", "category": "Entertainment"},
    47: {"question": "What is the fastest land animal?", "answer": "Cheetah", "category": "Science"},
    48: {"question": "Who is the Norse god of thunder?", "answer": "Thor", "category": "General"},
    49: {"question": "What is the name of the long sleep animals take in winter?", "answer": "Hibernation", "category": "Science"},
    50: {"question": "Which country produces the most coffee in the world?", "answer": "Brazil", "category": "Food"},
    51: {"question": "What is the chemical formula for water?", "answer": "H2O", "category": "Science"},
    52: {"question": "How many strings does a standard violin have?", "answer": "4", "category": "Music"},
    53: {"question": "Which vitamin do we get from sunlight?", "answer": "Vitamin D", "category": "Science"},
    54: {"question": "What is the capital of Italy?", "answer": "Rome", "category": "Geography"},
    55: {"question": "Who invented the lightbulb?", "answer": "Thomas Edison", "category": "History"},
    56: {"question": "What do bees collect from flowers to make honey?", "answer": "Nectar", "category": "Science"},
    57: {"question": "Which planet is closest to the Sun?", "answer": "Mercury", "category": "Science"},
    58: {"question": "What language is spoken in Brazil?", "answer": "Portuguese", "category": "Language"},
    59: {"question": "How many minutes are in one day?", "answer": "1440", "category": "General"},
    60: {"question": "What is the name of the galaxy we live in?", "answer": "Milky Way", "category": "Science"},
    61: {"question": "Which country gifted the Statue of Liberty to the USA?", "answer": "France", "category": "History"},
    62: {"question": "What is the main ingredient in chocolate?", "answer": "Cocoa", "category": "Food"},
    63: {"question": "How many human players are on the ice during a standard hockey game per team?", "answer": "6", "category": "Sports"},
    64: {"question": "What is the capital of New York state?", "answer": "Albany", "category": "Geography"},
    65: {"question": "Who was the first president of the United States?", "answer": "George Washington", "category": "History"},
    66: {"question": "What force pulls objects toward the center of the Earth?", "answer": "Gravity", "category": "Science"},
    67: {"question": "Which ocean is located between the Americas and Europe?", "answer": "Atlantic Ocean", "category": "Geography"},
    68: {"question": "What is the name of the fairy in Peter Pan?", "answer": "Tinker Bell", "category": "Entertainment"},
    69: {"question": "How many degrees are in a right angle?", "answer": "90", "category": "Math"},
    70: {"question": "What is the largest country by land area?", "answer": "Russia", "category": "Geography"},
    71: {"question": "Which metal is liquid at room temperature?", "answer": "Mercury", "category": "Science"},
    72: {"question": "Who wrote 'The Odyssey'?", "answer": "Homer", "category": "Literature"},
    73: {"question": "What is the most popular sport in the world?", "answer": "Football", "category": "Sports"},
    74: {"question": "Which bird cannot fly but is an excellent swimmer?", "answer": "Penguin", "category": "Science"},
    75: {"question": "What is the capital of Spain?", "answer": "Madrid", "category": "Geography"},
    76: {"question": "How many curves or loops are in a standard paperclip?", "answer": "3", "category": "General"},
    77: {"question": "What is the official currency of Japan?", "answer": "Yen", "category": "Finance"},
    78: {"question": "Which gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide", "category": "Science"},
    79: {"question": "Who is known as the King of Pop?", "answer": "Michael Jackson", "category": "Music"},
    80: {"question": "What is the largest internal organ in the human body?", "answer": "Liver", "category": "Science"},
    81: {"question": "Which island country is located next to Australia?", "answer": "New Zealand", "category": "Geography"},
    82: {"question": "How many centimeters are in one meter?", "answer": "100", "category": "General"},
    83: {"question": "What is the name of the scale used to measure earthquakes?", "answer": "Richter scale", "category": "Science"},
    84: {"question": "Who is the main protagonist in The Legend of Zelda video games?", "answer": "Link", "category": "Entertainment"},
    85: {"question": "What is the capital city of France?", "answer": "Paris", "category": "Geography"},
    86: {"question": "Which element does 'O' represent on the periodic table?", "answer": "Oxygen", "category": "Science"},
    87: {"question": "How many total cards are in a standard deck excluding jokers?", "answer": "52", "category": "General"},

}

# choose category and randomize question
score = 0
valid_categories = [
    "Science", "Geography", "Food", "Technology", "Sports",
    "History", "General", "Art", "Literature", "Music",
    "Language", "Entertainment", "Finance", "Math"
]

while True:
    category = input(
        f"Choose a category ({', '.join(valid_categories)}) or type 'exit': "
    ).strip()

    normalized_category = category.lower()

    if normalized_category == "exit":
        print(f"Your final score is: {score}")
        break

    valid_categories_lower = {name.lower() for name in valid_categories}

    if normalized_category not in valid_categories_lower:
        print("Invalid category")
        continue

    matching_questions = [
        q_data for q_data in questions.values()
        if q_data["category"].lower() == normalized_category
    ]

    if not matching_questions:
        print("No questions available for that category.")
        continue

    random_question = random.choice(matching_questions)
    print(random_question["question"])

    user_input = input("Enter your answer: ").strip()

    if user_input.lower() == "exit":
        print(f"Your final score is: {score}")
        break

    if user_input.lower() == random_question["answer"].lower():
        score += 1
        print("Correct!")
        print(f"Your current score is: {score}")
    else:
        print(f"Incorrect. The correct answer is: {random_question['answer']}")
        print(f"Your current score is: {score}")
