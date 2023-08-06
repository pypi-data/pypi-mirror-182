from botocore.exceptions import ClientError

from aws_recommendation_a1.utils import *


# Generated the recommendation for unused EBS volumes
def idle_ebs_volumes(self) -> list:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside ebs :: unused_ebs_volumes")

    recommendation = []
    regions = self.session.get_available_regions('ec2')

    for region in regions:
        try:
            client = self.session.client('ec2', region_name=region)
            marker = ''
            while True:
                response = client.describe_volumes(
                    Filters=[
                        {
                            'Name': 'status',
                            'Values': [
                                'in-use'
                            ]
                        },
                    ],
                    MaxResults=500,
                    NextToken=marker
                )
                for volume in response['Volumes']:
                    # device = volume['Attachments']['Device']
                    if '/dev/xvda' not in [x['Device'] for x in volume['Attachments']]:
                        read_datapoints = get_metrics_stats(
                            self=self,
                            region=region,
                            namespace='AWS/EBS',
                            dimensions= [
                                {
                                    'Name':'VolumeId',
                                    'Value': volume['VolumeId']
                                }
                            ],
                            metric_name='VolumeReadOps',
                            period=3600,
                            stats=['Sum']
                        )
                        sum_read_ops = 0
                        for datapoint in read_datapoints['Datapoints']:
                            print(type(datapoint))
                            print(datapoint)
                            sum_read_ops = sum_read_ops + datapoint['Sum']

                        flag = True

                        if sum_read_ops > 1:
                            flag = False

                        if flag:
                            write_datapoints = get_metrics_stats(
                                self=self,
                                region=region,
                                namespace='AWS/EBS',
                                dimensions=[
                                    {
                                        'Name': 'VolumeId',
                                        'Value': volume['VolumeId']
                                    }
                                ],
                                metric_name='VolumeReadOps',
                                period=3600,
                                stats=['Sum']
                            )
                            write_sum = 0
                            for datapoint in write_datapoints['Datapoints']:
                                write_sum = write_sum + datapoint['Sum']

                            if write_sum > 1:
                                flag = False

                        if flag:
                            try:
                                tags = volume['Tags']
                            except KeyError:
                                tags = None

                            recommend_flag = True
                            try:
                                for tag in tags:
                                    if 'Role' in tag['Key']:
                                        recommend_flag = False
                            except TypeError:
                                pass
                            if recommend_flag:
                                temp = {
                                    'Service Name': 'Volume',
                                    'Id': volume['VolumeId'],
                                    'Recommendation': 'Delete idle EBS volume',
                                    'Description': 'The selected EBS volume is considered "idle" and can be safely removed from the AWS account to reduce the EBS monthly costs.',
                                    'Metadata': {
                                        'Region': region,
                                        'Instance Type': volume['VolumeType'],
                                        'Tags': tags,
                                        'CreateTime': volume['CreateTime']
                                    },
                                    'Recommendation Reason': {
                                        'reason': "Volume is idle"
                                    }
                                }
                                recommendation.append(temp)
                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break
        except ClientError as e:
            logger.info("Something went wrong with the region {}: {}".format(region, e))

    return recommendation


# Generated the recommendation for general purpose ssd
def ebs_general_purpose_ssd(self) -> list:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside ebs :: ens_general_purpose_ssc()")

    recommendation = []
    regions = self.session.get_available_regions('ec2')

    for region in regions:
        try:
            client = self.session.client('ec2', region_name=region)
            marker = ''
            while True:
                response = client.describe_volumes(
                    MaxResults=500,
                    NextToken=marker
                )
                for volume in response['Volumes']:
                    storage_type = volume['VolumeType']
                    if storage_type == 'io1' or storage_type == 'io2':
                        try:
                            tags = volume['Tags']
                        except KeyError:
                            tags = None

                        temp = {
                            'Service Name': 'Volume',
                            'Id': volume['VolumeId'],
                            'Recommendation': 'Upgrade Storage Type',
                            'Description': 'Ensure that your Amazon EC2 instances are using General Purpose SSD volumes instead of Provisioned IOPS SSD volumes for cost-effective storage that fits a broad range of workloads',
                            'Metadata': {
                                'Region': region,
                                'Instance Type': volume['VolumeType'],
                                'Tags': tags,
                                'CreateTime': volume['CreateTime']
                            },
                            'Recommendation Reason': {
                                'reason': "the storage type configured for the selected Amazon EBS volume is Provisioned IOPS (PIOPS) SSD, therefore the verified EBS volume is not optimized with respect to cost."
                            }
                        }
                        recommendation.append(temp)

                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break
        except ClientError as e:
            logger.warning("Something went wrong with the region {}: {}".format(region, e))

    return recommendation