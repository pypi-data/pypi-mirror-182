from czitools import pylibczirw_metadata as czimd
import os
from pathlib import Path
from pylibCZIrw import czi

basedir = Path(__file__).resolve().parents[3]

# get the CZI filepath
filepath = os.path.join(basedir, r"data/w96_A1+A2.czi")


def test_bounding_box():

    czi_bbox = czimd.CziBoundingBox(filepath)

    assert (czi_bbox.scenes_bounding_rect[0] == czi.Rectangle(x=0, y=0, w=1960, h=1416))
    assert (czi_bbox.scenes_bounding_rect[1] == czi.Rectangle(x=19758, y=24, w=1960, h=1416))
    assert (czi_bbox.total_bounding_box == {'T': (0, 1),
                                            'Z': (0, 1),
                                            'C': (0, 2),
                                            'B': (0, 1),
                                            'X': (0, 21718),
                                            'Y': (0, 1440)})
    assert (czi_bbox.total_rect == czi.Rectangle(x=0, y=0, w=21718, h=1440))
