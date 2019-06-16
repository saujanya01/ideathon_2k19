import cv2
import pytesseract
import re

def aadhar_f(img):
    #img = cv2.imread('./data/pan.jpeg')
    #cv2.imshow('Original',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = gray
    #cv2.imshow("grayscale",img)
    
    (h,w) = img.shape
    #st = pytesseract.image_to_string(img[:,w//2:w])
    st = pytesseract.image_to_string(img)
    dob=re.findall(r'(((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/((?:0[1-9])|(?:1[0-2]))\/(\d{4}))',st)
    aad=re.findall(r'([0-9]{4}\s[0-9]{4}\s[0-9]{4})',st)
    return {'dob':dob,'a_no':aad}
    
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
# img = cv2.imread('adfront.jpg')
# s = aadhar_front(img)
# dob=re.findall(r'(((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/((?:0[1-9])|(?:1[0-2]))\/(\d{4}))',s)
# aad=re.findall(r'([0-9]{4}\s[0-9]{4}\s[0-9]{4})',s)


# print(s)