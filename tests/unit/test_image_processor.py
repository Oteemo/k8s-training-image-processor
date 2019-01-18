import base64
import cv2
from services.image_processor import ImageProcessor

# def test_load_image(shared_datadir):

def test_new_image(shared_datadir):
    """
    GIVEN an image file
    WHEN a new ImageProcessor object is created
    THEN check the encoded image and image name are defined correctly
    """
    image_file = open(shared_datadir / "pedestrian.jpg", "rb")
    encoded_image = base64.b64encode(image_file.read())
    new_image = ImageProcessor( str(encoded_image.decode("utf-8")), "pedestrian.jpg")

    assert new_image.encoded_image == str(encoded_image.decode("utf-8"))
    assert new_image.image_name == "pedestrian.jpg"