# Trip Backend

## Deployed to AWS and containes following APIs:

`curl -X GET http://trip-backend-env.wj8eidghpr.ca-central-1.elasticbeanstalk.com/api/airport/list`

`curl -X GET http://trip-backend-env.wj8eidghpr.ca-central-1.elasticbeanstalk.com/api/airport/[from]/[to]/distance -H 'Authorization: Basic [username:password]'`

Uploaded using Elastic Beanstalk:
1. Added requirements.txt and .ebextensions/django.config file to the project
2. Added a user with AWSElasticBeanstalkFullAccess role.
3. Tried to creat an eb environment but got an error for permission to ElasticLoadBalancing. 
4. Added ElasticLoadBalancingFullAccess role to user.
5. Deployed application successfully
6. Came arround this error when I was trying to call an API from it. 

    `Authentication credentials were not provided.`
7. Fixed it by adding this container command to django.config file located in ebextensions. 

    `01_wsgipass:
    command: 'echo "WSGIPassAuthorization On" >> ../wsgi.conf`
    
