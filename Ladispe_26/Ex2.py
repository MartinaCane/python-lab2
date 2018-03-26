from sys import argv

filename=argv[1]

txt=open(filename)

print("Your file ",filename,":")
list=[txt.readlines()]
print(list)
print(len(list))

tasks=[txt.readline(0)]
print(tasks)


'''
print("Insert the number corresponding to the action you want to perform:")
print("1. insert a new task; 2. remove a task; 3. show all the tasks, sorted in alphabetic order; 4. close the program.")
print("Your choice: ")
choice=input()

while choice!='4':
    if choice=='1':
        ask= input("Go on: ")
        tasks=[ask]
        choice2=input("You want to add more? (Y/N) ")
        while choice2=='Y':
            tasks.append(input("Go on: "))
            print("Your list is: ", tasks)
            choice2=input("You want to add more? (Y/N) ")
        if choice2=='N':
             choice=input("What now? ")

    if choice=='2':
        tasks.remove(input("Insert a task to be removed: "))
        print(tasks, " Task successfully delated ")
        choice3=input("You want to delate more? (Y/N) ")
        while choice3=='Y':
            tasks.remove(input("Go on: "))
            print(tasks, " Task successfully delated ")
            choice3=input("You want to delate more? (Y/N) ")
        if choice3=='N':
             choice=input("What now? ")

    if choice=='3':
        print(sorted(tasks))
        choice=input("What now? ")

print("Bye")'''