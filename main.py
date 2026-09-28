import pandas
import turtle
screen = turtle.Screen()
l='india-outline-map.gif'
screen.addshape(l)
turtle.shape(l)

l=['Andhra_Pradesh','Arunachal_Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal_Pradesh','Jharkhand','Karnataka','Kerala','Madhya_Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil_Nadu','Telangana','Tripura','Uttar_Pradesh','Uttarakhand','West_Bengal']
o='india_states.csv'
d=pandas.read_csv(o)
li=d.states.tolist()
p=screen.textinput('player','player name')
player=[]
player.append(p)
score=[]
hig=pandas.read_csv('highest.csv')
high=hig.score.max()
hi=hig.player.item()
print(hi)
gues=[]
guessed=0
while guessed<27:
    i=screen.textinput(title="INDIAN ststes",prompt=f'{guessed}/26 need to guess').title()
    if i=='Exit'or i=='Quit':
        score.append(guessed)
        li=[n for n in li if n not in gues ]
        d=pandas.DataFrame({'not guessed':li})
        df = pandas.read_csv('highest.csv')
        if guessed>high:
            highest_df = pandas.read_csv('highest.csv')
            highest_df = pandas.DataFrame(columns=['player', 'score'])
            new_score_row = pandas.DataFrame([{'player': p, 'score': guessed}])
            highest_df = pandas.concat([highest_df, new_score_row], ignore_index=True)
            highest_df.to_csv('highest.csv', index=0)
        d.to_csv('not_guessed.csv')

        break
    if i in li:
        to=turtle.Turtle()
        to.hideturtle()
        to.penup()
        to.goto(200,-100)
        to.write(f'highest={high},player={hi}')
        a=d[d.states==i]

        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        x=a.x.item()
        y=a.y.item()
        gues.append(i)

        t.goto(a.x.item(),a.y.item())
        t.write(i)
        guessed+=1

# Set up the listener
turtle.listen()

turtle.mainloop()