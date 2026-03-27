import numpy as np

from manim import *


def build_gradient_image(width=1024, height=512):
    # Bilinear interpolation between sampled corner colors from the reference image.
    x = np.linspace(0, 1, width)[None, :, None]
    y = np.linspace(0, 1, height)[:, None, None]

    top_left = np.array([79, 250, 231], dtype=float)
    top_right = np.array([98, 116, 250], dtype=float)
    bottom_left = np.array([83, 227, 235], dtype=float)
    bottom_right = np.array([101, 90, 254], dtype=float)

    top = (1 - x) * top_left + x * top_right
    bottom = (1 - x) * bottom_left + x * bottom_right

    return ((1 - y) * top + y * bottom).astype(np.uint8)

class Test(Scene):
    def construct(self):
        background = ImageMobject(build_gradient_image())
        background.height = config.frame_height
        if background.width < config.frame_width:
            background.width = config.frame_width
        background.move_to(ORIGIN)
        self.add(background)

        c = Circle(radius=2.5, color=WHITE, fill_opacity=0.5)
        self.play(DrawBorderThenFill(c), run_time=0.5)

        chinese_font = "Noto Sans CJK HK"
        header = Text("香港", font=chinese_font, font_size=50, color=BLACK, weight=BOLD).shift(UP * 1)
        title = Text("編程學會", font=chinese_font, font_size=72, color=BLACK, weight=BOLD)
        subtitle = Text("科普短片", font=chinese_font, font_size=36, color=BLACK, weight=BOLD).shift(DOWN * 1)
        self.play(Write(header), run_time=0.5)
        self.play(Write(title), run_time=0.5)
        self.play(Write(subtitle), run_time=0.5)

        a = Arc(2.7, TAU * 1 / 4, -TAU * 2.6 / 4, color=WHITE, stroke_width=18)
        self.play(Create(a))
        # a = Arc(3, TAU * 0.7 / 4, -TAU * 3 / 4, color=WHITE, stroke_width=18)
        # self.play(Create(a))
        self.wait(1)



