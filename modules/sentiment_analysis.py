from transformers import pipeline

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    Returns a dictionary with sentiment and score if strongly negative, otherwise None.
    """
    try:
        # Clean the text (remove special characters, etc.)
        cleaned_text = " ".join(text.split())  # Remove extra spaces
        cleaned_text = "".join(char for char in cleaned_text if char.isalnum() or char.isspace())

        # Analyze sentiment
        result = sentiment_analyzer(cleaned_text)[0]
    
        if result["label"] == "NEGATIVE" and result["score"] > 0.85:  # Adjust threshold
            return {
                "sentiment": result["label"],
                "score": result["score"]
            }
        return None
    
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return None
    