import cv2
import sys

print("Hello! Image Processing Operations")


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


def contrast(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final


opt = 'y'
print("Please select any one images to do the processing\na. Girls\nb. Fruits\nc. Tiger\nd. Flower")
option = input("Please enter the corresponding image option: ")
if option == "a":
    imagePath = "girls.jpg"
elif option == "b":
    imagePath = "fruits.png"
elif option == "c":
    imagePath = "tiger.jpeg"
else:
    imagePath = "flower.jpg"

while opt == "y":
    # Get user supplied values
    # Reading the image
    image = cv2.imread(imagePath)

    print("Following list operations can be performed\n1. GrayScale Convert\n2. Drawing Rectangles\n3. Adding Text"
          "\n4. Blurring Image\n5. Edge Detection \n6. Brightening Image\n7. Contrast Increase\n8. Cropping"
          "\n9. Resizing")
    options = int(input("Please enter the corresponding operation number : ").strip())
    if options == 1:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("original image", image)
        cv2.imshow("gray image", gray)
    elif options == 2:
        img_copy = image.copy()
        cv2.rectangle(img_copy, pt1=(140, 92), pt2=(620, 240), color=(255, 0, 0), thickness=5)
        cv2.imshow("original image", image)
        cv2.imshow("rectangle", img_copy)
    elif options == 3:
        img_copy = image.copy()
        cv2.putText(img_copy, "This is sample text", (250, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color=(0, 0, 255),
                    thickness=2)
        cv2.imshow("original image", image)
        cv2.imshow("Text", img_copy)
    elif options == 4:
        blurred = cv2.blur(image, (1, 20))
        cv2.imshow("original image", image)
        cv2.imshow("blurred image", blurred)
    elif options == 5:
        edge = cv2.Canny(image, 200, 300)
        cv2.imshow("original image", image)
        cv2.imshow("edge image", edge)
    elif options == 6:
        frame = increase_brightness(image, value=20)
        cv2.imshow("original image", image)
        cv2.imshow("Brightened image", frame)
    elif options == 7:
        frame = contrast(image)
        cv2.imshow("original image", image)
        cv2.imshow("Contrasted image", frame)
    elif options == 8:
        croped_image = image[140:600, 100:235]
        cv2.imshow("original image", image)
        cv2.imshow("Cropped image",croped_image)
    elif options == 9:
        resized_image = cv2.resize(image,(100,100))
        cv2.imshow("original image", image)
        cv2.imshow("resized image",resized_image)
    else:
        print("Please select the correct option")
        continue
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    opt = input("Do you want to continue? y/n :")
