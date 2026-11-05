# Security policy

This project is a pre-registration research prototype. It has no released version yet.

To report a vulnerability, use **GitHub private security advisories** for this repository (Security tab, "Report a vulnerability"). Please do not put details in a public issue.

The full policy, including scope, what to expect, and the security design documents, is in [`docs/security/SECURITY.md`](docs/security/SECURITY.md).

Deployment modes (see [`docs/deployment-modes.md`](docs/deployment-modes.md)): the default is the command-line client with the rules engine only, with no network and no AI model. A local model is optional and off by default. Chat and private-cloud setups are the adopting organisation's choice and need pseudonymisation, TLS 1.3 and no-retention terms.

**WARNING: Never paste raw maintenance records into any chat or AI app. Use the command-line client, or a setup your organisation has approved.**

Intended purpose: advisory checker of maintenance records and work packages. Read-only. Does not certify, release, or determine airworthiness. A certifying human decides.
