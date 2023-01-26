# coding: utf-8
from tkinter import mainloop, Button, Tk, Canvas, Label


class Jeu:
    """ Initialisation du menu """
    def __init__(self) -> None:
        self.window = Tk()
        canvas = Canvas(self.window,
                        width=400,
                        height=500,
                        bg="White")
        canvas.pack()
        boutonIA = Button(self.window,
                          text="Jouer contre Jeremy (dans un futur proche)",
                          width=45,
                          height=3)
        Boutonseul = Button(self.window,
                            text="Jouer à 2",
                            width=45,
                            height=3,
                            command=self.one_vs_one)
        Quitter = Button(self.window,
                         text="Quitter",
                         width=45,
                         height=3,
                         command=self.close)
        canvas.create_window(200, 100, window=boutonIA)
        canvas.create_window(200, 200, window=Boutonseul)
        canvas.create_window(200, 300, window=Quitter)
        mainloop()

    """ Fermerture du menu """
    def close(self):
        self.window.destroy()

    """ Lancement du jeu 1vs1 """
    def one_vs_one(self):
        self.close()
        self.window_1v1 = Tk()
        self.canva = Canvas(self.window_1v1, width=300, height=300, bg="White")
        self.canva.pack()
        self.canva.create_rectangle(99, 0, 101, 300, outline="Black")
        self.canva.create_rectangle(199, 0, 201, 300, outline="Black")
        self.canva.create_rectangle(0, 99, 300, 101, outline="Black")
        self.canva.create_rectangle(0, 199, 300, 201, outline="Black")
        self.canva.bind_all("<Button 1>", self.chooseCase)
        self.xT = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.oT = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        mainloop()

    """ Dessin de cercle ou de croix """
    def Draw(self, x, y, case):
        if (sum(self.xT)+sum(self.oT)) % 2 == 0:
            self.oT[case] = 1
            self.canva.create_text(x,
                                   y,
                                   text="O",
                                   fill="Black",
                                   font=('Helvetica', '80'))
        else:
            self.xT[case] = 1
            self.canva.create_text(x,
                                   y,
                                   text="X",
                                   fill="Black",
                                   font=('Helvetica', '80'))

        # Verification si un joueur a gagné
        if ((self.xT[0]+self.xT[1]+self.xT[2] == 3) or
           (self.xT[3]+self.xT[4]+self.xT[5] == 3) or
           (self.xT[6]+self.xT[7]+self.xT[8] == 3) or
           (self.xT[0]+self.xT[3]+self.xT[6] == 3) or
           (self.xT[1]+self.xT[4]+self.xT[7] == 3) or
           (self.xT[2]+self.xT[5]+self.xT[8] == 3) or
           (self.xT[0]+self.xT[4]+self.xT[8] == 3) or
           (self.xT[2]+self.xT[4]+self.xT[6] == 3)):
            self.win("Joueur 2")
        if ((self.oT[0]+self.oT[1]+self.oT[2] == 3) or
           (self.oT[3]+self.oT[4]+self.oT[5] == 3) or
           (self.oT[6]+self.oT[7]+self.oT[8] == 3) or
           (self.oT[0]+self.oT[3]+self.oT[6] == 3) or
           (self.oT[1]+self.oT[4]+self.oT[7] == 3) or
           (self.oT[2]+self.oT[5]+self.oT[8] == 3) or
           (self.oT[0]+self.oT[4]+self.oT[8] == 3) or
           (self.oT[2]+self.oT[4]+self.oT[6] == 3)):
            self.win("Joueur 1")
        elif (sum(self.xT)+sum(self.oT) >= 9):
            self.win("le morpion")

    """ Affichage du gagnant """
    def win(self, winner):
        self.window_1v1.destroy()
        Label(text=winner + " a gagné").pack()

    """ Choix de la case via input de la souris """
    def chooseCase(self, eventorigin):
        x0 = eventorigin.x
        y0 = eventorigin.y
        if 0 <= x0 < 100 and 0 < y0 < 100 and not (self.xT[0] or self.oT[0]):
            self.Draw(50, 50, 0)
        if 100 <= x0 < 200 and 0 < y0 < 100 and not (self.xT[1] or self.oT[1]):
            self.Draw(150, 50, 1)
        if 200 <= x0 < 300 and 0 < y0 < 100 and not (self.xT[2] or self.oT[2]):
            self.Draw(250, 50, 2)
        if 0 <= x0 < 100 and 100 < y0 < 200 and not (self.xT[3] or self.oT[3]):
            self.Draw(50, 150, 3)
        if 100 <= x0 < 200 and 100 < y0 < 200 and not (self.xT[4] or self.oT[4]):
            self.Draw(150, 150, 4)
        if 200 <= x0 < 300 and 100 < y0 < 200 and not (self.xT[5] or self.oT[5]):
            self.Draw(250, 150, 5)
        if 0 <= x0 < 100 and 200 < y0 < 300 and not (self.xT[6] or self.oT[6]):
            self.Draw(50, 250, 6)
        if 100 <= x0 < 200 and 200 < y0 < 300 and not (self.xT[7] or self.oT[7]):
            self.Draw(150, 250, 7)
        if 200 <= x0 < 300 and 200 < y0 < 300 and not (self.xT[8] or self.oT[8]):
            self.Draw(250, 250, 8)
