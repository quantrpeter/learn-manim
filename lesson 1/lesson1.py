from manim import *


class Test(Scene):
    def construct(self):
        c = Circle(radius=2.5, color=BLUE, fill_opacity=0.5)
        self.play(DrawBorderThenFill(c), run_time=0.5)

        chinese_font = "Noto Sans CJK HK"
        header = Text("香港", font=chinese_font, font_size=50, color=WHITE).shift(UP*1)
        title = Text("編程學會", font=chinese_font, font_size=72, color=WHITE)
        subtitle = Text("科普短片", font=chinese_font, font_size=36, color=WHITE).shift(DOWN * 1)
        title = Text("編程學會", font=chinese_font, font_size=72, color=WHITE)
        self.play(Write(header), run_time=0.5)
        self.play(Write(title), run_time=0.5)
        self.play(Write(subtitle), run_time=0.5)

        a=Arc(2.7, TAU*1/4, -TAU*2.6/4,color=BLUE, stroke_width=18)
        self.play(Create(a))

        c=NumberPlane().add_coordinates()
        self.play(Write(c))

        self.wait(1)



