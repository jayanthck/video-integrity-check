samffmpeg
lambda function to check the integrity of video

required: sam-cli, python 3.6, docker

commands:

to build the project locally: sam build --use-container

to invocke the function locally: sam local invoke IntegrityCheckFunction --event event.json

to package the function: sam package 
--output-template-file packaged.yaml 
--s3-bucket your bucketname

to deploy the function to aws: sam deploy 
--template-file packaged.yaml 
--stack-name sam-app 
--capabilities CAPABILITY_IAM 
--region eu-central-1

now invoke the function from aws lambda console
problem: The function runs properly when invocked locally using container(even when using the docker file) returns the status code 0 and doesn't generate any error , but after the deployment to aws the function runs successfully but integrity check fails and returns error code along with error even for a valid video 
