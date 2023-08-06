import cv2
import easyocr
import numpy as np
import math
from scipy.spatial import distance
from PIL import Image, ImageDraw, ImageFont
import re

#hozanのpointを決めて、その重心を探す。
#その重心が基準と離れているかどうかをチェックする。

class OCR_engine():
    def __init__(self, lang='en', check_word='HOZAN', threshold=10):
        # self.img = img
        self.reader = easyocr.Reader([lang])
        self.check_word = check_word
        self.threshold = threshold
        self.font = cv2.FONT_HERSHEY_COMPLEX

    def process_ocr(self, img):
        if self._is_grayscale(img) == True:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif self._is_grayscale(img) == False:
            pass
        self.img_copy = img.copy()
        result = self.reader.readtext(self.img_copy)

        return result

    def _is_grayscale(self, img):
        color_state = None
        if len(img.shape) < 3:
            color_state = True  # grayscale
        elif len(img.shape) == 3:
            color_state = False  # color
        return color_state

    def _draw_boxes(self, img, result):
        img_copy = img.copy()
        for detection in result:
            p0 = tuple((detection[0][0]))
            p1 = tuple((detection[0][1]))
            p2 = tuple((detection[0][2]))
            p3 = tuple((detection[0][3]))
            points = np.array([p0, p1, p2, p3], dtype=np.int32)
            text = detection[1]

            # detect rot_angle
            center, rot_ang = self._detect_rot_angle(img_copy, p0, p1, p2, p3)

            # get rotated_image
            if abs(rot_ang) > 30:
                # rotate image
                rot_img = self._get_rot_image(img_copy, center, rot_ang)
                dist = self._get_distance(p0, p1, p2, p3)

                # crop image
                img_crop = self._get_crop_image(img_dst=rot_img, dist=dist, offset=10, center=center)
                # OSR 2nd
                result2 = self.reader.readtext(img_crop)
                if len(result2) == 0:
                    continue
                else:
                    text = result2[0][1]
                    print('new text', text)
            else:
                pass

    def _detect_rot_angle(self, img, p0, p1, p2, p3):
        points = np.array([p0, p1, p2, p3], dtype=np.int32)
        # マスク画像生成
        img_h, img_w, _ = img.shape  # color
        img_black = np.zeros((img_h, img_w))
        img_mask = cv2.fillPoly(img_black, [points], (255, 255, 255), cv2.LINE_AA)

        # moment 計算
        m = cv2.moments(img_mask)
        area = m['m00']
        x_g = m['m10'] / m['m00']
        y_g = m['m01'] / m['m00']
        ang = 0.5 * math.atan2(2.0 * m['mu11'], m['mu20'] - m['mu02'])

        # print(x_g, y_g, ang, math.degrees(ang))
        center = (int(x_g), int(y_g))
        rot_ang = 1 * math.degrees(ang)

        return center, rot_ang

    def _get_distance(self, p0, p1, p2, p3):
        # 距離を計算
        d1 = distance.euclidean(p0, p1)
        d2 = distance.euclidean(p0, p3)

        dist = []
        if d1 > d2:
            dist.append(d1)
            dist.append(d2)
        else:
            dist.append(d2)
            dist.append(d1)

        return dist

    def _get_crop_image(self, img_dst, dist, offset, center):
        # Crop
        x_g = center[0]
        y_g = center[1]
        x_crop = int(x_g - 0.5 * dist[0])
        y_crop = int(y_g - 0.5 * dist[1])

        crop_w = int(dist[0])
        crop_h = int(dist[1])

        img_crop = img_dst[y_crop - offset:y_crop + crop_h + offset, x_crop - offset:x_crop + crop_w + offset]

        return img_crop

    def _get_rot_image(self, img, center, rot_ang):
        img_copy = img.copy()
        img_h, img_w, _ = img.shape
        # img_h, img_w = img.shape
        # 全体イメージを回転
        affin_trans = cv2.getRotationMatrix2D(center, rot_ang, 1)
        img_dst = cv2.warpAffine(img_copy, affin_trans, (img_w, img_h))
        return img_dst
