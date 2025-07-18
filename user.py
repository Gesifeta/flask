import datetime
class User:
    def __init__(self):
        self.is_logged = False
        self.first_name = ""
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


    def create_user(self,first_name, username, password):
        self.username = username
        self.password = password
        self.first_name = first_name

    def login(self, username, password):
        self.username = username
        self.password = password
        self.is_logged = True


    def logout(self):
        self.is_logged = False





