from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['search_query'].label = "Search NASA images for"


class LikeForm(forms.Form):
    like = forms.BooleanField(widget=forms.HiddenInput)
