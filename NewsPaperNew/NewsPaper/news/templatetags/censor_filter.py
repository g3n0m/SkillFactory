from django import template

register = template.Library()

censor_list = ['неебическим', 'инициативной', 'официальных']
value_new = []


@register.filter(name='censor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, '*****')
    return value
