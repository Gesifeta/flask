from user import User
import datetime

user = User()
blog = {
            "title": "Blog",
            "body": "This is my blog",
            "date_posted": datetime.datetime.now(),
        }

def is_user_authenticated(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged:
           print(func(args[0],kwargs))
        else:
            print("Not logged in")

    return wrapper



@is_user_authenticated
def create_blog(my_user,blogs):

    return (f"User {my_user.first_name} has posted article "
            f"titled  {blogs.get('title')}  date posted: {str(blogs.get('date_posted')).split(" ")[0]} .")

user.create_user("gemechu","gesifeta","365544")
user.login(username="admin", password="<PASSWORD>")
create_blog(user,title=blog["title"],body=blog["body"],date_posted=blog["date_posted"])