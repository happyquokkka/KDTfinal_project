# -*- coding: utf-8 -*-
"""토픽모델 최종 수정본_11.09_Final

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zL-v4rRyArXo2hFC26p8l-tVt_RZXL_u
"""


import numpy as np
import pandas as pd
import json
from . import models, views
import re

# Mecab 설치
# !set -x \
# && pip install konlpy \
# && curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash -x  # Mecab 설치

import nltk

nltk.download("stopwords")
nltk.download("punkt")

stopwords = "너무 수 있는 함께 정말 곳 더 의 많이 또 이 한 다시 참 그리고 보고 것 많은 가장 보이는 날 있어서 년 같아요 할 중 다 본 첫 하고 있어 일 있고 다른 있다 있습니다 너무나 월 수 날 정말 때 꼭 더 것 또 길 그 년 다시 나 이 봉 보고 중 한번 일 눈 속 광 저 분 시간 우리 이곳 모습 방문 거 구경 최고 등 하나 기분 전 젤 건 녘 집 잔 앤 샷 안 엄 샤 달 바 앞 대 담 십 가 바 랏 가 내 포 데 애 내 십 만 제 찌 레 벽 운 번 목 치 사 복 덕 닌 삼 지요 린이 휴 제주 제주도 여행".split()

# 데이터 preprocessing 함수화 시킴 정규화, nouns로 형태소 분석까지 list형태로 받음
from konlpy.tag import Mecab

a = [""]


def text_preprocessing(data):
    stop_word = stopwords
    tokenizer = Mecab()
    token_list = []

    for text in data:
        txt = re.sub("[^가-힣from konlpy.tag import Twitter]", "", text)
        token = tokenizer.nouns(txt)
        token = [t for t in token if t not in stop_word]
        token_list.append(token)
    return token_list


def conn(jeju):
    import pymysql

    host_name = "localhost"
    host_port = 3306
    username = "root"
    password = "00000000"
    database_name = jeju
    db = pymysql.connect(
        host=host_name,  # MySQL Server Address
        port=host_port,  # MySQL Server Port
        user=username,  # MySQL username
        passwd=password,  # password for MySQL username
        db=database_name,  # Database name
        charset="utf8",
    )
    return db


def Jaccard_similarity(doc1, doc2):
    doc1 = set(doc1)
    doc2 = set(doc2)
    doc2 = [x.strip() for x in doc2 if x.strip()]
    doc2 = set(doc2)
    # d = [i for i,j in zip(doc1,doc2) if i==j]
    list_2 = []
    for i in doc1:
        for j in doc2:
            # print(i,j)
            if i == j:
                list_2.append(i)
    # print(list_2)
    return len(list_2) / len(doc1 | doc2)


def sim_place(a, aa):
    b = text_preprocessing(a)
    c = sum(b, [])
    cb = []
    for i in range(0, len(aa)):
        Jaccard_similarity(c, aa["Keywords"][i].split(","))
        cb.append(Jaccard_similarity(c, aa["Keywords"][i].split(",")))
    hi = max(cb)
    # index_1=cb.index(hi)
    # max_value = [i for i, value in enumerate(cb) if value == hi]
    aa["sim"] = cb
    if hi > 0:
        aaa = aa[aa["sim"] == hi]
    else:
        aaa = pd.DataFrame(
            columns=["name", "keyword", "address", "Latitude", "Longitude"]
        )
    dic = {}
    dic["name"] = list(aaa["name"])
    dic["keyword"] = list(aaa["keyword"].values)
    dic["address"] = list(aaa["address"].values)
    dic["Latitude"] = list(aaa["Latitude"].values)
    dic["Longitude"] = list(aaa["Longitude"].values)

    return dic


def make_json(a):
    db1 = conn("jeju")
    sql = "select * from sights"
    aa = pd.read_sql(sql, db1)
    dic = sim_place(a, aa)
    file_path = "myungso.json"
    with open(file_path, "w", encoding="UTF-8") as outfile:
        json.dump(dic, outfile, ensure_ascii=False)
    return dic