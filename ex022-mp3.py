import pygame

pygame.init()

pygame.mixer.music.load('xistudo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
