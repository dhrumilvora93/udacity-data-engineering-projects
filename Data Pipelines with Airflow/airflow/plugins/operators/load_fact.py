from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):
    """
    This Operator would execute the given query
    -------------------
    conn_id : str
        connection_id
    query : str 
        query to execute
    """
    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 conn_id='postgres_default',
                 query='',
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.conn_id=conn_id
        self.query=query

    def execute(self, context):
        conn=PostgresHook(self.conn_id).get_conn()
        cur=conn.cursor()
        cur.execute(self.query)
        conn.commit()
        self.log.info('LoadFactOperator Ran Sucessfully')
