from application import db 

db.drop_all()
db.create_all()

user1 = User(name='Yusuf')
db.session.add(user1)
user2 = User(name='Yonis')
db.session.add(user2)
user3 = User(name='Ismail')
db.session.add(user3)


db.session.commit()