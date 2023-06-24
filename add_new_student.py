import check_input
from check_input import *
import path
import preprocessing
import train_model

class Student_Attendance():

    def __init__(self) -> None:

        self.name = None
        self.id = None

        self.path_train = None
        self.path_test = None

    def create_information(self):

        while True:
            self.name = check_input._input("Enter your name: ")
            if check_input.check_name_valid(self.name) == True: break
        while True:
            self.id = check_input._input("Enter your id: ")
            if check_input.check_id_valid(self.id, path.path_students_in_class) == True: break
        self.id = self.id.upper()
        check_input.write_students_file(path.path_students_in_class, self.id, self.name)

    def creat_data_to_attendance(self):

        self.path_train, self.path_test = check_input.data_to_attendance(self.id)

        preprocessing.augment_images(self.path_train)
        preprocessing.augment_images(self.path_test)

        print("Done")

# student = Student_Attendance()
# student.create_information()
# student.creat_data_to_attendance()





