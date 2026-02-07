
This modular structure mirrors real-world secure software design, where cryptography is isolated from application logic.

---

## Master Password Handling

- The **master password is never stored in plain text**.
- It is hashed using **SHA-256** and saved in `master.hash`.
- On each launch, the entered master password is hashed again and compared with the stored hash.
- Only upon successful verification does the program proceed.

This approach prevents password recovery even if the hash file is compromised.

---

## Encryption & Decryption Flow

1. The master password is transformed into a fixed-length key.
2. This key is used with **Fernet (AES-based symmetric encryption)**.
3. When saving credentials:
   - Passwords are encrypted before storage.
4. When retrieving credentials:
   - Passwords are decrypted only after successful authentication.

If the wrong master password is provided, decryption fails automatically.

---

## Secure File Handling

- Credentials are stored in `storage.json` in encrypted form.
- Each entry includes:
  - Service name
  - Username
  - Encrypted password
- Files are created automatically during runtime and never manually edited.

This ensures data persistence while maintaining confidentiality.

---

## Real-World Relevance

This project mirrors the **core architecture used in real password managers** such as Bitwarden or 1Password:

| Feature | This Project | Real-World Systems |
|------|-------------|------------------|
| Master password | ✔ | ✔ |
| Password hashing | ✔ | ✔ |
| Symmetric encryption | ✔ | ✔ |
| Encrypted local storage | ✔ | ✔ |
| Key derivation | Basic | PBKDF2 / Argon2 |
| Cloud sync | ✖ | ✔ |

While simplified, the security principles remain authentic and transferable.

---

## Learning Outcomes

Through this project, I developed practical understanding of:
- Cryptographic hashing vs encryption
- Secure key handling
- Python file I/O and JSON persistence
- Modular program design
- Common security pitfalls in credential storage

---

## Future Enhancements

- Password input masking (`getpass`)
- Salted key derivation (PBKDF2 / Argon2)
- Password strength validation
- Clipboard-based password copying
- GUI interface
- Cloud-based encrypted sync

---

## Disclaimer

This project is intended for **educational purposes only**.  
For production use, additional security hardening and external audits would be required.
