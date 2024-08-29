def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    # Вызов внутренней функции внутри test_function
    inner_function()

# Вызов внутренней функции test_function вне функции
inner_function()

# Вызов test_function, чтобы увидеть результат
# test_function()
