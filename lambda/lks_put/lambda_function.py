import os
import pymysql
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        user_id = event['pathParameters']['id']
        body = json.loads(event['body'])

        conn = pymysql.connect(
            host=os.environ['DB_HOST'],
            port=int(os.environ['DB_PORT']),
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            db=os.environ['DB_NAME'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with conn.cursor() as cursor:
            cursor.execute('SELECT id FROM users WHERE id = %s', (user_id,))
            if not cursor.fetchone():
                return {
                    'statusCode': 404,
                    'body': json.dumps('User not found')
                }

            update_fields = []
            params = []
            for field in ['name', 'email', 'institution', 'position', 'phone', 'image_url']:
                if field in body:
                    update_fields.append(f"{field} = %s")
                    params.append(body[field])
            
            if not update_fields:
                return {
                    'statusCode': 400,
                    'body': json.dumps('No fields to update')
                }

            params.append(user_id)
            query = f"UPDATE users SET {', '.join(update_fields)} WHERE id = %s"
            
            cursor.execute(query, params)
            conn.commit()

            cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
            user = cursor.fetchone()

        return {
            'statusCode': 200,
            'body': json.dumps(user, default=str)
        }

    except pymysql.IntegrityError as e:
        logger.error("Integrity error: %s", e)
        return {
            'statusCode': 409,
            'body': json.dumps('Email already exists')
        }
    except pymysql.MySQLError as e:
        logger.error("Database error: %s", e)
        return {
            'statusCode': 500,
            'body': json.dumps(f'Database error: {str(e)}')
        }
    except Exception as e:
        logger.error("Unexpected error: %s", e)
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
    finally:
        if 'conn' in locals():
            conn.close()