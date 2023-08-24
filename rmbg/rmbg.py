import base64
from io import BytesIO
from PIL import Image
from rembg import remove

def remove_background(input_image):
    output_image = remove(input_image)
    buffered = BytesIO()
    output_image.save(buffered, format="png")
    img_str = str(base64.b64encode(buffered.getvalue()))
    result = str(img_str)[2:len(img_str)-1]
    return result