# BERT

**BERT (Bidirectional Encoder Representations from Transformers)**

- **Bidirectional**: Reads text in both directions to capture richer context.
- **Encoder-only**: Uses only Transformer encoder layers (not a decoder), so it's not primarily generative.
- **Representations**: Produces contextual representations for words and subwords in a sentence.
- **Architecture**: Based on the Transformer encoder architecture.

---

BERT was a breakthrough Transformer model in natural language processing and achieved state-of-the-art results when released.

- **Released**: 2018 by Google Research (Google AI / Google Brain)

## Overview

- **Goal**: Learn deep, context-aware text representations.
- **Structure**: Stacked encoder layers with self-attention mechanisms.
- **Usage**: Because BERT is encoder-only, it is mainly used for understanding tasks (classification, QA, etc.), not for text generation.

## Pre-training

- **Datasets**: Trained on large corpora such as Wikipedia (≈2.5B words) and BookCorpus (≈500M words).

## Pre-training Objectives

- **Masked Language Modeling (MLM)**
  - Randomly mask tokens in the input sequence and train the model to predict the masked tokens from context.
  - Outcome: Learns relationships between tokens and contextual usage.
  - Example: "When life gives you [MASK], make lemonade." The model predicts the masked word.

- **Next Sentence Prediction (NSP)**
  - Trains the model to predict whether a given sentence B follows sentence A in the original text.
  - Purpose: Helps BERT learn relationships between sentences, useful for tasks like QA and natural language inference.
