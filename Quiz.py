class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    'Who created Javascript?\n (a) Brenden Eich\n (b) Elon Musk ',
    'Who created Microsoft?\n (a) Elon Musk\n (b) Bill Gate ',
]

questions =[
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'b')
]

def run_quiz(Question):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f'You got {score} out of {len(questions)} ')

run_quiz(questions)
