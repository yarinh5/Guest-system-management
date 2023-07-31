# פונקציה להוספת יחיד חדש למערכת
def add_individual(name, age, id_number):
    with open("data.txt", "a") as file:
        file.write(f"{name},{age},{id_number}\n")

# פונקציה להצגת רשימת כל היחידים במערכת
def show_all_individuals():
    with open("data.txt", "r") as file:
        for line in file:
            name, age, id_number = line.strip().split(",")
            print(f"Name: {name}, Age: {age}, ID: {id_number}")

# פונקציה לספירת כמות האורחים במערכת
def count_individuals():
    with open("data.txt", "r") as file:
        return len(file.readlines())

def main():
    while True:
        print("\nChoose an option:")
        print("1. Add Individual")
        print("2. Show All Individuals")
        print("3. Count Individuals")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            id_number = input("Enter ID number: ")
            add_individual(name, age, id_number)
            print("Individual added successfully!")

        elif choice == "2":
            print("\nAll Individuals:")
            show_all_individuals()

        elif choice == "3":
            total_individuals = count_individuals()
            print(f"\nTotal Individuals: {total_individuals}")

        elif choice == "4":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
