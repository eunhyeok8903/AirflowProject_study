from airflow.operators.python import PythonOperator
from airflow import DAG
import pendulum
import datetime
import random

with DAG(
        dag_id="dags_python_operator",  # 웹 콘솔 DAGS탭에서 보이는 값
        schedule= "0 6 * * *",
        start_date=pendulum.datetime(2024, 10, 12, tz="Asia/Seoul"),
        # 언제부터 dag이 시작될지 설정. tz(=timezone)이 UTC말고 Asia/Seoul로 맞춰주기
        catchup=False  # 누락분 작업 여부, 단 True일 경우 1일 기준이 아닌 전체 한번에 작업이므로 True시 확인 필요
) as dag:
    def test_function():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rd_int = random.randint(0,len(fruit))
        print(fruit[rd_int])

    py_t1 = PythonOperator(
        task_id  = 'py_t1',
        python_callable= test_function
    )