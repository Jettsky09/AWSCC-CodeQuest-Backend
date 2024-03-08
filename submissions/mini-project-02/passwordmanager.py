import json
import os

def print_menu():
    menu = ["1 - Add Username and Password",
            "2 - View",
            "3 - Search",
            "4 - Delete",
            "5 - Update",
            "6 - Exit"]
    
    for i in menu:
        print(i)

def input_checker(user_input):
    global running
    if user_input == "1":
        add()
    elif user_input == "2":
        view()
    elif user_input == "3":
        website = input("Enter the website: ").lower()
        search(website)
    elif user_input == "4":
        existing = False
        while not existing:
            website = input("Enter the website: ").lower()
            existing = is_existing(website)
        delete(website)
    elif user_input == "5":
        existing = False
        while not existing:
            website = input("Enter the website: ")
            existing = is_existing(website)
        update(website)
        website = input("Enter the website: ").lower()
        update(website)
    elif user_input == "6":
        running = False
        os.system('cls')   
        print("Goodbye!")
    else:
        print("ERROR!! Choose to 1-6")


def is_existing(website):
    with open('data3.json', 'r') as f:
        data = json.load(f)
        if website in data:
            return True
        return False

def add():
    website = input("Enter the website: ").lower()
    email = input("Enter the email: ")
    password = input("Enter the password: ")

    new_data = {
        website: [{
            'email': email,
            'password': password
        }]
    }

    with open('data3.json', 'r') as f:
        data = json.load(f)

    if is_existing(website) == True:
        data[website].append({'email': email, 'password': password})
    else:
        data.update(new_data)
    
    with open('data3.json', 'w') as f:
        json.dump(data, f, indent=10)

    os.system('cls')    
    print("Successfully added!")

def view():
    with open('data3.json', 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            print(f"Website: {key}")
            for i in range(len(val)):
                print(f"    {i+1} Email: {val[i]['email']}")
                print(f"      Password: {val[i]['password']}\n")
                
def search(website):
    with open('data3.json', 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            if key == website:
                print(f"Website: {key}")
                for i in range(len(val)):
                    print(f"    {i+1} Email: {val[i]['email']}")
                    print(f"      Password: {val[i]['password']}\n")
                return True
            
        print("No websites found.")
        return 
    
def update(website):
    with open('data3.json', 'r') as f:
        data = json.load(f)
        search(website)
            
        valid = False
        while not valid:
            user_input = int(input("Enter the account number:"))
            valid = 0 <= user_input-1 < len(data[website])

        change = input("What do you want to change 'password' or 'email'? ")
        new = input(f"Enter the new {change}: ")
        data[website][user_input-1][change] = new

    with open('data3.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print("Successfully updated!")


def delete(website):
    with open('data3.json', 'r') as f:
        data = json.load(f)
        search(website)

        valid = False
        while not valid:
            user_input = int(input("Enter the account number:"))
            valid = 0 <= user_input-1 < len(data[website])

        data[website].pop(user_input-1)

        if len(data[website]) == 0:
            data.pop(website)
        
    with open('data3.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Successfully Deleted!")

        
      
running = True

while running:
    print("=======PASSWORD MANAGER=======")
    print_menu()
    user_input = input("Enter a number: ")
    input_checker(user_input)
    
    


