from django import template

register=template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    THIS CUTS OUR THE VALUE OF "arg" FROM THE STRING!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
