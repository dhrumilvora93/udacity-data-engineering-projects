from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    """
    This Operator would execute the COPY query with the params provide below
    -------------------
    conn_id : str
        connection_id
    s3_src_path : str
        S3 source path for the file to load
    table : str
        target table to load in
    iam_role : str
        iam credentials required to load in redshift
    json_type : str
        type of json to be loaded
    region : str
        region in which the s3 bucket is
    extra_params : str
        extra params for COPY command if any
    """
   
    ui_color = '#358140'

    @apply_defaults
    def __init__(self,
                 s3_src_path='',
                 table='',
                 iam_role='',
                 json_type='',
                 region='',
                 extra_params='',                     
                 conn_id='postgres_default',
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.s3_src_path=s3_src_path
        self.conn_id=conn_id
        self.table=table
        self.iam_role=iam_role
        self.json_type=json_type
        self.region=region
        self.extra_params=extra_params
        
    def execute(self, context):
        copy_query=f"""
        copy {self.table}
        from {self.s3_src_path}
        iam_role {self.iam_role}
        format as JSON '{self.json_type}'
        region '{self.region}'
        {self.extra_params};
        """
        conn=PostgresHook(self.conn_id).get_conn()
        cur=conn.cursor()
        cur.execute(copy_query)
        conn.commit()
        self.log.info('StageToRedshiftOperator Ran Sucessfully')
        





