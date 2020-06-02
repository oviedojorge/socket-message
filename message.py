# number = input("Choisissez une proposition: ")
# number = int(number)

# if number == 0:
#     print("Première proposition")
# elif number == 1:
#     print("Seconde proposition")
# elif number == 2:
#     print("Troisième proposition")
# else:
#     print("Aucune proposition")

# message = input("Tapez votre message: ")
# message_title = input("Tapez le titre de votre message: ")
# message_dict = {message_title: message}
# print(message_dict)

user_command = ""
while user_command != "exit":
    print("itération")
    
    try:
        login
    except NameError:
        login = ""

    if login == "":
        # Demande à l'utilisateur de se connecter
        login_list = ["jorge", "jean", "jacques"]
        user_command = input("login: ")
        login = user_command
        if (login in login_list) == False:
            print("login incorrect, essayez à nouveau: ")
            login = ""
            continue

    # Impose un choix entre différentes propositions
    user_command = input(login + " Choisissez une proposition: ")
    action_number = user_command
    try:
        action_number = int(action_number)
    except ValueError:
        print("proposition incorrect, essayez à nouveau:")
        action_number = ""
        continue
    
    # Effectue différentes opérations selon la proposition sélectionée
    if action_number == 0:
        user_command = input(login + " Tapez votre message: ")
        message = user_command
        user_command = input(login + " Tapez le titre de votre message: ")
        message_title = user_command
        # Mémorise le message et son titre dans un dictionaire
        message_dict = {message_title: message}
        print(message_dict)
    elif action_number == 1:
        login = ""
        print("logout")
    
# user_command = input(login + ": ")