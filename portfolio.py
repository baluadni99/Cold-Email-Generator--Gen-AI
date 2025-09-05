import pandas as pd
import numpy as np
import uuid
from sentence_transformers import SentenceTransformer
import faiss


class Portfolio:
    def __init__(self, file_path="app/resource/portfolio sample.csv"):
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)

        # normalize column names
        self.df.columns = [c.strip() for c in self.df.columns]
        if "Techstack`" in self.df.columns and "Techstack" not in self.df.columns:
            self.df = self.df.rename(columns={"Techstack`": "Techstack"})

        if "Techstack" not in self.df.columns or "Links" not in self.df.columns:
            raise ValueError("CSV must have columns: Techstack, Links")

        # sentence-transformers model (small + fast)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # FAISS index (cosine via inner product on normalized vectors)
        self.index = None
        self.embeddings = None

    def load_portfolio(self):
        texts = self.df["Techstack"].fillna("").astype(str).tolist()
        if not texts:
            return
        embs = self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )
        embs = embs.astype("float32")
        self.embeddings = embs
        d = embs.shape[1]
        self.index = faiss.IndexFlatIP(d)  # inner product
        self.index.add(embs)

    def query_links(self, skills):
        # return a simple list of links (strings)
        if self.index is None or self.embeddings is None or not len(self.df):
            return []
        if not skills:
            return []

        links = []
        seen = set()
        for s in skills:
            s = (s or "").strip()
            if not s:
                continue
            q = self.model.encode([s], normalize_embeddings=True, convert_to_numpy=True)
            q = q.astype("float32")
            # top 2 matches per skill
            D, I = self.index.search(q, 2)
            for idx in I[0]:
                if idx == -1:
                    continue
                link = str(self.df.iloc[idx].get("Links", "")).strip()
                if link and link not in seen:
                    links.append(link)
                    seen.add(link)

        # keep it short and tidy
        return links[:3]
