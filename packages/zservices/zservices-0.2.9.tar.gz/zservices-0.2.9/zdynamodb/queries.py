from zdynamodb.dynamo import DynamoDB
from boto3.dynamodb.conditions import Key
from zdynamodb import logger


class DynamoQueries:
    def __init__(self, table_name, connection_params=None):
        logger.info('[DynamoDB]: Initiating DynamoQueries Class')
        self.db = DynamoDB(connection_params)
        self.table_name = table_name
        self.table = self.db.connection.Table(table_name)

    @staticmethod
    def projection_expression_and_attributes(query: dict, projection: list) -> dict:
        if not projection:
            return query
        projection_expression = ', '.join(map('#{0}'.format, projection))
        expression_attribute_names = {}
        for item in projection:
            expression_attribute_names[f'#{item}'] = str(item)
        query['ProjectionExpression'] = projection_expression
        query['ExpressionAttributeNames'] = expression_attribute_names
        return query

    @staticmethod
    def filter(model_data: dict | list, filter_fields: list) -> dict | list:
        if not filter_fields:
            return model_data

        if isinstance(model_data, dict):
            model_data_filtered = {k: v for k, v in model_data.items() if k not in filter_fields}
            return model_data_filtered

        if isinstance(model_data, list):
            model_data_filtered = []
            for item in model_data:
                item_filtered = {k: v for k, v in item.items() if k not in filter_fields}
                model_data_filtered.append(item_filtered)
            return model_data_filtered

    def get_pk_context(self, pk, pk_value, projection: list = None, model_filters: list = None):
        try:
            query = {
                "KeyConditionExpression": Key(pk).eq(pk_value),
            }
            query = self.projection_expression_and_attributes(query, projection)
            response = self.table.query(**query)
            model_data = response['Items']
            if model_filters:
                model_data = self.filter(model_data, model_filters)
            return model_data
        except Exception as e:
            logger.warning(f'[DynamoDB]: Unable to get data for {pk_value} from table {self.table_name}, e= {e}')
            raise e

    def get_index_context(self, index_key, index_value, index_name, projection: list = None,
                          model_filters: list = None):
        try:
            query = {
                "IndexName": index_name,
                "KeyConditionExpression": Key(index_key).eq(index_value)
            }
            query = self.projection_expression_and_attributes(query, projection)
            response = self.table.query(**query)
            model_data = response['Items']
            while 'LastEvaluatedKey' in response:
                query['ExclusiveStartKey'] = response['LastEvaluatedKey']
                response = self.table.query(**query)
                model_data.extend(response['Items'])
            if model_filters:
                model_data = self.filter(model_data, model_filters)
            return model_data
        except Exception as e:
            logger.warning(f'[DynamoDB]: Unable to get data for {index_value} from table {self.table_name}, e= {e}')
            raise e

    def add_context(self, item: dict, return_values='ALL_OLD'):
        try:
            response = self.table.put_item(Item=item, ReturnValues=return_values)
            model_data = response.get('Attributes', {}) | item
            return model_data
        except Exception as e:
            logger.warning(f'[DynamoDB]: Unable to add data for from table {self.table_name}, e= {e}')
            raise e

