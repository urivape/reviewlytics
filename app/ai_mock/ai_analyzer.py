class AIMockAnalyzer:
    """
    A mock class simulating AI analysis for product reviews.
    """

    def analyze_sentiment(self, text: str) -> str:
      """
      Simulates sentiment analysis based on keywords.
      """
      positive_keywords = ["excellent", "good", "love", "fantastic", "great", "amazing", "best", "recommend"]
      negative_keywords = ["bad", "terrible", "hate", "worst", "awful", "poor"]

      for keyword in positive_keywords:
          if keyword in text.lower():
              return "positive"
      for keyword in negative_keywords:
          if keyword in text.lower():
              return "negative"
      return "neutral"

    def calculate_readability(self, text: str) -> float:
        """
        Simulates readability calculation based on sentence length.
        """
        sentences = text.split('.')
        if not sentences:
            return 5.0  # Default if no sentences
        avg_sentence_length = sum(len(sentence.split())
                                  for sentence in sentences) / len(sentences)
        # Simple heuristic: shorter sentences are considered more readable
        return max(1.0, 7.0 - (avg_sentence_length * 0.15))

    def suggest_improvements(self, text: str) -> list[str]:
        suggestions = []
        word_count = len(text.split())
        if word_count < 15:
            suggestions.append("Consider adding more details to your review.")
        if "i think" in text.lower() or "it seems" in text.lower():
            suggestions.append("Try to be more direct in your opinions.")
        if "not sure" in text.lower():
            suggestions.append(
                "If you're unsure, try to explain what aspects were unclear.")
        return suggestions
