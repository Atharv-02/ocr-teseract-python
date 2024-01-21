# importing Flask and other modules
from flask import Flask, request, render_template
import pytesseract
import shutil
import os
import random
from pdf2image import convert_from_path

try:
    from PIL import Image
except ImportError:
    import Image

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route("/", methods=["POST"])
def gfg():
    content = request.files["file"]
    print(content)
    content.save(content.filename)
    # Store Pdf with convert_from_path function
    all_txt = []
    images = convert_from_path("resume.pdf")
    for i in range(len(images)):
        images[i].save("page" + str(i) + ".jpg", "JPEG")
        image_path_in_colab = "page" + str(i) + ".jpg"
        extractedInformation = pytesseract.image_to_string(
            Image.open(image_path_in_colab)
        )
        all_txt.append(extractedInformation)
        print(all_txt)
    return all_txt


if __name__ == "__main__":
    app.run(debug=True)
