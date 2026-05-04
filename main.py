from gamelib import *
import random
import time
score = 0
score2 = 0
win_timer = 0
winning = False
broom_count = 10
water_count = 10
game = Game(800,600,"Witch of the night")
witch = Image("image/Witch.gif",game)
witch.moveTo(400, 455)
witch.health = 0
bk = Image("image/bluebg.jpeg",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)
broom = []
water = []
villagers = []

#Level 1
for i in range(10):
    a = Image("image/broombg.png", game)
    a.resizeTo(30, 80)
    a.speed = random.randint(1, 4)
    broom.append(a)

for i in range(len(broom)):
    broom[i].moveTo(random.randint(50, 750), -random.randint(100, 1000))
floor = Image("image/floor.jpg",game)
floor.resizeTo(game.width, 100)
floor.moveTo(game.width/2,game.height-50)

witch.health = 0
witchbar = Shape("bar", game, 50,10, "blue")
witchbar.moveTo( 0, 100)
jumping = False
landed = False
factor = 1
#witch control
def witch_update():
    witch.draw()
    witchbar.moveTo( 0, 0)
    global jumping, landed, factor, score, broom
    if keys.Pressed[K_UP] and witch.top > 0:
        witch.y -= 5
    if keys.Pressed[K_DOWN] and witch.bottom < floor.top:
        witch.y += 5
    if keys.Pressed[K_LEFT] and witch.left > 0:
        witch.x -= 5
    if keys.Pressed[K_RIGHT] and witch.right < 800:
        witch.x += 5
#Modular Programming
def positionObjects(objects):
    for [i] in range(len(objects)):
        x = randint(600,0)
        y = randint(0, 600)
        objects[i].moveTo(x,-y)
        s = randint(4,8)
        objects[i].setSpeed(s,90)
        objects[i].visible = True

#Jumping    
    witch.draw()
    if jumping:
        jumping = True
        landed = False
        witch.y -= 15 * factor
        factor *= .96
        if factor < 0.1:
            jumping = False
            factor = 1


    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True
            
    if not witch.collidedWith(floor, "rectangle"):
        witch.y += 3
        landed = False
    else:
        landed = True
        witch.bottom = floor.top

title_font = Font("white", 80, "Arial", "black")

title_font.shadowColor = "black"

start_bk = Image("image/startscreen.jpeg", game)
start_bk.resizeTo(game.width, game.height)
play_button = Image("image/play.png", game)
#Start Screen
screen = "start"
while not game.over:
    game.processInput()

    if screen == "start":
            start_bk.draw()
            play_button.draw()
            game.drawText("Witch of the Holy Night", 110, 200, title_font)

    if play_button.collidedWith(mouse) and mouse.LeftClick:
            screen = "game"


    elif screen == "game":
            game.scrollBackground("left", 2)
            

            
            game.drawText("Brooms Caught: " +str(score), 10, 10)
            floor.draw()

            for i in range(len(broom)):
                broom[i].y += broom[i].speed

                if broom[i].collidedWith(floor) or broom[i].top > game.height:
                    broom[i].moveTo(random.randint(50, 750), -random.randint(100, 1000))
                    broom[i].speed = random.randint(1, 4)
            
                if witch.collidedWith(broom[i]):
                    witch.health += 1
                    score +=1
                    broom[i].moveTo(random.randint(50,750), -random.randint(100, 1000))
                if witch.health > 3:
                    game.over = True
                broom[i].draw()
            
    witch.draw()
    witchbar.draw()
    witch_update()
    

    game.update(60)

levelTwo = Image("image/blackbg.jpg",game)
levelTwo.resizeTo(game.width, game.height)
level_font = Font("white", 120, "Arial", "black")
level_font.shadowColor = "black"
level2_timer = 150
game.setBackground(levelTwo)
black_curtain = Image("image/blackbg.jpg", game)
black_curtain.resizeTo(1, game.height)
black_curtain.moveTo(game.width/2, game.height/2)


while black_curtain.width < game.width:
    game.processInput()
    bk.draw()
    floor.draw()
    
    black_curtain.width += 20
    black_curtain.draw()
    game.update(60)


game.setBackground(levelTwo)
floor = Image("image/blackfloor2.jpg", game)
floor.resizeTo(game.width, 100)
floor.moveTo(game.width/2, game.height-50)
witch.moveTo(game.width/2, floor.top - witch.height/2)


while black_curtain.width > 1:
    game.processInput()
    levelTwo.draw()
    floor.draw()
    
    black_curtain.width = max(1, black_curtain.width - 20)
    black_curtain.draw()
    game.over = False
    game.update(60)

#Level 2
game.over = False
witch.health = 0
score2 = 0
level2_timer = 150


