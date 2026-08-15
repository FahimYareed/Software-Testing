import allure

a, b = 2, 3

@allure.suite("Arithmetic Operations")
def test_add():
    with allure.step("Addition"):
        assert a + b == 5

@allure.suite("Arithmetic Operations")
def test_sub():
    with allure.step("Subtraction"):
        assert b - a == 1
