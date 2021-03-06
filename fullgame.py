import sys, pygame, random, time
from random import randint

pygame.init() # Required before ANYTHING

screen = pygame.display.set_mode((800, 480), pygame.NOFRAME)

print(pygame.mixer.get_init())
# screen.fill(background)
# music and sounds
pygame.mixer.pre_init(44100,16,2,4096) #Initialize mixer
pygame.mixer.music.set_volume(0.9) 

# Create Sound Objects
menu_sound = pygame.mixer.Sound("nenadsimicmenuclick.wav")
point_sound = pygame.mixer.Sound("scrampunk__okay.wav")
select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
nextLevel_sound = pygame.mixer.Sound("glassbell.wav")
wrongHole_sound = pygame.mixer.Sound("petenice__whoosh.wav")
cancelMenu_sound = pygame.mixer.Sound("raclure__cancel.wav")



menu_sound.set_volume(1)
point_sound.set_volume(1)
select_sound.set_volume(1)
nextLevel_sound.set_volume(1)
wrongHole_sound.set_volume(1)
cancelMenu_sound.set_volume(1)

# End Sound

# load images
bg = pygame.image.load("background.jpg") 
mm = pygame.image.load("mainmenuwithbuttons.jpg")
mmsplash = pygame.image.load("mainmenuspashscreen.jpg") 
qu = pygame.image.load("sure-exit.jpg") 
go = pygame.image.load("gameover.jpg")
main01 = pygame.image.load("main1-classicskee.jpg") 
main02 = pygame.image.load("main2-timedskee.jpg") 
main03 = pygame.image.load("main3-onfire.jpg") 
main04 = pygame.image.load("main4-skillz.jpg") 
gameover_image = pygame.image.load("gameover.jpg")


# Ignore mouse motion (Greatly reduces resources)
pygame.event.set_blocked(pygame.MOUSEMOTION) 

menustatus = 0
gameselection = 0
gamestart = 0

# Colors 
oldlace = (253, 245, 230)
black = (0,0,0)
sienna = (160, 82,45)
red = (255, 0, 0)
cadetblue = (95,158,160)
black = (0,0,0)
sienna = (160,82,45)
green = (0,255,0)
blue = (0,0,255)

# fonts
fontName = 'DS-DIGIB.TTF'
scoreFont = pygame.font.Font(fontName, 180) # Score font (Large)
myfont = pygame.font.Font(fontName, 380) #pygame.font.Font("DS-DIGIB", 450) #Large font for score
ballsfont = pygame.font.Font(fontName, 118) #Small font for ball count
timeFont = pygame.font.Font(fontName, 130) #font for currentTimeRemaining

# buffersystem setup (prevents double scoring)
CurrentTime = {
    "K_a": 0,
    "K_s": 0,
    "K_d": 0,
    "K_f": 0,
    "K_g": 0,
    "K_l": 0,
    "K_j": 0,
    }
cooldown = 1 # Seconds

def splash1():
	musicSwitch(11)
	screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
	splash01 = pygame.image.load("mainspash1.jpg")
	splash02 = pygame.image.load("mainspash2.jpg") 
	mm = pygame.image.load("mainmenuwithbuttons.jpg")
	splash001 = True
	while splash001:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()
					if event.type ==pygame.KEYDOWN:	
						if event.key == pygame.K_z:
							pygame.mixer.Sound.play(select_sound) 
							screen.blit(mm, (0, 0))
							pygame.display.flip()
							main()
							splash001 = False
				screen.blit(splash01, (0, 0))
				pygame.display.flip()
				pygame.time.wait(200)
				screen.blit(splash02, (0, 0))
				pygame.display.flip()
				pygame.time.wait(200)

