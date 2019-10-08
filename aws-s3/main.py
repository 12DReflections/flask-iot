import os
import boto3
from datetime import datetime
from dateutil.tz import tzutc
from dateutil import parser

'''
Download updated files from bucket, note bucket names should match the kiosk username.
Set this script up on a task scheduler to update the files accordingly.

Currently the movie in the s3 bucket should be called Freespace.mp4
'''

def main():

    # Check for File Path and Date Modified
    s3 = boto3.client('s3')
    user = os.getlogin().lower()
    objects = s3.list_objects(Bucket="video-media-0000")
    print(user)
    for key in objects['Contents']:
        if key['Key'].split('/')[0] == user and key['Key'].split('/')[1]:
            f_with_path = key['Key']
            mod = key['LastModified'] 
        else: 
            pass

    # Read from file the last modified date
    with open('./modified.txt', 'r') as f:
        local_modified = f.read()
        local_m =datetime.strptime(local_modified, '%Y-%m-%d %H:%M:%S+00:00')
        local_m = local_m.replace(tzinfo=tzutc())

    # Download the file and update the last modified
    # Remove existing file, replace with new file, update last modified, reboot system.
    if mod > local_m:
        s3.download_file("video-media-0000", user + '/Freespace.mp4', 'C:\\apps\\flask-iot\\static\\media\\Freespace.mp4') # download with download filename
        os.rename('C:\\apps\\flask-iot\\static\\media\\Freespace1.mp4',  'C:\\apps\\flask-iot\\static\\media\\Freespace2.mp4') # rename existing to number 4
        os.rename('C:\\apps\\flask-iot\\static\\media\\Freespace.mp4',  'C:\\apps\\flask-iot\\static\\media\\Freespace1.mp4') # rename new to number 3
        with open('./modified.txt', 'w') as f:
            f.write(str(mod))
        os.remove('C:\\apps\\flask-iot\\static\\media\\Freespace2.mp4') # remove number 4 (aka older version)
        os.system("shutdown -t 0 -r -f")

if __name__=='__main__':
    main()

'''
{'ResponseMetadata': {'RequestId': '0F12B793C16DA21C', 'HostId': 'd0IZCugb6BeNsdtn/Zrb8cXo8SCcS016TbEPwhcN3+kSMV+Z4IyXWpykAk06FU9RcpjFdRqknYM=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'd0IZCugb6BeNsdtn/Zrb8cXo8SCcS016TbEPwhcN3+kSMV+Z4IyXWpykAk06FU9RcpjFdRqknYM=', 'x-amz-request-id': '0F12B793C16DA21C', 'date': 'Wed, 18 Sep 2019 04:26:48 GMT', 'x-amz-bucket-region':
'ap-southeast-2', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'IsTruncated': False, 'Marker': '', 'Contents': [{'Key': 'kiosk-0002/', 'LastModified': datetime.datetime(2019, 9, 18, 1, 32, 33, tzinfo=tzutc()), 'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', 'Size': 0, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'freespace.media', 'ID': 'aad94e98908d74b0e56237930d00e3c9b106919d0369d5959f11b5a1735a6d2a'}}, {'Key': 'kiosk-0002/ypl2.jpeg', 'LastModified': datetime.datetime(2019, 9, 18, 1, 34, 1, tzinfo=tzutc()), 'ETag': '"37207aac658f527b96bd1a9dea442a27"', 'Size': 8344, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'freespace.media', 'ID': 'aad94e98908d74b0e56237930d00e3c9b106919d0369d5959f11b5a1735a6d2a'}}], 'Name': 'video-media-0000', 'Prefix': '', 'MaxKeys': 1000, 'EncodingType': 'url'}
'''
