#Create empty list to store tasks and their status
to_do_list=[]

#Function to add tasks
def add_task():
    task=input("Enter task assigned:")
    to_do_list.append({"Task":task,"Status":"Pending"})
    print("Task added successfully")

#Function to view tasks
def view_task():
    print("Your to do list:")
    if len(to_do_list)==0:
        print("No pending tasks!")
    else:
        for index,task in enumerate(to_do_list,1):
            print(f"{index}:{task['Task']}-{task['Status']}")
    print("\n")

#Function to remove tasks
def remove_task():
    if len(to_do_list)==0:
        print("List is empty")
    else:
        try:
            search_index=int(input("Enter task number to be removed:"))-1
            if search_index>=0 and search_index<len(to_do_list):
                removed_task=to_do_list.pop(search_index)
                print(f"Task Removed:{removed_task['Task']}")
                print("Task removed successfully!!")
            else:
                print("Invalid Task number")
        except ValueError:
            print("Please enter a valid task number!!")

#Mark task as completed
def mark_completed():
    if len(to_do_list)==0:
        print("list is empty")
    else:
        try:
            search_index=int(input("Enter task number:"))-1
            if search_index>=0 and search_index<len(to_do_list):
                to_do_list[search_index]["Status"]="Completed"
                print("Successfully updated!!!")
            else:
                print("Invalid task number!!")
        except ValueError:
            print("Invalid task number!! PLease try again")

#Menu Function 
def menu():
    while True:
        print("Operations:\n\
          1. Add a task.\n\
          2. View all tasks.\n\
          3. Remove a task.\n\
          4. Mark a Task as completed.\n\
          5. Exit application.")
        choice=int(input("Enter your choice:"))
        if choice==1:
            add_task()
        elif choice==2:
            view_task()
        elif choice==3:
            remove_task()
        elif choice==4:
            mark_completed()
        elif choice==5:
            print("Exiting application....")
            exit()
        else:
            print("Invalid choice. Enter valid choice!!!")

#Function call
menu()
