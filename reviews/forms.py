from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'review_title', 'review_text')
        labels = {
            'rating': 'Star rating',
            'review_title': 'Title',
            'review_text': 'Review',
        }

        rating_choices = [
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars'),
        ]

        widgets = {
            'review_title': forms.TextInput(
                attrs={'placeholder': 'Enter your review title here'}),
            'review_text': forms.Textarea(
                attrs={'placeholder': 'Enter your review here'}),
            'rating': forms.Select(choices=rating_choices),
        }
