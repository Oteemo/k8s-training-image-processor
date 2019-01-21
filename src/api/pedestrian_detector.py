# Local application imports
from services.image_processor import ImageProcessor

def post(image):
    image =  ImageProcessor(image["encoded_image"], image["image_name"])
    processed_image =  image.detectPedestrians()
    retval = {"processed_image": processed_image, "image_name" : image.image_name}
    return retval, 200
