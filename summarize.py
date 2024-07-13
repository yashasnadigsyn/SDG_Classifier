def summarize_content(text_content):
    stop_words = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "he", "in", "is", "it", "its", "of", "on", "that", "the",
    "to", "was", "were", "will", "with", "this", "have", "but", "not",
    "they", "his", "her", "she", "him", "you", "your", "yours", "me",
    "my", "i", "we", "our", "ours", "had", "been", "do", "does", "did",
    "doing", "am", "all", "any", "more", "most", "other", "some", "such",
    "no", "nor", "only", "own", "same", "so", "than", "too", "very",
    "can", "will", "just", "don", "should", "now", "linkedin", "instagram",
    "facebook", "join", "us"
}

    words = text_content.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    summarized =  " ".join(filtered_words)
    return summarized
