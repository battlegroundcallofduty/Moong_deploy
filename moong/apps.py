import os
import sys

from django.apps import AppConfig


class MoongConfig(AppConfig):
    name = 'moong'

    def ready(self):
        # migrate, collectstatic 등 관리 명령 실행 시에는 스케줄러 불필요
        if any(cmd in sys.argv for cmd in ['migrate', 'makemigrations', 'collectstatic', 'import_locations']):
            return

        # 개발 서버(runserver)에서는 자동 리로더가 ready()를 두 번 호출하므로 한 번만 실행
        if 'runserver' in sys.argv and os.environ.get('RUN_MAIN') != 'true':
            return

        from moong import scheduler
        scheduler.start()
