from task_tools.tasks import add_tasks,delete_tasks
from task_tools.task_storage import load_json,save_json

def main():
    '''The main function'''
    #Load tasks when the program starts
    tasks=load_json()
    running=True
    while running:

        print("---TASKS MANAGER---")
        print("1. Add tasks")
        print("2. view tasks")
        print("3. Delete tasks")
        print("4. Exit")

        choice=input("Enter your choice: ")
        if choice=="1":
            new_tasks=add_tasks()
            if new_tasks:
                tasks.extend(new_tasks)
                save_json(tasks)

        elif choice=="2":
            if not tasks:
                print("No tasks added")
            else:
                for i,tsk in enumerate(tasks,start=1):
                    print(f"{i}. {tsk}")
        elif choice=="3":
            tasks=delete_tasks(tasks)
            save_json(tasks)
        elif choice=="4":
            save_json(tasks)
            print("Tasks Saved successfully. Goodbye!")
            running=False
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()







