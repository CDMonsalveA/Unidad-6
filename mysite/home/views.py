from django.http import HttpResponse
from django.template import loader

# the html file is in the templates folder like this:
# mysite\home\templates\home\index.html
def index(request):
    """load index.html"""
    template = loader.get_template('index.html')
    context = {
        'title': 'Home',
    }
    return HttpResponse(template.render(context, request))