def main():
  screen.blit(mm, (0, 0))
  pygame.display.flip()
  #MenuScreen Loop
  intro = True
  while intro:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_c: # Play Classic Game Mode (1)
          select_sound.play()
          print("it's c!")
          gameModeSwitch(1) 
        if event.key == pygame.K_v: # Play Timed Game Mode (2)
          select_sound.play()
          print("it's v!")
          gameModeSwitch(2) 
        if event.key == pygame.K_p: # Play Fire Game Mode (3)
          select_sound.play()
          print("it's p!")
          gameModeSwitch(3)
        if event.key == pygame.K_1: # Play Skillz Game Mode (4)
          select_sound.play()
          print("it's 1!")
          gameModeSwitch(4)
        if event.key == pygame.K_w: # End Game
          select_sound.play()
          print("it's w")


def classicMode():

  """
  1. Give player X balls
  2. Detect scoring
  3. End game when X balls are used (Key Presses)
  """
  
  """
  Scoring/Key Guide:
  K_a = 10
  K_s = 20
  K_d = 30
  K_f = 40
  K_g = 50
  K_1 = 100
  K_j = 100
  K_p = 0

  K_x = exit game
  """

  # Music
  musicSwitch(3)

  # init game variables
  gameExit = False
  ballCount = 9
  score = 0

  # Game screen setup
  bg = pygame.image.load("background.jpg") 


  while not gameExit:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a and isKeyCooldown(event.key):
          score += 10
          ballCount -= 1
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_s and isKeyCooldown(event.key):
          score += 20
          ballCount -= 1
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_d and isKeyCooldown(event.key):
          score += 30
          ballCount -= 1
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_f and isKeyCooldown(event.key):
          score += 40
          ballCount -= 1
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_g and isKeyCooldown(event.key):
          score += 50
          ballCount -= 1
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_1 and isKeyCooldown(event.key):
          score += 100
          ballCount -= 1
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_j and isKeyCooldown(event.key):
          score += 100
          ballCount -= 1
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_x:
          gameExit = True
          #yousure() NEEDS EDIT --- !!!!!
        if ballCount == 0:
          gameOverScreen(score, 1)

    screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
    screen2 = pygame.display.set_mode((800,480), pygame.NOFRAME) 
    label = myfont.render(str(score), 1, black) #for the scoring
    label2 = ballsfont.render(str(ballCount), 1, green) #for the balls

    screen.blit(bg,(0,0))
    screen2.set_alpha(15)
    pygame.draw.rect(screen2, black, [700,360,90,90]) 
    screen.blit(label, (45,20)) #put the score text on the screen
    screen.blit(label2, (722,345)) #put the ballcount text on the screen

    pygame.display.update()

def timedMode():
  # Music
  musicSwitch(8)
  
  start = time.time()
  end = time.time()
  score = 0
  warningTime = 5
  timeLimit = 20 # timeLimit in seconds
  while end - start < timeLimit:
    currentTimeLeft = timeLimit - int(round(end-start))
    end = time.time()

    screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
    screen2 = pygame.display.set_mode((800,480), pygame.NOFRAME) 
    bg = pygame.image.load("background.jpg") 
 

    label = myfont.render(str(score), 1, black) #for the scoring
    if (currentTimeLeft <= warningTime):
      label2 = timeFont.render(str(currentTimeLeft), 1, red)
    else:
      label2 = timeFont.render(str(currentTimeLeft), 1, green)

    screen.blit(bg,(0,0))
    #screen2.set_alpha(15)
    pygame.draw.rect(screen2, black, [640,300,120,90]) 
    screen.blit(label, (45,10)) #put the score text on the screen
    screen.blit(label2, (650,300)) #put the ballcount text on the screen

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a and isKeyCooldown(event.key):
          score += 10
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_s and isKeyCooldown(event.key):
          score += 20
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_d and isKeyCooldown(event.key): 
          score += 30
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_f and isKeyCooldown(event.key):
          score += 40
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_g and isKeyCooldown(event.key):
          score += 50
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_1 and isKeyCooldown(event.key):
          score += 100
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_j and isKeyCooldown(event.key):
          score += 100
          pygame.mixer.Sound.play(point_sound)
        if event.key == pygame.K_x :
          pygame.quit() #cleanup
    pygame.display.update()		
  print(int(round(end - start)))
  
  gameOverScreen(score, 2)

