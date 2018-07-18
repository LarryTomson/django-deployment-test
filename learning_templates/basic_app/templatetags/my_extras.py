from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    Cut out all values of "arg" from the string!
    """
    return value.replace(arg, '')

    #first is what it is called second is call to the function
#register.filiter('cut', cut)
