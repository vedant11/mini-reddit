import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    post_message = models.TextField(default="this is an empty post body")

    def __str__(self):
        return self.post_text

    def was_published_recently(self):
        return (
            self.pub_date >= timezone.now() - datetime.timedelta(days=1)
            and self.pub_date <= timezone.now()
        )


class Choice(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


"""
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
"""
