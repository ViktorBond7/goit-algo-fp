items = {
    "pizza":     {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog":   {"cost": 30, "calories": 200},
    "pepsi":     {"cost": 10, "calories": 100},
    "cola":      {"cost": 15, "calories": 220},
    "potato":    {"cost": 25, "calories": 350}
}

def dynamic_programming(budget):
    n = len(items)
    names = list(items.keys())
    
    # dp[i][w] = макс. калорійність, використовуючи перші i предметів і бюджет w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # keep[i][w] = True, якщо i-тий предмет береться в оптимальне рішення при бюджеті w
    keep = [[False] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        name = names[i - 1]
        c = items[name]['cost']
        cal = items[name]['calories']
        for w in range(budget + 1):
            # не брати цей предмет
            dp[i][w] = dp[i - 1][w]
            # спробувати взяти, якщо вміщається у бюджет
            if c <= w:
                val_if_taken = dp[i - 1][w - c] + cal
                if val_if_taken > dp[i][w]:
                    dp[i][w] = val_if_taken
                    keep[i][w] = True
    
    # Відтворення вибору предметів (backtracking)
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if keep[i][w]:
            name = names[i - 1]
            selected.append(name)
            w -= items[name]['cost']
    selected.reverse()
    
    return dp[n][budget], selected


if __name__ == "__main__":
    max_cal, choice = dynamic_programming(100)
    print(f"Максимально можна набрати {max_cal} калорій, вибравши: {choice}")








