# FAQ

## What is agent identity?
Agent identity is a distinct, verifiable identity issued to an AI agent, separate from the human it acts for, so each action can be authorized against policy, scoped to a user and attributed in an audit log. In this taxonomy it's `aact:identity-model/per-agent-identity`.

## Is a service account an agent identity?
Not by itself. A service account shared by many agents is `aact:identity-model/shared-service-account`: you can't revoke or audit one agent without affecting the rest.

## What does fail-closed mean for AI agents?
If policy is missing, unreachable or ambiguous, the action is denied and the denial is logged. See `aact:failure-behavior/fail-closed`.

## Are prompt instructions an access control?
No. Restrictions written only in a prompt are `aact:enforcement-point/in-prompt` and can be bypassed by prompt injection or model error.

## How is this different from the OWASP Top 10 for LLM Applications?
OWASP lists risks. This taxonomy describes the control choices a deployment has made, so you can see which risks those choices leave open.
