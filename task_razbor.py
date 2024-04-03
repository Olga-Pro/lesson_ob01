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
    def __init__(self):
        self.tasks = [] #список задач

    def add_task(self, deadline, description):
        # добавляем задачи в виде словаря
        self.tasks.append({'deadline': deadline, 'description': description, 'status': 'не выполнено'})

    def complete_task(self, description):
        res = False
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'выполнено'
                print(f"Задача {description} отмечена выполненой")
                # print(f"{task['description']} - {task['deadline']} - {task['status']}")
                res = True
                break
        if not res:
            print(f"Задача {description} не найдена")
    def show_tasks(self):
        print("Текущие задачи;")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']} - {task['status']}")


t01 = Task()
t01.add_task("01/05/2024", "Прочитать книгу")
t01.add_task("02/05/2024", "Подвиг")
t01.add_task("03/05/2024", "Отпуск")

t01.show_tasks()

t01.complete_task("Прочитать книгу")
t01.complete_task("Прочитать 2 книги")

t01.show_tasks()

