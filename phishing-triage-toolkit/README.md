# Phishing Awareness & Triage Toolkit

**DecodeLabs Cyber Security Training — Project 3 (Industrial Training Kit, Batch 2026)**

A phishing detection and triage project built as part of a cybersecurity training
track. The goal: analyze sample messages for phishing indicators, document the red
flags found, and build a simple triage system that lets even a non-expert employee
decide, in under a minute, whether a message is safe, suspicious, or malicious.

## Why this project

80% of security breaches start with phishing, and attackers only need about 82
seconds on average to get their first click. Technical firewalls alone can't stop
that — the user is the real perimeter. This project builds the "human firewall"
skill set: reading a message the way an attacker built it, spotting the disguise,
and knowing what to do next.

## Repository structure

```
phishing-triage-toolkit/
├── README.md
├── samples/
│   └── sample_analysis.md      # 3 phishing samples + 1 legitimate control,
│                                # each broken down by red flag and verdict
├── checklist/
│   └── triage-checklist.md     # Non-expert, step-by-step triage checklist
└── decision-tree/
    └── decision-tree.md        # Visual (Mermaid) + text decision tree for
                                 # classifying a message as Safe / Suspicious /
                                 # Malicious, with the resulting action
```

## What's inside

- **`samples/sample_analysis.md`** — Four worked examples: a fake IT password-reset
  email (urgency + domain spoofing), a Business Email Compromise wire-transfer
  request (authority + secrecy), a callback/TOAD scam (phone-only lure, no link),
  and one legitimate email used as a control to show what a clean message looks
  like. Each sample lists the suspicious links/keywords, the specific red flags,
  a plain-language explanation of why it's unsafe (or safe), and a final verdict.

- **`checklist/triage-checklist.md`** — A four-step checklist (sender, tone, content,
  decision) that translates the red-flag patterns into simple yes/no questions
  anyone can run through without security training.

- **`decision-tree/decision-tree.md`** — The same logic as a decision tree, so a
  triage event always ends in one of three concrete outcomes: **Close** (safe),
  **Warn User** (suspicious — verify out of band), or **Block & Escalate**
  (malicious).

## Key skills demonstrated

Threat analysis, social-engineering pattern recognition (authority, urgency,
curiosity, fear/greed), domain-spoofing detection (typosquatting, homoglyphs,
subdomain traps), and security-awareness process design (Pause → Verify → Report).

## How to use this

1. Read `samples/sample_analysis.md` to see the reasoning applied to real-style
   examples.
2. Use `checklist/triage-checklist.md` as a quick-reference sheet for evaluating
   a new suspicious message.
3. Follow `decision-tree/decision-tree.md` when you need a clear, repeatable
   process to land on Safe / Suspicious / Malicious and the matching action.

## The golden rule

**Pause. Verify. Report.**
Never verify a suspicious request using contact details taken from the suspicious
message itself — always use a channel you already know to be legitimate.

---
*Built as part of the DecodeLabs Cyber Security Industrial Training Kit, 2026.*
