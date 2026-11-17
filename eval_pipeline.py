import json, time

def evaluate_response(prompt: str, response: str, expected_keywords: list) -> dict:
    start = time.time()
    matches = [kw for kw in expected_keywords if kw.lower() in response.lower()]
    score = len(matches) / len(expected_keywords) if expected_keywords else 1.0
    return {
        "passed": score >= 0.8,
        "score": round(score, 2),
        "matched_keywords": matches,
        "latency_ms": round((time.time() - start) * 1000, 2)
    }

if __name__ == "__main__":
    print(json.dumps(evaluate_response("Explain RAG", "RAG combines retrieval and generation.", ["retrieval", "generation"]), indent=2))
