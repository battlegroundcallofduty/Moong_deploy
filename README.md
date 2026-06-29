# Moong - 번개모임 SNS (개인 배포 버전)

사용자가 즉시 모임을 생성하고 참여할 수 있는 번개 만남 중심 SNS 플랫폼.  
5인 팀이 함께 개발한 프로젝트를 개인적으로 AWS EC2에 배포한 레포지토리입니다.

[원본 레포](https://github.com/battlegroundcallofduty/Moong_pro)

---

## 배포 환경

| 항목 | 내용 |
|------|------|
| 서버 | AWS EC2 (Ubuntu, 프리티어) |
| 웹 서버 | Nginx |
| WAS | Gunicorn |
| 프레임워크 | Django 6.0.1 |
| DB | SQLite |
| 정적 파일 | WhiteNoise |

요청 흐름: 클라이언트 → Nginx → Gunicorn → Django

---

## 주요 기능

| 기능 | 설명 |
|------|------|
| 회원 관리 | 회원가입, 로그인/로그아웃, 프로필 수정 |
| 피드 | 메인 피드 목록, 당일 만료 게시글 자동 필터링 |
| 모임 모집글 | 임시저장 → AI 해시태그 자동 생성 → 게시 단계별 플로우 |
| 해시태그 검색 | 해시태그 클릭/키워드 검색 |
| 모임 참여 관리 | 참여 신청/취소, 모임장 승인/거절, 대기 순번 자동 배정 |
| 댓글 | 작성/삭제, 모임장 공지 댓글 표시 |
| 마이페이지 | 생성/참여/종료 모임 이력 조회 |
| 지도 | Kakao Map API 기반 모임 장소 표시 |
| 스케줄러 | APScheduler로 매일 00:05 만료 게시글 자동 처리 |

---

## 배포를 위해 추가/수정한 것

- `settings.py` — SECRET_KEY, DEBUG, ALLOWED_HOSTS를 환경변수로 분리 (`django-environ`)
- `requirements.txt` — gunicorn, whitenoise, django-environ 추가
- `apps.py` — gunicorn 환경에서도 APScheduler 작동하도록 수정
- `Procfile` — gunicorn 실행 명령 정의
- migrations 파일 git 추적 활성화
