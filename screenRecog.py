# source myenv/bin/activate
import mss
import time
import numpy as np 
import cv2 
import pytesseract

class getImage:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def convertToCV2(self, panel):
        grayImage = cv2.cvtColor(panel, cv2.COLOR_BGR2GRAY)
        binaryImage = cv2.adaptiveThreshold(
        grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        denoisedImage = cv2.GaussianBlur(binaryImage, (5, 5), 0) 
        #cv2.imwrite("processed_panel.png", denoisedImage) 
        return denoisedImage
    
    def convertOCR(self, image):
        text = pytesseract.image_to_string(image, lang="eng") 
        return text

    def screenshot(self):
        with mss.mss() as sct:
            monitor = {"top": self.y, "left": self.x, "width": self.width, "height": self.height}
            #time.sleep(3)
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)

            processedImage = self.convertToCV2(img)
            extractedText = self.convertOCR(processedImage)
            #print("Extracted Text:", extractedText)

            #cv2.imshow("Processed Image", processedImage)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            return extractedText




