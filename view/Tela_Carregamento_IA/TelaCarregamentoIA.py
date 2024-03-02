from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
class TelaCarregamentoIAView(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.setup_progressbar)

    def setup_progressbar(self, dt):
        self.progress = 0
        self.progress_bar = self.ids.progress_bar
        self.progress_bar.max = 100
        self.progress_bar.value = 0
        self.loading_event = Clock.schedule_interval(self.update_progress, 0.02)

    def update_progress(self, dt):
        self.progress += 1
        self.progress_bar.value = self.progress
        if self.progress >= 100:
            self.loading_event.cancel()
            self.manager.current = 's6'
    pass