from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import pandas as pd

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

df = pd.read_csv(filename)

user_input = input("what do you want to do (Please Enter the Fist letter in the Name Capital): ")
choice = user_input.lower()

class simple_missions:
    # Split the text into words
    words = choice.split()

    if "last" in choice:
        number = int([word for word in words if word.isdigit()][0])
        print(df.tail(number))


    elif "first" in choice:
        number = int([word for word in words if word.isdigit()][0])
        print(df.head(number))


    elif "average" in choice:
        # Find the index of the word "column"
        index = words.index("average")

        # Get the word before the column word
        previous_word = words[index + 1]
        previous_word = previous_word[0].upper() + previous_word[1:]

        # Print the previous word
        print(df[previous_word].mean())


    elif "max" in choice:
        # Find the index of the word "column"
        index = words.index("maximum") if "maximum" in words else words.index("max")

        # Get the word before the column word
        previous_word = words[index + 1]
        previous_word = previous_word[0].upper() + previous_word[1:]

        # Print the previous word
        print(df[previous_word].max())


    elif "min" in choice:
        # Find the index of the word "column"
        index = words.index("minimum") if "minimum" in words else words.index("min")

        # Get the word before the column word
        previous_word = words[index + 1]
        previous_word = previous_word[0].upper() + previous_word[1:]

        # Print the previous word
        print(df[previous_word].min())


    elif "column" in choice and "sort" not in choice:
        import re
        if "and" in user_input:
            capital_words = re.findall(r"\b[A-Z]\w+", user_input)
            print(df[capital_words])

        else:
            index = words.index("column")
            previous_word = words[index - 1]
            previous_word = previous_word[0].upper() + previous_word[1:]
            print(df[previous_word])



    elif "row" in choice:
        if "from" in choice:
            numbers = [int(word) for word in words if word.isdigit()]
            first_num = numbers[0] - 1
            second_num = numbers[1]
            print(df.iloc[first_num: second_num])

        elif "and" in choice:
            numbers = [int(word) for word in words if word.isdigit()]
            for number in numbers:
                number = number - 1
                print(df.iloc[number])
        else:
            print("Theres something wrong, please try again!")


    elif "sort" in choice:
        index = words.index("column")
        column = words[index - 1]
        column = column[0].upper() + column[1:]

        print(df.sort_values(column, ascending=True))

    else:
        print("There is Error please try again!!!")

    closing = input("Before closing, Do you want to save the data (yes, no)? ")
    if closing == "yes":
        df.to_csv('Downloads/yes.csv')
        print("saved to downloads")
    
    elif closing == "No":
        print("Ok, Thank you")
        exit

    else:
        print("Error, Pleas try again")

class complex_missions:
    pass