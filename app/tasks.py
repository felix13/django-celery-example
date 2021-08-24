# Create your tasks here
from app.models import Comment
from celery import shared_task
import time

    
@shared_task   
def spam_filter(comment_id):
    print('spam filtering begins, assume it takes a long time to finish')
    # sleep 5 seconds
    time.sleep(5)
    comment = Comment.objects.get(pk=comment_id)
    bad_words = ['stupid', 'idiot', 'loser']
    is_spam = True if any(word in comment.comment for word in bad_words) else False 
    if is_spam:
        comment.delete()   
    return is_spam    
    
