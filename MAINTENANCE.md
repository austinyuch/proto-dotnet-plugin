# Maintenance and trust boundaries

Owner: austinyuch. Upstream: RemiKalbe/proto-dotnet-plugin.
Initial upstream revision: d27613b0a2c86fbdc37223f4b75e28d6e10df214.
Reviewed plugin SHA-256: `769673f5163e639c4e05886f77ce4c2791e952c5c5f37044e21d47f5e04166b6`.

## Updates

Fetch upstream changes into a review branch; never automatically merge them.
Review plugin download URLs, executable paths, version detection, and any hooks.
Retain Microsoft SDK downloads. If plugin bytes change, review the change before
updating APPROVED_SHA256 in the wrapper. The wrapper itself must also be reviewed.
Test a pinned SDK version in a disposable environment, then publish the reviewed
commit and explicitly update consumers with its full commit SHA.
No automatic upstream sync or SDK installation is configured.

## Rollback

The wrapper prints a timestamped `~/.prototools.backup-*` path before mutation.
Restore that exact file to `~/.prototools` and run `proto_activate` in Bash.
No existing SDKs or system runtimes are removed.

## Security limits

Fork and commit pinning protect plugin selection, not the entire supply chain.
The plugin currently declares no SDK checksum; independent verification of SDK
archives against Microsoft's release metadata remains a control gap.
Trust in GitHub, proto, Microsoft, the local Python interpreter and this account
remains. Hash verification only covers plugin.toml, not the wrapper or SDK.
Branch protection, MFA and maintainer access must be managed separately.
No CI/SAST gate is configured in this initial wrapper; syntax and negative-path
checks are local validation and are not a SAST result.

## Checks

Run `python3 -m py_compile scripts/configure_proto.py` and verify that branch names,
short SHAs and unexpected plugin bytes are rejected. Use dry-run before applying.
