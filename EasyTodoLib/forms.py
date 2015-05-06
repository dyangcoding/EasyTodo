from django.forms import ModelForm

class AddTodoForm(ModelForm):
    def __init__(self, todo, *args, **kwargs):
        super(AddTodoForm, self).__init__(*args, **kwargs)
