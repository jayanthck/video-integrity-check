FROM lambci/lambda:python3.6
COPY checkintegrity/* ./
RUN ls
RUN pwd
RUN /var/task/ffmpeg -version
RUN /var/task/ffprobe -version
RUN python3 -c "from checkintegrity import *; lambda_handler(None,None)"
