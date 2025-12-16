how to calculate self-attention using vectors

step 1:
    create a 3 vector from each encoder's input vector (in this case, the embedding of each word)
    so for each embedding(word or subword) which is represnedted in 512 dimensions vectors,
    for each embedding (word/subword) we have to create a 3 vector => Query Vector, Key Vector and Value Vector,
    These vectors are created by multiplying the embedding by three matrices that we trained during the training process.