def task():
    tasks=[]
    print("-----WELCOME TO THE TASK MANAGEMENT APP-----")
    
    total_tasks=int(input("Enter how many task you want to add="))
    for i in range(1,total_tasks+1):
        task_name=input(f"Enter task {i} =")
        tasks.append(task_name)
        
    print(f"Today's tasks are \n {tasks}")
    while True:
        opr=int(input("Enter 1-ADD\n2-UPDATE\n3-DELETE\n4-VIEW\n5-EXIT/STOP/"))
        if opr==1:
            add=input("Enter task you want to add=")
            tasks.append(add)
            print(f"Task {add} has been added successfully added....")
        elif opr==2:
            upd_val=input("Enter the task name you want to update=")
            if upd_val in tasks:
                up=input("Enter new task:")
                ind=tasks.index(upd_val)
                tasks[ind]=up
                print(f"Updated task{upd_val}")
        elif opr==3:
            dele_val=input("Which value you want to delete??")
            if dele_val in tasks:
                ind=tasks.index(dele_val)
                del tasks[ind]
                print(f"Task {dele_val} has been deleted...")
        elif opr==4:
            print(f"Total tasks {tasks}")
        else:
            print("Closing the program.....")
            break
task()
