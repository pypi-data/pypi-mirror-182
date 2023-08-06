import math

from shapely.geometry import LineString
from shapely.ops import clip_by_rect, unary_union

from pyroll.core import Profile, RollPass
from pyroll.core.shapes import rectangle


@RollPass.InProfile.intersections
def intersections(self: RollPass.InProfile):
    roll_pass = self.roll_pass()
    upper_intersections = roll_pass.in_profile.cross_section.boundary.intersection(roll_pass.upper_contour_line)
    lower_intersections = roll_pass.in_profile.cross_section.boundary.intersection(roll_pass.lower_contour_line)

    return unary_union([upper_intersections, lower_intersections])


@RollPass.upper_left_intersection_point
def upper_left_intersection_point(self: RollPass):
    for point in self.in_profile.intersections.geoms:
        if point.x < 0 < point.y:
            return point


@RollPass.upper_right_intersection_point
def upper_right_intersection_point(self: RollPass):
    for point in self.in_profile.intersections.geoms:
        if point.x > 0 and point.y > 0:
            return point


@RollPass.lower_right_intersection_point
def lower_right_intersection_point(self: RollPass):
    for point in self.in_profile.intersections.geoms:
        if point.x > 0 > point.y:
            return point


@RollPass.lower_left_intersection_point
def lower_left_intersection_point(self: RollPass):
    for point in self.in_profile.intersections.geoms:
        if point.x < 0 and point.y < 0:
            return point


@RollPass.left_lendl_width_boundary
def left_lendl_width_boundary(self: RollPass):
    return LineString([self.upper_left_intersection_point, self.lower_left_intersection_point])


@RollPass.right_lendl_width_boundary
def right_lendl_width_boundary(self: RollPass):
    return LineString([self.upper_right_intersection_point, self.lower_right_intersection_point])


@RollPass.lendl_width
def lendl_width(self: RollPass):
    return self.left_lendl_width_boundary.distance(self.right_lendl_width_boundary)


@RollPass.lendl_initial_area
def lendl_initial_area(self: RollPass):
    return clip_by_rect(
        self.in_profile.cross_section, -self.lendl_width / 2,
        -math.inf, self.lendl_width / 2, math.inf).area


@RollPass.lendl_final_area
def lendl_final_area(self: RollPass):
    return clip_by_rect(
        self.out_profile.cross_section, -self.lendl_width / 2,
        -math.inf, self.lendl_width / 2, math.inf).area


@RollPass.InProfile.equivalent_rectangle
def in_equivalent_rectangle(self: RollPass.InProfile):
    roll_pass = self.roll_pass()

    eq_width = self.width
    eq_height = roll_pass.lendl_initial_area / roll_pass.lendl_width

    return rectangle(eq_width, eq_height)


@RollPass.OutProfile.equivalent_rectangle
def out_equivalent_rectangle(self: RollPass.InProfile):
    roll_pass = self.roll_pass()

    eq_width = self.width
    eq_height = roll_pass.lendl_final_area / roll_pass.lendl_width

    return rectangle(eq_width, eq_height)
