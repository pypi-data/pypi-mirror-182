from botocore.exceptions import ClientError

from aws_recommendation.utils import *


# Generate the recommendation for idle elastic load balancer
def idle_elastic_load_balancer(self):
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside elb :: idle_elastic_load_balancer()")

    recommendation = []
    regions = self.session.get_available_regions('elbv2')

    for region in regions:
        try:
            client = self.session.client('elbv2', region_name=region)
            marker = ''
            while True:
                if marker == '':
                    response = client.describe_load_balancers()
                else:
                    response = client.describe_load_balancers(
                        Marker=marker
                    )
                for lb in response['LoadBalancers']:
                    datapoints = get_metrics_stats(
                        self,
                        region=region,
                        namespace='AWS/EC2',
                        dimensions=[
                            {
                                'Name': 'LoadBalancerName',
                                'Value': lb['LoadBalancerName']
                            }
                        ],
                        metric_name='RequestCount',
                        stats=['Sum'],
                        unit=None
                    )
                    sum_request_count = 0
                    for datapoint in datapoints['Datapoints']:
                        sum_request_count = sum_request_count + datapoint['Sum']

                    recommend_flag = True
                    if sum_request_count >= 100:
                        recommend_flag = False

                    if recommend_flag:
                        tags_response = client.describe_tags(
                            ResourceArns=[
                                lb['LoadBalancerArn']
                            ]
                        )
                        try:
                            for tag in tags_response['TagDescriptions'][0]['Tags']:
                                if 'Role' in tag['Key']:
                                    recommend_flag = False
                        except TypeError:
                            pass
                        if recommend_flag:
                            temp = {
                                'Service Name': 'Elastic load balacer',
                                'Id': lb['LoadBalancerName'],
                                'Recommendation': 'Terminate Elastic Load Balancer',
                                'Description': 'The selected Elastic Load Balancer can be safely removed from the AWS account to reduce the ELB monthly costs.',
                                'Metadata': {
                                    'Region': region,
                                    'Type': lb['Type'],
                                    'Tags': tags_response['TagDescriptions'][0]['Tags'],
                                },
                                'Recommendation Reason': {
                                    # 'Average CPU Datapoints(7 days)': [float('{:.2f}'.format(x)) for x in tmp_lst_cpu]
                                }
                            }
                try:
                    marker = response['NextMarker']
                    if marker == '':
                        break
                except KeyError:
                    break

        except ClientError as e:
            logger.error("Something went wrong with the region {}: {}".format(region, e))

    return recommendation