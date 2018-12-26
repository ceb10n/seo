from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo


class Post:

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', '')
        self.user = kwargs.get('user', '')
        self.date = kwargs.get('date', '')
        self.slug = kwargs.get('slug', '')
        self.title = kwargs.get('title', '')
        self.content = kwargs.get('content', '')
        self.excerpt = kwargs.get('excerpt', '')
        self.thumbnail = kwargs.get('thumbnail', '')


class Wordpress:
    """A wordpress utility class

    The `Wordpress` class uses the lib wordpress_xmlrpc to expose some common
    tasks using Wordpress.

    Example::
        wp = Wordpress('https://url.com/xmlrpc.php', 'user', 'password')

    Attributes:
        url (str): The xmlrpc url of your blog
        user (str): A valid user of your wordpress blog
        password (str): The password of the given user
    """

    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password

    def get_posts(self, amount=10, status='publish'):
        config = {
            'number': amount,
            'post_status': status}

        wp = Client(self.url, self.user, self.password)
        wp_posts = wp.call(GetPosts(config))
        posts = []

        for post in wp_posts:
            posts.append(Post(
                id=post.id,
                user=post.user,
                date=post.date,
                slug=post.slug,
                title=post.title,
                content=post.content,
                excerpt=post.excerpt,
                thumbnail=post.thumbnail))

        return posts
