import logging

from OBP_security_pillar.s3.s3_bucket_logging_enabled import s3_bucket_logging_enabled
from OBP_security_pillar.s3.s3_bucket_versioning_enabled import s3_bucket_versioning_enabled

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def s3_compliance(self) -> list:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside s3 :: s3_compliance()")

    response = [
        s3_bucket_versioning_enabled(self),
        s3_bucket_logging_enabled(self)
    ]

    return response
