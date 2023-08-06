from easy_inference.providers.provider_base import FrameProvider
import cv2

class Webcam(FrameProvider):
    def __init__(self, source=0) -> None:
        super().__init__()
        self._video_capture = cv2.VideoCapture(source)

    def __iter__(self): return self

    def __next__(self):
        self.log_fps()
        _, frame = self._video_capture.read()
        return frame
