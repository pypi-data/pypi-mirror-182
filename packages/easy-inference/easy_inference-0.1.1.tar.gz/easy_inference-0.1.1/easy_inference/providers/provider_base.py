import numpy as np
import time
import os
from typing import Generator
from abc import ABC, abstractmethod

class FrameProvider(ABC):
    def __init__(self) -> None:
        self._last_time = time.monotonic()
        super().__init__()
        self._enable_log = os.getenv("FPS", 0)

    def log_fps(self) -> None:
        " Call this method somewhere in the __next__ method to log the fps of the generator loop."
        # TODO: add python logging support
        if self._enable_log:
            print(f'FPS: {1/(time.monotonic() - self._last_time):.2f}')
        self._last_time = time.monotonic() 

    def __iter__(self) -> Generator[int, np.ndarray, str]:
        pass

    @abstractmethod
    def __next__(self) -> np.ndarray:
        pass

