from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class comment(models.Model):
    """
        Comment Model
    """
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    createdAt = models.DateTimeField(default=timezone.now)
    query = models.ForeignKey('queries', on_delete=models.CASCADE,
                              related_name='comments')

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user.username)

    class Meta:
        """
            ordering by createdAt
        """
        ordering = ['-createdAt']
        db_table = "comment"


class queries(models.Model):
    """
        queries Model
    """
    class queriesObjects(models.Manager):
        """
            queriesObjects Model
        """
        def get_queryset(self):
            """
                get_queryset Get all queries that are public
            """
            return super().get_queryset().filter(public=True)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    rawQuery = models.TextField(blank=False, null=True)
    relatedTo = models.CharField(max_length=255, blank=False, null=False, default='')
    public = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queries')
    objects = models.Manager()
    queriesObjects = queriesObjects()

    def __str__(self):
        return f'{self.name} - {self.description} - {self.user.username}'

    class Meta:
        """
            ordering by createdAt
        """
        ordering = ['-createdAt']
        db_table = "queries"
