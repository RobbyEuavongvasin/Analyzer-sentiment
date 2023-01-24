from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    :param text: str, the text to analyze
    :return: tuple, containing the sentiment polarity and subjectivity
    """
    # create a TextBlob object
    blob = TextBlob(text)
    
    # calculate the sentiment
    sentiment = blob.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity
    
    return (polarity, subjectivity)

# Example usage
text = "I am happy and content with my life."
polarity, subjectivity = analyze_sentiment(text)
print("Polarity: ", polarity)
print("Subjectivity: ", subjectivity)
