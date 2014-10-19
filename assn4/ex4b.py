def get_username():
    print("Please enter usename:")
    username = input()
    if (username == ""):
        username = "anonymous"
    print("Welcome,", username)
