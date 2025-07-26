THEME_COLOR = "#375362"

from tkinter import * 
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        # Setup Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20 , pady=20, bg=THEME_COLOR)

        # Setup Canvas & Text
        self.canvas = Canvas(height=250, width=300)
        self.text = self.canvas.create_text(150 , 125 , width=280, text="Hello", font=("Ariel", 20 , "italic"))
        self.canvas.grid(column = 1, row = 1, columnspan=2)
        
        # True & False Image Path
        true_button_image = PhotoImage(file = r"day-34\quizzler-app-start\images\true.png")
        false_button_image = PhotoImage(file = r"day-34\quizzler-app-start\images\false.png")

        # True Button
        self.true_button = Button(image=true_button_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column = 1 , row=2, pady=40)  

        # False Button
        self.false_button = Button(image= false_button_image, highlightthickness=0 , pady=20, command= self.false_answer)
        self.false_button.grid(column=2, row=2, pady=40)

        # Score Label
        self.label = Label(text="Score: 0", bg=THEME_COLOR, font=("arial", 10, "bold"), fg = "white")
        self.label.grid(column = 2 , row= 0, pady=20, sticky="e")

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(self.canvas , bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="Game has Ended")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_answer(self):
        user_answer = self.quiz.check_answer("True")
        self.label.config(text = f"Score: {self.quiz.score}")
        self.give_feedback(user_answer)

    def false_answer(self):
        user_answer = self.quiz.check_answer("False")
        self.label.config(text = f"Score: {self.quiz.score}")
        self.give_feedback(user_answer)
       
    def give_feedback(self , user_answer):
        if user_answer:
            self.canvas.config(self.canvas, bg="green")
        else:
            self.canvas.config(self.canvas, bg="red")
        self.window.after(1000,self.get_next_question)
        
        




            
        