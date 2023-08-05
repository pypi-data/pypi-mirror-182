from tkadwite.gradient import draw_gradient, use_gradient
from tkinter import Canvas


__all__ = [
    "AdwCanvas"
]


class AdwCanvas(Canvas):
    def wm_draw_gradient(self, direction="x", start="blue", end="red"):
        draw_gradient(self, axis=direction, color1=start, color2=end)

    draw_gradient = wm_draw_gradient
