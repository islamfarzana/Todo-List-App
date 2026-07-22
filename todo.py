tasks = []

print("Welcome to Todo App!")

for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)

print("Your tasks:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
    