# .NET Observability Standard

## Purpose

This standard defines logging, metrics, tracing, health checks, audit events, and operational diagnostics.

Observability must help operators understand behavior without leaking secrets or creating uncontrolled cost.

## Signals

Use:

- Logs for discrete diagnostic and operational events
- Metrics for aggregated system behavior
- Traces for request and dependency flow
- Health checks for instance and dependency status
- Audit events for security-relevant actions

Do not force every fact into every signal.

## Structured Logging

Use message templates with named properties.

Prefer:

```csharp
logger.LogInformation(
    "Processed {RecordCount} records for job {JobId}",
    recordCount,
    jobId);
```

Avoid interpolation:

```csharp
logger.LogInformation($"Processed {recordCount} records for job {jobId}");
```

Do not log sensitive values.

## Log Levels

Use levels consistently:

- Trace: extremely detailed diagnostics
- Debug: developer diagnostics
- Information: normal significant events
- Warning: abnormal but recoverable behavior
- Error: operation failure requiring attention
- Critical: application or system-wide failure

Do not log routine expected validation failures as errors unless operationally significant.

Do not log expected cancellation as an error.

## Exception Logging

Log an exception once at the boundary that owns handling and operational context.

Avoid logging and rethrowing at every layer.

Include:

- Operation
- Safe target identifier
- Correlation
- Outcome
- Exception object

Do not include secrets.

## Correlation

Propagate correlation through:

- HTTP
- Messaging
- Background jobs
- External requests
- Audit events

Use established trace context where available.

Do not accept arbitrary untrusted correlation values without length and format limits.

## Metrics

Metrics should be:

- Low cardinality
- Stable
- Actionable
- Documented

Measure:

- Request rate
- Error rate
- Duration
- Queue depth
- Processing rate
- Retry count
- Dependency latency
- Resource saturation
- Business outcomes where appropriate

Do not use user IDs, request IDs, emails, or unbounded paths as metric labels.

## Tracing

Instrument important boundaries:

- Incoming requests
- Outgoing HTTP
- Database
- Messaging
- Background jobs
- Critical internal operations

Use OpenTelemetry-compatible instrumentation where appropriate.

Avoid recording sensitive payloads.

Sample intentionally.

## Health Checks

Define:

- Liveness
- Readiness
- Dependency status

Liveness should not depend on every external service.

Readiness should represent ability to serve traffic.

Protect detailed diagnostics.

Do not expose secrets or internal topology publicly.

## Audit Events

Audit security-sensitive actions such as:

- Authentication events
- Authorization denial
- Permission changes
- Data export
- Administrative operations
- Destructive actions
- Secret or key changes
- Configuration changes

Audit events should include:

- Actor
- Action
- Target
- Outcome
- Time
- Correlation
- Source where appropriate

Minimize personal data and protect audit storage.

## Background Services

Expose:

- Last successful run
- Last failure
- Current state
- Queue depth
- Processing duration
- Retry count
- Poison-message count
- Shutdown behavior

Do not rely solely on one startup log entry.

## External Dependencies

Record safe operational context:

- Dependency name
- Operation
- Duration
- Outcome
- Retry
- Circuit state when applicable

Do not log full URLs containing tokens or sensitive query strings.

## Performance and Cost

Control:

- Verbosity
- Sampling
- Retention
- Cardinality
- Payload size
- Stack-trace volume

Do not enable verbose framework logs indiscriminately in production.

## Privacy and Redaction

Classify fields before logging.

Redact:

- Credentials
- Tokens
- Cookies
- Authorization headers
- Private keys
- Sensitive personal data
- Full request or response bodies by default

Do not assume telemetry backends are less sensitive than databases.

## Testing

Test:

- Structured property names
- Secret redaction
- Log level for critical behavior
- Correlation propagation
- Health-check states
- Metric cardinality constraints where practical
- Audit event creation
- Expected cancellation behavior

Avoid brittle assertions on complete human-readable log strings.

## Documentation

Document:

- Signal names
- Metric units
- Dimensions
- Health semantics
- Alert expectations
- Audit retention
- Redaction policy
- Sampling
- Operator troubleshooting path

## Guiding Rule

> Emit enough structured evidence to operate and investigate the system, but no more sensitive or high-cardinality data than necessary.
