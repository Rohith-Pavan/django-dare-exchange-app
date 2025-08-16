from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from .models import Dare, DareCompletion, DareRating
from .forms import DareForm, DareCompletionForm, DareRatingForm

def health_check(request):
    """Simple health check endpoint for deployment."""
    return HttpResponse("OK", status=200)

class DareListView(ListView):
    model = Dare
    template_name = 'dare_list.html'
    context_object_name = 'dares'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter out completed dares if user is logged in
        if self.request.user.is_authenticated:
            completed_dares = DareCompletion.objects.filter(
                completed_by=self.request.user
            ).values_list('dare_id', flat=True)
            queryset = queryset.exclude(id__in=completed_dares)
        return queryset

class DareDetailView(DetailView):
    model = Dare
    template_name = 'dare_detail.html'
    context_object_name = 'dare'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['has_completed'] = DareCompletion.objects.filter(
                dare=self.object,
                user=self.request.user
            ).exists()
            context['user_rating'] = DareRating.objects.filter(
                dare=self.object,
                user=self.request.user
            ).first()
        return context

class DareCreateView(LoginRequiredMixin, CreateView):
    model = Dare
    form_class = DareForm
    template_name = 'dare_form.html'
    success_url = reverse_lazy('dare_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, 'Dare created successfully!')
        return super().form_valid(form)

class DareUpdateView(LoginRequiredMixin, UpdateView):
    model = Dare
    form_class = DareForm
    template_name = 'dare_form.html'
    success_url = reverse_lazy('dare_list')

    def get_queryset(self):
        return Dare.objects.filter(creator=self.request.user)

class DareDeleteView(LoginRequiredMixin, DeleteView):
    model = Dare
    template_name = 'dare_confirm_delete.html'
    success_url = reverse_lazy('dare_list')

    def get_queryset(self):
        return Dare.objects.filter(creator=self.request.user)

@login_required
def accept_dare(request, pk):
    dare = get_object_or_404(Dare, pk=pk)
    
    if request.method == 'POST':
        form = DareCompletionForm(request.POST)
        if form.is_valid():
            completion = form.save(commit=False)
            completion.dare = dare
            completion.user = request.user
            completion.save()
            messages.success(request, f'You accepted the dare: {dare.title}')
            return redirect('dare_detail', pk=pk)
    else:
        form = DareCompletionForm()
    
    return render(request, 'dare_complete.html', {
        'dare': dare,
        'form': form
    })

@login_required
def rate_dare(request, pk):
    dare = get_object_or_404(Dare, pk=pk)
    
    # Check if user has completed this dare
    if not DareCompletion.objects.filter(dare=dare, completed_by=request.user).exists():
        messages.error(request, 'You must complete a dare before rating it.')
        return redirect('dare_detail', pk=pk)
    
    if request.method == 'POST':
        form = DareRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.dare = dare
            rating.user = request.user
            rating.save()
            messages.success(request, f'You rated the dare: {dare.title}')
            return redirect('dare_detail', pk=pk)
    else:
        form = DareRatingForm()
    
    return render(request, 'dare_rate.html', {
        'dare': dare,
        'form': form
    })

@login_required
def user_profile(request, username):
    # This would show user's dare history, ratings, etc.
    return render(request, 'user_profile.html', {
        'username': username
    })

def signup(request):
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Dare Exchange, {user.username}!')
            return redirect('dare_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})
