# -*- coding: utf8 -*-
"""
Get result and test result with model save before
"""
import load_data
import config, Logger
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sklearn.linear_model import SGDClassifier
import pickle
import traceback

LABELS = config.TARGET_NAMES


def load_model(path):
    try:
        with open(path, 'rb') as fid:
            model = pickle.load(fid)
            return model
    except Exception as e:
        traceback.print_exc()
        exit(0)


class TextClassification(object):
    def __init__(self, model_path):
        self.__model = load_model(model_path)

    def detect(self, test_data):
        """
        Get label for each data item in list test_data
        :param test_data: list
        :return: list
        """
        try:
            predicted = self.__model.predict(list(test_data))
            return predicted
        except:
            return None

    def predict(self, test_data):
        """
        Lấy tỉ lệ chính xác khi đưa vào một list dữ liệu
        :param test_data: list
        :return: None
        """
        try:
            predicted = self.__model.predict(test_data.get_data())
            print("Correct: %f" % np.mean(predicted == test_data.get_target()))
        except:
            pass


if __name__ == '__main__':
    import load_data

    """
    SVM
    """
    obj = TextClassification(config.SAVE_SVM_PATH)
    txt = ["học sinh đá bóng ở sân trường", "Tôi là một học sinh"]
    for i, j in zip(txt, obj.detect(txt)):
        print(i, ': ' + LABELS[j])
    """
    Load test data and check result
    """





    """
    NB
    """
    obj.predict(load_data.load_test_data())

    obj = TextClassification(config.SAVE_NB_PATH)
    txt = ["học sinh đá bóng ở sân trường", "Tôi là một học sinh"]
    for i, j in zip(txt, obj.detect(txt)):
        print(i, ': ' + LABELS[j])
    """
    Load test data and check result
    """
    obj.predict(load_data.load_test_data())
