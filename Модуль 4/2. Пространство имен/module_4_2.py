def test_function(): # Функция test_function
    def inner_function(): # Функция inner_function внути функции test_function
        print("Я в области видимости функции test_function")
    inner_function() # inner_function внутри функции test_function

# Попытка вызывать inner_function вне функции test_function
inner_function()

# Результат - ошибка имя inner_functionне обнаружено. Предлагает заменить на test_function.

