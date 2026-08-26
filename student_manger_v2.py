import json
# load students
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

students= load_students()

def add_students(students):
    print("\n--ADD STUDENT--")
    name=input("Enter student name:")
    age=int(input("Enter student age:"))
    student= {
    "name": name,
    "age": age
        }
    students.append(student)
    save_students(students)
    print(f"\nStudent Added successfuly!")
    print(f"Name: {name}")
    print(f"Age: {age}")

def edit_students(students):
    print("\n--EDIT STUDENT--")
    name=input("Enter student name to edit:")
    found=False
    for student in students: 
     if student['name']==name:
        try:
            new_age=int(input("Enter student new age:"))
        except ValueError:
            print("number only")
            break
        student['age']=new_age
        save_students(students)
        new_name=input("Enter student new name:")
        if new_name!="":
            student['name']=new_name
            save_students(students)
                        
                
            print(f"\nStudent Updated succesfully!")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
        found=True
        break
    if not found: 
        print("Student not found")

def view_students(students):
      print("\n---STUDENTS LIST")
      for student in students:
          print(f"Name: {student['name']}, Age: {student['age']}")
      if not students:
        print("No Student found")
        return

def delete_students(students):
    print("\n---DELETE STUDENT----")
    name=input("Enter Student name to delete: ")
    found=False
    for student in students:
        if student["name"]==name:
            students.remove(student)
            save_students(students)
            print(f"{name} deleted sucessfully!")
            found=True
            break
        if not found:
            print("Student not found.")



    


def main():
    while True:
        print("\n==== STUDENT MANGEMENT SYSTEM=====")
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
            add_students(students)


        elif choice==2:
            edit_students(students)

        elif choice==3:
            view_students(students)
           
        elif choice==4:
            delete_students(students)
          
        elif choice==5:
            print("Existing!..")
            break
        else:
            print("Invalid input,chose 1,2,3 and Try again")

if __name__== "__main__":
    main()