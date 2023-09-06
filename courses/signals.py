from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Course

@receiver(m2m_changed, sender=Course.students.through)
def total_enrolled_changed(sender, instance, **kwargs):
    instance.total_enrolled = instance.students.count()
    instance.save()