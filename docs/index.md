# Agent Access Control Taxonomy

An open, vendor-neutral vocabulary for describing how AI agents are identified,
authorized, credentialed and audited.

Use it to classify an agent deployment, compare products on the same axes, or
write a policy that security, platform and AI teams all read the same way.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22806079.svg)](https://doi.org/10.5281/zenodo.22806079)

**DOI:** https://doi.org/10.5281/zenodo.22806079
**Canonical site:** https://agenticfabriq.github.io/agent-access-control-taxonomy/
**Maintainer:** [Agentic Fabriq](https://www.agenticfabriq.com/) · **Content:** CC BY 4.0 · **Code & schema:** Apache-2.0

---

## Why this exists

"Agent identity" currently means five different things depending on who's
selling. An API key in an env var, a service account, a workload identity, an
OAuth token delegated by a user, and a per-agent identity with its own policy
all get called the same thing. That makes RFPs, audits and architecture
reviews slower than they need to be.

This taxonomy splits the question into independent dimensions, so a deployment
is described by a record, not a label.

## Dimensions

| # | Dimension | Question it answers | File |
|---|---|---|---|
| 1 | Identity model | What is the agent, as far as the system is concerned? | [`taxonomy/identity-model.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/identity-model.yaml) |
| 2 | Delegation model | Whose authority is the agent acting with? | [`taxonomy/delegation-model.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/delegation-model.yaml) |
| 3 | Credential model | What secret does it present, and who holds it? | [`taxonomy/credential-model.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/credential-model.yaml) |
| 4 | Authorization model | How is each action decided? | [`taxonomy/authorization-model.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/authorization-model.yaml) |
| 5 | Enforcement point | Where is the decision enforced? | [`taxonomy/enforcement-point.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/enforcement-point.yaml) |
| 6 | Failure behavior | What happens when the decision can't be made? | [`taxonomy/failure-behavior.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/failure-behavior.yaml) |
| 7 | Human oversight | When does a person get involved? | [`taxonomy/human-oversight.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/human-oversight.yaml) |
| 8 | Audit granularity | What gets recorded, attributed to whom? | [`taxonomy/audit-granularity.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/audit-granularity.yaml) |
| 9 | Resource surface | What kinds of systems can the agent reach? | [`taxonomy/resource-surface.yaml`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/taxonomy/resource-surface.yaml) |

Each term has a stable ID (`aact:<dimension>/<term>`), a one-sentence
definition, inclusion and exclusion notes, and related terms.

## Classify a deployment

A deployment record validates against
[`schema/deployment-record.schema.json`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/schema/deployment-record.schema.json).
Worked examples live in [`examples/`](https://github.com/agenticfabriq/agent-access-control-taxonomy/tree/main/examples).

```yaml
id: example-internal-sales-agent
identity_model: aact:identity-model/per-agent-identity
delegation_model: aact:delegation-model/on-behalf-of-user
credential_model: aact:credential-model/brokered-short-lived-token
authorization_model: aact:authorization-model/per-action-policy
enforcement_point: [aact:enforcement-point/gateway]
failure_behavior: aact:failure-behavior/fail-closed
human_oversight: aact:human-oversight/approval-for-high-risk
audit_granularity: aact:audit-granularity/per-action-with-principal-chain
resource_surface: [aact:resource-surface/saas-api, aact:resource-surface/mcp-server]
```

## Scope and neutrality

- Terms describe **patterns**, not products. No term is named after a vendor.
- Where a product is used as an example, the example says which pattern it
  illustrates and links to the vendor's own documentation.
- Statements that come from a vendor's own marketing are labeled as
  first-party claims.
- The maintainer sells a product in this space. That's disclosed here, and
  corrections from anyone are welcome via issues or merge requests.

## How to cite

See [`CITATION.cff`](https://github.com/agenticfabriq/agent-access-control-taxonomy/blob/main/CITATION.cff). Cite the release tag you used; term IDs are
stable across minor versions.

## Related open references from the same maintainer

- [Agent Integration Playbook](https://agenticfabriq.github.io/): practical guides for OAuth, least privilege and failure modes
- [Agent Integration Scope Index](https://github.com/agenticfabriq/agent-integration-scope-index): minimum OAuth scopes per provider for common agent tasks
- [Text-to-SQL Evaluation Taxonomy](https://github.com/agenticfabriq/text-to-sql-evaluation-taxonomy)

## About the maintainer

Agentic Fabriq builds [Fabriq Enterprise](https://www.agenticfabriq.com/), a
control layer providing per-agent identity, user-scoped permissions and audit
for AI agents. This taxonomy is maintained independently of that product's
roadmap.
