from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm
from django.shortcuts import get_object_or_404
from .forms import TopicForm
from .models import Company
from .forms import CompanyForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q




@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard(request):
    return render(request, 'dashboard.html')
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required
def topic_create(request):
    
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('topic_list')
        else:
          form = TopicForm()

        return render(request, 'topic_form.html', {'form': form})


@login_required
def topic_update(request, pk):
    topic = get_object_or_404(Topic, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topic_list')
    else:
        form = TopicForm(instance=topic)

    return render(request, 'topic_form.html', {'form': form})


@login_required
def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk, user=request.user)

    if request.method == 'POST':
        topic.delete()
        return redirect('topic_list')

    return render(request, 'topic_confirm_delete.html', {'topic': topic})

@login_required
def topic_list(request):
    topics = Topic.objects.filter(user=request.user)
    return render(request, 'topic_list.html', {'topics': topics})

@login_required
def company_list(request):
    companies = Company.objects.filter(user=request.user)
    return render(request, 'company_list.html', {'companies': companies})


@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('company_list')
    else:
        form = CompanyForm()

    return render(request, 'company_form.html', {'form': form})


@login_required
def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk, user=request.user)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company_form.html', {'form': form})


@login_required
def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk, user=request.user)

    if request.method == 'POST':
        company.delete()
        return redirect('company_list')

    return render(request, 'company_confirm_delete.html', {'company': company})

@login_required
def delete_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk, user=request.user)
    
    if request.method == "POST":
        topic.delete()
        return redirect("topic_list")
    
    return render(request, "delete_topic.html", {"topic": topic})


@login_required
def create_topic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            
            messages.success(request, "Topic created successfully!")
            return redirect("topic_list")
    else:
        form = TopicForm()
    
    return render(request, "create_topic.html", {"form": form})
    messages.success(request, "Topic updated successfully!")
    messages.success(request, "Topic deleted successfully!")

@login_required
def update_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk, topic__user=request.user)

    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Entry updated successfully!")
            return redirect("topic_detail", pk=entry.topic.id)
    else:
        form = EntryForm(instance=entry)

    return render(request, "entry_form.html", {"form": form})

@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk, topic__user=request.user)
    topic_id = entry.topic.id
    entry.delete()
    messages.success(request, "Entry deleted successfully!")
    return redirect("topic_detail", pk=topic_id)



@login_required
def dashboard(request):
    topics = Topic.objects.filter(user=request.user)
    entries = Entry.objects.filter(topic__user=request.user)

    total_topics = topics.count()
    total_entries = entries.count()

    easy_count = topics.filter(difficulty="Easy").count()
    medium_count = topics.filter(difficulty="Medium").count()
    hard_count = topics.filter(difficulty="Hard").count()

    # Example progress logic
    completed_topics = topics.filter(difficulty="Easy").count()  # example logic
    progress = 0

    if total_topics > 0:
        progress = int((completed_topics / total_topics) * 100)

    context = {
        "topics": topics,
        "total_topics": total_topics,
        "total_entries": total_entries,
        "easy_count": easy_count,
        "medium_count": medium_count,
        "hard_count": hard_count,
        "progress": progress,
    }

    return render(request, "dashboard.html", context)


@login_required
def toggle_complete(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, user=request.user)

    topic.completed = not topic.completed
    topic.save()

    if topic.completed:
        messages.success(request, "Topic marked as completed!")
    else:
        messages.info(request, "Topic marked as incomplete!")

    return redirect("dashboard")

from django.db.models import Count, Q

@login_required
def dashboard(request):
    topics = Topic.objects.filter(user=request.user)

    total_topics = topics.count()
    completed_topics = topics.filter(status='completed').count()

    progress = 0
    if total_topics > 0:
        progress = int((completed_topics / total_topics) * 100)

    # Difficulty breakdown
    easy = topics.filter(difficulty='easy').count()
    medium = topics.filter(difficulty='medium').count()
    hard = topics.filter(difficulty='hard').count()

    context = {
        'total_topics': total_topics,
        'completed_topics': completed_topics,
        'progress': progress,
        'easy': easy,
        'medium': medium,
        'hard': hard,
    }

    return render(request, 'dashboard.html', context)

@login_required
def toggle_topic_status(request, pk):
    topic = Topic.objects.get(pk=pk, user=request.user)

    if topic.status == 'completed':
        topic.status = 'pending'
    else:
        topic.status = 'completed'

    topic.save()
    return redirect('topic_list')

def mock_interview(request):
    return render(request, 'mock_interview.html')