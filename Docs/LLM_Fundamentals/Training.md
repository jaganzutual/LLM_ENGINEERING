# Training

### Transformers: Two-Phase Training
Transformers typically use a two-phase training approach: pre-training followed by fine-tuning.

#### 1. Pre-training
During pre-training, a Transformer learns broad language patterns from large amounts of unannotated text.

The model acquires a general understanding of language structure, semantics, and context from large datasets—this is like learning the fundamentals of a language before specializing.

##### Learned characteristics
- Syntax
- Grammar
- Common phrases and idioms
- Word relationships
- Long-range dependencies

#### 2. Fine-tuning
After pre-training, Transformers are fine-tuned on a specific downstream task (classification, QA, etc.) to adapt the general knowledge to the task requirements.
