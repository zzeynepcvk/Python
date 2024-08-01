#questions 

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer==answer


#Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuesiton(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+ q)

        answer = input('cevabınız : ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

        

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuesiton()

    def showScore(self):
        print('score :',self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex+1

        if questionNumber > totalQuestion:
            print('Quiz bittii.')
        else:
            print(f'Quesiton {questionNumber} of {totalQuestion}.'.center(100,'-'))

q1 = Question('en iyi programlama dili hangisi?',['C#','Python','js','java'],'Python')
q2 = Question('en popüler programlama dili hangisi?',['C#','Python','js','java'],'Python')
q3 = Question('en çok kazandıran programlama dili hangisi?',['C#','Python','js','java'],'Python')

questions =[q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()

#başarılı