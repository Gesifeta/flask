import datetime
class User:
    def __init__(self, is_logged):
        self.is_logged = False
        self.username = None
        self.password = None
        self.email = None
        self.is_admin = False
        self.is_active = True
        self.blog = {
            "title": "Blog",
            "body": "This is my blog",
            "date_posted": datetime.datetime,
        }


    def login(self, username, password):
        self.username = username
        self.password = password
        self.is_logged = True

    def create_blog(self,title,text):
        self.title = title
        self.text = text

    def logout(self):
        self.is_logged = False



