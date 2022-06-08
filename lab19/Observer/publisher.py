class Publisher:
    def __init__(self, file_path):
        self.listeners = []
        self.file_path = file_path
        self.file_obj = open(self.file_path, "r")

    def subscribe(self, listener):
        self.listeners.append(listener)

    def notify(self, line):
        for listener in self.listeners:
            listener.update(line)

    def update(self):
        assert self.file_obj is not None
        line = self.file_obj.readline().strip()
        if line:
            self.notify(line)
            return True
        return False
