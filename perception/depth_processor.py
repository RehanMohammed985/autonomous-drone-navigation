import numpy as np
import cv2

class DepthProcessor:
    def __init__(self):
        pass

    def process_depth_frame(self, depth_frame):
        """
        Input: raw depth frame (e.g. from stereo or RGB-D camera)
        Output: processed depth map with noise reduction and filtering
        """
        # Normalize depth to 0-255 for visualization (optional)
        depth_normalized = cv2.normalize(depth_frame, None, 0, 255, cv2.NORM_MINMAX)
        depth_normalized = depth_normalized.astype(np.uint8)

        # Apply median blur to reduce noise
        depth_filtered = cv2.medianBlur(depth_normalized, 5)
        return depth_filtered
