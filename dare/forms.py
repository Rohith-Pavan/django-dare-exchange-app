from django import forms
from .models import Dare, Category, DareCompletion, DareRating


class DareForm(forms.ModelForm):
    class Meta:
        model = Dare
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter dare title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the dare...'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        if not self.fields['category'].queryset.exists():
            self.fields['category'].empty_label = "No categories available - create one in admin first"


class DareCompletionForm(forms.ModelForm):
    class Meta:
        model = DareCompletion
        fields = ['proof_text', 'proof_image', 'proof_video_url']
        widgets = {
            'proof_text': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Describe how you completed this dare...'
            }),
            'proof_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'proof_video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://youtube.com/watch?v=... (optional)'
            }),
        }
        labels = {
            'proof_text': 'Proof Description',
            'proof_image': 'Proof Image (Optional)',
            'proof_video_url': 'Video Proof URL (Optional)',
        }


class DareRatingForm(forms.ModelForm):
    class Meta:
        model = DareRating
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(
                choices=[(i, f'{i} Star{"s" if i != 1 else ""}') for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Share your thoughts about this dare... (optional)'
            }),
        }
        labels = {
            'rating': 'Your Rating',
            'comment': 'Comment (Optional)',
        }