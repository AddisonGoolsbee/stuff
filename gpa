def main():
    grades = [4,4,4,4,4,3.7,4,3.7,4,4,3.3,3.3,3.7,4,4,3.7,3.7,4,3.7,4,4,4,4]
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