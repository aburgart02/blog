import datetime
import random
import sqlite3
import string
import unittest
import regex
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
    def generate_article():
        letters = string.ascii_lowercase
        article = {
            'id': random.randint(1000, 2000),
            'title': ''.join(random.choice(letters) for _ in range(10)),
            'text': ''.join(random.choice(letters) for _ in range(10)),
            'date': datetime.date.today(),
            'userId_id': 1,
            'topicId_id': 1
        }
        return article

    def test_home_page_title(self):
        self.driver.get(self.url)
        self.assertEqual("Main", self.driver.title)

    def test_registration(self):
        url = f'{self.url}/registration'
        user = self.generate_user()
        response = requests.post(url, data=user)
        self.assertEqual(str(response.status_code), "200")

    def test_get_articles(self):
        user = self.generate_user()
        conn = sqlite3.connect('../db.sqlite3')
        articles = [self.generate_article() for _ in range(1)]
        for article in articles:
            sql = f''' INSERT INTO application_article(id, title, text, date, userId_id, topicId_id) VALUES(
                '{article['id']}','{article['title']}','{article['text']}','{article['id']}','{article['id']}','{article['id']}') '''
            cur = conn.cursor()
            cur.execute(sql, user)
            conn.commit()
        self.driver.get(self.url)
        page = self.driver.page_source
        titles = regex.findall('<a href="\/article\/.*">(.*)</a>', page)
        for article in articles:
            sql = f''' DELETE FROM application_article WHERE id = {article['id']} '''
            cur = conn.cursor()
            cur.execute(sql, user)
            conn.commit()
        self.assertTrue(all(elem in titles for elem in [article['title'] for article in articles]))

