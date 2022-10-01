import numpy as np
import cv2
from PIL import Image, ImageGrab


class RCModel():

    def __init__(self, name="test"):
        self._name = name
        self._new_race()

    def _new_race(self):
        self._x = None
        self._y = None
        self._w = None
        self._vector = None
        self._feature = None
        self._poses = []

