from manim import *


class Test(Scene):
    def construct(self):
        c = Circle(radius=3, color=BLUE, fill_opacity=0.5)
        self.play(DrawBorderThenFill(c), run_time=0.5)

        chinese_font = "Noto Sans CJK HK"
        title = Text("香港編程學會", font=chinese_font, font_size=72, color=WHITE)
        subtitle = Text("科普短片", font=chinese_font, font_size=36, color=WHITE).shift(DOWN * 1)
        self.play(Write(title), run_time=0.5)
        self.play(Write(subtitle), run_time=0.5)
        self.wait(1)



