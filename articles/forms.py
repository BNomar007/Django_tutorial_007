from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)  # getting titles from db
        if qs.exists():
            self.add_error('title', f'"{title}" title already exists.')
        return data



'''
class OldWayArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data  # dictionary    
        title = cleaned_data.get('title')
        if title.lower().strip() == 'new':
            raise forms.ValidationError('This title already exists!')
        return title
    
'''