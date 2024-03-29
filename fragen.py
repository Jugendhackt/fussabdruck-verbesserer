class Question:

    def __init__(self, fragg, abdruck = 0):
        self.frage = fragg
        self.abdruck = abdruck
        self.hint = None
        self.answers=[]

    def add_answer(self, answer, faktor=1,hint=None):
        self.answers.append(Answer(answer, faktor = faktor,hint=hint))

    def add_hint(self,hint):
        self.hint = hint

    def __str__(self):
        return self.frage + ' (' + ", ".join(self.answers) + ')'

    def toJSON(self):
        answers = []
        for answer in self.answers:
            answers.append(answer.title)

        return  {
            'frage':self.frage,
            'antworten':answers, 
            'hint':self.hint
        }

    def getAbdruck (self, answer_id):
        answer = self.answers[answer_id]
        return self.abdruck * answer.faktor
    
    def getAnswerHint (self, answer_id):
        answer = self.answers[answer_id]
        return answer.hint


class Answer:

    def __init__(self, title, faktor=1,hint=None):
        self.title = title
        self.faktor = faktor
        self.hint = hint

    def __str__(self):
        return self.title

def getQuestions():
    result = []
    question = Question('Treiben Sie Sport', 1130)
    question.add_answer("nein")
    question.add_answer("ja", faktor=1.1)
    result.append(question)

    question = Question('Wie lange duschst du', 999)
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

if __name__ == "__main__": 
    questions = getQuestions()
    result = []
    for question in questions:
        result.append(question.toJSON())
    print(result)

    abdruck = questions[0].getAbdruck(1) + questions[1].getAbdruck(0) + questions[2].getAbdruck(2)
    print(abdruck)