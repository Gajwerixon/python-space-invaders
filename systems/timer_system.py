class TimerSystem:
    """Timer system class"""
    def __init__(self, cooldown):
        self.duration = cooldown
        self.time_left = cooldown
        self.active = False

    def start(self):
        """Start timer"""
        self.active = True
        self.time_left = self.duration

    def update(self, dt):
        """Update timer"""
        if self.active:
            self.time_left -= dt
            if self.time_left <= 0:
                self.active = False
