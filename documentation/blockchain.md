# Blockchain


## What is a Block?

A Blockchain is a chain of blocks that contain information. The data which is stored inside a block depends on the type of blockchain.

For Example, A Bitcoin Block contains information about the 

- Sender, 
- Receiver, 
- number of bitcoins to be transferred.

The first block in the chain is called the Genesis block. Each new block in the chain is linked to the previous block.


A block has a hash, this works as a fingerprint which is unique to each block. It identifies a block and all of its contents, and it’s always unique, just like a fingerprint. 

So once a block is created, any change inside the block will cause the Hash to change. Therefore, the Hash is very useful when you want to detect changes to intersections. If the fingerprint of a block changes, it does not remain the same block.

Each Block has

1. Data
2. Hash
3. Hash of the previous block

Consider the following example, where we have a chain of 3 blocks. The 1st block has no predecessor. Hence, it does not contain has the previous block. Block 2 contains a hash of block 1. While block 3 contains Hash of block 2.


Block 1
- Hash: 2ZB1
- Previous Hash: 0000

Block 2
- Hash: AAB2
- Previous Hash: 2ZB1

Block 3
- Hash: VJR3
- Previous Hash: AAB2

