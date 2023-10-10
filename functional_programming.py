from functools import reduce

students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "David", "age": 19, "grades": [80, 86, 93, 88]},
    {"name": "Ella", "age": 20, "grades": [91, 88, 84, 90]},
    {"name": "Frank", "age": 21, "grades": [85, 89, 92, 87]},
    {"name": "Grace", "age": 22, "grades": [93, 90, 85, 92]},
    {"name": "Henry", "age": 20, "grades": [84, 86, 89, 92]},
    {"name": "Ivy", "age": 21, "grades": [90, 88, 93, 85]},
    {"name": "Jack", "age": 22, "grades": [89, 92, 86, 90]},
    {"name": "Kelly", "age": 19, "grades": [86, 88, 92, 84]},
    {"name": "Liam", "age": 20, "grades": [88, 85, 90, 87]},
    {"name": "Mia", "age": 21, "grades": [87, 91, 89, 92]},
    {"name": "Noah", "age": 22, "grades": [90, 92, 85, 88]},
    {"name": "Olivia", "age": 19, "grades": [86, 93, 90, 88]},
    {"name": "Peter", "age": 20, "grades": [92, 88, 85, 90]},
    {"name": "Quinn", "age": 21, "grades": [89, 84, 88, 92]},
    {"name": "Ryan", "age": 22, "grades": [85, 90, 92, 89]},
    {"name": "Sophia", "age": 20, "grades": [91, 87, 89, 90]},
    {"name": "Thomas", "age": 21, "grades": [88, 93, 92, 87]}
]

# Фильтрация данных
filtered_students = filter(lambda student: student["age"] < 22 and student["grades"][0] > 90 and student["grades"][3] > 90, students)

# Преобразование данных
average_grades_per_student = map(lambda student: {"name": student["name"], "average_grade": sum(student["grades"]) / len(student["grades"])},students)

total_average_grade = reduce(lambda total, student: total + sum(student["grades"]) / len(student["grades"]), students, 0) / len(students)

# Агрегация данных
student_with_highest_average_grade = max(students, key=lambda student: sum(student["grades"]) / len(student["grades"]))

print("Отфильтрованные студенты:", list(filtered_students))
print("Средняя сумма баллов каждого студента:", list(average_grades_per_student))
print("Средняя сумма баллов всех студента:", total_average_grade)
print("Студент с наивысшим средним баллом:", student_with_highest_average_grade)

users = [
    {"name": "Alice", "expenses": [100, 50, 75, 200]},
    {"name": "Bob", "expenses": [50, 75, 80, 100]},
    {"name": "Charlie", "expenses": [200, 300, 50, 150]},
    {"name": "David", "expenses": [100, 200, 300, 400]},
    {"name": "Eve", "expenses": [150, 80, 90, 120]},
    {"name": "Frank", "expenses": [50, 60, 70, 80]},
    {"name": "Grace", "expenses": [200, 250, 100, 150]},
    {"name": "Henry", "expenses": [100, 150, 200, 250]},
    {"name": "Isabella", "expenses": [300, 400, 500, 600]},
    {"name": "Jack", "expenses": [50, 75, 100, 125]},
    {"name": "Kelly", "expenses": [100, 200, 300, 400]},
    {"name": "Liam", "expenses": [150, 200, 250, 300]},
    {"name": "Mia", "expenses": [50, 75, 100, 125]},
    {"name": "Noah", "expenses": [200, 300, 400, 500]},
    {"name": "Olivia", "expenses": [100, 150, 200, 250]},
    {"name": "Peter", "expenses": [300, 450, 600, 750]},
    {"name": "Quinn", "expenses": [50, 75, 100, 125]},
    {"name": "Ryan", "expenses": [100, 200, 300, 400]},
    {"name": "Sophia", "expenses": [150, 250, 350, 450]},
    {"name": "Tom", "expenses": [200, 400, 600, 800]}
]


# Отфильтровать пользователей по заданным критериям
filtered_users = [user for user in users if sum(user['expenses']) < 400]

# Рассчитать общую сумму расходов для каждого пользователя
total_expenses_per_user = {user['name']: sum(user['expenses']) for user in users}

# Получить общую сумму расходов всех отфильтрованных пользователей
total_expenses_filtered = sum([sum(user['expenses']) for user in filtered_users])

print("Отфильтрованные пользователи:", filtered_users)
print("Общая сумма расходов каждого пользователя:", total_expenses_per_user)
print("Общая сумма расходов всех отфильтрованных пользователей:", total_expenses_filtered)

orders = [
  {"order_id": 1, "customer_id": 101, "amount": 150.0},
  {"order_id": 2, "customer_id": 102, "amount": 200.0},
  {"order_id": 3, "customer_id": 101, "amount": 75.0},
  {"order_id": 4, "customer_id": 103, "amount": 100.0},
  {"order_id": 5, "customer_id": 101, "amount": 50.0},
  {"order_id": 6, "customer_id": 102, "amount": 175.0},
  {"order_id": 7, "customer_id": 103, "amount": 125.0},
  {"order_id": 8, "customer_id": 104, "amount": 80.0},
  {"order_id": 9, "customer_id": 101, "amount": 90.0},
  {"order_id": 10, "customer_id": 102, "amount": 60.0},
  {"order_id": 11, "customer_id": 105, "amount": 95.0},
  {"order_id": 12, "customer_id": 103, "amount": 135.0},
  {"order_id": 13, "customer_id": 101, "amount": 70.0},
  {"order_id": 14, "customer_id": 102, "amount": 100.0},
  {"order_id": 15, "customer_id": 104, "amount": 55.0},
  {"order_id": 16, "customer_id": 105, "amount": 120.0},
  {"order_id": 17, "customer_id": 106, "amount": 85.0},
  {"order_id": 18, "customer_id": 101, "amount": 130.0},
  {"order_id": 19, "customer_id": 103, "amount": 45.0},
  {"order_id": 20, "customer_id": 106, "amount": 70.0}
]

# 1. Фильтрация заказов
filtered_orders = [order for order in orders if order["customer_id"] == 101]

# 2. Подсчет суммы заказов
total_amount = sum(order["amount"] for order in filtered_orders)

# 3. Подсчет средней стоимости заказов
average_amount = total_amount / len(filtered_orders)

print("Отфильтрованные заказы:", filtered_orders)
print("Общая сумма заказов:", total_amount)
print("Средняя сумма заказа:", average_amount)