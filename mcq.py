print ("Let's tke a test!!")
class Question:
    def __init__(self, prompt, answer):
        self.prompt=prompt
        self.answer=answer
question_prompts=[
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n",
    "What color are grapes?\n(a) Red\n(b) Purple\n(c) Orange\n",
    "What color are oranges?\n(a) Red\n(b) Purple\n(c) Orange\n"
]
questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
        outcome=("You got " + str(score)+" out of "+str(len(questions))+" correct")
        print (outcome)
run_test(questions)
