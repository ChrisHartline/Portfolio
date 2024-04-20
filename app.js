document.getElementById('generateWallet').addEventListener('click', function() {
    // BitcoinJS library is included via CDN in the HTML, so it's globally available here
    const bitcoin = window.bitcoin;
    // Generate a random mnemonic (seed phrase) - remember, in a real app, you might want to let the user input this or securely generate and store it
    const mnemonic = "praise you muffin lion enable neck grocery crumble super myself license ghost"; // This should be generated or input by the user in real use cases
    const seed = bitcoin.bip39.mnemonicToSeedSync(mnemonic);
    const root = bitcoin.bip32.fromSeed(seed);
    
    // Derive the first account based on BIP32 path
    const path = "m/0'/0/0"; // This is a common path for the first account, but your application might require a different path
    const child = root.derivePath(path);

    const { address } = bitcoin.payments.p2pkh({ pubkey: child.publicKey });

    // Display the generated wallet details
    document.getElementById('walletAddress').textContent = address;
    document.getElementById('walletPrivateKey').textContent = child.toWIF();
});
