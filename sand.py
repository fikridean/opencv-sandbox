import cv2

# Import the image
image = cv2.imread('assets/base.jpg', 1)
image = cv2.resize(image, (500, 500))
# image = cv2.resize(image, (0, 0), fx=0.1, fy=0.5)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('assets/base2.jpg', image)

# Display the image
cv2.imshow('Sand', image)
cv2.waitKey(0)
cv2.destroyAllWindows()