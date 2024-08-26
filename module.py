def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

inner_function() # При вызове функции inner_function выдаёт ошибку, из за того что функция не определена в глобальном пространстве имён
