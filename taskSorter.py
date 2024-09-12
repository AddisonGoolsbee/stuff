import sys

def sort_tasks(input_block):
    lines = input_block.strip().splitlines()
    tasks = [line.strip() for line in lines if line and line[0].isdigit() and line[1].isspace() and line[2].isdigit()]
    for index, task in enumerate(tasks):
        if len(task) >= 4 and task[3] in '-':
            tasks[index] = task[:3] + task[4:]


    def sort_key(task):
        num1, num2 = int(task[0]), int(task[2])
        return (-num1 / num2, -num1)  # Sort by ratio, then by the first number in case of a tie
    
    return sorted(tasks, key=sort_key)
    

def main():
    print("Enter lines in the format N N task. Lines not in this format will be ignored. ^D to end")
    input_block = sys.stdin.read()
    sorted_tasks = sort_tasks(input_block)
    print("\nSorted Tasks:")
    for task in sorted_tasks:
        print(task)

if __name__ == "__main__":
    main()
