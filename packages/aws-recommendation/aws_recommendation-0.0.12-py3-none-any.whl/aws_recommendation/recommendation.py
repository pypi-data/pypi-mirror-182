from aws_recommendation.ec2 import *
from aws_recommendation.rds import *
from aws_recommendation.cost_estimations import *
from aws_recommendation.redshift import *
from aws_recommendation.ebs import *
from aws_recommendation.s3 import *
from aws_recommendation.elb import *
from aws_recommendation.cloudwatch import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Generic Suggestions
def get_generic_suggestions(self) -> list:
    logger.info(" ---Inside get_generic_suggestions()")

    recommendations = [
        {
            'Service Name': 'Volume',
            'Id': 'Generic',
            'Recommendation': 'Move GP2 volumes to GP3',
            'Description': 'The move GP2 volumes to GP3 saves cost',
            'Metadata': {},
            'Recommendation Reason': {}
        },
        {
            'Service Name': 'EC2',
            'Id': 'Generic',
            'Recommendation': 'Use m5 or t3 rather than m3',
            'Description': 'Consider using m5 or t3 family instead of m3 as m3 is older generation and expensive as compared to latest generation',
            'Metadata': {},
            'Recommendation Reason': {}
        },
    ]
    return recommendations


# Merge the recommendations and return the list
def get_recommendations(self) -> list:
    recommendations= []
    recommendations += delete_or_downsize_instance_recommendation(self)
    recommendations += purge_unattached_vol_recommendation(self)
    recommendations += purge_8_weeks_older_snapshots(self)
    recommendations += reserved_instance_lease_expiration(self)
    recommendations += unassociated_elastic_ip_addresses(self)
    recommendations += unused_ami(self)

    recommendations += downsize_underutilized_rds_recommendation(self)
    recommendations += rds_idle_db_instances(self)
    recommendations += rds_general_purpose_ssd(self)

    recommendations += get_generic_suggestions(self)
    recommendations += estimated_savings(self)
    recommendations += under_utilized_redshift_cluster(self)

    recommendations += idle_ebs_volumes(self)
    recommendations += ebs_general_purpose_ssd(self)

    recommendations += enable_s3_bucket_keys(self)
    recommendations += s3_bucket_versioning_enabled(self)
    recommendations += s3_bucket_lifecycle_configuration(self)

    recommendations += idle_elastic_load_balancer(self)

    recommendations += log_group_retention_period_check(self)

    return recommendations