def fireMode():
  # Music
  musicSwitch(9)
  
  # init game variables
  score = 0
  balls = 9
  firehole = randint(1, 7)

  gameExit = False

  # Game screen setup
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  screen2 = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  bg = pygame.image.load("skillzbackground.jpg") 
  myfont = pygame.font.Font(fontName, 230) #Large font for score
  ballsfont = pygame.font.Font(fontName, 118) #Small font for ball count
  screen.blit(bg,(0,0))
  

  while not gameExit:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a and isKeyCooldown(event.key):  
          if firehole == 1:
            score += 1
            balls -= 1
            pygame.mixer.Sound.play(point_sound)
          else:
            balls -= 1	 
            pygame.mixer.Sound.play(wrongHole_sound)
        if event.key == pygame.K_s and isKeyCooldown(event.key):
          if firehole == 2:
            score += 1
            balls -= 1
            pygame.mixer.Sound.play(point_sound)	
          else:
            balls -= 1
            pygame.mixer.Sound.play(wrongHole_sound)
        if event.key == pygame.K_d and isKeyCooldown(event.key):
          if firehole == 3:
            score += 1
            balls -= 1
            pygame.mixer.Sound.play(point_sound)	
          else:
            balls -= 1
            pygame.mixer.Sound.play(wrongHole_sound)
        if event.key == pygame.K_f and isKeyCooldown(event.key):
          if firehole == 4:
            score += 1
            balls -= 1
            pygame.mixer.Sound.play(point_sound)
          else:
            balls -= 1
            pygame.mixer.Sound.play(wrongHole_sound)
        if event.key == pygame.K_g and isKeyCooldown(event.key):
          if firehole == 5:
            score += 1
            balls -= 1
            pygame.mixer.Sound.play(point_sound)
          else:
            balls -= 1
            pygame.mixer.Sound.play(wrongHole_sound)
        if event.key == pygame.K_j and isKeyCooldown(event.key):
          if firehole == 6:
            score += 1
            balls -= 1
            pygame.mixer.Sound.play(point_sound)
          else:
            balls -= 1
            pygame.mixer.Sound.play(wrongHole_sound)
        if event.key == pygame.K_l and isKeyCooldown(event.key):
          if firehole == 7:
            score += 1
            balls -= 1
            pygame.mixer.Sound.play(point_sound)
          else:
            balls -= 1
            pygame.mixer.Sound.play(wrongHole_sound)
        if event.key == pygame.K_x:
          gameExit = True	
        if balls == 0:
          gameExit = True
          gameOverScreen(score, 3)

    # Game Screen Updates
    label = myfont.render(str(score), 1, black) #for the scoring
    label2 = ballsfont.render(str(balls), 1, black) #for the balls
    screen.blit(bg,(0,0)) # Displays background image
    pygame.draw.rect(screen2, sienna, [700,300,90,90]) 
    screen.blit(label, (670,10)) #put the score text on the screen
    screen.blit(label2, (715,282)) #put the ballcount text on the screen
				
    #Displays the image on the hole that was randomly selected		
    if firehole == 1:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,280))
    if firehole == 2:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,220))
    if firehole == 3:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,145))
    if firehole == 4:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,60))
    if firehole == 5:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,5))
    if firehole == 6:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (300,5))
    if firehole == 7:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (500,5))	

    pygame.display.update()

