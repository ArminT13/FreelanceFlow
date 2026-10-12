def add_project():
    name = input("Name: ")
    price = int(input("Price: "))
    
    project = {
        "name": name,
        "price": price
    }
    
    return project

projects = []

while True:
    print("\n===== FreelanceFlow =====")
    print("1. Add Project")
    print("2. Show Projects")
    print("3. Total Income")
    print("4. Exit")

    choice = input("Choose: ")

    match choice:
        case "1":
            project = add_project()
            projects.append(project)

        case "2":
            for project in projects:
                print("Name:", project["name"])
                print("Price:", project["price"])

        case "3":
            total = 0

            for project in projects:
                total = total + project["price"]

            print(total, "$")

        case "4":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice!")