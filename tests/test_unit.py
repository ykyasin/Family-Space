# Import the necessary modules
import unittest
from flask import url_for
from flask_testing import TestCase
import time
from urllib.request import urlopen
from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# import the app's classes and objects
from application import app, db
from application.models import User, Post

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        db.create_all()
        user1 = User(name='Yusuf')
        db.session.add(user1)
        post1 = Post(detail='Testing the post', user=user1)
        post2 = Post(detail='New post', user=user1)
        db.session.add(post1)
        db.session.add(post2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_login_get(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get(url_for('home'), follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_main_get(self):
        response = self.client.get(url_for('main',user="Yusuf"))
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_post(self):
        response = self.client.get(url_for('main',user=User.query.first().name))
        self.assertIn(b'Testing the post', response.data)

    def test_read_user(self):
        response = self.client.get(url_for('login'))
        self.assertIn(b'Yusuf', response.data)

class TestCreate(TestBase):
    def test_create_user(self):
        response = self.client.post(url_for('login'),
            data=dict(name="John"),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"John", response.data)
 
    def test_create_post(self):
        response = self.client.post(url_for('main',user=User.query.first().name),
            data=dict(submit = True, detail='Another Post to test'),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Another Post to test', response.data)


class TestUpdate(TestBase):
    def test_update_user(self):
        response = self.client.post(url_for('main',user=User.query.first().name),
            data=dict(submit4 = True, chname='Max'),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)
        

    def test_invalid_update_user(self):
        response = self.client.post(url_for('main',user=User.query.first().name),
            data=dict(submit4 = True, chname=''),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)

class TestDelete(TestBase):
    def test_delete_user(self):
        response = self.client.post(url_for('main',user='Yusuf'),
            data=dict(yesdel = True),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        response = self.client.post(url_for('main',user='Yusuf'),
            data=dict(submit2 = True, post = 1),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)
       



