
from ..models import *
from django import template


register = template.Library()


@register.filter(name='isexitincart')
def isexitincart(product, cart):

    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='cartquantity')
def cartquantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return False


@register.filter(name='total_price')
def total_price(product, cart):
    totalprice = product.price * cartquantity(product, cart)
    return totalprice


@register.filter(name="final_price")
def final_price(product, cart):
    sum = 0
    for pro in product:
        sum = sum + total_price(pro, cart)
    return sum


@register.filter(name="order_amount")
def order_amount(num1, num2):
    return num1*num2


@register.filter(name="sum_of_order")
def sum_of_order():
    pub = order.objects.aggregate(sum('price'))
    return pub


@register.filter(name="currency")
def currency(num):
    return "$"+str(num)
