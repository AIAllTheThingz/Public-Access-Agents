# PowerShell Security Standard

## Purpose

This standard defines security requirements for PowerShell 7.x code.

Security requirements apply to code, tests, configuration, documentation, logging, deployment examples, and completion evidence.

The standard assumes all external input is untrusted until validated.

## Core Security Principles

- Default deny when authorization or target identity is ambiguous.
- Use least privilege.
- Separate discovery from modification.
- Validate before use.
- Minimize trust boundaries.
- Minimize secret exposure.
- Preserve TLS and certificate validation.
- Prefer idempotent, reversible actions.
- Record enough evidence for audit without logging secrets.
- Fail safely.
- Do not weaken controls for convenience.

## Secrets

Never hardcode or commit:

- Passwords
- API keys
- Access tokens
- Refresh tokens
- Private keys
- Client secrets
- Connection strings containing credentials
- Session cookies
- Recovery codes
- Secret answers
- Production certificate material

Do not place secrets in:

- Source code
- Test fixtures
- Documentation examples
- Logs
- Reports
- Error messages
- Command history instructions
- Process arguments when safer mechanisms exist
- Temporary files without protection

Use approved secret stores, environment injection, secure platform APIs, or `[PSCredential]` as appropriate.

## Credential Handling

Use `[PSCredential]` for username and password credentials.

Requirements:

- Do not convert secure values to plaintext unless a required integration leaves no alternative.
- Keep plaintext exposure as short as possible.
- Do not write credential objects to output.
- Do not serialize credentials into reports.
- Do not cache credentials in global variables.
- Do not embed credentials in URI strings.
- Do not include secrets in native-command arguments when an input stream, file descriptor, environment mechanism, or provider is safer.
- Redact credential identifiers when they are sensitive.
- Document interactive and unattended authentication behavior.

A `SecureString` is not automatically portable secret storage.

## Secret Redaction

Logs, errors, verbose output, and reports must redact:

- Tokens
- Passwords
- Authorization headers
- Cookies
- Private-key material
- Sensitive query parameters
- Secret configuration properties

Redaction must occur before serialization.

Do not rely on users to avoid enabling `-Verbose`.

## Configuration Security

Environment-specific values must not be hardcoded.

Configuration must be validated for:

- Required properties
- Data types
- Allowed values
- Path safety
- URI scheme
- Host allowlists where appropriate
- Secret references
- Unknown properties when strict schemas are required

Treat PSD1 carefully. PowerShell data files can contain limited expressions. Do not treat untrusted PSD1 content as inert text.

Sample configuration must use fictitious values.

## Input Validation

Validate external input before it reaches:

- File operations
- Registry operations
- Native commands
- Remote commands
- API calls
- SQL queries
- Directory-service queries
- Service changes
- Scheduled-task changes
- Process execution
- Destructive operations

Validation should use allowlists when practical.

Reject input that is:

- Null or empty when not allowed
- Outside an expected range
- Outside an approved path
- An unsupported URI scheme
- An unexpected host
- A dangerous wildcard
- A control character
- A shell metacharacter in a constrained field
- An unapproved enum or mode
- An arbitrary script block
- A malformed identifier

Validation must match the actual security boundary. Pattern matching alone is not always sufficient.

## Path Security

Before modifying or deleting paths:

- Resolve the intended path.
- Use `-LiteralPath` unless wildcard behavior is required.
- Reject empty paths.
- Reject root paths.
- Reject parent traversal outside the approved root.
- Reject reparse points or symbolic links when they could escape the approved root.
- Verify file versus directory expectations.
- Verify the target belongs to the intended operation.
- Use `ShouldProcess`.
- Verify the result.

Do not concatenate untrusted strings into file paths without normalization and boundary checks.

## Command Injection

Do not use `Invoke-Expression` by default.

Do not construct executable command strings from untrusted input.

For native commands:

