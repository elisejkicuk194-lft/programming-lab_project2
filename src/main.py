print("=== Список покупок ===")
print("Введите 'help' для списка команд.")

items = ""  # хранилище продуктов.

while True:
  raw = input("> ").strip()
  if raw == "":
    continue

  space = raw.find(" ")
  if space == -1:
    command = raw.lower()
    argument = ""
  else:
    command = raw[:space].lower()
    argument = raw[space + 1:].strip()

  if command == "help":
    print("Команды:")
    print("  add <товар>      — добавить товар")
    print("  remove <товар>   — удалить товар")
    print("  list             — показать список")
    print("  clear            — очистить список")
    print("  exit             — выход")
    continue

  if command == "add":
    if argument == "":
      print("Формат: add <товар>")
      continue

    # Проверка на дубликаты
    # Ищем вхождение " ;товар;" чтобы избежать ложных совпадений
    if (";" + items).find(";" + argument + ";") != -1:
      print("Товар уже в списке.")
    else:
      items += argument + ";"
      print("Добавлено: " + argument)
    continue

  if command == "remove":
    if argument == "":
      print("Формат: remove <товар>")
      continue
    old_items = items
    items = items.replace(argument + ";", "")
    if old_items == items:
      print("Товар не найден.")
    else:
      print("Удалено: " + argument)
    continue

  if command == "list":
    if items == "":
      print("Список пуст.")
    else:
      print(items)
    continue

  if command == "clear":
    items = ""
    print("Список очищен.")
    continue

  if command == "exit":
    print("До свидания!")
    break

  print("Неизвестная команда. Введите 'help'.")
