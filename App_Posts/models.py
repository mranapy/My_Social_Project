from django.db import models
from django.contrib.auth.models import User

######### Post #########
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=100, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date']
    def __str__(self):
        return self.caption

######### Like Model #########
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)


