# JavaScript and TypeScript Observability Standard

## Purpose

This standard defines logging, metrics, tracing, health, browser telemetry, and
audit behavior.

Observability must help operators understand the system without leaking secrets
or creating unbounded cost.

## Signals

Use:

- Logs for discrete events
- Metrics for aggregate behavior
- Traces for request and dependency flow
- Health checks for instance state
- Audit events for security-sensitive changes
- Browser error and performance telemetry where appropriate

Do not put every fact into every signal.

## Structured Logging

Use a structured logger for applications.

Log named fields:

- Operation
- Outcome
- Duration
- Correlation
- Safe target identifier
- Error category

Avoid string concatenation and unstructured object dumping.

Libraries should not impose application logging globally.

## Log Levels

Use:

- trace
- debug
- info
- warn
- error
- fatal where the logger supports it

Do not log expected validation failures or aborts as errors unless operationally
significant.

## Error Logging

Log an error once at the boundary that owns handling and operational context.

Avoid logging and rethrowing at every layer.

Include the `Error` object safely.

Do not log secrets or full sensitive payloads.

## Correlation

Propagate correlation through:

- HTTP
- Messaging
- Background jobs
- Browser-to-server requests
- External services

Use standard trace context where available.

Bound untrusted correlation identifiers.

## Metrics

Metrics must be:

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
- Browser performance
- Business outcomes where appropriate

Do not use user IDs, emails, raw URLs, or request IDs as metric labels.

## Tracing

Instrument important boundaries:

- Incoming requests
- Outgoing HTTP
- Database
- Messaging
- Background jobs
- Critical browser interactions
- Server rendering

Use OpenTelemetry-compatible instrumentation where appropriate.

Do not capture sensitive payloads by default.

## Health Checks

Define:

- Liveness
- Readiness
- Dependency health

Liveness should not depend on every dependency.

Protect detailed diagnostics.

## Browser Telemetry

Collect only what is necessary.

Review:

- Consent
- Personal data
- URLs
- Query strings
- Session replay
- Source maps
- Stack traces
- Retention
- Third-party processors

Do not ship secrets in browser telemetry configuration.

## Audit Events

Audit:

- Authentication events
- Authorization denial
- Permission changes
- Administrative actions
- Destructive work
- Data export
- Secret or key changes
- Configuration changes

Include actor, action, target, outcome, time, and correlation.

Protect audit storage.

## Performance and Cost

Control:

- Log volume
- Sampling
- Retention
- Cardinality
- Payload size
- Stack-trace volume
- Browser beacon frequency

Do not enable verbose framework logging indiscriminately in production.

## Testing

Test:

- Structured fields
- Secret redaction
- Correlation
- Health states
- Audit creation
- Abort logging
- Browser error capture
- Metric cardinality constraints where practical

Avoid brittle assertions on full rendered log strings.

## Guiding Rule

> Emit enough structured evidence to operate and investigate the system, but no more sensitive or high-cardinality data than necessary.
