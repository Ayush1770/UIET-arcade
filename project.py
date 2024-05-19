from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("UIET ARCADE")
root.geometry("650x535")
label=Label(root,text="WELCOME TO UIET ARCADE ",font="Arial 20 bold")
label.pack(side=TOP)
root.maxsize(650,535)

def guess():
    
    from tkinter import messagebox
    from random import randint

   
    root = Tk()
    root.geometry("500x500")
    root.title("Number Guessing Game")

    
    def GenerateNumberFunc():
        global Number
        
        Number = randint(1, 100)

        
        messagebox.showinfo("A Number was Generated!", "Please Guess the Number")

    
    def GuessNumberFunc():
        global Number
        
        UserResponse = AnswerEntry.get()

        
        UserResponse = int(UserResponse)

        
        if UserResponse > Number:
            ResultLabel.config(text="Incorrect! Please Guess Lower", fg="Red")
        elif UserResponse < Number:
            ResultLabel.config(text="Incorrect! Please Guess Higher", fg="Red")
        else:
            ResultLabel.config(text="You Guess Correctly! The Number was {}".format(Number), fg="Green")
            AnswerEntry.delete(0, "end")

   
    Title = Label(root, text="Number Guessing Game", font=("Arial", 30))
    Title.pack()

    
    MainFrame = Frame(root)
    MainFrame.pack(pady=60)

    
    GuessNumLabel = Label(MainFrame, text="Guess a number from 1 to 100:", font=("Arial", 20))
    GuessNumLabel.pack()

    
    AnswerEntry = Entry(MainFrame, font=("Arial", 16))
    AnswerEntry.pack(pady=10)

    
    GenerateNumberBtn = Button(MainFrame, text="Generate Number", width=16, font=("Arial", 16), background="Dodgerblue",
                               command=GenerateNumberFunc)
    GenerateNumberBtn.pack()

   
    GuessBtn = Button(MainFrame, text="Guess", width=16, font=("Arial", 16), background="#15e650",
                      command=GuessNumberFunc)
    GuessBtn.pack(pady=5)

    
    ResultLabel = Label(MainFrame, text="", font=("Arial", 16))
    ResultLabel.pack()

   
    root.mainloop()
def Tic():
    import random
    global player
    def next_turn(row, column):

        global player

        if buttons[row][column]['text'] == "" and check_winner() is False:

            if player == players[0]:

                buttons[row][column]['text'] = player

                if check_winner() is False:
                    player = players[1]
                    label.config(text=(players[1] + " turn"))

                elif check_winner() is True:
                    label.config(text=(players[0] + " wins"))

                elif check_winner() == "Tie":
                    label.config(text="Tie!")

            else:

                buttons[row][column]['text'] = player

                if check_winner() is False:
                    player = players[0]
                    label.config(text=(players[0] + " turn"))

                elif check_winner() is True:
                    label.config(text=(players[1] + " wins"))

                elif check_winner() == "Tie":
                    label.config(text="Tie!")

    def check_winner():

        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return True

        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True

        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True

        elif empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Tie"

        else:
            return False

    def empty_spaces():

        spaces = 9

        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def new_game():

        global player

        player = random.choice(players)

        label.config(text=player + " turn")

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="", bg="#F0F0F0")

    window = Tk()
    window.title("Tic-Tac-Toe")
    players = ["x", "o"]
    player = random.choice(players)
    buttons = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    label = Label(text=player + " turn", font=('consolas', 40))
    label.pack(side="top")

    reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
    reset_button.pack(side="top")

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                          command=lambda row=row, column=column: next_turn(row, column))
            buttons[row][column].grid(row=row, column=column)

    window.mainloop()

def snake():
    import random

    GAME_WIDTH = 600
    GAME_HEIGHT = 600
    SPEED = 90
    SPACE_SIZE = 20
    BODY_PARTS = 3
    SNAKE_COLOR = "#00FF00"
    FOOD_COLOR = "#FF0000"
    BACKGROUND_COLOR = "#000000"

    class Snake:

        def _init_(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                self.squares.append(square)

    class Food:

        def _init_(self):
            x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

    def next_turn(snake, food):

        x, y = snake.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:

            global score

            score += 1

            label.config(text="Score:{}".format(score))

            canvas.delete("food")

            food = Food()

        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]

        if check_collisions(snake):
            game_over()

        else:
            window.after(SPEED, next_turn, snake, food)

    def change_direction(new_direction):

        global direction

        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        elif new_direction == 'down':
            if direction != 'up':
                direction = new_direction

    def check_collisions(snake):

        x, y = snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over():

        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                           font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")

    window = Tk()
    window.title("Snake game")
    window.resizable(False, False)

    score = 0
    direction = 'down'

    label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    next_turn(snake, food)

    window.mainloop()

