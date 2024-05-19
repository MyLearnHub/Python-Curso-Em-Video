import pygame

pygame.init()
pygame.mixer.music.load("../../exercicios/ex021.mp3")
pygame.mixer.music.play()

input("Pressione Enter para parar a reprodução...")
pygame.mixer.music.stop()
pygame.mixer.quit()
