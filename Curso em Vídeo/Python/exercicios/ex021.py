import pygame

audio_file = "ex021.mp3"
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()

input("Pressione Enter para parar a reprodução...")
pygame.mixer.music.stop()
pygame.mixer.quit()
