import json
try:
    with open("students.json", "r") as file:
        students=json.load(file)
except FileNotFoundError:
    students=[]

while True:
    print("==== STUDENT MANGEMENT SYSTEM=====")
    print()
    print("1.Add student")  
    print("2.Edit student") 
    print("3.View Students")
    print("4.Dlete student")
    print("5.Exit")

    try:
        choice=int(input("Chose an option from above:"))
    except ValueError:
        print("Numbers only")
        continue

    

    if choice==1:
        print("\n--ADD STUDENT--")
        name=input("Enter student name:")
        age=int(input("Enter student age:"))

        student= {
            "name": name,
            "age": age
        }
        students.append(student)
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print(f"\nStudent Added successfuly!")
        print(f"Name: {name}")
        print(f"Age: {age}")


    elif choice==2:
        print("\n--EDIT STUDENT--")
        name=input("Enter student name to edit:")

        found=False
        for student in students:    
            if student['name']==name:
                new_age=int(input("Enter student new age:"))
                student['age']=new_age
                with open("students.json", "w") as file:
                    json.dump(students, file, indent=4)
                new_name=input("Enter student new name:")
                if new_name!="":
                    student['name']=new_name
                    with open("students.json", "w") as file:
                        json.dump(students, file, indent=4)
                    
            
                print(f"\nStudent Updated succesfully!")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")

                found=True
                break
            if not found:
                print("Student not found")

    elif choice==3:
        print("\n---STUDENTS LIST")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}")

    elif choice==4:
        print("\n---DELETE STUDENT----")
        name=input("Enter Student name to delete: ")
        found=False
        for student in students:
            if student["name"]==name:
                students.remove(student)
                with open("students.json", "w") as file:
                    json.dump(students, file, indent=4)
                print(f"{name} deleted sucessfully!")
                found=True
                break
            if not found:
                print("Student not found.")

          
    elif choice==5:
        print("Existing!..")
        break
    else:
        print("Invalid input,chose 1,2,3 and Try again")




