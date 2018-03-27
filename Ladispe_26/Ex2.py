from sys import argv

filename=argv[1]

txt=open(filename)
print("Your file ",filename,":")
list=(txt.readlines())
txt.close()
print(list)


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

        list.remove(input("Insert a task to be removed: "))

        print(list, " Task successfully delated ")

        choice3=input("You want to delate more? (Y/N) ")

        while choice3=='Y':

            list.remove(input("Go on: "))

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
    new.write('\n')
    i=i+1

new.close()
print("File changed, bye")