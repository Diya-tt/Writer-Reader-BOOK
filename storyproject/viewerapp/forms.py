from django import forms
from viewerapp.models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields=["comment"]
        widgets={
            "comment":forms.TextInput(attrs={"class":"form-control","placeholder":"Comment"})
        }