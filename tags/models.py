from django.db import models
from django.contrib.contenttype.models import ContentType
# from django.contrib.contenttype.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TagItem(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    # type (product , video, article)
    # ID  
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForefine()