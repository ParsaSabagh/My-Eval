from my_eval import my_eval

def inputting():
    inputted_string = input("Please Enter Your Math Phrase Here: ")
    if inputted_string == "":
        inputting()
    return inputted_string


my_eval(inputting())
