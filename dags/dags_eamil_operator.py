from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
        dag_id="dags_email_operator",  # 웹 콘솔 DAGS탭에서 보이는 값
        schedule= "0 18 * * *",
        start_date=pendulum.datetime(2024, 10, 12, tz="Asia/Seoul"),
        # 언제부터 dag이 시작될지 설정. tz(=timezone)이 UTC말고 Asia/Seoul로 맞춰주기
        catchup=False  # 누락분 작업 여부, 단 True일 경우 1일 기준이 아닌 전체 한번에 작업이므로 True시 확인 필요
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        to = 'uu1995uu@naver.com',
        subject = 'Airflow 이메일 오퍼레이터 테스트', #메일제목
        html_content = 'Airflow 작업이 완료되었습니다'
    )
