class Student:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name= name #assign the value of "name" to the instance variable "name"
        self.major= major
        self.code_portfolio_score= code_portfolio_score
        self.group_project_score= group_project_score
        self.exam_score= exam_score
    def print(self):
        print(f"Name:{self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score}, Group Project Score:{self.group_project_score}, Exam Score:{self.exam_score}")#access the instance variables
a= Student("Bob","BMI",85,85,85) #create an instance of Student
a.print()