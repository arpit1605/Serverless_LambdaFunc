import json
import boto3

def lambda_handler(event, context):
    try:
        # Extract the user review from the event
        review = event.get('review', '')
        if not review:
            raise ValueError("No review provided in the event")

        # Initialize the Amazon Comprehend client
        comprehend = boto3.client('comprehend')

        # Analyze the sentiment of the review
        response = comprehend.detect_sentiment(Text=review, LanguageCode='en')

        # Extract the sentiment result
        sentiment = response.get('Sentiment', 'UNKNOWN')

        # Log the sentiment result
        print(f"Review: {review}")
        print(f"Sentiment: {sentiment}")
    
        return {
            'statusCode': 200,
            'body': json.dumps({
                'review': review,
                'sentiment': sentiment
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
