# -*- coding: utf-8 -*-
import requests
from config import *
import sqlite3

from models import DBSession
from models.vote_record import VoteRecord


class BiHuHelper(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()

    def login(self):
        self.userId = USERID
        self.accessToken = ACCESSTOKEN

    def get_followee_list(self):
        return FOLLOWEE_LIST

    def get_person_articles(self, userId):
        data = {
            "userId": self.userId,
            "accessToken": self.accessToken,
            "queryUserId": userId,
            "pageNum": 1
        }

    def vote_article(self, artId):
        data = {
            "userId": self.userId,
            "accessToken": self.accessToken,
            "artId": artId
        }
        r = requests.post(VOTE_ARTICLE_API, data, verify=False)
        result = r.json()
        vote = VoteRecord(artId=artId, result=result['res'], message=result['resMsg'])
        session = DBSession()
        session.add(vote)
        session.commit()
        session.close()

if __name__ == "__main__":
    bh = BiHuHelper('username', 'password')
    bh.vote_article(53363)