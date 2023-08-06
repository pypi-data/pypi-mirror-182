import math
import sys

from matplotlib import pyplot as plt
from shapely.ops import clip_by_rect

from pyroll.report.pluggy import plugin_manager, hookimpl
from pyroll.core import RollPass, Unit


def plot_intersection_points(ax: plt.Axes, unit: RollPass):
    ax.scatter(unit.upper_left_intersection_point.x, unit.upper_left_intersection_point.y, color='C0')
    ax.scatter(unit.upper_right_intersection_point.x, unit.upper_right_intersection_point.y, color='C0')
    ax.scatter(unit.lower_left_intersection_point.x, unit.lower_left_intersection_point.y, color='C0')
    ax.scatter(unit.lower_right_intersection_point.x, unit.lower_right_intersection_point.y, color='C0')


def plot_lendl_width_boundaries(ax: plt.Axes, unit: RollPass):
    ax.plot(*unit.left_lendl_width_boundary.xy, color='C0')
    ax.plot(*unit.right_lendl_width_boundary.xy, color='C0')


def plot_lendl_area(ax: plt.Axes, unit: RollPass):
    lendl_initial_area = clip_by_rect(unit.in_profile.cross_section, -unit.lendl_width / 2, -math.inf,
                                      unit.lendl_width / 2, math.inf)
    lendl_final_area = clip_by_rect(unit.out_profile.cross_section, -unit.lendl_width / 2, -math.inf,
                                    unit.lendl_width / 2, math.inf)

    ax.fill(*lendl_initial_area.boundary.xy, color="red", alpha=0.5)
    ax.fill(*lendl_final_area.boundary.xy, color="blue", alpha=0.5)


def plot_pass_groove_contour(ax: plt.Axes, roll_pass: RollPass):
    ax.plot(*roll_pass.upper_contour_line.xy, color="k")
    ax.plot(*roll_pass.lower_contour_line.xy, color="k")


@hookimpl(specname="unit_plot")
def unit_plot(unit: Unit):
    """Plot roll pass contour and its profiles"""
    if isinstance(unit, RollPass):
        fig: plt.Figure = plt.figure(constrained_layout=True, figsize=(4, 4))
        ax: plt.Axes = fig.subplots()

        ax.set_aspect("equal", "datalim")
        ax.grid(lw=0.5)
        plt.title("Lendl Areas and Boundaries")
        plot_pass_groove_contour(ax, unit)
        plot_intersection_points(ax, unit)
        plot_lendl_width_boundaries(ax, unit)
        plot_lendl_area(ax, unit)

        return fig


plugin_manager.register(sys.modules[__name__])
