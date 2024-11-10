''''
1. Capture or Select the Screen/Panel
Capture the Screen: Use Python libraries like Pillow for basic image handling or mss for screen captures.
Select a Panel: If the panel is part of an application or a webpage, you can use PyQt to capture just the specific part of the window.
2. Preprocess the Image for OCR
Manga panels may have various fonts, stylized text, and noise, so preprocessing the image improves OCR accuracy.
Convert to Grayscale: Convert the image to grayscale to help the OCR engine focus on the text.
Binarization: Use thresholding to create a black-and-white version, which improves readability for OCR.
Noise Reduction: Apply blur or denoise filters, if necessary, to make text clearer.
3. Use OCR for Text Extraction
Pytesseract: pytesseract is a popular Python wrapper for Tesseract OCR, an open-source OCR engine.
Install Tesseract OCR (an external dependency) and configure pytesseract to read the image text.
4. Translate the Text (Optional)
For non-English text, use a translation API such as Google Translate API or a library like translate-python to convert the extracted text to the desired language.
'''

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
        cv2.imwrite("processed_panel.png", denoisedImage)  # Save if needed
        return denoisedImage
    
    def convertOCR(self, image):
        text = pytesseract.image_to_string(image, lang="eng") 
        return text

    def screenshot(self):
        with mss.mss() as sct:
            monitor = {"top": self.y, "left": self.x, "width": self.width, "height": self.height}
            time.sleep(3)
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)

            processedImage = self.convertToCV2(img)
            extractedText = self.convertOCR(processedImage)
            print("Extracted Text:", extractedText)

            cv2.imshow("Processed Image", processedImage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

image = getImage(0, 0, 1280, 800)
image.screenshot()

'''
#pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def screenshot(x,y,width,height):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        time.sleep(3)
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)

       # cv2.imshow("Captured Panel", img)
        #cv2.waitKey(0)
       # cv2.destroyAllWindows()

    processedImage = convertToCV2(img)
    extractedText = convertOCR(processedImage)
    print("Extracted Text:", extractedText)

    cv2.imshow("Processed Image", processedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convertToCV2(panel):
    grayImage = cv2.cvtColor(panel, cv2.COLOR_BGR2GRAY)
    binaryImage = cv2.adaptiveThreshold(
    grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    denoisedImage = cv2.GaussianBlur(binaryImage, (5, 5), 0) 
    cv2.imwrite("processed_panel.png", denoisedImage)  # Save if needed
    return denoisedImage

def convertOCR(image):
    text = pytesseract.image_to_string(image, lang="eng")  # Specify language if needed
    print('finished')
    return text
'''