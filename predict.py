"""
================
Phan Loai Van Ban Tieng Viet
================
"""

from preProcessData import FeatureExtraction, NLP
from fileProcess import FileReader, FileStore
import os.path
from argparse import ArgumentParser
from sklearn.metrics import classification_report
from gensim import corpora, matutils
from sklearn.svm import LinearSVC
from pyvi import ViTokenizer
import pickle as pickle
import settings
import json
import os
from random import randint
import numpy as np
import requests
from underthesea import ner
print(__doc__)


def selectPlaceByNer(list):
    """
     một phần tử trong list sẽ gồm 4 trường.
     VD: ('Việt Nam', 'Np', 'B-NP', 'B-LOC')
    """
    list = ner(list)
    for text in list:
        if text[3] == "B-LOC" or text[3] == "I-LOC":
            yield(text[0])


def findCoordinatePlace(place):
    COORDINATE_DEFAULT = [108.21168188005686, 16.059664953500032]
    try:
        if 'đường' in place:
            place = place.replace('đường', '')
        data_json = requests.get(
            'https://api.viettelmaps.com.vn:8080/gateway/placeapi/v2/place-api/geocode?address='+place+'&key='+settings.TOKEN).json()
        coordinates = list(data_json['results'][0]
                           ['geometry']['location'].values())[::-1]
        return coordinates
    except:
        return COORDINATE_DEFAULT


if __name__ == '__main__':
    #  Read input data
    # data = readInput()
    while(1):
        print("==="*5)
        data = input("Nhap ky tu: ")
        classifier = pickle.load(
            open('trained_model/mlpclassifier_model.pk', 'rb'))

        # tf-idf
        vectorizer = pickle.load(open(settings.VECTOR_EMBEDDING, 'rb'))
        data_features = []
        data_features.append(' '.join(NLP(text=data).remove_stopwords()))
        features = vectorizer.transform(data_features)

        # predict
        if (max(classifier.predict_proba(features)[0]) < settings.THRESHOLD):
            """
                continue
            """
            print("Không thuộc class nào")
            continue

        text_category = classifier.predict(features)[0]
        print("===" * 5)
        print("\n Loại địa điểm cần tìm: {}".format(text_category))

        name_geography = ' '.join(str(e) for e in selectPlaceByNer(data))
        coordinates = findCoordinatePlace(name_geography)
        print("\n Địa điểm: {}".format(name_geography))
        print("\n Tọa độ: {}".format(coordinates))

        url = "https://api.viettelmaps.vn/gateway/searching/v1/search/geojson/address?access_token=6ht5fdbc-1996-4f54-87gf-5664f304f3d2"
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {"limit": "10", "offset": "0", "sortByDistance": "true",
                   "query": "", "proximity": "", "mode": "search_result"}
        payload['query'] = text_category
        payload['proximity'] = coordinates
        # print(payload)
        response = requests.post(url, headers=headers,
                                 data=json.dumps(payload))
        print("\n {}".format(response.text))