- Pass the executable separately.
- Pass each argument as a discrete value.
- Validate values.
- Test spaces, quotes, Unicode, and shell metacharacters.
- Avoid invoking an intermediate shell unless required.
- Check exit codes.

For PowerShell commands, call functions and cmdlets directly with named parameters.

## Native Executables

Before invoking a native executable:

- Resolve the expected executable path.
- Avoid relying on an untrusted current directory.
- Avoid path hijacking.
- Verify origin or signature when supply-chain risk warrants it.
- Pass arguments safely.
- Capture standard output and standard error intentionally.
- Check `$LASTEXITCODE`.
- Do not expose secrets in process listings.

Do not download an executable and immediately run it without verification.

## Remote Code and Downloads

Remote content must not be executed automatically.

Before using downloaded content:

- Use HTTPS.
- Preserve certificate validation.
- Verify trusted source.
- Verify checksum or signature where available.
- Store in a controlled location.
- Inspect or validate content.
- Require explicit authorization before execution.
- Document version and origin.

Avoid piping web responses directly into PowerShell execution.

## TLS and Certificates

Do not:

- Disable certificate validation
- Accept all certificates
- Ignore hostname mismatch
- Downgrade TLS without explicit requirement
- Trust self-signed certificates silently
- Modify global certificate-validation callbacks

When private PKI or self-signed certificates are required, install or reference the appropriate trust chain through an approved process.

Document certificate prerequisites and expected validation behavior.

## Least Privilege

Do not require administrator or root privileges unless required.

Requirements:

- Detect required privilege early.
- Fail with an actionable message.
- Separate privileged from non-privileged operations.
- Use scoped permissions.
- Avoid broad directory, registry, cloud, or API permissions.
- Do not grant permissions as a side effect unless explicitly required.
- Do not bypass access controls.

Document required roles, rights, or scopes.

## State-Changing Operations

All state-changing operations must:

- Validate target identity.
- Validate current state.
- Use `SupportsShouldProcess`.
- Use `$PSCmdlet.ShouldProcess()`.
- Respect `-WhatIf`.
- Respect `-Confirm`.
- Use explicit high-risk execution opt-in when appropriate.
- Be idempotent where practical.
- Verify resulting state.
- Report partial failures.
- Avoid broad wildcard targets.
- Avoid default destructive behavior.

High-risk examples include:

- Deletion
- Bulk modification
- Reboot
- Service interruption
- Permission changes
- Identity changes
- Certificate removal
- Firewall changes
- Remote execution across many systems
- Data migration
- Resource destruction

## Confirmation and Non-Interactive Execution

Interactive confirmation is not a substitute for safe design.

For unattended automation:

- Use explicit execution mode.
- Require validated configuration.
- Avoid prompts.
- Preserve `ShouldProcess`.
- Use approval mechanisms outside the script when required.
- Log authorization context without secrets.
- Fail rather than assume.

Do not add a `-Force` switch that disables all safety validation.

## Idempotency and Verification

State-changing code should:

1. Discover current state.
2. Compare with desired state.
3. Modify only what differs.
4. Verify resulting state.
5. Return whether a change occurred.

Do not report success before verification.

When rollback is not possible, document irreversibility and require stronger authorization.

## Remoting

For PowerShell remoting:

- Validate target names.
- Use approved authentication.
- Avoid embedding credentials.
- Use encrypted transport appropriate to the environment.
- Limit endpoints and session configuration.
- Close sessions.
- Pass only required variables.
- Do not send secret values to untrusted targets.
- Avoid broad delegation.
- Document CredSSP or delegation requirements and risks.
- Validate remote module availability.
- Treat remote output as untrusted input.

Do not enable remoting or modify trust settings automatically unless explicitly required.

## API Security

For REST or other API calls:

