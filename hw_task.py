# Менеджер задач
#
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты:
# описание задачи,
# срок выполнения и
# статус (выполнено/не выполнено).
# Реализуй функцию
# для добавления задач,
# отметки выполненных задач и
# вывода списка текущих (не выполненных) задач.
class Task():
    def __init__(self, id, description, end_date, status="не выполнена"):
        self.id = id
        self.description = description
        self.end_date = end_date
        self.status = status

    def close_task(self):
        # отметить задачу выолненной
        self.status = "выполнена"

    def control_status(self):
        # проверка статуса задачи для вывода невыполненных задач
        return self.status == "не выполнена"

def print_list_task(par_list):
    print("Текущий список задач:")
    for i in par_list:
        if i.control_status():
            print(f"Задача {i.id} - {i.description} - до {i.end_date} - {i.status}")

list_task = []
task1 = Task(12345, "сделать дз", "01.04.2024")
task2 = Task(12346, "купить продукты", "01.04.2024")
task3 = Task(12347, "приготовить ужин", "01.04.2024")

list_task.append(task1)
list_task.append(task2)
list_task.append(task3)

print_list_task(list_task)

task1.close_task()

print_list_task(list_task)


