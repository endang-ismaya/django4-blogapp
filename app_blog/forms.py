from django import forms
from .models import Comment, Subsribe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content", "email", "name", "website")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs["placeholder"] = "Type your comment..."
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["name"].widget.attrs["placeholder"] = "Name"
        self.fields["website"].widget.attrs["placeholder"] = "Website"


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subsribe
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Enter your email here..."
