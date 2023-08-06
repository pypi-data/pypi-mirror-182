import os, time
def version_declaration():
    """
    The module is about library`s version
    And the author is HuiBuBu(LanBuBu)
    """
    print("""
lison_technology-->The program is stable
    """)

class out:
    def motion(self, frames, second):
        """
        Achieve dynamic effects
        """
        second / frames
        print(self)
        time.sleep(round(second, 2))
        os.system("cls")
    def draw(self, width,height, form):
        """
        THERE CAN DRAW MANY PICTURES
        :return:
        """
        SymbolsOrLettersUsed = self
        if form == "square":
            for width_i in range(width):
                for height_i in range(height):
                    print(SymbolsOrLettersUsed)

