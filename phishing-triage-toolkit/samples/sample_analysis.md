# Sample Message Analysis — DecodeLabs Project 3

Four sample messages below: three phishing attempts (covering different vectors and
psychology from the training deck) and one legitimate email for contrast. Each includes
the raw message, the red flags found, the suspicious indicators, and a final verdict.

---

## Sample 1 — Fake IT Password Reset (Urgency + Authority)

**Channel:** Email

```
From: IT Security <it-support@decodelabs-secure.com>
To: a.raza@decodelabs.tech
Subject: URGENT: Your Password Expires in 2 Hours

Dear Employee,

Our system has detected that your account password will expire in 2 hours.
Failure to update it immediately will result in permanent loss of access to
your email and internal tools.

Click below to verify your identity and reset your password now:
hxxp://decodelabs.tech.login-update-portal.com/reset

This is an automated message. Do not reply.

IT Security Team
```

**Suspicious links/keywords:** "URGENT," "2 hours," "permanent loss of access,"
the reset link.

**Red flags identified:**
1. **Sender-domain mismatch** — claims to be DecodeLabs IT but sends from
   `decodelabs-secure.com`, a lookalike domain, not the real `decodelabs.tech`.
2. **Nested/fake subdomain (subdomain trap)** — the link buries the real company
   name as a subdomain of an attacker-owned root: reading right to left, the true
   root domain is `login-update-portal.com`, not `decodelabs.tech`.
3. **Artificial urgency** — a 2-hour deadline is designed to trigger a fight-or-flight
   response and skip verification.
4. **Generic greeting** ("Dear Employee") instead of the recipient's name.
5. **No out-of-band verification path offered** — only one channel (the link) is given.

**Why it's unsafe:** The domain does not belong to DecodeLabs, and the link is
structured to disguise a credential-harvesting page as an internal IT portal. Clicking
would send real credentials to an attacker-controlled site.

**Verdict:** 🔴 **Malicious → Block domain & escalate**

---

## Sample 2 — Business Email Compromise / Wire Transfer (Authority + Secrecy)

**Channel:** Email

```
From: CEO - STRICTLY CONFIDENTIAL <ceo.office@decodelabs-exec.com>
To: finance@decodelabs.tech
Subject: IMMEDIATE ACTION REQUIRED: Transfer Authorization

I'm traveling and tied up in back-to-back meetings, can't take calls right now.

I need you to process a wire transfer of $18,500 to a vendor today before close
of business. This is time-sensitive and must remain strictly confidential — do
not loop in anyone else on this, including the rest of finance.

I'll send the account details separately. Confirm you can action this now.

Thanks,
[CEO Name]
```

**Suspicious links/keywords:** "STRICTLY CONFIDENTIAL," "do not loop in anyone else,"
"traveling... can't take calls," urgency around same-day wire transfer.

**Red flags identified:**
1. **Sender-domain mismatch** — `decodelabs-exec.com` is not the real company domain.
2. **Urgent bypass request** — demands secrecy and explicitly asks to skip normal
   finance approval procedures.
3. **Unreachability excuse** — "can't take calls" removes the easiest way to verify
   (a phone call), which is a classic BEC tactic.
4. **Authority pressure** — impersonates the C-suite to discourage questioning.
5. **Financial request with no prior context** — no invoice, PO, or vendor history
   referenced.

**Why it's unsafe:** This matches the classic Business Email Compromise "lost wallet /
urgent wire" pattern from the training deck. Legitimate executives don't ask staff to
bypass approval workflows or keep transfers secret from their own team.

**Verdict:** 🔴 **Malicious → Block domain & escalate**

---

## Sample 3 — Fake Subscription Renewal / Callback Scam (TOAD)

**Channel:** Email

```
From: Microsoft Billing <billing@micro-soft-support.com>
To: a.raza@decodelabs.tech
Subject: Payment Overdue: Action Required to Avoid Service Suspension

Your Microsoft 365 subscription payment of $190.60 has failed.

To avoid suspension of your account and loss of access to your files, please
call our support line immediately:

1-800-XXX-XXXX

Have your account number ready. Lines are open 24/7.
```

**Suspicious links/keywords:** No hyperlink at all — only a phone number, "payment
failed," "avoid suspension," urgency to call immediately.

**Red flags identified:**
1. **No malicious link, only a phone number (TOAD — telephone-oriented attack
   delivery)** — this is designed to bypass email URL filters entirely by moving
   the attack to a live phone call.
2. **Lookalike sender domain** — `micro-soft-support.com` is not a Microsoft domain.
3. **Fabricated billing problem** with no invoice number, account details, or prior
   correspondence.
4. **Fear-based urgency** — threat of losing access to files.

**Why it's unsafe:** Calling the number connects the target to a scammer posing as
"support," who will then ask for payment details, remote access, or account
credentials over the phone — the classic callback scam described in the deck.

**Verdict:** 🔴 **Malicious → Block & escalate (report the number, do not call it)**

---

## Sample 4 — Legitimate Internal Email (Control Sample)

**Channel:** Email

```
From: Sarah Lee <sarah.lee@decodelabs.tech>
To: team@decodelabs.tech
Subject: Q3 Project Status Update - Non-Urgent

Hi Team,

Please review the attached project status for Q3 at your earliest convenience.
No immediate action is required.

Thanks,
Sarah

[Attachment: Q3_Status.pdf]
```

**Suspicious links/keywords:** None found.

**Checks performed:**
- Sender domain matches the real company domain (`decodelabs.tech`) exactly.
- No urgency, no request for credentials, money, or sensitive data.
- Attachment is a standard, named PDF with no unusual extension.
- Tone and content are consistent with routine internal communication.

**Why it's safe:** No red flags from the checklist are present — correct domain, no
pressure tactics, no unusual request, reasonable attachment type.

**Verdict:** 🟢 **Safe → Close, no action needed**
