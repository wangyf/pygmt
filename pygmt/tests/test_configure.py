"""
Tests for gmt configure
"""
import pytest

from .. import Figure, configure


@pytest.mark.mpl_image_compare
def test_configure():
    configure(FONT_ANNOT_PRIMARY="blue")
    fig = Figure()
    fig.basemap(
        region="0/10/0/10", projection="X10c/10c", frame=["af", '+t"Blue Annotation"']
    )

    with configure(FONT_LABEL="red", FONT_ANNOT_PRIMARY="red"):
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
