from key_map import KEY_MAP


class ControlBoard(object):
    __slots__ = ('names', 'cmds','execute_func')


    def __init__(self, execute_function):
        self.names = []
        self.cmds = {}
        self.execute_func = execute_function


    def add_command(self, name, command):
        if name not in self.names:
            self.names.append(name)
            self.cmds[name] = bytearray(command)


    def remove_command(self, name):
        if name in self.names:
            self.names.remove(name)
            del self.commands[name]


    def execute_command(self, name):
        if name in self.names:
            self.execute_func(self.cmds[name])
