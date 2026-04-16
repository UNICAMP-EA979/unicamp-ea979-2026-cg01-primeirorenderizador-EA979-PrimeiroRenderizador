import unittest

import numpy as np
import urenderer
from numpy.testing import assert_array_almost_equal


class TestCamera(unittest.TestCase):
    def test_projection_matrix(self) -> None:
        camera = urenderer.node.Camera()

        camera.near_plane = 1.0
        camera.far_plane = 10.0
        camera.screen_width = 1920.0
        camera.screen_height = 1080.0
        camera.vertical_fov = 60.0

        matrix = np.array([[1.75759066,  0.,  0.,  0.],
                           [0.,  3.12460562,  0.,  0.],
                           [0.,  0., -1.22222222, -2.22222222],
                           [0.,  0., -1.,  0.]])

        assert_array_almost_equal(camera.projection_matrix, matrix)

        camera.near_plane = 1.123
        camera.far_plane = 321.0
        camera.screen_width = 456.0
        camera.screen_height = 789.0
        camera.vertical_fov = 90.0

        matrix = np.array([[-0.86721271,  0.,  0.,  0.],
                           [0., -0.50120278,  0.,  0.],
                           [0.,  0., -1.00702145, -2.25388509],
                           [0.,  0., -1.,  0.]])

        assert_array_almost_equal(camera.projection_matrix, matrix)
