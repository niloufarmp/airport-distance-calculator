# Trip UI

## Deployed to AWS at http://mytripapp.tk.s3-website.us-east-2.amazonaws.com/

1. Added s3 role to user
2. Created S3 bucket
2. Installed AWS-Cli
3. AWS configure --profile [user-name]
4. npm run build
5. Added this to package.json:
    `"deploy-s3": "aws s3 --profile [user-name] sync ./dist/trip s3://mytripapp.tk --region us-east-2"`
6. npm run build deploy-s3
