import cv2

class ShapeDetector:
    def __init__(self):
        pass
    def detect(self, c):
        shape = "undefined"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 3:
            shape = "triangle"

        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h);
            shape = "square" if 0.95 <= ar <= 1.05 else shape = "rectangle"

        elif len(approx) == 5:
            shape = "pentagon"

        else:
            shape = "circle"

        return shape
