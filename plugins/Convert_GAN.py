# Based on the https://github.com/shaoanlu/faceswap-GAN repo (master/FaceSwap_GAN_v2_train.ipynb)

import cv2
import numpy

class Convert(object):
    def __init__(self, encoder):
        self.encoder = encoder

    def patch_image( self, original, face_detected ):
        #TODO ?

        face = cv2.resize(face_detected.image, (64, 64))
        face = numpy.expand_dims(face, 0)
        new_face = self.encoder(face / 255.0)[0]

        original[slice(face_detected.y, face_detected.y + face_detected.h), slice(face_detected.x, face_detected.x + face_detected.w)] = cv2.resize(new_face, (face_detected.w, face_detected.h))
        return original
