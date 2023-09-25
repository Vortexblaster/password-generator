#Author: Vortex
#Password Validator
from secrets import choice
from random import randint

def character_type_position(password):
    """ Determines the occurance of 4 types of characters: uppercase and lowercase letters, digits, and special characters

    Arguments:
        password (list): a list of characters
    
    Returns:
        character_position (list): a list that contains the index of the most recent occurance of a given type of character, storing None if no such type is found.
    """
    character_position = [None] * 4
    special_characters = "!-$%&'()*+,./:;<=>?_[]^`{|}~"
    
    for i in range(len(password)):
        character_position[0] = i if password[i].isupper() else character_position[0]                       #0 is uppercase
        character_position[1] = i if password[i].islower() else character_position[1]                       #1 is lowercase
        character_position[2] = i if password[i].isdigit() else character_position[2]                       #2 is digits
        character_position[3] = i if password[i] in special_characters else character_position[3]           #3 is special
    
    return character_position


def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """
    valid = True
    secure = True
    forbidden_characters = " @#"
    character_position = [None] * 4
    required_length = 8
    result = None

    if len(password) < required_length:
        valid = False
    
    if valid:
        for char in forbidden_characters:
            if char in password:
                valid = False
                break
    
    if valid:
        character_position = character_type_position(password)
        
        for element in character_position:        
            if element == None:                                                                              #Checking if there are no occurances
                secure = False
    
    if valid == True:
        if secure == True:
            result = "Secure"
        else:
            result = "Insecure" 
    
    elif valid == False:
        result = "Invalid"
    
    return result

def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n. 
    """
    password = [None] * n
    character_position = [None] * 4
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!-$%&'()*+,./:;<=>?_[]^`{|}~"
    
    password = [choice(characters) for i in range(n)]
    character_position = character_type_position(password)
    
    for i in range(len(character_position)):
        if character_position[i] == None:
            subset = [position for position in range(len(password)) if position not in character_position] #preventing the overwriting of required characters
            index_to_replace = choice(subset)
            character_position[i] = index_to_replace                                                       #adding the new index so it doesn't get overwritten
            
            match i:
                case 0:
                    password[index_to_replace] = characters[randint(26, 51)]
                case 1:
                    password[index_to_replace] = characters[randint(0,25)]
                case 2:
                    password[index_to_replace] = characters[randint(52,61)]
                case 3:
                    password[index_to_replace] = characters[randint(62,89)]
    
    password = "".join(password)                                                                           #required string cast after because of string immutability

    return password

if __name__ == "__main__":
    """ Code that will run if program is executed from terminal
    Arguments:
        None.

    Returns:
        Nothing is returned but effects of program are printed to the terminal.
    """
    selection = ""

    while selection != "Q":
        selection = input("\n     1. Password validatior\n     2. Password generator\n     Q to quit\n" + "-" * 25 + ">:")
        if selection == "1":
            print(validate(input("\nPlease input the password to validate: ")))
        
        if selection == "2":
            password = generate(int(input("\nPlease input the length of password to generate: ")))
            print("\nThe generated password is: %s" %(password))



