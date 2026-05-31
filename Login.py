# LOGIN DETAILS 

saved_username = "Saru"
saved_password = "1234"

#  TASK LIST 

tasks = []

# LOGIN

print("===== TASK MANAGEMENT SYSTEM =====")

username = input("Enter Username: ")
password = input("Enter Password: ")

# LOGIN CHECK

if username == saved_username and password == saved_password:

    print("\nLogin Successful!")

    # MAIN MENU LOOP

    while True:

        print("\n===== MAIN MENU =====")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Logout")

        choice = input("\nEnter Your Choice: ")

        # CREATE TASK

        if choice == "1":

            print("\n===== CREATE TASK =====")

            task_name = input("Enter Task Name: ")

            # Default Status

            task = {
                "name": task_name,
                "status": "Pending"
            }

            # Add Task

            tasks.append(task)

            print("Task Added Successfully!")

        # VIEW TASKS

        elif choice == "2":

            print("\n===== TASK LIST =====")

            if len(tasks) == 0:

                print("No Tasks Available")

            else:

                for i in range(len(tasks)):

                    print("\nTask", i + 1)
                    print("Task Name :", tasks[i]["name"])
                    print("Task Status :", tasks[i]["status"])

        # UPDATE TASK STATUS

        elif choice == "3":

            print("\n===== UPDATE TASK STATUS =====")

            if len(tasks) == 0:

                print("No Tasks To Update")

            else:

                # Display Available Tasks

                print("\nAvailable Tasks:")

                for task in tasks:

                    print("-", task["name"], ":", task["status"])

                # Get Task Name

                task_name = input("\nEnter Task Name To Update: ")

                found = False

                # Search Task

                for task in tasks:

                    if task["name"].lower() == task_name.lower():

                        found = True

                        print("\nSelect New Status")
                        print("1. Pending")
                        print("2. In Progress")
                        print("3. Completed")

                        status_choice = input("Enter Status Choice: ")

                        # Update Status

                        if status_choice == "1":

                            task["status"] = "Pending"

                        elif status_choice == "2":

                            task["status"] = "In Progress"

                        elif status_choice == "3":

                            task["status"] = "Completed"

                        else:

                            print("Invalid Status Choice")
                            break

                        print("Task Status Updated Successfully!")
                        break

                # Task Not Found

                if found == False:

                    print("Task Not Found")

        # DELETE TASK

        elif choice == "4":

            print("\n===== DELETE TASK =====")

            if len(tasks) == 0:

                print("No Tasks To Delete")

            else:

                # Display Tasks

                print("\nAvailable Tasks:")

                for task in tasks:

                    print("-", task["name"])

                # Get Task Name

                task_name = input("\nEnter Task Name To Delete: ")

                found = False

                # Search and Delete

                for task in tasks:

                    if task["name"].lower() == task_name.lower():

                        tasks.remove(task)

                        found = True

                        print("Task Deleted Successfully!")
                        break

                if found == False:

                    print("Task Not Found")

        # LOGOUT

        elif choice == "5":

            print("\nLogout Successful")
            break

        # INVALID CHOICE

        else:

            print("Invalid Choice")

# INVALID LOGIN

else:

    print("Invalid Username or Password")
