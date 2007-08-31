# -*- coding: utf8 -*-

import sys
import pygame
from pygame.locals import *
import Tools

class Gui:
  '''
  Screen graphics and sounds are embedded in this class
  '''
  def __init__(self): 
    resolution=width,height=1024,768
    self.player_pos=[190,404,620,835]

    pygame.init()
    pygame.mouse.set_visible(0)
    self.screen=pygame.display.set_mode(resolution,pygame.FULLSCREEN)
#    self.screen=pygame.display.set_mode(resolution)
  
    self.snd_intro=Tools.load_sound("romans.wav")
    self.snd_question=Tools.load_sound("left.wav")
    self.snd_rightanswer=Tools.load_sound("kling.wav")
    self.snd_wronganswer=Tools.load_sound("click.wav")
    self.snd_click=Tools.load_sound("apert.wav")
    self.snd_applause=Tools.load_sound("applause.wav")

    self.fnt_title = pygame.font.Font(None, 80)
    self.fnt_clock = pygame.font.Font(None, 160)
    self.fnt_question = pygame.font.Font(None, 35)
    self.fnt_answer = pygame.font.Font(None, 40)
    self.fnt_score = pygame.font.Font(None, 32)

    self.color1=(250,50,50)
    self.color2=(50,250,250)
    self.color3=(250,255,5)

    self.background,bg_rect = Tools.load_image("pantalla_01b.jpg")
    self.endscreen,bg_rect = Tools.load_image("boceto_end.png")
    self.icon_ok,icon_ok_rect = Tools.load_image("ok.png",-1)
    self.icon_wrong,icon_ok_wrong = Tools.load_image("wrong.png",-1)
    self.scoreboard_area=bg_rect
    self.scoreboard_area.top=700
    
    self.clockpos=(815,75)
       
    if pygame.joystick.get_count() > 0:
       print "Joystick detectado!";
       self.js=pygame.joystick.Joystick(0)
       self.js.init()
       print self.js.get_name()," axis:",self.js.get_numaxes()," buttons:",self.js.get_numbuttons()       
       
# SHOW INTRO
  def show_intro(self):

    self.screen.blit(self.background, (0, 0))
   
    text = self.fnt_title.render(unicode("¡ ATENCIÓN !!!",'utf-8'), 1, (225,180, 10))

    self.screen.blit(text, (90,220))
    pygame.display.flip()
    self.snd_intro.play()
    pygame.time.delay(3000)


# SHOW QUESTION
  def show_question(self,q): 

    self.screen.blit(self.background,(0,0),(0,0,1024,700))
    pygame.display.flip()

    text = self.fnt_question.render(q.question, 1, (0,0,0))
    textpos = text.get_rect(left=90,top=230)
    self.screen.blit(text, textpos)
    text = self.fnt_answer.render(q.answer1, 1, self.color1)
    textpos.left+=85
    textpos.top+=120
    self.screen.blit(text, textpos)
    text = self.fnt_answer.render(q.answer2, 1, self.color2)
    textpos.top+=78
    self.screen.blit(text, textpos)
    text = self.fnt_answer.render(q.answer3, 1, self.color3)
    textpos.top+=78
    self.screen.blit(text, textpos)

    pygame.display.flip()
    self.snd_question.play()
 
# WAIT FOR ANSWERS 
  def wait_for_answers(self,player):
    pygame.event.clear()
    for seconds in range(5):
       text = self.fnt_clock.render(str(seconds), 1, (0,0,0))
       clockarea=text.get_rect()
       self.screen.blit(text, self.clockpos)
       pygame.display.flip()

       starttick=pygame.time.get_ticks()
       elapsedtime=0

       while elapsedtime < 1:    
         event=pygame.event.poll()
         if event.type == QUIT:
              sys.exit(0)

# KEYS SECTION
         if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
               sys.exit(0)
            if event.key == K_1:
               if player[0].set_answer(1):
                 self.press_button(self.color1,self.player_pos[0])
            if event.key == K_q:
               if player[0].set_answer(2):
                 self.press_button(self.color2,self.player_pos[0])
            if event.key == K_a:
               if player[0].set_answer(3):
                 self.press_button(self.color3,self.player_pos[0])
            if event.key == K_x:
               if player[1].set_answer(1):
                 self.press_button(self.color1,self.player_pos[1])
            if event.key == K_c:
               if player[1].set_answer(2):
                 self.press_button(self.color2,self.player_pos[1])
            if event.key == K_v:
               if player[1].set_answer(3):
                 self.press_button(self.color3,self.player_pos[1])
            if event.key == K_n:
               if player[2].set_answer(1):
                 self.press_button(self.color1,self.player_pos[2])
            if event.key == K_m:
               if player[2].set_answer(2):
                 self.press_button(self.color2,self.player_pos[2])
            if event.key == K_COMMA:
               if player[2].set_answer(3):
                 self.press_button(self.color3,self.player_pos[2])
            if event.key == K_l:
               if player[3].set_answer(1):
                 self.press_button(self.color1,self.player_pos[3])
            if event.key == K_p:
               if player[3].set_answer(2):
                 self.press_button(self.color2,self.player_pos[3])
            if event.key == K_QUOTE:
               if player[3].set_answer(3):
                 self.press_button(self.color3,self.player_pos[3])

