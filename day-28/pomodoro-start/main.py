from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_text.config(text= "Timer")
    canvas.itemconfig(countdown_timer, text="00:00")
    check_marks.config(text="")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_second = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_text.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_text.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_text.config(text="Work", fg=GREEN)
        count_down(work_second)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60 

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(countdown_timer, text =f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✅"
        check_marks.config(text = marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100 , pady=50, bg=YELLOW)

canvas = Canvas(width = 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=r"day-28\pomodoro-start\tomato.png")
canvas.create_image(100 , 112, image= tomato_image )
countdown_timer = canvas.create_text(100,130, text="00:00", fill="white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)


timer_text = Label(text = "Timer", font = (FONT_NAME , 30, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
timer_text.grid(column=1, row=0)

start_button = Button(width=10 , text="Start", font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start_button.grid(column=0 , row=5)

reset_button = Button(width=10 , text="Reset", font=(FONT_NAME, 10), highlightthickness=0, command= reset_timer)
reset_button.grid(column=2 , row=5)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
check_marks.grid(column = 1 , row = 6 )


window.mainloop()