import random
import sqlite3
import string
import unittest
import requests
from selenium import webdriver


class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000"
        self.driver = webdriver.Edge()

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def generate_user():
        letters = string.ascii_lowercase
        data = {
            'username': ''.join(random.choice(letters) for _ in range(10)),
            'email': ''.join(random.choice(letters) for _ in range(10)),
            'password': ''.join(random.choice(letters) for _ in range(10))
        }
        return data

    @staticmethod
    def generate_article(user):
        letters = string.ascii_lowercase
        data = {
            'title': ''.join(random.choice(letters) for _ in range(10)),
            'text': ''.join(random.choice(letters) for _ in range(10)),
            'topic': ''.join(random.choice(letters) for _ in range(10)),
            'user': user
        }
        return data

    def test_home_page_title(self):
        self.driver.get(self.url)
        self.assertIn("Main", self.driver.title)

    def test_registration(self):
        url = f'{self.url}/registration'
        user = self.generate_user()
        response = requests.post(url, data=user)
        self.assertIn(str(response.status_code), "200")

    def test_get_articles(self):
        user = self.generate_user()
        conn = sqlite3.connect('../db.sqlite3')
        sql = f''' INSERT INTO application_article(id, title, text, date, userId_id, topicId_id) VALUES({random.randint(100, 200)},'title','text','date',1,1) '''
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()
        article = self.generate_article(user)
        article_url = f'{self.url}/add-article'
        article_response = requests.post(article_url, data=article)
        self.assertIn(str(article_response.status_code), "200")

