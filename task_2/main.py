import turtle
import math

def draw_tree(x, y, length, angle, level):
    if level == 0:
        return

    # Обчислюємо координати другого кінця гілки
    x2 = x + length * math.cos(math.radians(angle))
    y2 = y + length * math.sin(math.radians(angle))

    # Малюємо гілку
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x2, y2)

    # Наступні двi гілки: ліва та права
    new_length = length * 0.8  # Коефіцієнт зменшення довжини
    draw_tree(x2, y2, new_length, angle + 45, level - 1)  # Ліва гілка
    draw_tree(x2, y2, new_length, angle - 45, level - 1)  # Права гілка

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 7): "))

    turtle.speed("fastest")
    turtle.bgcolor("white")
    turtle.color("green")

    # Початкове положення і параметри
    start_x = 0
    start_y = -250
    initial_length = 100
    initial_angle = 90

    draw_tree(start_x, start_y, initial_length, initial_angle, level)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()


          
