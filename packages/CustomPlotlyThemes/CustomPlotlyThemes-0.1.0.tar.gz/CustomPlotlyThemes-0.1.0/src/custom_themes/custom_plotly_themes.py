"""Custom themes for plotly"""
import plotly.io as pio
from custom_themes.colorschemes import *


def _colorscheme_type(background, foreground):
    """Finds if the colorscheme is a dark or light scheme"""
    sum_foreground = (
        int(foreground[1:3], 16)
         + int(foreground[3:5], 16) 
         + int(foreground[5:7], 16)
    )
    sum_background = (
        int(background[1:3], 16)
        + int(background[3:5], 16) 
        + int(background[5:7], 16)
    )
    if sum_background > sum_foreground:
        return "light"
    return "dark"


def make_template(colorscheme: str, colors: dict):
    """
    Make a template based on two background colors, two foreground colors and 
    eight accent colors.

    Parameters
    ----------
    colorscheme: str
        Name of new colorscheme
    colors: dict
        Dictionary with the 12 new colors. They need to be named 
        'primary_background', 'secondary_background', 'primary_foreground', 
        'secondary_foreground' and 'accent1' to 'accent8'.
    """
    colorscheme_type = _colorscheme_type(
        colors["primary_background"],
        colors["primary_foreground"],
    )
    if colorscheme_type == "dark":
        template = pio.templates["plotly_dark"]
    else:
        template = pio.templates["plotly"]

    template.layout["plot_bgcolor"] = colors["secondary_background"]
    template.layout["paper_bgcolor"] = colors["primary_background"]
    template.layout["xaxis"]["gridcolor"] = colors["secondary_foreground"]
    template.layout["xaxis"]["linecolor"] = colors["primary_foreground"]
    template.layout["xaxis"]["zerolinecolor"] = colors["primary_foreground"]
    template.layout["yaxis"]["gridcolor"] = colors["secondary_foreground"]
    template.layout["yaxis"]["linecolor"] = colors["primary_foreground"]
    template.layout["yaxis"]["zerolinecolor"] = colors["primary_foreground"]
    template.layout["font"]["color"] = colors["primary_foreground"]
    template.layout["colorway"] = [
        colors["accent1"],
        colors["accent2"],
        colors["accent3"],
        colors["accent4"],
        colors["accent5"],
        colors["accent6"],
        colors["accent7"],
        colors["accent8"],
    ]

    pio.templates[colorscheme] = template


# Make custom colorschemes
make_template("solarized_dark", solarized_dark)
make_template("solarized_light", solarized_light)
