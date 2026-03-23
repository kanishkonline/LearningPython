import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("❌ Image not found!")
    exit()

# Show image
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Resize
resized = cv2.resize(img, (300, 300))
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)

# Flip
flipped = cv2.flip(img, 1)
cv2.imshow("Flipped Image", flipped)
cv2.waitKey(0)

# Rotate
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)

# Blur
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Blurred Image", blur)
cv2.waitKey(0)


# Edge Detection
edges = cv2.Canny(img, 100, 200)
cv2.imshow("Edges", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()