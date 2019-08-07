import json
import os
import subprocess

def lambda_handler(event, context):

    FFmpeg_static = "/var/task/ffmpeg"
    videofile = "/var/task/small.mp4"
     
   #ffmpeg commad to check the video integrity
    cp = subprocess.run([FFmpeg_static, '-v','error' ,'-i' ,videofile ,'-f', 'null', 'null'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
    print('output:',cp.stdout)
    print('error:',cp.stderr)
    print('statusCode',cp.returncode)

    return {
        'statusCode': 200,
        'body': json.dumps(cp.stderr)
    }
