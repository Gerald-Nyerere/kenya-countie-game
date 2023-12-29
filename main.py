import turtle
import pandas


screen = turtle.Screen()
screen.title("KENYA COUNTY GAME")
image = "county.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("kenya_counties.csv")
all_counties = data.county.to_list()
geused_county = []

#use the loop to allow the user to keep geuessing
while len(geused_county) < 50:
    #convert the geus to Title Case
    answer_county = screen.textinput(title=f"{len(geused_county)}/50 counties Correct", prompt="What's another county's name?").title()

    
    #Keep track of the score
    if answer_county == "Exit":
        missing_counties = []
        for county in all_counties:
            if county not in  geused_county:
                missing_counties.append(county)
        new_data = pandas.DataFrame(missing_counties)
        new_data.to_csv("counties_to_learn.csv")
        break

    #check if the geus is among the 47 counties
    if  answer_county in all_counties:
        geused_county.append(answer_county)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        county_data = data[data.county == answer_county]
        t.goto(int(county_data.x), int(county_data.y))
        #write correct guesses onto map
        t.write(answer_county)