def skillMode(score=0, level=1):
  # Music
  musicSwitch(2)

  # Game variables
  holeList = ["1", "2", "3", "4", "5", "6", "7"] 
  balls = 9
  gameExit = False
  bonusScore = 500
  # Game screen setup
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 

  bg = pygame.image.load("skillzbackground.jpg") 
  bg = pygame.transform.scale(bg, (800, 480))

  myfont = pygame.font.Font(fontName, 120) #Large font for score
  levelFont = pygame.font.Font(fontName, 70) 
  ballslabelFont = pygame.font.Font(fontName, 60) #Small font for ball count
  ballsFont = pygame.font.Font(fontName, 80) #Small font for ball count
  screen.blit(bg,(0,0))

  ballslabelFont.set_underline(True)


  pygame.draw.circle(screen, red, (500,500), 4)

  while not gameExit:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a and "1" in holeList and isKeyCooldown(event.key):
            score += 10
            balls -= 1
            holeList.remove("1")
            pygame.mixer.Sound.play(point_sound)	 
        elif event.key == pygame.K_s and "2" in holeList and isKeyCooldown(event.key):
          score += 20
          balls -= 1
          holeList.remove("2")
          pygame.mixer.Sound.play(point_sound)	
        elif event.key == pygame.K_d and "3" in holeList and isKeyCooldown(event.key):
          score += 30
          balls -= 1
          holeList.remove("3")
          pygame.mixer.Sound.play(point_sound)	
        elif event.key == pygame.K_f and "4" in holeList and isKeyCooldown(event.key):
          score += 40
          balls -= 1
          holeList.remove("4")
          pygame.mixer.Sound.play(point_sound)
        elif event.key == pygame.K_g and "5" in holeList and isKeyCooldown(event.key):
          score += 50
          balls -= 1
          holeList.remove("5")
          pygame.mixer.Sound.play(point_sound)
        elif event.key == pygame.K_l and "6" in holeList and isKeyCooldown(event.key):
          score += 100
          balls -= 1
          holeList.remove("6")
          pygame.mixer.Sound.play(point_sound)
        elif event.key == pygame.K_j and "7" in holeList and isKeyCooldown(event.key):
          score += 100
          balls -= 1
          holeList.remove("7")
          pygame.mixer.Sound.play(point_sound)
        else:
          balls -= 1
          pygame.mixer.Sound.play(wrongHole_sound)
        if event.key == pygame.K_x:
          gameOverScreen(score, 4)	
        if (balls == 0 and len(holeList) == 0 ) or len(holeList) == 0:
          level += 1
          nextLevel_sound.play()
          skillMode(score + bonusScore, level)
        elif (balls == 0):
          gameOverScreen(score, 4)
    Levellabel = levelFont.render("Level " + str(level), 1, blue) #for the Level
    label = myfont.render(str(score), 1, black) #for the scoring
    label2 = ballslabelFont.render("Shots", 1, black) #for the balls

    ballsNumLabel = ballsFont.render(str(balls), 1, blue)
    screen.blit(bg,(0,0)) # Displays background image
    screen.blit(label, (580,10)) #put the score text on the screen
    screen.blit(label2, (620,300)) #put the 'shots:' text on the screen
    screen.blit(ballsNumLabel, (660,350)) #put the shot count left (int) on the screen
    screen.blit(Levellabel, (10,20)) #put the level text on the screen

    # Circles
    if "2" in holeList:
      pygame.draw.ellipse(screen, red, (293, 70, 245, 230), 10)
    else:
      pygame.draw.ellipse(screen, green, (293, 70, 245, 230), 10)
    if "3" in holeList:
      pygame.draw.ellipse(screen, red, (367, 145,  91, 90), 10)
    else:
      pygame.draw.ellipse(screen, green, (367, 145,  91, 90), 10)
    if "4" in holeList:
      pygame.draw.ellipse(screen, red, (372, 75,  88, 70), 10)
    else:
      pygame.draw.ellipse(screen, green, (372, 75,  88, 70), 10)
    if "5" in holeList:
      pygame.draw.ellipse(screen, red, (386, 10,  72, 61), 10)
    else:
      pygame.draw.ellipse(screen, green, (386, 10,  72, 61), 10)
    if "6" in holeList:
      pygame.draw.ellipse(screen, red, (275, 5,  65, 75), 10)
    else:
     pygame.draw.ellipse(screen, green, (275, 5,  65, 75), 10)
    if "7" in holeList:
      pygame.draw.ellipse(screen, red, (506, 5,  65, 75), 10)
    else:
      pygame.draw.ellipse(screen, green, (506, 5,  65, 75), 10)
    if "1" in holeList:
      pygame.draw.ellipse(screen, red, (372, 360,  70, 70), 15)
    else:
      pygame.draw.ellipse(screen, green, (372, 360,  70, 70), 15)


    """
        if firehole == 1:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,280))
    if firehole == 2:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,220))
    if firehole == 3:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,145))
    if firehole == 4:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,60))
    if firehole == 5:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (400,5))
    if firehole == 6:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (300,5))
    if firehole == 7:
      mask = pygame.image.load("fsocietymask.jpg") 
      screen.blit(mask, (500,5))	

    """
    pygame.display.update()


