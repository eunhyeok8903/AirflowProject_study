from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
        dag_id="dags_bash_test",  # 웹 콘솔 DAGS탭에서 보이는 값
        schedule= "0 18 * * *",
        start_date=pendulum.datetime(2024, 10, 12, tz="Asia/Seoul"),
        # 언제부터 dag이 시작될지 설정. tz(=timezone)이 UTC말고 Asia/Seoul로 맞춰주기
        catchup=False,  # 누락분 작업 여부, 단 True일 경우 1일 기준이 아닌 전체 한번에 작업이므로 True시 확인 필요
) as dags:

    t1_test1 = BashOperator(
        task_id = "t1_test1",
        bash_command="/opt/airflow/plugins/shell/bash_test.sh test1" #실행주체는 워커컨테이너라 경로 이렇게 지정해주기
    )

    t1_test2 = BashOperator(
        task_id = "t1_test2",
        bash_command="/opt/airflow/plugins/shell/bash_test.sh test2" #실행주체는 워커컨테이너라 경로 이렇게 지정해주기
    )

    t1_test3 = BashOperator(
        task_id = "t1_test2",
        bash_command="/opt/airflow/plugins/shell/bash_test.sh test3" #실행주체는 워커컨테이너라 경로 이렇게 지정해주기
    )


    t1_test1 >> t1_test2 >> t1_test3