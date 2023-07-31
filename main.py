from datetime import datetime

class Individual:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

class GuestManagementSystem:
    def __init__(self):
        self.individuals = []

    def add_individual(self, name, age, id_number):
        individual = Individual(name, age, id_number)
        self.individuals.append(individual)

    def show_all_individuals(self):
        for individual in self.individuals:
            print(f"Name: {individual.name}, Age: {individual.age}, ID: {individual.id_number}")

    def count_individuals(self):
        return len(self.individuals)

def main():
    guest_system = GuestManagementSystem()

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
            guest_system.add_individual(name, age, id_number)
            print("Individual added successfully!")

        elif choice == "2":
            print("\nAll Individuals:")
            guest_system.show_all_individuals()

        elif choice == "3":
            total_individuals = guest_system.count_individuals()
            print(f"\nTotal Individuals: {total_individuals}")

        elif choice == "4":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
