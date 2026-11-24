from pathlib import Path

from dip_coding_project.image_io import load_image

SAMPLE = Path(__file__).parent.parent / "sample" / "34469040.jpg"


def test_load_image_returns_color_array():
    img = load_image(str(SAMPLE))
    assert img.ndim == 3 and img.shape[2] == 3
