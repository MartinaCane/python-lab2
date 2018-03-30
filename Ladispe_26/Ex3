from sys import argv

filename=argv[1]

txt=open(filename)
print("Your file ",filename,":")
list=(txt.readlines())
print(list)
txt.close()



print("Insert the number corresponding to the action you want to perform:")

print("1. insert a new task; 2. remove a task; 3. show all the tasks, sorted in alphabetic order; 4. close the program.")

print("Your choice: ")

choice=input()


while choice!='4':

    if choice=='1':

        list.append(input("Go on: "))

        choice2=input("You want to add more? (Y/N) ")

        while choice2=='Y':

            list.append(input("Go on: "))

            print("Your list is: ", list)

            choice2=input("You want to add more? (Y/N) ")

        if choice2=='N':

             choice=input("What now? ")



    if choice=='2':

        item=input("Insert a task to be removed: ")
        i=0
        j=0
        while i<len(list):
            a = list[i]
            if item in a:
                list.pop(i)
            i=i+1

        print("This is now your list:\n", list, "\n Task successfully delated ")

        choice3=input("You want to delate more? (Y/N) ")

        while choice3=='Y':
            item = input("Go on: ")
            i = 0
            j = 0
            while i < len(list):
                a = list[i]
                if item in a:
                    list.pop(i)
                i = i + 1

            print(list, " Task successfully delated ")

            choice3=input("You want to delate more? (Y/N) ")

        if choice3=='N':

             choice=input("What now? ")



    if choice=='3':

        print(sorted(list))

        choice=input("What now? ")


from sys import argv
filename = argv[1]
new = open(filename, "w")
final=list[:]
i=0
while i<len(final):
    new.write(final[i])
    i=i+1
print(final)

new.close()
print("File changed, bye")
