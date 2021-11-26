import cv2

img = cv2.imread('1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cnts, _ = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in cnts:
    if cnt.size>10:
        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(img, ellipse, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imwrite("dst.png", img)