# main.py

from blockchain.chain import Blockchain

def main():
    my_chain = Blockchain()

    # Add some blocks with custom data
    my_chain.add_block("Swati's first block 🧚‍♀️✨")
    my_chain.add_block("Manifesting success 💫📈")
    my_chain.add_block("Third block just vibin' 😎")

    # Print the whole chain
    print("\n🌟 BLOCKCHAIN LEDGER 🌟")
    for block in my_chain.chain:
        print(block)
        print("-" * 60)

    # Validate the chain
    print("\n🔍 Chain is valid?", my_chain.is_chain_valid())

if __name__ == "__main__":
    main()
