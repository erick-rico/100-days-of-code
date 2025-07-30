from turtle import Turtle

class Line(Turtle):
    
    def __init__(self):
        super().__init__()
        
    def draw_center_line(self):
        """Dibuja una línea punteada vertical en el centro de la pantalla."""
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.setheading(270)
        self.pensize(5)
        self.hideturtle()
    
        # Dibuja la línea punteada
        for _ in range(30): # 30 segmentos (600 altura / 20 por segmento = 30)
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)