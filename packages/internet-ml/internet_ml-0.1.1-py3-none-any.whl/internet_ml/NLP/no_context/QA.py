import sys
from pathlib import Path

from transformers import pipeline

sys.path.append(str(Path(__file__).parent.parent.parent) + "/tools/NLP/data")
import internet

QA_MODEL = pipeline("question-answering")

def answer(query: str) -> str:
    global QA_MODEL
    results = internet.google(question)
    return (QA_MODEL(question=query, context=str(results[0])), results[1])