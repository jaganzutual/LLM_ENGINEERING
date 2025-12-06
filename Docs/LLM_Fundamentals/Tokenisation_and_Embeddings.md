# Tokenisation and Embeddings

### Tokenisation
Tokenisation is the process of converting raw text into smaller units called "tokens" for Transformer models. This enables text parsing and analysis.

#### Word-level
Individual words are treated as tokens.
```
"Hello World" -> ["Hello", "World"]
```

#### Character-level
Each character is treated as a token.
```
"Hello" -> ["h", "e", "l", "l", "o"]
```

### Subword-level
Words are broken down into subword units (useful for handling rare words and morphology).
```
"Jagan" -> ["J", "agan"]
"Hello World" -> ["Hello", "World"]
```

---

### Embeddings: The Goal of Pre-training

- **Context-aware embeddings**: Pre-training produces embeddings that capture semantic and syntactic relationships between tokens.
- **Reusable representations**: These learned encodings become building blocks for downstream models like BERT or GPT.
- **How**: Models learn contextualized token representations via self-attention and stacked Transformer layers during pre-training.