def rock():
    import random

    root = Tk()

    root.geometry("600x600")

    root.title("Rock,Paper and Scissors")

    computer_value = {
        "0": "Rock",
        "1": "Paper",
        "2": "Scissor"
    }

    def reset_game():
        b1["state"] = "active"
        b2["state"] = "active"
        b3["state"] = "active"
        l1.config(text="Player              ")
        l3.config(text="Computer")
        l4.config(text="")

    def button_disable():
        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    def isrock():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "DRAW (*￣０￣)"
        elif c_v == "Scissor":
            match_result = "You WIN (≧∇≦)!"
        else:
            match_result = "You LOSE ಥ_ಥ"
        l4.config(text=match_result)
        l1.config(text="Rock            ")
        l3.config(text=c_v)
        button_disable()

    def ispaper():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Paper":
            match_result = "DRAW (*￣０￣)"
        elif c_v == "Scissor":
            match_result = "You LOSE ಥ_ಥ"
        else:
            match_result = "You WIN (≧∇≦)!"
        l4.config(text=match_result)
        l1.config(text="Paper           ")
        l3.config(text=c_v)
        button_disable()

    def isscissor():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "You LOSE ಥ_ಥ"
        elif c_v == "Scissor":
            match_result = "DRAW (*￣０￣)"
        else:
            match_result = "You WIN (≧∇≦)!"
        l4.config(text=match_result)
        l1.config(text="Scissor         ")
        l3.config(text=c_v)
        button_disable()

    Label(root,
          text="ROCK PAPER & SCISSORS (👉ﾟヮﾟ)👉",
          font="normal 25 bold",
          fg="Black").pack(pady=20)

    frame = Frame(root)
    frame.pack()

    l1 = Label(frame,
               text="Player              ",
               font=24)

    l2 = Label(frame,
               text="VS             ",
               font="normal 15 bold")

    l3 = Label(frame, text="Computer", font=24)

    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack()

    l4 = Label(root,
               text="",
               font="normal 20 bold",
               bg="white",
               width=15,
               borderwidth=2,
               relief="solid")
    l4.pack(pady=20)

    frame1 = Frame(root)
    frame1.pack()

    b1 = Button(frame1, text="🪨",
                font=10, fg="white", width=7,
                bg="black", command=isrock)

    b2 = Button(frame1, text="📃",
                font=10, fg="white", width=7,
                bg="black", command=ispaper)

    b3 = Button(frame1, text="✂",
                font=100, fg="white", width=7,
                bg="black", command=isscissor)

    b1.pack(side=LEFT, padx=10)
    b2.pack(side=LEFT, padx=10)
    b3.pack(padx=10)

    Button(root, text="Reset Game",
           font=10, fg="white",
           bg="black", command=reset_game).pack(pady=20)

    root.mainloop()

def colour():
    import tkinter.font as font
    import random

    colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink"]
    global timer,score,word_color
    timer = 40
    score = 0
    word_color = ''
    def CountDown():
        global timer
        if (timer >= 0):
            time_left.config(text="Game Ends in : " + str(timer) + "s")
            timer -= 1
            time_left.after(1000, CountDown)
            if (timer == -1):
                time_left.config(text="Game Over!!!")

    def startGame():
        global word_color

        if (timer == 40):
            CountDown()
            word_color = random.choice(colors).lower()
            display_words.config(text=random.choice(colors), fg=word_color)
            color_entry.bind('<Return>', displayNextWord)

    def resetGame():
        global timer, score, word_color
        timer = 40
        score = 0
        word_color = ''
        game_score.config(text="Your Score : " + str(score))
        display_words.config(text='')
        time_left.config(text="Game Ends in : -")
        color_entry.delete(0, END)


    def displayNextWord(event):
        global word_color
        global score
        if (timer > 0):
            if (word_color == color_entry.get().lower()):
                score += 1
                game_score.config(text="Your Score : " + str(score))
            color_entry.delete(0, END)
            word_color = random.choice(colors).lower()
            display_words.config(text=random.choice(colors), fg=word_color)

    window = Tk()
    window.geometry('600x300')
    window.title("Color Game")
    window.geometry("500x200")

    app_font = font.Font(family='Helvetica', size=12)

    game_desp = "Game Description: Enter the color of the word,not the word itself !!"
    myFont = font.Font(family='Helvetica')

    game_description = Label(window, text=game_desp, font=app_font, fg="black")
    game_description.pack()

    game_score = Label(window, text="Your Score : " + str(score), font=(font.Font(size=16)), fg="green")
    game_score.pack()

    display_words = Label(window, font=(font.Font(size=28)), pady=10)
    display_words.pack()

    time_left = Label(window, text="Game Ends in : -", font=(font.Font(size=14)), fg="orange")
    time_left.pack()

    color_entry = Entry(window, width=30)
    color_entry.pack(pady=10)

    btn_frame = Frame(window, width=80, height=40, bg='red')
    btn_frame.pack(side=BOTTOM)

    start_button = Button(btn_frame, text="Start", width=20, fg="black", bg="pink", bd=0, padx=20, pady=10,
                          command=startGame)
    start_button.grid(row=0, column=0)

    reset_button = Button(btn_frame, text="Reset", width=20, fg="black", bg="light blue", bd=0, padx=20, pady=10,
                          command=resetGame)
    reset_button.grid(row=0, column=1)

    window.geometry('600x300')
    window.mainloop()

frame = Frame(root, borderwidth=6,bg="grey", relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1 = Button(frame,fg="red",text="Snake Game",command=snake)
b1.pack(side=TOP,padx=25,pady=40)

b2 = Button(frame,fg="red",text="Guess The number",command=guess)
b2.pack(side=TOP,padx=30,pady=40)

b3 = Button(frame,fg="red",text="Guess Colour",command=colour)
b3.pack(side=TOP,padx=30,pady=40)

b4 = Button(frame,fg="red",text="Rock Paper scissors",command=rock)
b4.pack(side=TOP,padx=20,pady=40)

b5 = Button(frame,fg="red",text="Tic Tac Toe",command=Tic)
b5.pack(side=TOP,padx=20,pady=20)

photo=Image.open("img.png")
img=photo.resize((500,500))
my=ImageTk.PhotoImage(img)
rit=Label(image=my)
rit.pack()
root.mainloop()
