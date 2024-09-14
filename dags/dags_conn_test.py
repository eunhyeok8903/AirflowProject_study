from airflow import DAG
import pendulum
import datetime
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id="dags_conn_test",  # 웹 콘솔 DAGS탭에서 보이는 값
        schedule= None,
        start_date=pendulum.datetime(2024, 9, 14, tz="Asia/Seoul"),
        # 언제부터 dag이 시작될지 설정. tz(=timezone)이 UTC말고 Asia/Seoul로 맞춰주기
        catchup=False,  # 누락분 작업 여부, 단 True일 경우 1일 기준이 아닌 전체 한번에 작업이므로 True시 확인 필요
) as dags:

    t1 = EmptyOperator(
        task_id = "t1"
    )

    t2 = EmptyOperator(
        task_id = "t2"
    )

    t3 = EmptyOperator(
        task_id = "t3"
    )

    t4 = EmptyOperator(
        task_id = "t4"
    )

    t5 = EmptyOperator(
        task_id = "t5"
    )

    t6 = EmptyOperator(
        task_id = "t6"
    )

    t7 = EmptyOperator(
        task_id = "t7"
    )

    t8 = EmptyOperator(
        task_id = "8"
    )

    t1 >> [t2,t3] >>t4
    t5 >> t4
    [t4, t7] >> t6 >> t8