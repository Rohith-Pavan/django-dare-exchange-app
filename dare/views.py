from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg
from .models import Dare, Category, DareCompletion, DareRating
from .forms import DareForm, DareCompletionForm, DareRatingForm


class DareListView(ListView):
    model = Dare
    template_name = 'dare_list.html'
    context_object_name = 'dares'
    paginate_by = 12


class DareDetailView(DetailView):
    model = Dare
    template_name = 'dare_detail.html'
    context_object_name = 'dare'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dare = self.get_object()
        
        # Add completion info
        try:
            context['completion'] = dare.completion
        except DareCompletion.DoesNotExist:
            context['completion'] = None
        
        # Add rating info
        ratings = dare.ratings.all()
        context['ratings'] = ratings
        context['average_rating'] = ratings.aggregate(Avg('rating'))['rating__avg']
        context['user_rating'] = None
        
        if self.request.user.is_authenticated:
            try:
                context['user_rating'] = ratings.get(rated_by=self.request.user)
            except DareRating.DoesNotExist:
                pass
        
        return context


class DareCreateView(LoginRequiredMixin, CreateView):
    model = Dare
    form_class = DareForm
    template_name = 'dare_form.html'
    
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class DareUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Dare
    form_class = DareForm
    template_name = 'dare_form.html'
    
    def test_func(self):
        dare = self.get_object()
        return self.request.user == dare.posted_by


class DareDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Dare
    template_name = 'dare_confirm_delete.html'
    success_url = reverse_lazy('dare_list')
    
    def test_func(self):
        dare = self.get_object()
        return self.request.user == dare.posted_by


@login_required
def dare_accept(request, pk):
    dare = get_object_or_404(Dare, pk=pk)
    
    if dare.accepted_by is None:
        dare.accepted_by = request.user
        dare.status = 'accepted'
        dare.save()
        messages.success(request, f'You have successfully accepted the dare: "{dare.title}"')
    else:
        messages.warning(request, 'This dare has already been accepted.')
    
    return redirect('dare_detail', pk=dare.pk)


@login_required
def dare_complete(request, pk):
    dare = get_object_or_404(Dare, pk=pk)
    
    # Check if user can complete this dare
    if dare.accepted_by != request.user:
        messages.error(request, 'You can only complete dares you have accepted.')
        return redirect('dare_detail', pk=dare.pk)
    
    if dare.status in ['completed', 'verified']:
        messages.warning(request, 'This dare has already been completed.')
        return redirect('dare_detail', pk=dare.pk)
    
    if request.method == 'POST':
        form = DareCompletionForm(request.POST, request.FILES)
        if form.is_valid():
            completion = form.save(commit=False)
            completion.dare = dare
            completion.completed_by = request.user
            completion.save()
            
            dare.status = 'completed'
            dare.save()
            
            messages.success(request, 'Congratulations! You have submitted proof of completion. Waiting for verification.')
            return redirect('dare_detail', pk=dare.pk)
    else:
        form = DareCompletionForm()
    
    return render(request, 'dare_complete.html', {'form': form, 'dare': dare})


@login_required
def dare_verify(request, pk):
    dare = get_object_or_404(Dare, pk=pk)
    
    # Only the dare poster can verify completion
    if dare.posted_by != request.user:
        messages.error(request, 'Only the dare creator can verify completion.')
        return redirect('dare_detail', pk=dare.pk)
    
    try:
        completion = dare.completion
        completion.verified_by_poster = True
        completion.save()
        
        dare.status = 'verified'
        dare.save()
        
        messages.success(request, f'You have verified the completion of "{dare.title}"!')
    except DareCompletion.DoesNotExist:
        messages.error(request, 'No completion submission found for this dare.')
    
    return redirect('dare_detail', pk=dare.pk)


@login_required
def dare_rate(request, pk):
    dare = get_object_or_404(Dare, pk=pk)
    
    # Check if dare is completed/verified
    if dare.status not in ['completed', 'verified']:
        messages.error(request, 'You can only rate completed dares.')
        return redirect('dare_detail', pk=dare.pk)
    
    # Check if user already rated this dare
    existing_rating = DareRating.objects.filter(dare=dare, rated_by=request.user).first()
    
    if request.method == 'POST':
        form = DareRatingForm(request.POST, instance=existing_rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.dare = dare
            rating.rated_by = request.user
            rating.save()
            
            action = 'updated' if existing_rating else 'submitted'
            messages.success(request, f'Your rating has been {action}!')
            return redirect('dare_detail', pk=dare.pk)
    else:
        form = DareRatingForm(instance=existing_rating)
    
    return render(request, 'dare_rate.html', {'form': form, 'dare': dare, 'existing_rating': existing_rating})


from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["GET", "HEAD"])
def health_check(request):
    """Simple health check endpoint for monitoring"""
    from django.http import JsonResponse
    return JsonResponse({'status': 'healthy', 'message': 'Application is running'})


class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dare_list')


def signup_view(request):
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
