import pytest
from Invoice import Invoice
import mock


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

@pytest.fixture()
def input_number():
    input_number = 54
    return input_number

@pytest.fixture()
def input_answer():
    input_answer = "y"
    return input_answer

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_InputNumber(invoice, input_number):
    with mock.patch('builtins.input', return_value=input_number):
        assert invoice.inputNumber(input_number) == 54

def test_TaxToBePaid(invoice, products):
    invoice.taxToBePaid(products)
    assert invoice.taxToBePaid(products) == 4.86
    
def test_InputAnswer(invoice, input_answer):
    with mock.patch('builtins.input', return_value=input_answer):
        assert invoice.inputAnswer(input_answer) == "y"