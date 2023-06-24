from add_new_student import *
from train_model import *

def check_input():
    while True:
        inp = input("Enter your choice: ")
        try:
            inp = int(inp)
            if inp in [1, 2, 3, 4]: return inp
        except:
            print("Your Selection Is Not Available!")

def menu():
    print("Face Recognition")
    print("1. Add new Student.")
    print("2. Run.")
    print("3. Out")

def main():
    while True:
        menu()
        choice = check_input()
        if choice == 1:
            student = Student_Attendance()
            student.create_information()
            student.creat_data_to_attendance()
            training()
            print("Done!")
        if choice == 2:
            run()
        if choice == 3:
            print("Thank You!")
            break


if __name__ == "__main__":
    main()