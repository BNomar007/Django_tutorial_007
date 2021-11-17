from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template
import random   

def home_view(Request, *args, **kwargs):

    random_id = random.randint(1, 7)  
    # from the dabase
    article_obj = Article.objects.get(id=random_id)

    article_queryset = Article.objects.all()
    context = {
        'object_list' : article_queryset,
        'object': article_obj,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
    }
    # django template

    # first way to do it
    HTML_STRING = render_to_string('home-view.html', context=context)

    # second way to do it
    '''
    tmpl = get_template('home-view.html')
    tmpl.string = tmpl.render(context=context)
    
    '''
    return HttpResponse(HTML_STRING)