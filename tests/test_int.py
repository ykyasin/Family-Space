import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import User, Post

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        app.config['SECRET_KEY'] = "secure"
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/Admin/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

        user1 = User(name='Yusuf')
        db.session.add(user1)
        db.session.commit()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)


class TestUserCreation(TestBase):
    def test_user_creation(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[2]').send_keys('Bob')
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').click()
        time.sleep(1)

        assert url_for('login') in self.driver.current_url

class TestUserLogin(TestBase):
    def test_user_login(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/form/input[2]').click()
        time.sleep(1)
        assert url_for('main',user='Yusuf') in self.driver.current_url



if __name__ == '__main__':
    unittest.main(port=5000)