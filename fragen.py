class Question:

    def __init__(self, fragg):
        self.frage = fragg
        self.answers=[]

    def add_answer(self, answer):
        self.answers.append(answer)

    def __str__(self):
        return self.frage + ' (' + ", ".join(self.answers) + ')'

    def toJSON(self):
        return  {
            'frage':self.frage,
            'antworten':self.answers
        },

def getQuestions():
    result = []
    question = Question('Treiben Sie Sport')
    question.add_answer("nein")
    question.add_answer("ja")
    result.append(question)

    question = Question('Wie lange duschst du')
    question.add_answer("3 min")
    question.add_answer("5 min")
    question.add_answer("10 min")
    result.append(question)
    
    question = Question('Wie oft essen Sie Fleisch?')
    question.add_answer("täglich")
    question.add_answer("mehrmals wöchentlich")
    question.add_answer("einmal die Woche")
    question.add_answer("nie")
    result.append(question)
    
    return result


questions = getQuestions()
result = []
for question in questions:
    result.append(question.toJSON)
print(result)