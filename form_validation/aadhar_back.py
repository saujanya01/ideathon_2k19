import cv2
import pytesseract
import os
import re

def aadhar_b(img):
    
    # file = os.listdir('./data/aadhar')
    # for i in file:
    #     x=x.split('.')
    #     if x[0].endswith('back')
    #     filename = i
    #img = cv2.imread('./data/aadhar/'+filename)
    #cv2.imshow('Original',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = gray
    #cv2.imshow("grayscale",img)
    
    (h,w) = img.shape
    st = pytesseract.image_to_string(img[:,w//2:w])
    #s = st.split('\n')
    #st = pytesseract.image_to_string(img)
    addpos=re.split("Address:",st)
    addi=addpos[1]
    addend=re.split(r'([0-9]{6})',addi)
    ''.join(addend)
    address=addend[0]+addend[1]
    return {'address':address}
    '''
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

# img = cv2.imread('adback.jpeg')
# s = aadhar_back(img)
# addpos=re.split("Address:",s)
# addi=addpos[1]
# addend=re.split(r'([0-9]{6})',addi)
# ''.join(addend)
# address=addend[0]+addend[1]
# print(s)








