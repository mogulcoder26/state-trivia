import turtle
import pandas as pd

state_data = pd.read_csv("/50_states.csv")
all_states = state_data["state"].to_list()
print(all_states)

### Setting up the Screen with US Map ###
s = turtle.Screen()
s.title("US State Quiz")
Image = "blank_states_img.gif"
s.addshape(Image)
turtle.addshape(Image)
turtle.shape(Image)

writer = turtle.Turtle()
writer.hideturtle()
writer.pencolor("red")
writer.penup()

i = 0


def Winner():
    turtle.textinput(prompt=f"""You Guessed All!""", title="Win!")
    exit()


def NotifyDuplicacy(name):
    turtle.textinput(prompt=f"You Have Guessed {name} before", title="Duplicate!")


def checkDuplicacy(name, Correct_Guesses):
    for i in range(0, len(Correct_Guesses)):
        if name == Correct_Guesses[i]:
            return False
    return True


def NotifyIncorrect(name):
    turtle.textinput(prompt=f'''There's no state "{name}"''', title="Duplicate!")


Correct_Guesses = []
learning_states = []

for _ in range(0, 49):
    name = turtle.textinput(prompt="Guess a State!", title="Type the name :")
    name = name[0].upper() + name[1::]
    if name == "Exit":
        for state in all_states:
            if state not in Correct_Guesses:
                learning_states.append(state)
        df = pd.DataFrame(learning_states)
        df.to_csv("25_pandas/learnthis.csv")
        break
    print(f"name, {name}")

    try:
        if state_data[state_data["state"] == name]["state"].to_list()[
            0
        ] == name and checkDuplicacy(name, Correct_Guesses):
            Correct_Guesses.append(name)
            print("Correct!")
            i += 1
            s.title(f"{i}/10 Correct")
            coords = (
                state_data[state_data["state"] == name].x.to_list()[0],
                state_data[state_data["state"] == name].y.to_list()[0],
            )
            print(coords)
            writer.goto(coords)
            writer.write(name, font=("Courier", 8, "normal"))
        else:
            NotifyDuplicacy(name)
            print("Duplicacy Detected!")
    except Exception as e:
        NotifyIncorrect(name)
        print(f"Incorrect,{e}")

if i == 49:
    Winner()
