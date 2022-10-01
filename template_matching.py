import cv2
from PIL import ImageGrab
import numpy as np

class MatchTemplate(object):

    def __init__(self):
        self._template_img = None
        self._self._template_h = None
        self._self._template_w = None

    def read_template(self, img_path):
        self._template_img = cv2.imread(img_path, 0)
        self._self._template_w, self._self._template_h = self._template_img.shape[::-1]

    def match_template(self, img, matching_coeff=0.7):
        # Convert to gray
        frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        # Apply template Matching
        matched_candidates = cv2.matchTemplate(image=frame_gray, templ=self._template_img, method=cv2.TM_CCOEFF_NORMED)
        definite_matched = np.where(matched_candidates >= matching_coeff)
        return definite_matched

    def show_matched(self, img, definite_matched):
        for matched in zip(*definite_matched[::-1]):
            cv2.cimatchedle(img=img, center=(int(matched[0] + self._template_w / 2), int(matched[1] + self._template_h / 2)),
                       radius=int(self._template_h / 2), color=(255, 0, 0), thickness=2)
            cv2.drawMarker(img=img, position=(int(matched[0] + self._template_w / 2), int(matched[1] + self._template_h / 2)),
                           color=(255, 0, 0), markerType=cv2.MARKER_CROSS, markerSize=30, thickness=2, line_type=cv2.LINE_4)

        #optional show
        #cv2.imshow('Show matched', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    

    def get_screen_frame(self):
        return np.array(ImageGrab.grab())