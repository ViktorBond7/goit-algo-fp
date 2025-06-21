items = {
    "pizza":     {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog":   {"cost": 30, "calories": 200},
    "pepsi":     {"cost": 10, "calories": 100},
    "cola":      {"cost": 15, "calories": 220},
    "potato":    {"cost": 25, "calories": 350}
}

def greedy_selection(budget):
    # Обчислюємо ratio для кожної страви
    ratios = [
        (name, data["calories"] / data["cost"]) for name, data in items.items()
    ]
    
    # Сортуємо за спаданням ratio
    ratios.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    selected = []
    remaining_budget = budget

    for name, _ in ratios:
        cost = items[name]["cost"]
        cal  = items[name]["calories"]
        # Якщо можемо взяти цю страву — беремо
        if cost <= remaining_budget:
            selected.append(name)
            total_calories += cal
            remaining_budget -= cost

    return total_calories, selected

if __name__ == "__main__":
    budget = 100
    cal, choice = greedy_selection(budget)
    print(f"Максимально можна набрати {cal} калорій, вибравши: {choice}")


