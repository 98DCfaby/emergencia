from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, css_class):
    return value.as_widget(attrs={'class': css_class})
