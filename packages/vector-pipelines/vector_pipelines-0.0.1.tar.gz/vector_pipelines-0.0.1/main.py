from vector_pipelines import pipeline, OpenAIEmbeddingGenerator, QdrantBackend, QuestionAnswering

pipe = pipeline(
    embedding_generator=OpenAIEmbeddingGenerator(...),
    backend=QdrantBackend(...),
    task=QuestionAnswering(...)
)

pipe.insert("bla bla bla bla")

pipe.search("shit")