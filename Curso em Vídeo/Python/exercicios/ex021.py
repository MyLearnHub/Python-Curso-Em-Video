import pygame

pygame.init()
pygame.mixer.music.load("output.wav")
pygame.mixer.music.play()
pygame.event.wait()  # Desnecessário para execução

input("Pressione Enter para parar a reprodução...")
pygame.mixer.music.stop()
pygame.mixer.quit()
