def make_list(inputted_string):  # like "( 2 ** 10 ) / ( 2 * 16 )"
    inputted_string = inputted_string.replace(" ", "")
    inputted_list = []
    for character in inputted_string:
        inputted_list.append(character)
    return inputted_list
# will be['(', '2', '*', '*', '1', '0', ')', '/', '(', '2', '*', '1', '6', ')']


# like ['(', '2', '*', '*', '1', '0', ')', '/', '(', '2', '*', '1', '6', ')']
# notice the "*" , "*"
def make_signs(inputted_list):
    new_inputted_list = []
    last_character = ""
    for character in inputted_list:
        if character == "*" and last_character != "*":
            new_inputted_list.append("*")
        elif character == "*" and last_character == "*":
            new_inputted_list.pop()
            new_inputted_list.append("**")
        elif character == "+" or character == "-" or character == "/" \
                or character == "(" or character == ")" or character.isdigit():
            new_inputted_list.append(character)
        last_character = character
    return new_inputted_list
# will be ['(', '2', '**', '1', '0', ')', '/', '(', '2', '*', '1', '6', ')']
# notice the "**"


# like ['(', '2', '**', '1', '0', ')', '/', '(', '2', '*', '1', '6', ')']
# notice the "1" , "0" and "1" , "6"
def make_numbers(new_inputted_list):
    classified_list = []
    last_character = ""
    the_number = 0
    list_length = len(new_inputted_list)
    for character in new_inputted_list:
        if character.isdigit():
            the_number = (the_number * 10) + int(character)
        if character.isdigit() is False and last_character.isdigit():
            classified_list.append(the_number)
            the_number = 0
        if character == "+" or character == "-" or character == "/" \
                or character == "(" or character == ")" or character == "**" \
                or character == "*":
            classified_list.append(character)
        if list_length == 1 and character.isdigit():
            classified_list.append(the_number)
            the_number = 0
        last_character = character
        list_length -= 1
    return classified_list
# will be ['(', 2, '**', 10, ')', '/', '(', 2, '*', 16, ')']
# notice the 10 and 16


# like ['(', 2, '**', 10, ')', '/', '(', 2, '*', 16, ')']
def solve_the_innermost_bracket(classified_list):
    character_count = 0
    character2_count = 0
    the_innermost_bracket = []
    classified_list_copy = classified_list.copy()
    classified_list_copy.reverse()
    for character in classified_list:
        if character == ")":
            right_bracket = character_count
            for character2 in classified_list_copy[(len(classified_list)
                                                    - right_bracket - 1):]:
                if character2 == "(":
                    left_bracket = right_bracket - character2_count
                    the_innermost_bracket = classified_list[left_bracket
                                                            + 1:right_bracket]
                    solved_phrase = solve_phrase(the_innermost_bracket)
                    classified_list[left_bracket: right_bracket + 1] \
                        = solved_phrase  # replacing
                character2_count += 1
        if the_innermost_bracket is False:
            break
        character_count += 1
    return classified_list
    # will be [ 1024, '/', '(', 2, '*', 16, ')']
    # this will again go to the solve_the_innermost_bracket() in while loop


def solve_phrase(phrase):  # like [ 2, "**", 10]
    while "**" in phrase or "*" in phrase or "/" in phrase or "+" in phrase \
            or "-" in phrase:
        if "**" in phrase:
            solve_powers(phrase)
        if "*" in phrase or "/" in phrase:
            solve_multiplications(phrase)
        if "+" in phrase or "-" in phrase:
            solve_pluses(phrase)
    return phrase  # will be [1024]


def solve_bracket(classified_list):
    solved_phrase = list()
    if "(" in classified_list:
        classified_list = solve_the_innermost_bracket(classified_list)
        solve_bracket(classified_list)
    else:
        solved_phrase = solve_phrase(classified_list)
    print(f"The Result is : {solved_phrase[0]}")
  
    inputted_string = inputting()
    my_eval(inputted_string)


def solve_powers(phrase):
    character_count = 0
    for character in phrase:
        if character == "**":
            phrase_result = phrase[character_count - 1] ** phrase[character_count + 1]
            phrase[character_count - 1: character_count + 2] = [phrase_result]  # replacing
        character_count += 1
    solve_phrase(phrase)


def solve_multiplications(phrase):
    character_count = 0
    for character in phrase:
        if character == "*":
            phrase_result = phrase[character_count - 1] * phrase[character_count + 1]
            phrase[character_count - 1: character_count + 2] = [phrase_result]
        elif character == "/":
            phrase_result = phrase[character_count - 1] / phrase[character_count + 1]
            phrase[character_count - 1: character_count + 2] = [phrase_result]
        character_count += 1
    solve_phrase(phrase)


def solve_pluses(phrase):
    character_count = 0
    for character in phrase:
        if character == "+":
            phrase_result = phrase[character_count - 1] + phrase[character_count + 1]
            phrase[character_count - 1: character_count + 2] = [phrase_result]
        elif character == "-":
            phrase_result = phrase[character_count - 1] - phrase[character_count + 1]
            phrase[character_count - 1: character_count + 2] = [phrase_result]
        character_count += 1
    solve_phrase(phrase)


def my_eval(inputted_string):
    inputted_list = make_list(inputted_string)
    new_inputted_list = make_signs(inputted_list)
    classified_list = make_numbers(new_inputted_list)
    solve_bracket(classified_list)
