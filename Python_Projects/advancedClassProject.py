class Rower:

    def __init__(self, name, side):
        self.name = name
        self.side = side
    
    def print_rower(self):
        print(self.name, self.side)

Bryce = Rower("Bryce", "Both")
Justin_G = Rower("Justin G", "Port")
Tony = Rower("TJ", "Starboard")

Bryce.print_rower()
Justin_G.print_rower()
Tony.print_rower()