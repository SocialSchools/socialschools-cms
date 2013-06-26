from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('socialschools_cms/includes/socialschools_login.html')
def socialschools_login():
    login_url = getattr(settings, 'CSS_LOGIN_URL', None)
    return { 'login_url': login_url }
