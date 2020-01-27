import turtle as t


radio = 150
quintas = ("C", "G", "D", "A", "E", "B",
           "F#/Gb", "Db", "Ab", "Eb", "Bb", "F")
correccion = (20, 20, 21, 25, 29, 31,
              31, 36, 33, 31, 25, 20)
t.shape("turtle")
t.penup()
t.goto(0, -radio) 
t.pendown()
t.circle(radio)
t.penup()
t.goto(0, 0) 
t.left(90)
t.pendown()

for quinta in range(12):
    t.forward(radio)
    t.penup()
    t.forward(correccion[quinta]) 
    t.write(quintas[quinta], font=("Arial", 10, "bold"))
    t.goto(0, 0)
    t.right(30)
    t.pendown()

t.hideturtle()
