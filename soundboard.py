from kivy.core.audio import SoundLoader


class SoundBoard(object):
    __slots__ = ('sounds', 'playing', 'files')


    def __init__(self):
        self.sounds = []
        self.files = {}
        self.playing = None


    def add_sound(self, name, filepath):
        if name not in self.sounds:
            self.sounds.append(name)
            self.files[name] = filepath

    def get_sound(self, name):
        if name in self.files:
            return self.files[name]

    def remove_sound(self, name):
        if name in self.sounds:
            self.sounds[name].unload()
            del self.sounds[name]


    def play_sound(self, name):
        self.stop_sound()
        self.playing = SoundLoader.load(self.files[name])
        self.playing.play()


    def stop_sound(self):
        if self.playing is not None:
            self.playing.stop()
