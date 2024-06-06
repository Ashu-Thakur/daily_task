# Project: Student Grade CalculatorFeatures
# 1. Take marks input for five subjects.
# 2. Calculate total marks.
# 3. Calculate percentage.
# 4. Determine the grade based on the percentage. (below 50 = "D", 51 to 60 = "C", 61 to 80="B", 81 to 100="A")
# 5. Display the results.

# Sample Input :-Enter the marks for 5 subjects:
# Subject 1: 45
# Subject 2: 55
# Subject 3: 60
# Subject 4: 70
# Subject 5: 65

# Sample output Results:
# Subject1, 45, D
# Subject2, 55, C
# Subject3, 60, C
# Subject4, 70, B
# Subject5, 65, B
# Total Marks: 295 / 500
# Percentage: 59.00%
# Grade: D


class Student():

    def __init__(self,count_of_subject,marks):
        self.total_subjects = count_of_subject
        self.marks = marks
        self.Subjects = {}
        self.total_marks = 0
        self.percentage = 0
        self.grade = ""
        # now all the data is stored properly
        self.stored_data()

    # storing the data 
    def stored_data(self):
        
        for i in enumerate(self.marks, 1):
            
            self.Subjects[f'subject{i[0]}'] = [self.__handle_grade(i[1]) , i[1]]

            # adding the marks to the total marks
            self.total_marks += i[1]

    # for printing purpose
    def priniting_output(self):

        for key , item  in self.Subjects.items():
            print(f"{key} , {item[1]} , {item[0]}")
        
        print(f"Total Marks: {self.total_marks} / {self.total_subjects * 100}")
        self.percentage = self.total_marks / self.total_subjects
        print(f"Percentage: {self.percentage:.2f}%")
        self.grade = self.__handle_grade(self.total_marks)
        print(f"Grade: {self.grade}")

    # private methode to handle grade ___
    def __handle_grade(self, mark)->str:
            # default grade is D
            grade = 'D'
            # taking each subject marks
            get_mark = mark

            if 100 >= get_mark >= 81:
                grade = 'A'
            
            elif 80 >= get_mark >= 61:
                grade = 'B'
            
            elif 60 >= get_mark >= 51:
                grade = 'C'

            return grade
            
            


count = 1
while(True):
    total_subject = int (input("Enter Total Subject_count :"))
    marks = []
    for i in range(1,total_subject + 1):
        try :
            number = float(input(f"Enter Your Marks for subject number {i} :"))
            if 0 <= number <= 100:
                marks.append(number)
        except Exception as e :
            print("Invalid Input")

    print("-------------Summary--------------")
    obj = Student(count_of_subject = total_subject, marks = marks)
    obj.priniting_output()

    # ask user for reapeat the task or not
    choice = input("Wanna Do it Again ,yes / NO :...")
    if choice.lower() != 'yes':
        break
        
        


