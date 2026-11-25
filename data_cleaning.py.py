import pandas as pd
import numpy as np

# 1. ЗАГРУЗКА И ПЕРВИЧНЫЙ ОСМОТР
print("--- 1. Первичный осмотр ---")
df = pd.read_csv('superstore.csv', encoding='latin-1') # иногда нужна эта кодировка

print("Размер данных:", df.shape)
print("\nИнформация о колонках и типах данных:")
print(df.info())

print("\nОписательная статистика:")
print(df.describe())

# 2. ПОИСК ПРОПУСКОВ
print("\n--- 2. Поиск пропусков ---")
# Выводим количество пропусков в каждой колонке
print(df.isnull().sum())

# ВАШ КОД ЗДЕСЬ:
# Посмотрите, в каких колонках есть пропуски.
# Если пропуски в Postal Code (индекс), возможно, их лучше заполнить или удалить?
# Напишите код, чтобы удалить строки, где вообще нет никаких данных (если такие есть):
df = df.dropna(how='all')


# 3. ПОИСК И УДАЛЕНИЕ ДУБЛИКАТОВ
print("\n--- 3. Поиск дубликатов ---")
print("Количество дубликатов до очистки:", df.duplicated().sum())

df = df.drop_duplicates()

print("Количество дубликатов после очистки:", df.duplicated().sum())
print("Размер данных после очистки:", df.shape)

df['Postal Code'] = df['Postal Code'].astype(str)
# Если есть пропуски, заполняем их строкой 'Unknown'
df['Postal Code'] = df['Postal Code'].fillna('Unknown')

# 4. РАБОТА С ДАТАМИ (Приведение типов)
print("\n--- 4. Работа с датами ---")
print("Тип данных колонки Order Date до:", df['Order Date'].dtype)

# ВАШ КОД ЗДЕСЬ:
# Преобразуйте колонку 'Order Date' в формат datetime с помощью pd.to_datetime()
df['Order Date'] = pd.to_datetime(df['Order Date'])
# Сделайте то же самое для колонки 'Ship Date'
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 5. ПОИСК АНОМАЛИЙ (Выбросов)
print("\n--- 5. Поиск аномалий ---")
# Ищем отрицательные значения в продажах (Sales) и прибыли (Profit)
# В этом датасете есть возвраты, поэтому Profit может быть отрицательным.
# Проверим максимальные значения:
print("Максимальная скидка (Discount):", df['Discount'].max())
print("Максимальная прибыль (Profit):", df['Profit'].max())

# Считаем время доставки в днях
df['Delivery_Days'] = (df['Ship Date'] - df['Order Date']).dt.days

df = df.dropna(subset=['Order Date'])
print(f"Размер данных после удаления строк без даты: {df.shape}")

# Проверим статистику по времени доставки
print("\nСтатистика по времени доставки (в днях):")
print(df['Delivery_Days'].describe())

# ВАШ КОД ЗДЕСЬ:
# Давайте создадим новый столбец 'Order_Year' (год заказа) из колонки 'Order Date'
df['Order_Year'] = df['Order Date'].dt.year

print("\nСколько заказов доставлено за N дней:")
print(df['Delivery_Days'].value_counts().sort_index())

# 6. СОХРАНЕНИЕ ОЧИЩЕННЫХ ДАННЫХ
print("\n--- 6. Сохранение ---")
# Сохраняем очищенный датасет в новый файл, чтобы не потерять исходник
df.to_csv('superstore_cleaned.csv', index=False)
print("Очищенный датасет сохранен в superstore_cleaned.csv!")
