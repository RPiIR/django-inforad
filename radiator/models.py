from django.db import models
import datetime

STATUS_CHOICES = (
    (0, 'No Problems'),
    (1, 'Some Issues'),
    (2, 'Unavailable'),
)

# Create your models here.
class Alarm(models.Model):
    slug = models.SlugField(max_length=128, unique=True)
    message = models.TextField(null=True, blank=True, editable=False)
    description = models.TextField(null=True, blank=True, help_text='We will auto fill the description from the first event message if not set')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, editable=False, default=0)
    order = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.datetime.now, editable=False)
    date_updated = models.DateTimeField(default=datetime.datetime.now, editable=False)

    class Meta:
        ordering = ('order', 'date_created')

    def __unicode__(self):
        if self.message:
            return self.message
        else:
            return self.slug

