from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="csarron/mobilebert-uncased-squad-v1",
    tokenizer="csarron/mobilebert-uncased-squad-v1"
)

predictions = qa_pipeline({
    'context': "The game was played on February 7, 2016 at Levi's Stadium in the San Francisco Bay Area at Santa Clara, California.",
    'question': "What day was the game played on?"
})

print(predictions)