- Use HTTPS.
- Validate certificate and hostname.
- Use scoped tokens.
- Avoid tokens in query strings.
- Set timeouts.
- Handle pagination.
- Handle rate limits.
- Avoid logging authorization headers.
- Validate response schema.
- Treat response content as untrusted.
- Restrict redirects when they could leak credentials.
- Avoid automatic retry of non-idempotent state-changing requests unless the API provides an idempotency mechanism.

Document authentication flow and required scopes.

## Database Security

When interacting with databases:

- Use parameterized queries.
- Do not concatenate untrusted values into query text.
- Use least-privileged accounts.
- Avoid embedding connection credentials.
- Validate target database and schema.
- Use transactions where appropriate.
- Handle partial failure.
- Avoid logging sensitive query parameters.
- Document connection encryption requirements.

## Logging and Audit

Logs should include:

- Timestamp
- Operation
- Target
- Outcome
- Correlation or job identifier when applicable
- Error category
- Whether a change occurred

Logs must not include:

- Passwords
- Tokens
- Authorization headers
- Private keys
- Sensitive personal data unless explicitly required and protected
- Full credential objects
- Secret configuration

Use UTC and ISO 8601 for machine-consumed timestamps.

Ensure logs do not falsely report an action under `-WhatIf`.

## Temporary Files

Temporary files must:

- Use controlled locations
- Use unpredictable names when collision or tampering matters
- Avoid secrets when possible
- Use restrictive permissions when sensitive
- Be cleaned up in `finally`
- Not be executed unless explicitly verified
- Not be committed
- Not be placed in source directories

If cleanup fails, report it.

## Serialization and Reports

Before exporting objects:

- Remove secrets.
- Remove credential objects.
- Remove raw headers and tokens.
- Limit sensitive fields.
- Use appropriate file permissions.
- Avoid insecure formats for secret storage.
- Document report location and retention expectations.

Do not assume JSON, XML, or CSV protects sensitive data.

## Code Signing Compatibility

Generated PowerShell code should remain compatible with Authenticode signing.

Do not:

- Self-modify after signing
- Require runtime rewriting of signed files
- Append operational data to source files
- Generate temporary script files merely for execution unless explicitly documented
- Disable signature validation

When code signing is required, document:

- Code Signing EKU
- Signing command
- Timestamping
- Signature validation
- Trust-chain requirements
- Effects of modifying signed files
- Execution-policy considerations

Code signing does not replace testing, authorization, or secure configuration.

## Supply-Chain Security

Before adding a dependency:

- Confirm it is necessary.
- Prefer trusted sources.
- Record the module name and minimum version.
- Review maintenance status.
- Review required permissions.
- Review transitive dependencies.
- Pin or constrain versions when reproducibility matters.
- Avoid automatic trust changes.
- Avoid automatic installation during normal execution.

Do not add a dependency merely to save a few lines of maintainable built-in code.

## PSScriptAnalyzer and Security Rules

Run PSScriptAnalyzer.

Do not suppress security-related findings broadly.

Any suppression must document:

- Rule
- Reason
- Scope
- Risk
- Mitigation
- Removal condition

## Security Testing

Test, where applicable:

- Dangerous path rejection
- Command-injection rejection
- Secret redaction
- `WhatIf` suppression
- Privilege checks
- Certificate validation behavior
- Unsupported URI schemes
- Untrusted script-block rejection
- Non-zero native-command exits
- API failure and timeout
- Partial failure
- Idempotent repeated execution
- Safe cleanup

## Exception Process

A security exception requires:

- Explicit requirement
- Threat or risk description
- Safer alternatives considered
- Reason alternatives are insufficient
- Narrow implementation scope
- Mitigation
- Test evidence
- Documentation
- Review or expiration condition

The agent must not create an exception merely because the secure implementation is more work.

## Prohibited Claims

Do not claim code is:

- Secure
- Hardened
- Production ready
- Compliant
- Zero trust
- Safe for all environments

without defined criteria and supporting evidence.

## Guiding Rule

> When security, authorization, or target identity is uncertain, make no change and report what must be resolved.
