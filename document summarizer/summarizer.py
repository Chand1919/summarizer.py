def summarize_text(text, sentence_count=5):
    if not text.strip():
        return "No text found to summarize."

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentence_count)

    if not summary:
        return "No meaningful summary could be generated."
    
    return '\n'.join(str(sentence) for sentence in summary)



