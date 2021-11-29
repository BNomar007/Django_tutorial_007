from django import forms

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'recipe name'}), help_text='You need help! <a href="/contact">Contact us</a>')
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'placeholder':'Descriptions'}))
    # directions = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'placeholder':'Directions'}))
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                'placeholder': f'Recipe {str(field)}',
                'rows': 5,
                'class': 'form-control',
            }
            self.fields[str(field)].label = ''
            self.fields[str(field)].widget.attrs.update(new_data)


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                'placeholder': str(field),
                'class': 'form-control'
            }
            self.fields[str(field)].label = ''
            self.fields[str(field)].widget.attrs.update(new_data)