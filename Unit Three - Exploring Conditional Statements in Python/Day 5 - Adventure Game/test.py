class QuestionAnswer:
    def __init__(self):
        self.id = ""
        self.question = ""
        self.choices = []
        self.choice_mapping = []

class QABank:
    def __init__(self):
        self.bank = {}
        self.setup_bank()

    def setup_bank(self):
        qa = QuestionAnswer()
        qa.id = "superhero_pick"
        qa.question = "What is your favourite super hero?"
        qa.choices = ["Batman", "Superman", "Spiderman", "Wonderwoman"]
        qa.choice_mapping = ["confrontorseek", "confrontorseek", "confrontorseek", "confrontorseek"]
        self.bank[qa.id] = qa

        qa = QuestionAnswer()
        qa.id = "confrontorseek"
        qa.question = "Confront or seek assistance?"
        qa.choices = ["Confront", "Seek Assistance"]
        qa.choice_mapping = ["confront", "seek"]
        self.bank[qa.id] = qa

        qa = QuestionAnswer()
        qa.id = "confront"
        qa.question = "Be Nice or Be Mean?"
        qa.choices = ["Nice", "Mean"]
        qa.choice_mapping = ["nice", "mean"]
        self.bank[qa.id] = qa

        qa = QuestionAnswer()
        qa.id = "nice"
        qa.question = "Well done. This is the best way to solve all problems"
        qa.choices = []
        qa.choice_mapping = []
        self.bank[qa.id] = qa

        qa = QuestionAnswer()
        qa.id = "seek"
        qa.question = "Beg or ask politely?"
        qa.choices = ["beg", "ask"]
        qa.choice_mapping = ["beg", "ask"]
        self.bank[qa.id] = qa


        qa = QuestionAnswer()
        qa.id = "random"
        qa.question = "What is your favourite colour?"
        qa.answers = ["Red", "Blue", "Green", "Purple"]
        self.bank[qa.id] = qa

    def get_initial_question(self):
        return(self.bank["superhero_pick"])

def pose_question(q: QuestionAnswer):
    while( True ):
        print(q.question)
        for index, choice in enumerate(q.choices):
            print (index, choice)

        if len(q.choices) > 0:
            answer = input()

            if answer.isdigit() and int(answer) >= 0 and int(answer) < len(q.choices):
                return(int(answer))
            else:
                print("Invalid choice, try again")
        else:
            return None

def determine_next_question(answer, current_question: QuestionAnswer, qabank):
    next_question_string = current_question.choice_mapping[answer]
    if next_question_string in qabank.bank:
        next_question = qabank.bank[next_question_string]
    else:
        next_question = None
    return(next_question)

def main():
    qabank = QABank()
    current_question = qabank.get_initial_question()
    while(True):
        if current_question is None:
            break
        answer = pose_question(current_question)
        if answer is not None:
            current_question = determine_next_question(answer, current_question, qabank)
        else:
            current_question = None

if __name__ == "__main__":
    main()