from boto3 import session
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


__author__ = 'Dheeraj Banodha'
__version__ = '0.0.1'


class aws_client:
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self.session = session.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    from .rds import rds_compliance
    from .s3 import s3_compliance

    # consolidate compliance.py details
    def get_compliance(self) -> list:
        """
        :return list: consolidated list  of compliance.py checks
        """
        logger.info(" ---Inside get_compliance()")
        compliance = []
        compliance.extend(self.rds_compliance())
        compliance.extend(self.s3_compliance())

        return compliance
