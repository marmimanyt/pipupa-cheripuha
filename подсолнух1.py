import turtle # импорт графического модуля 
t = turtle.Turtle() # загружаем модуль Черепашка
t.shape() # курсор невидимый
t.width(5) 
t.speed (0)
for i in range(7):
    t.begin_fill()
    t.fillcolor("yellow")
    t.goto(-1200,-900)
    t.forward (2900)
    t.left(90)
    t.forward (2500)
    t.left(90)    
    t.forward (2500)
    t.left(90)    
    t.forward (2500)
    t.left(90)    
    t.end_fill()
t.penup()
t.goto (0,0)
t.pendown()
while True:
        t.width(9)
        t.circle(900)
        t.width(5) 
        t.forward (300)
        t.left (190)
        for i in range(7):
            t.forward (90)
            t.circle (90)
            turtle.end_fill()
            if abs (t.pos())<1:
                break


turtle.done()

echo "# pipupa" >> README.md 
git init 
git add README.md 
git commit -m "first commit" 
git branch -M main 
git remote add origin https://github.com/marmimanyt/pipupa.git
 git push - ты главный