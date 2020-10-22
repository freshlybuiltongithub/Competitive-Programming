"""
Hackerrank Solution for Day 12: Inheritance
"""


class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,id,scores):
        super().__init__(firstName,lastName,id)
        self.scores = scores
        
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = sum(self.scores)/len(self.scores)
        if average>=90:
            return 'O'
        elif 80<=average and 90>average:
            return 'E'
        elif 70<=average and 80>average:
            return 'A'
        elif 55<=average and 70>average:
            return 'P'
        elif 40<=average and 55>average:
            return 'D'
        else:
            return 'T'


