from importlib import resources
import io 

def rgb_to_hex(r, g, b):
    """
        Cette fonction convertie une combinaison RGB en code hexadécimal
        Params:
            r : red, intensité de rouge
            g : green, intensité de vert
            b : blue, intensité de bleu
        returns : une séquence hexadéciamle

        exemple : rgb_to_hex(255, 165, 1)
        résultat : "FFA51"
    """

    return "#0{:X}{:X}{:X}".format(int(r), 
                                int(g), 
                                int(b))


class Mise_enforme:
    """
    La classe regroupe l'ensemble des mise en formes indispensables 
    pour la production d'un document quarto
    """

    # création du constructeur

    def __init__(self) -> None:
        self.lkp_blue = rgb_to_hex(0, 34, 93)
        self.lkp_green = rgb_to_hex(0, 136, 81)
        self.lkp_magenta = rgb_to_hex(148, 0, 113)
        self.lkp_grey = rgb_to_hex(169, 169, 169).replace("0","")
        self.lkp_comp_blue = rgb_to_hex(0, 113, 148)
        self.lkp_light_blue = rgb_to_hex(35, 95, 221)
        self.lkp_light_green = rgb_to_hex(0, 227, 166)

   
