"""First program
Sam McGuire
This is a demo for MPLD"""

def hello_world():
    print("Hello world")
    user_name = input("What is your name:  ")
    print("Hello, ", user_name)

    if user_name == "Sam":
        print(user_name, ", that is a cool name!")
    else:
        print(user_name, "who the hell names their kid", user_name, "!")

def bob_module():
    print("Boo!")


bob_module()
hello_world()