'''
Определите класс Account, имитирующий банковский счет.
Класс должен включать атрибуты для хранения
идентификатора владельца,
баланса счета,
и методы для депозита - пополнение и снятие средств,
если на счету достаточно средств
'''
class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposite(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. На счете: {self.balance}")

    def withdrow(self, money):
        if money > self.balance:
            print(f"Недостаточно средств. На счете: {self.balance}")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} руб. На счете: {self.balance}")

    def print_balance(self):
        print(f"Текущий баланс: {self.balance}")

man = Account("98098089098", 1000)
man.print_balance()
man.withdrow(450)
man.withdrow(800)
man.deposite(50000)
man.print_balance()

