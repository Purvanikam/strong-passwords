# Password Strength Report

**Student / Author:**  
**Date:**  
**Tool(s) used:** (e.g., passwordmeter.com, zxcvbn browser tool)

---

## 1) Method
- Generate or pick sample passwords (see PASSWORDS.md).
- Test each password using an online strength checker in private mode.
- Record the score, tool feedback, and any entropy estimate.
- Fill the table below and write observations.

---

## 2) Passwords tested

| ID | Password (masked)   | Length | Type        | Tool score | Tool feedback                  | Entropy (bits) | Notes |
|----|---------------------|--------|-------------|------------|-------------------------------|----------------|-------|
| 1  | p*******3           | 11     | Very Weak   |            |                               |                |       |
| 2  | B********4          | 13     | Moderate    |            |                               |                |       |
| 3  | G7******9           | 12     | Strong      |            |                               |                |       |
| 4  | c********e          | 28     | Passphrase   |            |                               |                |       |

**(Mask passwords when presenting. Keep plaintext only in your private notes.)**

---

## 3) Results & Observations
- Which password performed best (score + why).
- Common weaknesses flagged by the tool (dictionary words, short length, predictable substitutions).
- Any surprising tool feedback.

---

## 4) Best Practices (summary)
- Use at least 12 characters for low-risk, 16+ for moderate-risk, 20+ for high-risk accounts.
- Use a mix of uppercase, lowercase, numbers, and symbols.
- Prefer long passphrases (3–5 unrelated words) or high-entropy random strings.
- Use a password manager and enable 2FA (two-factor authentication) where available.
- Use unique passwords for every account; never reuse.

---

## 5) Common Attacks (short)
- Brute-force: Attempts every possible combination; time required grows exponentially with length and charset.
- Dictionary attack: Uses lists of common passwords and words — avoid dictionary words.
- Rainbow table / precomputed hashes: Defender-side: use salted hashing and slow hash functions (bcrypt, Argon2).

---

## 6) Final Recommendations
- Use a password manager (KeePassXC, Bitwarden, 1Password).
- For very critical accounts, use 2FA (authenticator app or hardware token).
- Regularly review and rotate passwords if evidence of compromise exists.

---
