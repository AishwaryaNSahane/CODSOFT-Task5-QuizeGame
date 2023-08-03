import tkinter as tk
from tkinter import messagebox
import random

quiz_data = [
    {
        'question': 'who developed Python programming language?',
        'choices': ['1. Wick van rossum', '2. Rasmus Lerdorf', '3. Guido van Rossume', '4. Niece'],
        'answer': '3. Guido van Rossume'
    },
    {
    
        'question': 'Which keyword is used for function in python?',
        'choices': ['1 Function', '2. def', '3. Fun', '4. Define'],
        'answer': '2. def'
    },
    {
        'question': 'In Python Programming Language comments are represent by which Symbol?',
        'choices': ['1. //', '2. #', '3. !', '4. /*'],
        'answer': '2. #'
    },
     {
        'question': 'Which of the following is not a core datatype in Python ?',
        'choices': ['1. Tuple', '2. Lists', '3. Class', '4. Dictionary'],
        'answer': '3. Class'
    },
     {
        'question': 'In which Language Python is written?',
        'choices': ['1. English', '2. PHP', '3. C', '4. All of the above'],
        'answer': '3. C'
    },
     {
        'question': 'Which of the following brackets are used in python to create List ?',
        'choices': ['1. ()', '2. []', '3. {}', '4. none of these'],
        'answer': '2. []'
    },
     {
        'question': 'Is Python supports exception handling?',
        'choices': ['1. YES', '2. NO' ,'3. Might be','4. none of the mention'],
        'answer': '1. YES'
    },
     {
        'question': 'What is the name of the operater ** in Python?',
        'choices': ['1. Exponential', '2. Modulus', '3. Floor division', '4. None of the mentioned above'],
        'answer': '1. Exponential'
    },
     {
        'question': 'Python Dictionary is used to store the data in a _______ format.',
        'choices': ['1. Key value pair', '2. Group value pair', '3. Select value pair', '4. None of the mentioned above'],
        'answer': '1. Key value pair'
    },
    {
    'question': 'In Python _________ defines a block of statements. ',
        'choices': ['1. Block', '2. Loop', '3. Indentation', '4. None of the mentioned above'],
        'answer': '3. Indentation'
    }
]

class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("600x500")
        self.configure(bg="lightpink")
        self.score = 0
        self.current_question = 0
        self.questions_answered = []
        self.create_widgets()

    def create_widgets(self):
        self.heading_label = tk.Label(self, text="Quize Game", font=("Arial", 22, "bold"), bg="lightpink",fg="purple")
        self.heading_label.pack(pady=20)

        self.question_label = tk.Label(self, text="", font=("Arial", 18, "bold"), wraplength=550, bg="yellow")
        self.question_label.pack(pady=10)

        self.choice_var = tk.StringVar()
        self.choice_var.set("")
        self.choices_radio = []
        for i in range(4):
            radio = tk.Radiobutton(self, text="", variable=self.choice_var, value="", font=("Arial", 16),bg="lightpink", anchor='w', command=self.submit_answer)
            self.choices_radio.append(radio)
            radio.pack(pady=5, anchor='w')

        self.feedback_label = tk.Label(self, text="", font=("Arial", 14, "bold"), bg="lightpink")
        self.feedback_label.pack(pady=10)

        self.prev_question_button = tk.Button(self, text="Previous Question", font=("Arial", 14, "bold"), command=self.prev_question)
        self.prev_question_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_question_button = tk.Button(self, text="Next Question", font=("Arial", 14, "bold"), command=self.next_question)
        self.next_question_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.submit_button = tk.Button(self, text="Submit", font=("Arial", 14, "bold"), bg="green",fg="purple", command=self.submit_quiz)
        self.submit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.score_button = tk.Button(self, text="View Score", font=("Arial", 14, "bold"), command=self.show_score)
        self.score_button.pack(side=tk.RIGHT, padx=10, pady=10)
        self.score_button.pack_forget()

        self.load_question(0)

    def load_question(self, question_index):
        if question_index < 0:
            
            return
        if question_index < len(quiz_data):
            self.current_question = question_index
            question = quiz_data[question_index]['question']
            choices = quiz_data[question_index]['choices']
            self.question_label.config(text=f"{question_index + 1}. {question}")
            for i in range(4):
                self.choices_radio[i].config(text=choices[i], value=choices[i])
            self.choice_var.set("")
            self.feedback_label.config(text="")
            self.prev_question_button.config(state=tk.DISABLED if question_index == 0 else tk.NORMAL)
            self.next_question_button.config(state=tk.DISABLED if question_index == len(quiz_data) - 1 else tk.NORMAL)
            self.submit_button.config(state=tk.NORMAL if question_index == len(quiz_data) - 1 else tk.DISABLED)
        else:
            self.show_final_results()

    def submit_answer(self):
        user_answer = self.choice_var.get()
        correct_answer = quiz_data[self.current_question]['answer']
        if user_answer == correct_answer:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text="Incorrect! The correct answer is: " + correct_answer, fg="red")

    def prev_question(self):
        self.submit_answer()
        self.load_question(self.current_question - 1)

    def next_question(self):
        self.submit_answer()
        self.load_question(self.current_question + 1)

    def submit_quiz(self):
        self.submit_answer()
        self.load_question(len(quiz_data))
        self.show_final_results()

    def show_final_results(self):
        final_result = f"Your final score is: {self.score}/{len(quiz_data)}"
        if self.score == len(quiz_data):
            final_result += "\nCongratulations! You got all the questions right!"
        elif self.score >= len(quiz_data) // 2:
            final_result += "\nGood job! You did well!"
        else:
            final_result += "\nKeep practicing to improve your score."

        messagebox.showinfo("Quiz Finished", final_result)
        self.score_button.pack()

    def show_score(self):
        score_message = f"Your final score is: {self.score}/{len(quiz_data)}"
        messagebox.showinfo("Quiz Score", score_message)

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.score = 0
            self.load_question(0)
            self.score_button.pack_forget()
        else:
            self.destroy()

if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
