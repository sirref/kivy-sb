from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from functools import partial

class ControlBoardTab(TabbedPanelHeader):
    __slots__ = ('mdl', 'gl', 'btn')

    def __init__(self, command_model):
        super().__init__(text='Controls')
        self.mdl = command_model
        self.btn = []
        self.content = ScrollView()

        self.gl = GridLayout(cols=4, size_hint_y=None)
        self.gl.bind(minimum_height=self.gl.setter('height'))

        for i, cmd in enumerate(self.mdl.names):
            self.btn.append(Button(text=cmd, size_hint_y=None))
            self.btn[i].on_press = partial(self.mdl.execute_command, cmd)

        for i in self.btn:
            self.gl.add_widget(i);

        self.content.add_widget(self.gl)
