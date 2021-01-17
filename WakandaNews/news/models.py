from django.db import models
from django.contrib.auth.models import User

# Create your models here.

	# Categories: Lifestyle, Sports, Travels, Skeping, Fashion, Night Party, See Beach, Technology,
	# Corporate, Event Time, Politics NOW Let's add em to our "News" model

NEWS_CATEGORIES = (
    ('lifestyle', 'Lifestyle'),
    ('sports', 'Sports'),
    ('travels', 'Travels'),
    ('skeping', 'Skeping'),
    ('fashion', 'Fashion'),
    ('night party', 'Night Party'),
    ('see beach', 'See Beach'),
    ('technology', 'Technology'),
    ('corporate', 'Corporate'),
    ('event time', 'Event Time'),
    ('politics', 'Politics'),
    
)

#Now, let's add a category field to our News Model
# Now, run migrations again...will ya?

class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255)
    category = models.CharField(max_length=100, choices=NEWS_CATEGORIES)
    body = models.TextField()
    feature_image = models.FileField(upload_to='news-gallery/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'news')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'News'

    def __str__(self):
        return '{} by {} on {}'.format(self.title, self.author, self.pub_date)
