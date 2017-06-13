from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

from soundboard_tab import SoundBoardTab
from controlboard_tab import ControlBoardTab



class SirBoard(App):
    __slots__ = ('tp', 'sb_tab', 'ct_tab', 'st_tab', 'snd_model', 'ctl_model')


    def __init__(self, snd_model, ctl_model):
        super().__init__()
        self.snd_model = snd_model
        self.ctl_model = ctl_model

        self.__create_tabs()


    def build(self):
        return self.tp


    def __create_tabs(self):
        # Tab 1, the sound board
        self.sb_tab = SoundBoardTab(self.snd_model)

        # Tab 2, the controls
        self.ct_tab = ControlBoardTab(self.ctl_model)


        # Tab 3, settings tab
        self.st_tab = TabbedPanelHeader(text='Settings')


        # Main tabbed panel
        self.tp = TabbedPanel(do_default_tab=False)
        self.tp.add_widget(self.sb_tab)
        self.tp.add_widget(self.ct_tab)
        self.tp.add_widget(self.st_tab)




    def __update_settings_tab(self):
        # scroll view comprised of several sections
        # Each section willbe a cell in the grid layout
        sv = ScrollView()
        gl = GridLayout(cols=1, size_hint_y=None)
        gl.bind(minimum_height=gl.setter('height'))


        # Sounds Settings
        gl.add_widget(Label(text='Sound settings', size_hint_y=None, height=80))
        gl.add_widget(self.__create_settings_section(self.snd_model.sounds.keys()))



        # Controls
        gl.add_widget(Label(text='Controls settings', size_hint_y=None, height=80))
        gl.add_widget(self.__create_settings_section(self.ctl_model.commands.keys()))


        # Pull it all together
        sv.add_widget(gl)
        self.st_tab.content = sv;


    def __create_settings_section(self, data):
        gl = GridLayout(cols=2, size_hint_y=None)
        gl.bind(minimum_height=gl.setter('height'))
        for i in data:
            gl.add_widget(Label(text=i, size_hint_y=None, height=80))
            gl.add_widget(Button(text='Remove '+i, size_hint_y=None, height=80))
        return gl