# JOYSTICK (SMASHED KEYPAD) SECTION            
         if self.js.get_button(0):
               if player[0].set_answer(3):
                 self.press_button(self.color3,self.player_pos[0])
         if self.js.get_button(3):
               if player[0].set_answer(2):
                 self.press_button(self.color2,self.player_pos[0])
         if self.js.get_button(1):
               if player[0].set_answer(1):
                 self.press_button(self.color1,self.player_pos[0])
                 
         if self.js.get_button(2):
               if player[1].set_answer(1):
                 self.press_button(self.color1,self.player_pos[1])
         if self.js.get_button(5):
               if player[1].set_answer(2):
                 self.press_button(self.color2,self.player_pos[1])
         if self.js.get_button(7):
               if player[1].set_answer(3):
                 self.press_button(self.color3,self.player_pos[1])

         if self.js.get_button(6):
               if player[2].set_answer(1):
                 self.press_button(self.color1,self.player_pos[2])
         if self.js.get_axis(0) > 0: 
               if player[2].set_answer(2):
                 self.press_button(self.color2,self.player_pos[2])
         if self.js.get_button(4):
               if player[2].set_answer(3):
                 self.press_button(self.color3,self.player_pos[2])
               
         if self.js.get_axis(1) > 0: 
               if player[3].set_answer(1):
                 self.press_button(self.color1,self.player_pos[3])
         if self.js.get_axis(0) < 0: 
               if player[3].set_answer(2):
                 self.press_button(self.color2,self.player_pos[3])
         if self.js.get_axis(1) < 0: 
               if player[3].set_answer(3):
                 self.press_button(self.color3,self.player_pos[3])

            
         elapsedtime=(pygame.time.get_ticks() - starttick ) / 1000

       clockarea=clockarea.move(self.clockpos)
       self.screen.blit(self.background,self.clockpos,clockarea)
       pygame.display.flip()


# PRESS BUTTON  	
  def press_button(self,color,x):
    rect=pygame.draw.circle(self.screen, color, (x,666), 36, 0)
    pygame.display.flip()
    self.snd_click.play()
   
   
# SHOW RESULT   
  def show_result(self,player,questions):

    self.screen.blit(self.background, (0,700),self.scoreboard_area)
    pygame.display.flip()

    for i in range(4):
# one point for a right answer
      if player[i].answer == questions.rightanswer:
        player[i].score+=1
        self.snd_rightanswer.play()
        self.screen.blit(self.icon_ok,(self.player_pos[i]-25,625))
# one negative point for a wrong answer
      else:
        if player[i].answer != 0:
          player[i].score-=1
        self.screen.blit(self.icon_wrong,(self.player_pos[i]-25,625))
        self.snd_wronganswer.play()
# and zero points for no answer
      text = self.fnt_score.render(str(player[i].score), 1, (200, 200, 250))
      self.screen.blit(text, (self.player_pos[i]+56,658))
      pygame.display.flip()
      pygame.time.delay(1000)
      
    pygame.time.delay(5000)
        
# SHOW_END
  def show_end(self,player):
    self.screen.blit(self.endscreen, (0, 0))
   
    text = self.fnt_title.render(unicode("PUNTUACION",'utf-8'), 1, (250,200, 0))
    self.screen.blit(text, (300,200))

    bestscore=-9999
    for p in player:
      if p.score > bestscore:
         bestscore=p.score

    n=1
    for p in player:
      line="Jugador "+str(n)+": "+str(p.score)+" puntos"
      if p.score == bestscore:
         text = self.fnt_question.render(unicode(line+" ¡Has vencido!",'utf-8'), 1, self.color1)
      else:   
         text = self.fnt_question.render(unicode(line,'utf-8'), 1, self.color2)
          
      self.screen.blit(text, (300,250+(n*80)))
      n=n+1
      
    pygame.display.flip()
    self.snd_applause.play()

    pygame.event.clear()
    while 1:
      event=pygame.event.wait()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          sys.exit(0)
        if event.key == K_SPACE: 
          break               
   
   
