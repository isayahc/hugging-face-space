Setting up a GPG (GNU Privacy Guard) key for signing your commits is a good way to secure your work and prove that the commits are indeed from you. Here's a step-by-step guide to setting up a GPG key on a Unix-like system:

### Step 1: Install GPG
If you don't already have GPG installed, you can install it using your package manager. For example, on Debian-based systems, use:
```bash
sudo apt-get install gnupg
```

### Step 2: Generate a GPG Key Pair
```bash
gpg --full-generate-key
```
Follow the prompts to generate your key pair. You’ll need to specify the kind of key you want, the key size (a 4096-bit key is recommended), and the duration the key should be valid. You will also need to provide your name and the email address associated with your Git commits.

### Step 3: List GPG Keys
Once you've generated your GPG key, list your keys by typing:
```bash
gpg --list-secret-keys --keyid-format=long
```

Look for the key that matches your Git commit email.

### Step 4: Get the GPG Key ID
Take note of the GPG key ID of the key you just created. It's the part after the `/` in the `sec` line.

### Step 5: Export the GPG Key
```bash
gpg --armor --export YOUR_GPG_KEY_ID
```
Replace `YOUR_GPG_KEY_ID` with the ID you found in the previous step. This will print your GPG key in the ASCII armor format, which you'll need to copy.

### Step 6: Add the GPG Key to Your GitHub Account
- Go to your GitHub settings.
- Click on "SSH and GPG keys".
- Click on "New GPG key".
- Paste your GPG key into the text area and save.

### Step 7: Configure Git to Use Your GPG Key
```bash
git config --global user.signingkey YOUR_GPG_KEY_ID
```

### Step 8: Sign Your Commits
To sign a commit, you just need to add `-S` to your `git commit` command:
```bash
git commit -S -m "Your commit message"
```

### Step 9: Tell Git to Sign All Your Commits
If you want to sign all your commits by default, you can configure Git to do so:
```bash
git config --global commit.gpgsign true
```

### Step 10: Push Your Commit to GitHub
When you push your signed commit to GitHub, it should now show up as "Verified".

Remember to always keep your private key secure and never share it with anyone. If you forget your passphrase, you will lose access to anything encrypted with your private key, so keep it in a safe place.