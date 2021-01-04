from application import db 
from application.models import User, Post
db.drop_all()
db.create_all()

user1 = User(name='Yusuf')
user2 = User(name='Ali')
post1 = Post(detail='My first post', user = user1)
db.session.add(user1)
db.session.add(user2)
db.session.add(post1)


db.session.commit()