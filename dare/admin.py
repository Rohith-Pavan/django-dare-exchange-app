from django.contrib import admin
from .models import Dare, Category, DareCompletion, DareRating


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Dare)
class DareAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'posted_by', 'accepted_by', 'status', 'created_at']
    list_filter = ['category', 'status', 'created_at', 'accepted_by']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category', 'posted_by', 'accepted_by')


@admin.register(DareCompletion)
class DareCompletionAdmin(admin.ModelAdmin):
    list_display = ['dare', 'completed_by', 'verified_by_poster', 'submitted_at']
    list_filter = ['verified_by_poster', 'submitted_at']
    search_fields = ['dare__title', 'completed_by__username', 'proof_text']
    readonly_fields = ['submitted_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('dare', 'completed_by')


@admin.register(DareRating)
class DareRatingAdmin(admin.ModelAdmin):
    list_display = ['dare', 'rated_by', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['dare__title', 'rated_by__username', 'comment']
    readonly_fields = ['created_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('dare', 'rated_by')
