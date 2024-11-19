"""
Oscar Gomme
Groupe 403
Désinner avec arcade
"""

import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class CreateLandscape(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        CreateLandscape.draw_rectangles()
        CreateLandscape.draw_arcs()
        CreateLandscape.draw_circles()
        CreateLandscape.draw_ellipses()
        CreateLandscape.draw_triangles()
        CreateLandscape.draw_lines()
        CreateLandscape.draw_polygones()
        CreateLandscape.afficher_texte()

    @staticmethod
    def draw_rectangles():
        r = arcade.rect.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT * 0.4)
        arcade.draw.draw_rect_filled(r, arcade.color.AO)
        r = arcade.rect.LBWH(0, SCREEN_HEIGHT * 0.4, SCREEN_WIDTH, SCREEN_HEIGHT * 0.6)
        arcade.draw.draw_rect_filled(r, arcade.color.DEEP_SKY_BLUE)

    @staticmethod
    def draw_arcs():
        arcade.draw_arc_filled(320, 400, 70, 35, arcade.color.ALICE_BLUE, 0, 180)
        arcade.draw_arc_filled(350, 400, 70, 85, arcade.color.ALICE_BLUE, 0, 180)
        arcade.draw_arc_filled(370, 400, 70, 40, arcade.color.ALICE_BLUE, 0, 180)
        arcade.draw_arc_filled(480, 380, 30, 55, arcade.color.ALICE_BLUE, 0, 180)
        arcade.draw_arc_filled(515, 380, 65, 80, arcade.color.ALICE_BLUE, 0, 180)
        arcade.draw_arc_filled(550, 380, 70, 45, arcade.color.ALICE_BLUE, 0, 180)

    @staticmethod
    def draw_circles():
        arcade.draw_circle_filled(SCREEN_HEIGHT * 0.15, SCREEN_WIDTH * 0.6, 50, arcade.color.SUNGLOW)

    @staticmethod
    def draw_ellipses():
        arcade.draw_ellipse_filled(175, 85, 250, 125, arcade.color.FRENCH_SKY_BLUE)

    @staticmethod
    def draw_triangles():
        arcade.draw.draw_triangle_filled(310, 150, 360, 300, 410, 150, arcade.color.DARK_ELECTRIC_BLUE)
        arcade.draw.draw_triangle_filled(350, 100, 400, 250, 450, 100, arcade.color.AUROMETALSAURUS)
        arcade.draw.draw_triangle_filled(380, 40, 430, 190, 480, 40, arcade.color.BLACK_OLIVE)
        arcade.draw.draw_triangle_filled(410, 0, 460, 150, 510, 0, arcade.color.DARK_ELECTRIC_BLUE)

    @staticmethod
    def draw_lines():
        line_list = [(72, 360), (72, 340), (140, 418), (160, 418), (139, 361), (125, 375), (12, 361), (26, 375)]
        arcade.draw_lines(line_list, arcade.color.DARK_TANGERINE, 5)

    @staticmethod
    def draw_polygones():
        points = [(500, 100), (510, 110), (550, 30), (540, 20)]
        arcade.draw.draw_polygon_filled(points, arcade.color.FRENCH_PUCE)

    @staticmethod
    def afficher_texte():
        arcade.draw_text("Oscar Gomme", 600, 10, arcade.color.GAINSBORO)


def main():
    window = CreateLandscape(SCREEN_WIDTH, SCREEN_HEIGHT, "Landscape")
    window.run()


if __name__ == "__main__":
    main()
