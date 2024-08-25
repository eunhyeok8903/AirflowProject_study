from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", #웹 콘솔 DAGS탭에서 보이는 값
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), #언제부터 dag이 시작될지 설정. tz(=timezone)이 UTC말고 Asia/Seoul로 맞춰주기
    catchup=False, #누락분 작업 여부, 단 True일 경우 1일 기준이 아닌 전체 한번에 작업이므로 True시 확인 필요
    dagrun_timeout=datetime.timedelta(minutes=60),
    #tags=["example", "example2"], #웹콘솔 DAGS 아래에 태크들이 있고, 검색시 유용
    #params={"example_key": "example_value"}, #Task에 넘겨줄 파라미터 작성
) as dag:

    bash_t1 = BashOperator(
        task_id="bash_t1", #이거도 웹 콘솔에서 보여지는 task id설정, 일반적으로 task 명과 동일하게 준다함
        bash_command="echo Test"
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME"
    )

    bash_t1 >> bash_t2  # 실행 순서 작성