import pygame
from pygame.mixer import music

class SoundEffect(pygame.mixer.Sound):
    def __init__(self, sound_file_path, volume=100):
        super().__init__(sound_file_path)
        self.volume = volume / 100
        self.set_volume(volume)
    
    def play(self):
         pygame.mixer.Sound.play(self)

class Music:
    def __init__(self, music_file_path, volume, loop=True):
        self.file_path = music_file_path
        self.loop = loop
        pygame.mixer.music.set_volume(volume / 100)


    def play(self):
        pygame.mixer.music.load(self.file_path)
        if self.loop:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play(-1)
    
    def pause(self):
        pygame.mixer.music.pause()
    
    def stop(self, unload=True):
        pygame.mixer.music.stop()

        if unload:
            pygame.mixer.music.unload()


def load_music(music_path, volume=100, loop=True) -> Music:
    return Music(music_path, volume)

def load_sound(sound_path, volume=100, ) -> SoundEffect:
    return SoundEffect(sound_path, volume)