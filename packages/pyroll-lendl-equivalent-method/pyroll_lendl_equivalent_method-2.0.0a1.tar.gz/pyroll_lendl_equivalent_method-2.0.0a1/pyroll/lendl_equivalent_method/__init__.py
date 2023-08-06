import importlib.util

from pyroll.core import RollPass, Hook

RollPass.InProfile.equivalent_rectangle = Hook[float]()
"""Get the dimensions of the equivalent rectangle of the rotated profile."""


RollPass.InProfile.intersections = Hook[float]()
"""Intersection points between incoming profile and groove"""


RollPass.upper_left_intersection_point = Hook[float]()
"""Upper left intersection point between incoming profile and groove"""


RollPass.upper_right_intersection_point = Hook[float]()
"""Upper right intersection point between incoming profile and groove"""


RollPass.lower_right_intersection_point = Hook[float]()
"""Lower right intersection point between incoming profile and groove"""


RollPass.lower_left_intersection_point = Hook[float]()
"""Lower left intersection point between incoming profile and groove"""


RollPass.left_lendl_width_boundary = Hook[float]()
"""Line between the left side intersection points"""


RollPass.right_lendl_width_boundary = Hook[float]()
"""Line between the right side intersection points"""


RollPass.lendl_width = Hook[float]()
"""Distance between left and right boundary"""


RollPass.lendl_initial_area = Hook[float]()
"""Initial Lendl area"""


RollPass.lendl_final_area = Hook[float]()
"""Final Lendl area"""


from . import hookimpls

REPORT_INSTALLED = bool(importlib.util.find_spec("pyroll.report"))

if REPORT_INSTALLED:
    from . import report
