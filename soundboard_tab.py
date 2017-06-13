from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

from functools import partial

from soundboard import SoundBoard


class SoundBoardTab(TabbedPanelHeader):
    __slots__ = ('mdl', 'gl', 'nav_btn', 'snd_btn', 'pg')


    def __init__(self, sound_model):
        super().__init__(text='Sound')
        self.mdl = sound_model
        self.pg = 0

        self.content = GridLayout(cols=2)
        self.nav_btn = [
            Button(text='<-', size_hint_y=None, height=80),
            Button(text='->', size_hint_y=None, height=80)
        ]
        self.nav_btn[0].bind(on_press=lambda a:self.__nav_button(-1))
        self.nav_btn[1].bind(on_press=lambda a:self.__nav_button(1))


        self.snd_btn = [Button() for _ in range(4)]

        for i in self.nav_btn:
            self.content.add_widget(i)

        for i in self.snd_btn:
            self.content.add_widget(i)

        self.update()


    def update(self):
        for i in range(self.pg*4, (self.pg+1)*4):
            self.snd_btn[i%4].text = self.mdl.sounds[i]
            # fn = self.mdl.get_sound(self.mdl.sounds[i])
            # temp = SoundLoader.load(fn)
            self.snd_btn[i%4].on_press = partial(self.mdl.play_sound, self.mdl.sounds[i])



    def __nav_button(self, dir):
        if dir == -1:
            if self.pg > 0:
                self.pg -= 1
        elif dir == 1:
            if self.pg < (len(self.mdl.sounds)//4)-1:
                self.pg += 1
        self.update()


    def __sound_button(self, sound):
        print(sound)
        print()
