# TASK MANAGEMENT SYSTEM

users = {}

tasks = []

# CREATE ACCOUNT

print("====================================")
print("      TASK MANAGEMENT SYSTEM")
print("====================================")

print("\n===== CREATE ACCOUNT =====")

new_username = input("Create Username: ")
new_password = input("Create Password: ")

users[new_username] = new_password

print("\nAccount Created Successfully!")

# LOGIN

print("\n===== LOGIN =====")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username in users and users[username] == password:

    print("\nLogin Successful!")

    while True:

        print("\n===== MAIN MENU =====")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Logout")

        choice = input("Enter Your Choice: ")

        # CREATE TASK
        if choice == "1":

            task_name = input("Enter Task Name: ")

            task = {
                "name": task_name,
                "status": "Pending"
            }

            tasks.append(task)

            print("Task Added Successfully!")

        # VIEW TASKS
        elif choice == "2":

            print("\n===== TASK LIST =====")

            if len(tasks) == 0:
                print("No Tasks Available")

            else:
                for i in range(len(tasks)):
                    print(
                        str(i + 1) + ".",
                        tasks[i]["name"],
                        "-",
                        tasks[i]["status"]
                    )

        # UPDATE TASK STATUS
        elif choice == "3":

            if len(tasks) == 0:

                print("No Tasks To Update")

            else:

                print("\n===== TASK LIST =====")

                for i in range(len(tasks)):
                    print(
                        str(i + 1) + ".",
                        tasks[i]["name"],
                        "-",
                        tasks[i]["status"]
                    )

                try:

                    task_no = int(input("Enter Task Number: "))

                    if 1 <= task_no <= len(tasks):

                        print("\n1. Pending")
                        print("2. In Progress")
                        print("3. Completed")

                        status_choice = input(
                            "Enter New Status Choice: "
                        )

                        if status_choice == "1":
                            tasks[task_no - 1]["status"] = "Pending"

                        elif status_choice == "2":
                            tasks[task_no - 1]["status"] = "In Progress"

                        elif status_choice == "3":
                            tasks[task_no - 1]["status"] = "Completed"

                        else:
                            print("Invalid Status Choice")
                            continue

                        print("Task Status Updated Successfully!")

                    else:
                        print("Invalid Task Number")

                except ValueError:
                    print("Please Enter A Valid Number")

        # DELETE TASK
        elif choice == "4":

            if len(tasks) == 0:

                print("No Tasks To Delete")

            else:

                print("\n===== TASK LIST =====")

                for i in range(len(tasks)):
                    print(str(i + 1) + ".", tasks[i]["name"])

                try:

                    task_no = int(
                        input("Enter Task Number To Delete: ")
                    )

                    if 1 <= task_no <= len(tasks):

                        deleted_task = tasks.pop(task_no - 1)

                        print(
                            deleted_task["name"],
                            "Deleted Successfully!"
                        )

                    else:
                        print("Invalid Task Number")

                except ValueError:
                    print("Please Enter A Valid Number")

        # LOGOUT
        elif choice == "5":

            print("\nLogout Successful!")
            break

        # INVALID CHOICE
        else:

            print("Invalid Choice! Please Try Again.")

else:

    print("\nInvalid Username Or Password")
