pets = []

id_counter = 1

def line(length=76):
    return "=" * length

def print_header(title):
    title_length = len(title)
    padding_length = (76 - title_length) // 2
    print(line(76))
    print(f"{' ' * padding_length}{title}{' ' * padding_length}")
    print(line(76))

def view_pets():
    print_header("List of Pets:")
    if len(pets) == 0:
        print("No pets available.")
    else:
        for pet in pets:
            print(f"ID: {pet['id']}, Name: {pet['name']}, Species: {pet['species']}, Gender: {pet['gender']}, Color: {pet['color']}, Birthdate: {pet['birthdate']}")

def add_pet():
    global id_counter
    print_header("Adding Pet...")
    id = id_counter
    name = input("Enter the pet's name: ").title()
    species = input("Enter the pet's species: ").title()
    gender = input("Enter the pet's gender: ").title()
    color = input("Enter the pet's color: ").title()
    birthdate = input("Enter the pet's birthdate (dd.mm.yyyy): ").title()
    pets.append({"id": id, "name": name, "species": species, "gender": gender, "color": color, "birthdate": birthdate})
    print(f"\n{name} the {species} has been added!")
    id_counter += 1

def search_pet():
    pet_id = int(input("Enter the pet ID to search: "))
    for pet in pets:
        if pet['id'] == pet_id:
            print(f"ID: {pet['id']}, Name: {pet['name']}, Species: {pet['species']}, Gender: {pet['gender']}, Color: {pet['color']}, Birthdate: {pet['birthdate']}")
            return
    print("Pet not found.")

def edit_pet():
    pet_id = int(input("Enter the pet ID to edit: "))
    for pet in pets:
        if pet['id'] == pet_id:
            pet['name'] = input("Enter the new name: ").title()
            pet['species'] = input("Enter the new species: ").title()
            pet['gender'] = input("Enter the new gender: ").title()
            pet['color'] = input("Enter the new color: ").title()
            pet['birthdate'] = input("Enter the new birthdate (dd.mm.yyyy): ").title()
            print(f"Pet ID {pet_id} has been updated.")
            return
    print("Pet not found.")

def delete_pet():
    pet_id = int(input("Enter the pet ID to delete: "))
    for pet in pets:
        if pet['id'] == pet_id:
            confirmation = input(f"Are you sure you want to delete {pet['name']} the {pet['species']}? (yes/no): ").lower()
            if confirmation == 'yes':
                pets.remove(pet)
                print(f"Pet ID {pet_id} has been deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("Pet not found.")

def sort_pets():
    criteria = input("Enter the criteria to sort by (name, species, gender, color, birthdate): ").lower()
    if criteria in ['name', 'species', 'gender', 'color', 'birthdate']:
        pets.sort(key=lambda pet: pet[criteria])
        print(f"Pets have been sorted by {criteria}.")
    else:
        print("Invalid sorting criteria. Please choose from name, species, gender, color, or birthdate.")

print_header("PET MANAGEMENT")

while True:
    print_header("Options")
    options = [
        "1. View Pets",
        "2. Add Pet",
        "3. Search Pet",
        "4. Edit Pet",
        "5. Delete Pet",
        "6. Sort Pets",
        "7. Exit"
    ]
    for option in options:
        print(option)

    print_header("Choose Option")
    option_choice = int(input())

    if option_choice == 1:
        view_pets()
    elif option_choice == 2:
        add_pet()
    elif option_choice == 3:
        search_pet()
    elif option_choice == 4:
        edit_pet()
    elif option_choice == 5:
        delete_pet()
    elif option_choice == 6:
        sort_pets()
    elif option_choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose again.")
    
    print()