from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime

STATUS_CHOICES = (
    (0, 'No Problems'),
    (1, 'Some Issues'),
    (2, 'Unavailable'),
)

class AlertType(models.Model):

    label = models.CharField(_("label"), max_length=40)
    display = models.CharField(_("display"), max_length=50)
    description = models.CharField(_("description"), max_length=100)

    # by default only on for media with sensitivity less than or equal to this number
    default = models.IntegerField(_("default"))

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _("alert type")
        verbose_name_plural = _("alert types")

    @classmethod
    def create(cls, label, display, description, default=2, verbosity=1):
        """
        Creates a new AlertType.

        This is intended to be used by other apps as a post_syncdb manangement step.
        """
        try:
            alert_type = cls._default_manager.get(label=label)
            updated = False
            if display != alert_type.display:
                alert_type.display = display
                updated = True
            if description != alert_type.description:
                alert_type.description = description
                updated = True
            if default != alert_type.default:
                alert_type.default = default
                updated = True
            if updated:
                alert_type.save()
                if verbosity > 1:
                    print("Updated %s AlertType" % label)
        except cls.DoesNotExist:
            cls(label=label, display=display, description=description, default=default).save()
            if verbosity > 1:
                print("Created %s AlertType" % label)


# Create your models here.
class Alarm(models.Model):
    alert_type = models.ForeignKey(AlertType, verbose_name=_("alert type"))
    slug = models.SlugField(max_length=128, unique=True)
    message = models.TextField(null=True, blank=True, editable=True)
    description = models.TextField(null=True, blank=True, help_text='We will auto fill the description from the first event message if not set')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, editable=True, default=0)
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

