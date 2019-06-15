class Question:

    def __init__(self, fragg,abdruck = 0):
        self.frage = fragg
        self.abdruck = abdruck
        self.answers=[]

    def add_answer(self, answer, faktor=1):
        self.answers.append(Answer(answer, faktor = faktor))

    def __str__(self):
        return self.frage + ' (' + ", ".join(self.answers) + ')'

    def toJSON(self):
        answers = []
        for answer in self.answers:
            answers.append(answer.title)

        return  {
            'frage':self.frage,
            'antworten':answers
        },

class Answer:

    def __init__(self, title, faktor=1):
        self.title = title
        self.faktor = faktor

    def __str__(self):
        return self.title

def getQuestions():
    result = []
    question = Question('Treiben Sie Sport', 1130)
    question.add_answer("nein")
    question.add_answer("ja", faktor=1.1)
    result.append(question)

    question = Question('Wie lange duschst du', 9999)
    question.add_answer("3 min", faktor=3)
    question.add_answer("5 min", faktor=5)
    question.add_answer("10 min", faktor=10)
    result.append(question)
    
    question = Question('Wie oft essen Sie Fleisch?', 1204)
    question.add_answer("täglich", faktor=20)
    question.add_answer("mehrmals wöchentlich", faktor=12.2)
    question.add_answer("einmal die Woche", faktor=3)
    question.add_answer("nie")
    result.append(question)
    
    return result


questions = getQuestions()
result = []
for question in questions:
    result.append(question.toJSON)
print(result)