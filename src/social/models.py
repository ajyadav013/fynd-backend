"""
Social Model
"""
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class SocialUser(models.Model):
    """
    Social platform user model
    """
    SOCIAL_PLATFORM_FACEBOOK = "facebook"
    SOCIAL_PLATFORM_CHOICES = (
        (SOCIAL_PLATFORM_FACEBOOK, _("Facebook")),
    )
    user = models.ForeignKey(
        User, related_name="socialuser", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    social_platform = models.CharField(
        max_length=20, choices=SOCIAL_PLATFORM_CHOICES)
    social_platform_user_id = models.CharField(max_length=20)
