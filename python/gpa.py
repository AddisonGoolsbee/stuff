# Calculate my GPA
import os
from ast import literal_eval
from dotenv import load_dotenv

load_dotenv()

def main():
    grades_array = os.getenv('GRADES')
    grades = literal_eval(grades_array)
    total = 0

    for grade in grades:
        if grade > 4.0 or grade < 1.0:
            raise Exception('invalid grade')
        total += grade
    gpa = total / len(grades)
    print(gpa)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        exit(1)