import uuid

def get_uuid():
        return str(uuid.uuid4())

class DynamodbUtil():
    ''' helper class to deal with dynamodb '''
