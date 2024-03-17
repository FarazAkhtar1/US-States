from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("US States Game")

image = "Projects\\US States Game\\blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()  
turtle.shape(image)  



data = pandas.read_csv("Projects\\US States Game\\50_states.csv")
list_of_states = data["state"].to_list()
print(list_of_states)

with open("Projects\\US States Game\\no_of_correct.txt", mode="w") as text_file:
    text_file.write("0")



game_is_on = True
while game_is_on:

    with open("Projects\\US States Game\\no_of_correct.txt") as text_file:
        no_of_correct_guessed = text_file.read()
        no_of_correct_guessed_in_int = int(no_of_correct_guessed)
    
    
    answer_state = screen.textinput(title= f"{no_of_correct_guessed_in_int}/ 50", prompt= "Whats another state name?").title()
    print(answer_state)

    if answer_state in list_of_states:
        with open("Projects\\US States Game\\no_of_correct.txt", mode="w") as text_file:
            no_of_correct_guessed_in_int+=1
            text_file.write(str(no_of_correct_guessed_in_int))
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(int(data["x"][data["state"] == answer_state]),int(data["y"][data["state"] == answer_state] ))
        state_turtle.write(f"{answer_state}")

screen.exitonclick()
