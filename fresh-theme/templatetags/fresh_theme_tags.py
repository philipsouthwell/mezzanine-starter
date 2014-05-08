from __future__ import unicode_literals

from django.db.models import Q

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine import template
from mezzanine.utils.models import get_user_model

User = get_user_model()

register = template.Library()

@register.inclusion_tag('fresh-theme/tags/posts_display_small.html')
def blog_news_feed():
    """
    Put a list of up to 10 currently published blog posts of category 'News'
    into the template context.

    Usage::

        {% blog_news_feed %}

    """
    blog_posts = BlogPost.objects.published()
    title_or_slug = lambda s: Q(title=s) | Q(slug=s)
    # try:
    #     category = BlogCategory.objects.get(title_or_slug('News'))
    #     blog_posts = blog_posts.filter(categories=category)
    # except BlogCategory.DoesNotExist:
    #     return []
    return list(blog_posts[:10])
