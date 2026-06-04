#! python 3.13.5

import random, ast

capitals = ast.literal_eval(open(r'C:\Users\HTC\python_code\Automate the boring stuff book project\Chapter_8(reading & writing files)(quiz files)\data.txt', encoding = 'utf-8').read())

for quizNumber in range(35):
    quizFile = open('quizfile%s.txt' % (quizNumber + 1), 'w')
    answerFile = open('answerfile%s.txt' % (quizNumber + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nBatch:\n\nSection:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNumber + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)
    
    for questionNumber in range(50):
        correctAns = capitals[states[questionNumber]]
        wrongAns = list(capitals.values())
        del wrongAns[wrongAns.index(correctAns)]
        wrongAns = random.sample(wrongAns, 3)
        ansOptions = wrongAns + [correctAns]
        random.shuffle(ansOptions)

    for questionNumber in range(50):
        quizFile.write('%s. What is the capital of %s?\n' % (questionNumber + 1, states[questionNumber]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('abcd'[i], ansOptions[i]))
        quizFile.write('\n')

        answerFile.write('%s. %s\n' % (questionNumber + 1, 'abcd'[ansOptions.index(correctAns)]))

quizFile.close()
answerFile.close()