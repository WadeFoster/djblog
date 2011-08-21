from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
import datetime, markdown

class LivePostManager(models.Manager):
    def get_query_set(self):
        return super(LivePostManager, self).get_query_set().filter(
            status=1
        ).filter(pub_date__lt=datetime.datetime.now).order_by("-pub_date", "-id")

class Post(models.Model):

    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    STATUS_CLOSED = 2

    STATUSES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_CLOSED, 'Closed'),
    )

    title     = models.CharField(max_length=200)
    slug      = models.SlugField(unique=True)
    status    = models.IntegerField(choices = STATUSES, default = STATUS_DRAFT)
    body_html = models.TextField(blank=True)
    body_markdown = models.TextField()
    pub_date  = models.DateTimeField('Date Published')

    objects = models.Manager()
    live = LivePostManager()

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        y = self.entry_date.strftime('%Y')
        m = self.entry_date.strftime('%b').lower()
        d = self.entry_date.strftime('%d')

        return ('blog_entry_detail', None, { 'year': y,
            'month': m, 'day': d, 'slug': self.slug })

    class Meta:
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

@receiver(pre_save, sender=Post)
def do_formatting(sender, instance, **kwargs):
    instance.body_html = markdown.markdown(instance.body_markdown)