water = [] 
for i in range(10):
    a = Image("image/water1.png", game)
    a.resizeTo(30, 80)
    a.speed = random.randint(1, 4)
    a.moveTo(random.randint(50, 750), -random.randint(100, 1000))
    water.append(a)

    
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    game.drawText("Water Caught: " +str(score2), 10, 10)
    
    witch_update()

    for i in range(len(water)):
        water[i].y += water[i].speed

        if water[i].collidedWith(floor) or water[i].top > game.height:
            water[i].moveTo(random.randint(50, 750), -random.randint(100, 1000))
            water[i].speed = random.randint(1, 4)
            
        if witch.collidedWith(water[i]):
            witch.health += 1
            score2 += 1
            water[i].moveTo(random.randint(50, 750), -random.randint(100, 1000))
        
        water[i].draw()


    if level2_timer >0:

        if level2_timer > 0:
            game.drawText("LEVEL 2", 215, 250, level_font)
            level2_timer -= 1
    floor2 = Image("image/blackfloor2.jpg",game)
    floor2.resizeTo(game.width, 100)
    floor2.moveTo(game.width/2,game.height-50)

    if score2 >= 3:
        game.over = True

    game.update(60)


floor3 = Image("image/blackfloor2.jpg", game)
floor3.resizeTo(game.width, 100)
floor3.moveTo(game.width/2, game.height-50)

   


# Level 3
game.over = False
witch.health = 0
score3 = 0

fireballs = []
water_shots = []

shoot_timer = 0   




villagers = []
spacing = game.width // 6

for i in range(5):
    v = Image("image/villagers.png", game)
    v.moveTo(spacing * (i + 1), floor3.top - v.height/2)
    villagers.append(v)


for i in range(5):
    f = Image("image/fireball.png", game)
    f.resizeTo(20, 20)
    f.visible = False
    fireballs.append(f)


while not game.over:
    game.processInput()
    game.scrollBackground("left", 2)

    floor3.draw()
    witch_update()

    
    if shoot_timer > 0:
        shoot_timer -= 1

   
    if keys.Pressed[K_w] and shoot_timer == 0 and len(villagers) > 0:
        target = random.choice(villagers)

        w = Image("image/water1.png", game)
        w.resizeTo(20, 40)
        w.moveTo(witch.x, witch.y)

        dx = target.x - w.x
        dy = target.y - w.y
        dist = (dx**2 + dy**2) ** 0.5

        if dist != 0:
            w.dx = dx / dist * 6
            w.dy = dy / dist * 6

        water_shots.append(w)

        shoot_timer = 20

    
    for w in water_shots[:]:
        w.x += w.dx
        w.y += w.dy
        w.draw()

        remove_water = False

       
        if w.top < 0 or w.bottom > game.height or w.left < 0 or w.right > game.width:
            remove_water = True

        
        for v in villagers[:]:
            if w.collidedWith(v):
                villagers.remove(v)
                score3 += 1
                remove_water = True

        if remove_water == True:
            water_shots.remove(w)

    
    for f in fireballs:
        if f.visible == False:
            if random.randint(0,100) < 2 and len(villagers) > 0:
                v = random.choice(villagers)
                f.moveTo(v.x, v.y)
                f.visible = True

                dx = witch.x - f.x
                dy = witch.y - f.y
                dist = (dx**2 + dy**2) ** 0.5

                if dist != 0:
                    f.dx = dx / dist * 4
                    f.dy = dy / dist * 4

        if f.visible == True:
            f.x += f.dx
            f.y += f.dy
            f.draw()

            if f.top > game.height:
                f.visible = False

            if f.collidedWith(witch):
                witch.health -= 2

                if witch.health < 0:
                    game.over = True
                    game.quit()

   
    for v in villagers:
        v.draw()

    game.drawText("Villagers Hit: " + str(score3), 10, 10)

    if score3 >= 5:
        print("Level 3 Complete")
        game.over = True

    game.update(60)

#Level 4
game.over = False


end_bg = Image("image/blackbg.jpg", game)
end_bg.resizeTo(game.width, game.height)


floor4 = Image("image/blackfloor2.jpg", game)
floor4.resizeTo(game.width, 100)
floor4.moveTo(game.width/2, game.height-50)


house = Image("image/house.png", game)
house.resizeTo(game.width, game.height)
house.moveTo(game.width/2, game.height/2)


door_hitbox = Shape("rectangle", game, 60, 90)
door_hitbox.moveTo(166, 434)
door_hitbox.visible = True



witch.moveTo(400, floor4.top - witch.height/2)


end_font = Font("white", 60, "Arial", "black")
end_font.shadowColor = "black"


while not game.over:
    game.processInput()

    
    end_bg.draw()
    floor4.draw()
    house.draw()

   
    witch_update()

  
    if (witch.collidedWith(door_hitbox)):
      game.over = True

   
    game.drawText("Reach the door to finish...", 180, 50, end_font)

    game.update(60)



game.over = False
timer = 180

final_font = Font("white", 100, "Arial", "black")
final_font.shadowColor = "black"

while not game.over:
    game.processInput()

    end_bg.draw()
    game.drawText("THE END", 250, 250, final_font)

    timer -= 1
    if timer <= 0:
        game.over = True

    if mouse.LeftClick:
        print(mouse.x, mouse.y)

    game.update(60)

game.quit()
