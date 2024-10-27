salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_shortfall = 0

# Цикл на 10 месяцев
for month in range(months):
    # Рассчитываем недостающую сумму
    shortfall = spend - salary

    if shortfall > 0:
        total_shortfall += shortfall
    spend *= (1 + increase)

required_capital = round(total_shortfall)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",required_capital)
