from __future__ import unicode_literals

from django.db.models import Count, Q

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine import template
from mezzanine.utils.models import get_user_model

User = get_user_model()

register = template.Library()

# A modification of blog_recent_posts from mezzanine_blocks
@register.as_tag
def blog_recent_news_posts(limit=5, category="News"):
    """
    Put a list of recently published blog posts into the template
    context. A category title can also be specified to filter the recent posts returned.

    Usage::

        {% blog_recent_news_posts limit=5 category="News" as recent_posts %}

    """
    blog_posts = BlogPost.objects.published()
    title_or_slug = lambda s: Q(title=s) | Q(slug=s)
    try:
        category = BlogCategory.objects.get(title_or_slug(category))
        blog_posts = blog_posts.filter(categories=category)
        if not blog_posts:
            post1 = BlogPost()
            post1.title = 'A feed for the home page'
            post1.content = 'This block displays the ten most recent blog posts of category "News"' \
                            ' in their entirety. Just create a blog post and give it the category "News"'
            post2 = BlogPost()
            post2.title = 'Great for links and deals'
            post2.content = 'Use this space for brief comments and links to other pages. If using with Cartridge' \
                            'it\'s perfect to highlight items.'
            post3 = BlogPost()
            post3.title = 'These example posts are not stored in the database'
            post3.content = 'If you try and edit them inline you\'ll only get an error message. ' \
                            'As soon as you publish a blog post of category "News" they will disappear.'
            blog_posts = [post1, post2, post3,]
            return blog_posts

    except BlogCategory.DoesNotExist:
        post1 = BlogPost()
        post1.title = 'A feed for the home page'
        post1.content = 'This block displays the ten most recent blog posts of category "News"' \
                        ' in their entirety. Just create a blog post and give it the category "News"'
        post2 = BlogPost()
        post2.title = 'Great for links and deals'
        post2.content = 'Use this space for brief comments and links to other pages. If using with Cartridge' \
                        'it\'s perfect to highlight items.'
        post3 = BlogPost()
        post3.title = 'These example posts are not stored in the database'
        post3.content = 'If you try and edit them inline you\'ll only get an error message. ' \
                        'As soon as you publish a blog post of category "News" they will disappear.'
        blog_posts = [post1, post2, post3,]
        return blog_posts
    return list(blog_posts[:limit])