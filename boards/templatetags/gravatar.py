from django import template
from django.conf import settings

# import code for encoding urls and generating md5 hashes
import hashlib
from urllib.parse import urlencode

register = template.Library()

@register.filter
def gravatar(user):
    # Set your variables here
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    # construct the url
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url
