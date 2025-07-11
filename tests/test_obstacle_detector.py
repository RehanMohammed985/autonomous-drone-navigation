import unittest
import numpy as np
from perception.obstacle_detector import ObstacleDetector

class TestObstacleDetector(unittest.TestCase):
    def setUp(self):
        # Initialize with dummy model path (mock if needed)
        self.detector = ObstacleDetector(model_path="yolov8.pt", device="cpu")

    def test_detect_no_obstacles(self):
        # Create a blank image
        dummy_img = np.zeros((640, 480, 3), dtype=np.uint8)
        results = self.detector.detect(dummy_img)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()
