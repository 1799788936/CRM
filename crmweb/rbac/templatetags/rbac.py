from django.template import Library
from crmweb import settings


register = Library()


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    """
    {% for item in request.session.permission_menu %}
                    <a href="{{ item.url }}" class="active">
                        <span class="icon-wrap"><i class="fa {{ item.icon }}"></i></span> {{ item.title }}</a>
                {% endfor %}
    """
    print(request.session[settings.MENU_SESSION_KEY])
    return {"menu_list": request.session[settings.MENU_SESSION_KEY]}