from __future__ import unicode_literals

from django.db.models import Count, Q

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.generic.models import Keyword
from mezzanine import template
from mezzanine.utils.models import get_user_model

User = get_user_model()

register = template.Library()

# A modification of blog_recent_posts from mezzanine_blocks
@register.as_tag
def blog_recent_news_posts(limit=5, tag=None, username=None, category=None):
    """
    Put a list of recently published blog posts into the template
    context. A tag title or slug, category title or slug or author's
    username can also be specified to filter the recent posts returned.

    Usage::

        {% blog_recent_posts 5 as recent_posts %}
        {% blog_recent_posts limit=5 tag="django" as recent_posts %}
        {% blog_recent_posts limit=5 category="python" as recent_posts %}
        {% blog_recent_posts 5 username=admin as recent_posts %}

    """
    blog_posts = BlogPost.objects.published().select_related("user")
    title_or_slug = lambda s: Q(title=s) | Q(slug=s)
    if tag is not None:
        try:
            tag = Keyword.objects.get(title_or_slug(tag))
            blog_posts = blog_posts.filter(keywords__keyword=tag)
        except Keyword.DoesNotExist:
            return []
    if category is not None:
        try:
            category = BlogCategory.objects.get(title_or_slug(category))
            blog_posts = blog_posts.filter(categories=category)
        except BlogCategory.DoesNotExist:
            pass
    if username is not None:
        try:
            author = User.objects.get(username=username)
            blog_posts = blog_posts.filter(user=author)
        except User.DoesNotExist:
            return []
    if not blog_posts:
        post1 = BlogPost()
        post1.title = 'A feed for the home page'
        post1.content = 'This block displays the ten most recent blog posts of category "News"' \
                        ' in their entirety. Just create a blog post and give it the category "News"'
        post2 = BlogPost()
        post2.title = 'Great for links and deals'
        post2.content = 'Use this space for brief comments and links to other pages. If using with Cartridge it\'s ' \
                        'perfect to highlight items.'
        post3 = BlogPost()
        post3.title = 'These example posts are not stored in the database'
        post3.content = 'If you try and edit them inline you\'ll only get an' \
                        ' error message. As soon as you publish a blog post of category "News" they will disappear.'
        blog_posts = [post1, post2, post3,]
        return blog_posts

    return list(blog_posts[:limit])