def gameOverScreen(endScore, gameModeNumber):
  
  # Music
  musicSwitch(10)
    
  screen.blit(gameover_image, (0,0)) # Display "Game Over"
  pygame.display.flip() # flip (update) Display

  label = scoreFont.render(str(endScore), 1, black) # Score label

  screen.blit(label, (380, 100)) # Create image
  pygame.display.update() # Update Display

  showingEndScreen = True
  while showingEndScreen:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_z: # Play again
          pygame.mixer.Sound.play(select_sound) 
          gameModeSwitch(gameModeNumber)
        if event.key == pygame.K_x: # Return to main menu
          pygame.mixer.Sound.play(select_sound) 
          splash1()

def setCurrentKeyTime(KeyPressed):
  CurrentTime[KeyPressed] = getCurrentTime() # Update pastTimeOfKeyPressed to currentRunTime

def getCurrentKeyTime(KeyPressed):
  return CurrentTime[KeyPressed] # 'K_z' : ' pastTimeOfKeyPressed'

def getCurrentTime():
  return time.process_time() # currentRunTime

def isKeyCooldown(KeyPressed): # Return bool based on cooldown status
  prefix = "K_"
  KeyPressed = str(pygame.key.name(KeyPressed)) # Actual key parsed will be 'a'
  KeyPressed = prefix + KeyPressed # Adds 'K_' to 'a' to become 'K_a' as per keyname constants
  timeElapsed = getCurrentTime() - getCurrentKeyTime(KeyPressed) # Time elapsed = currentRunTime - pastTimeOfKeyPressed

  if timeElapsed >= cooldown:
    setCurrentKeyTime(KeyPressed) # Set key time to new time 
    return True
  else:
    return False

def gameModeSwitch(gameModeNumber):
  if gameModeNumber == 1: # Play Classic Mode
    classicMode()
  if gameModeNumber == 2: # Play Timed Mode
    timedMode()
  if gameModeNumber == 3: # Play Fire Mode
    fireMode()
  if gameModeNumber == 4: # Play Skill Mode
    skillMode()

def musicSwitch(songNumber):
  if songNumber == 1:
    pygame.mixer.music.load("hackthepolice.mp3")
    pygame.mixer.music.play(-1, 2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 2:
    pygame.mixer.music.load("blueprints.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 3:
    pygame.mixer.music.load("consumatesurvivor.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 4:
    pygame.mixer.music.load("darlenesgun.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 5:
    pygame.mixer.music.load("fucksociety.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 6:
    pygame.mixer.music.load("h4ndshake.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 7:
    pygame.mixer.music.load("illusionofchoice.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 8:
    pygame.mixer.music.load("pyth0n.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 9:
    pygame.mixer.music.load("trustyourself.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 10:
    pygame.mixer.music.load("waltznumber2.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
  if songNumber == 11:
    pygame.mixer.music.load("whatsyouraskintro.mp3")
    pygame.mixer.music.play(-1,2)
    pygame.mixer.music.set_volume(.5)
splash1()
