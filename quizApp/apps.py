from django.apps import AppConfig


class QuizappConfig(AppConfig):
    name = 'quizApp'

    def ready(self):
        import quizApp.signals
