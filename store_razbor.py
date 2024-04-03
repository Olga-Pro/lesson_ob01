# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как
# адрес,
# название и
# ассортимент товаров.
# Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
#
# Шаги:
#
# 1. Создай класс Store:
#  -Атрибуты класса:
#  name: название магазина.
#  address: адрес магазина.
#  items: словарь, где ключ - название товара, а значение - его цена.
#  Например, {'apples': 0.5, 'bananas': 0.75}.
#
# Методы класса:
#  __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для items`.
#  метод для добавления товара в ассортимент.
#  метод для удаления товара из ассортимента.
#  метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
#  метод для обновления цены товара.
#
# 2. Создай несколько объектов класса Store:
#  Создай не менее трех различных магазинов с разными названиями,
#  адресами и добавь в каждый из них несколько товаров.
#
# 3. Протестировать методы:
#  Выбери один из созданных магазинов и протестируй все его методы:
#  добавь товар, обнови цену, убери товар и запрашивай цену.
#
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.
class Store():
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, new_item, price_item):
        self.items[new_item] = price_item
        print(f"Добавлен товар {new_item} по цене {price_item} в магазин {self.name}")

    def del_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Удален товар {item_name} из магазина {self.name}")

    def info_price(self, key):
        print(f"Цена товара {key} = {self.items.get(key, None)}")

    def upd_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Изменена цена товара {item_name}. Текущая цена = {new_price}")
        else:
            print(f"Товар {item_name} не найден в магазине {self.name}")

    def all_items(self):
        #вывести весь прайс-лист
        print(f"Все товары магазина {self.name} по адресу: {self.address}")
        print(self.items)

shop01 = Store("Пятерочка", "улица Ленина, дом 5", {})
shop02 = Store("Дикси", "улица Центральная, дом 15", {})
shop03 = Store("Магнит", "улица Парковая, дом 100", {})

print(f"Магазин {shop01.name}")
shop01.add_item("Яблоки", 100)
shop01.add_item("Томаты", 200)
shop01.add_item("Огурцы",150)

shop01.all_items()
shop01.info_price("Томаты")
shop01.del_item("Томаты")
shop01.all_items()
shop01.add_item("Томаты", 220)
shop01.all_items()
shop01.upd_price("Томаты", 225)
shop01.upd_price("Огурцы", 155)
shop01.all_items()