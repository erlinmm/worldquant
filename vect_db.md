# Recommendation for your situation

Use ChromaDB for the fastest path to working. Your Fusion index will have hundreds to low thousands of records — nowhere near ChromaDB's limits. You get pre-filter by role/tags (critical for retrieval precision) and zero infrastructure. If you later want to inspect or query the index with SQL, migrate to sqlite-vec — same data, better tooling.
Embedding model recommendation
```
# sentence-transformers — runs locally, no API call, no cost per embedding
pip install sentence-transformers

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")   # 384-dim, fast, good quality
# or for better quality at higher cost:
model = SentenceTransformer("all-mpnet-base-v2")   # 768-dim

# Runs fully offline — important for a preprocessing step
# Fusion index is small enough that local embedding is fast (seconds not hours)
```
