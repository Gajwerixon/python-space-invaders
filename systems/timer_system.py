class TimerSystem:
    """Timer system class"""
    def __init__(self, cooldown):
        self.duration = cooldown
        self.time_left = cooldown
        self.active = False

    def set_duration(self, new_duration):
        """Set new duration"""
        self.duration = new_duration

    def start(self):
        """Start timer"""
        self.active = True
        self.time_left = self.duration

    def update(self, dt):
        """Update timer base on dt"""
        if self.active:
            self.time_left -= dt
            if self.time_left <= 0:
                self.active = False
