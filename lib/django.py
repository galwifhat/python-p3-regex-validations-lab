from django import forms
# pip install django


class EmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        # Optional: Add more rules or extract parts
        return email
