import requests
BLOG_POST_URL = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body


