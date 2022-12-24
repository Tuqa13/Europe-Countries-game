import turtle
import pandas

screen = turtle.Screen()
screen.title("Europe Countries Game")

image = "blank_map.gif"
screen.addshape(image)
turtle.shape(image)


answer_country = screen.textinput(title="Guess the country", prompt="What's the guess?").title()
data = pandas.read_csv("Europe.csv")
countries_list = data.country.to_list()

x = 0
y = 0
correct_guessed = []


while len(correct_guessed) < len(countries_list):
    if answer_country == "Exit":
        break
    if answer_country.lower() == "uk":
        answer_country = "United Kingdom"
    if answer_country.lower() == "bih" or answer_country.lower() == "b&h":
        answer_country = "Bosnia and Herzegovina"
    if answer_country in countries_list:
        myTurtle = turtle.Turtle()
        myTurtle.hideturtle()
        myTurtle.penup()
        destination = data[data.country == answer_country]
        myTurtle.goto(int(destination.x), int(destination.y))
        myTurtle.write(answer_country, font=("Calibri", 10, "bold italic"))
        correct_guessed.append(destination)

    answer_country = screen.textinput(title=f"{len(correct_guessed)} / {len(countries_list)}  Countries correct."
                                      , prompt="What's the guess?").title()

