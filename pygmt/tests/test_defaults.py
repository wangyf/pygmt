"""
Tests for gmt defaults
"""
import pytest

from .. import Figure, set


@pytest.mark.mpl_image_compare
def test_set():
    set(FONT_ANNOT_PRIMARY="blue")
    fig = Figure()
    fig.basemap(
        region="0/10/0/10", projection="X10c/10c", frame=["af", '+t"Blue Annotation"']
    )

    with set(FONT_LABEL="red", FONT_ANNOT_PRIMARY="red"):
        fig.basemap(
            region="0/10/0/10",
            projection="X10c/10c",
            frame=['xaf+l"red label"', "yaf", '+t"red annotation"'],
            X="15c",
        )

    fig.basemap(
        region="0/10/0/10",
        projection="X10c/10c",
        frame=["af", '+t"Blue Annotation"'],
        X="15c",
    )
    return fig
