questions = [
    {
        "text": "It's a rainy day night. What are you doing?",
        "choices": {
            "1": "studying for tests",
            "2": "shopping online for new clothes because you can never get enough",
            "3": "cooking up a mid-night snack for yourself",
            "4": "binging a tv show under your blankets while you rot in bed",
            "5": "on a call with your best friend"
        }
    },
    {
        "text": "what is your favorite season?",
        "choices": {
            "1":"winter",
            "2":"autumn",
            "3":"spring",
            "4":"summer",
            "5":"all of them!"
        }
    },
    {
        "text": "What is your favorite dessert?",
        "choice": {
            "1": "tiramisu"
            "2": ""
            "3": "milk"
            "4": "caramel machiatto"
            "5": "brown sugar milk tea"
        }
    }
    {
         "text": "Which animals resonates with you the most",
        "choice": {
            "1": "raven"
            "2": "snake"
            "3": "butterfly"
            "4": "cat"
            "5": "dove"
        }
    }
    {
         "text": "Choose a superpower",
        "choice": {
            "1": "invisibility"
            "2": "immortality"
            "3": "animal-communication"
            "4": "teleportation"
            "5": "flying"
        }
    }
    {
         "text": "Pick a nature landscape",
        "choice": {
            "1": "snowy mountains",
            "2": "volcanic beach",
            "3": "mossy forest",
            "4": "lily-pad pond",
            "5": "bubbling creek"
        }
    }
    {
         "text": "Which quote resonates with you the most",
        "choice": {
            "1": "Pain and suffering are always inevitable for a large intelligence and a deep heart. The really great men must, I think, have great sadness on earth.",
            "2": "You will always be fond of me. I represent to you all the sins you never had the courage to commit.",
            "3": "One of the deep secrets of life is that all that is really worth the doing is what we do for others.",
            "4": "Don't feel bad for one moment about doing what brings you joy.",
            "5": "Things are going round and round in my head--or maybe my head is going round and round in things."
        }
    }

]
results = {
    "1": "Crime and Punishment: You're morally grey",
    "2": "The Picture of Dorian Gray: You're an artist",
    "3": "Alice and Wonderland: You don't really belong, in a good way!",
    "4": "A Court of Thorns and Roses: You give main character vibes.",
    "5": "Howl's Moving Castle: You're a sweet innocent person."
}
numEach = [0,0,0,0,0]

def run(): 
    print()"Welcome! Answer questions to find out which book suits you the most!")
    for questionNum in range(len(questions)):
        getQuestion(questionNum)

def getQuestion(num):
    test = questions[num]["text"]
    print[text]
    choices = question[num]["choices"]
    for i in range(len(choices)):
        print(f"(i + 1). (choices[f"(i + 1)"))



