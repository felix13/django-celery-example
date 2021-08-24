from django.shortcuts import render, redirect
from app.forms import CommentForm
from app.models import Comment
from app import tasks

    
def home(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            # Check spam asynchronously.
            tasks.spam_filter.delay(comment_id=comment.id)
            return redirect('home')
    else:
        form = CommentForm()
        
    return render(request, "app/home.html", {'form': form, 'comments': comments })

