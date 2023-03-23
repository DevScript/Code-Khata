import cv2 as cv
import numpy as np

box = cv.imread("box.png")
box_in_sence = cv.imread("box_in_scene.png")
cv.imshow("box", box)
cv.imshow("box_in_sence", box_in_sence)

orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(box, None)
kp2, des2 = orb.detectAndCompute(box_in_sence, None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
goodMatches = []

matches = sorted(matches, key=lambda x: x.distance)
for i in range(len(matches)):
    if (matches[i].distance < 0.46 * matches[-1].distance):
        goodMatches.append(matches[i])

result = cv.drawMatches(box, kp1, box_in_sence, kp2, goodMatches, None)

obj_pts, scene_pts = [], []

for f in goodMatches:
    obj_pts.append(kp1[f.queryIdx].pt)
    scene_pts.append(kp2[f.trainIdx].pt)

H, _ = cv.findHomography(np.float32(obj_pts), np.float32(scene_pts), cv.RHO)
h, w = box.shape[0:2]

pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
dst = cv.perspectiveTransform(pts, H).reshape(-1, 2)
for i in range(4):
    dst[i][0] += w

cv.polylines(result, [np.int32(dst)], True, (0, 255, 0), 3, cv.LINE_AA)

cv.imshow("orb-match", result)
cv.imwrite("orv-match.jpg", result)

cv.waitKey(0)
cv.destroyAllWindows()
