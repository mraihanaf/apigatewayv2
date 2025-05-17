# CI/CD Development
## Install Dependencies
`pip install -r requirements.txt`

## Setting Github Environments
AWS_ACCESS_KEY_ID=your aws access key<br/>
AWS_SECRET_ACCESS_KEY=your secret access key<br/>
AWS_SESSION_TOKEN=your sessions token<br/>
AWS_REGION=us-east-1<br/>
EFS_PATH=yourpath/app.log<br/>
S3_BUCKET_NAME=your bucket name<br/>
API_GATEWAY_URL=your API Gateway URL<br/>
ECR_REPOSITORY=your name ECR<br/>
ECR_REGISTRY=your url image<br/>
EB_APP_NAME=your eb app name<br/>
EB_ENV_NAME=your eb env name

## Lambda Functions Environments
DB_HOST=your db host<br/>
DB_PORT=your db port<br/>
DB_USER=your db user<br/>
DB_PASSWORD=your db password<br/>
DB_NAME=your db name

## Running Apps
python app.py

# Problem Solving
You must solve the problem in the CI/CD

aws s3 cp flask-app.zip s3://lks-jakpus1-rai-dockerimage-737713706142/flask-app.zip