from django.db import models
from posting.models import Posting

class Comment(models.Model):
    post = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.post.title}'