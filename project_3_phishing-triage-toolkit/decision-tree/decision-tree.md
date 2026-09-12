# Phishing Triage Decision Tree

## Visual (Mermaid)

```mermaid
flowchart TD
    A[Incoming suspicious message] --> B{Sender domain matches\nknown company domain?}
    B -- No --> M[MALICIOUS]
    B -- Yes --> C{Message creates urgency,\nauthority pressure, or secrecy?}
    C -- Yes --> D{Asks for credentials,\nMFA code, payment, or\nsensitive data?}
    D -- Yes --> M
    D -- No --> S[SUSPICIOUS]
    C -- No --> E{Contains unexpected link,\nQR code, or unusual\nattachment type?}
    E -- Yes --> S
    E -- No --> F[SAFE]

    M --> M1[Block domain/sender &\nEscalate to security team]
    S --> S1[Warn user &\nVerify via known,\nout-of-band channel]
    F --> F1[Close — no action needed]
```

## Text version (for non-rendering environments)

1. **Does the sender domain match the real, known company/brand domain exactly?**
   - No → **MALICIOUS** → Block domain & escalate.
   - Yes → go to 2.

2. **Does the message push urgency, authority, or secrecy** (e.g., "act now,"
   "confidential," "don't tell anyone," impersonating a boss or IT)?
   - Yes → go to 3.
   - No → go to 4.

3. **Does it directly ask for a password, MFA code, payment details, or other
   sensitive data?**
   - Yes → **MALICIOUS** → Block domain & escalate.
   - No → **SUSPICIOUS** → Warn user, verify through a known separate channel.

4. **Does it contain an unexpected link, QR code, or an unusual attachment
   type (.iso, .js, .scr, etc.)?**
   - Yes → **SUSPICIOUS** → Warn user, verify through a known separate channel.
   - No → **SAFE** → Close, no action needed.

## Outcomes
| Verdict | Action |
|---|---|
| 🟢 Safe | Close — no further action |
| 🟡 Suspicious | Warn the user; verify the request through a known, separate channel before acting |
| 🔴 Malicious | Block the domain/sender and escalate to the security team so it can be purged from other inboxes |
