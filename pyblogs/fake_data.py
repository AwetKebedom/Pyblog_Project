import urllib.request



class User:

    def __init__(self, username, email):
        # Check if username already exist
        # Check if email is valid

        self.username = username
        self.email    = email

users = []
# Create a lot of random users
for name in ('john', 'nick', 'charles', 'zoe', 'tesfit', 'awet', 'reuven', 'michael','avner'):
    fake_mail = "{}@gmail.com".format(name)
    user      = User(name, fake_mail)
    users.append(user)

class News:

    def __init__(self, title, content):
        self.title = title
        self.content = content



list_of_news = ['arsenal is leading','dimention data has won Gold medal', 'manchester united bought messi','table tennis has scheduled']
news_obj = []
for new in list_of_news:
    title = 'sport'
    news = News(title, new)
    news_obj.append(news)



