Explain in detail the workings of a dynamic array:

- What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

# Accessing an array, adding or removing from the back or front is O(1), because you know the index. If you have to search for a value, then it becomes O(N)

- What is the worse case scenario if you try to extend the storage size of a dynamic array?

# The worst case would be O(N) in the event that you would have to move every single element.

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

# A block is a record of data that has proof of work, previous block, and transactions. The chain refers to the hash of the previous block that is REQUIRED to access the next block in the chain.

Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

# Proof of work is a diffcult process that takes a massive amount of computing power. After this proof of work is generated, it is easy to verify.

# This prevents an attack because no single computer or even system of computers would be able to beat the collective power of all other miners to

# be able to alter the chain. And even if they do, you can verify it simply.
