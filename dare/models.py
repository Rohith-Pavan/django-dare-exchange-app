from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Dare(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('verified', 'Verified'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_dares')
    accepted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_dares')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('dare_detail', kwargs={'pk': self.pk})
    
    @property
    def is_completed(self):
        return self.status in ['completed', 'verified']


class DareCompletion(models.Model):
    dare = models.OneToOneField(Dare, on_delete=models.CASCADE, related_name='completion')
    completed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    proof_text = models.TextField(help_text="Describe how you completed the dare")
    proof_image = models.ImageField(upload_to='dare_proofs/', blank=True, null=True, help_text="Upload an image as proof (optional)")
    proof_video_url = models.URLField(blank=True, null=True, help_text="Link to video proof (YouTube, etc.)")
    submitted_at = models.DateTimeField(auto_now_add=True)
    verified_by_poster = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Completion of '{self.dare.title}' by {self.completed_by.username}"


class DareRating(models.Model):
    dare = models.ForeignKey(Dare, on_delete=models.CASCADE, related_name='ratings')
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate from 1 (boring) to 5 (amazing)"
    )
    comment = models.TextField(blank=True, help_text="Optional comment about the dare")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['dare', 'rated_by']
    
    def __str__(self):
        return f"{self.rated_by.username} rated '{self.dare.title}' - {self.rating}/5"
