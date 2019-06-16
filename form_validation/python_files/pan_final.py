import cv2
import pytesseract

def pan_final(img):
    #img = cv2.imread('./data/pan.jpeg')
    cv2.imshow('Original',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = gray
    #cv2.imshow("grayscale",img)
    
    (h,w) = img.shape
    #st = pytesseract.image_to_string(img[:,w//2:w])
    st = pytesseract.image_to_string(img)
    return st
    '''
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

img = cv2.imread('/home/saujanya/code_asylums/ML/ideathon/data/pan.jpeg')
s = pan_final(img)
print(s)