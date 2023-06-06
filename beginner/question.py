def get_user_input():
    feeling = input("How are you feeling today? ")
    return feeling

def give_response(feeling): 
    if feeling == "happy":
        response = "I'm glad you're happy!"
    elif feeling == "sad":
       response = "I'm sorry you're sad."
    else:
        response = "I don't understand."
         
    return response

def main():
    user_input = get_user_input()
    response = give_response(user_input)

    print(response)
        
if __name__ == "__main__":
    main()