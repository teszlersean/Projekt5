
import numpy as np
import cv2

#tokenek mennyisége
tokenamount = 0
#háromszög alakú tokenek értéke 200 ft
triangle = 0
trianglevalue = 0
#négyzet alakú tokenek értéke 400 ft
square = 0
squarevalue = 0
#ötszög alakú tokenek értéke 400 ft
pentagon = 0
pentagonvalue = 0
#csillag alakú tokenek értéke 500 ft
star = 0
starvalue = 0

img = cv2.imread('fotok/tokens3.png')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.imshow("img", img)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 200, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 200, 0))
        triangle = triangle + 1
        trianglevalue += 200
    elif len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 200, 0))
          square = square + 1
          squarevalue += 400
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 200, 0))
        pentagon = pentagon + 1
        pentagonvalue += 400
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 200, 0))
        star = star + 1
        starvalue += 500
    else:
        cv2.putText(img, "Token", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 200, 0))
        tokenamount = tokenamount + 1

finalamount = trianglevalue + squarevalue + pentagonvalue + starvalue


print(f"{tokenamount/2} db token van.")
print(f"{triangle} db háromszög token, melyeknek össz értéke {trianglevalue}.")
print(f"{square} db négyzet token, melyeknek össz értéke {squarevalue}.")
print(f"{pentagon} db ötszög token, melyeknek össz értéke {pentagonvalue}.")
print(f"{star} db csillag token, melyeknek össz értéke {starvalue}.")
print(f"Az összes token értéke forintban: {finalamount} ft")


cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()





