# Node.js Standard

## Purpose

This standard governs server-side JavaScript and TypeScript on Node.js 24 LTS.

## Runtime Policy

- Use an actively supported Node.js LTS release.
- Pin the intended runtime family in repository metadata.
- Keep the installed patch current with security releases.
- Do not use Current or nightly releases for production by default.
- Do not support end-of-life Node.js releases.
- Record runtime assumptions in completion evidence.

## ESM

New Node.js projects must use ESM unless a concrete requirement demands
CommonJS.

Requirements:

- Set `"type": "module"`.
- Use `import` and `export`.
- Use package `exports`.
- Include relative file extensions when required by Node ESM.
- Use `import.meta.url` rather than CommonJS globals.
- Do not mix `require` and ESM without an explicit interoperability boundary.

## Built-In Modules

Use `node:` specifiers:

```typescript
import { readFile } from "node:fs/promises";
import path from "node:path";
```

Prefer promise-based APIs.

Avoid synchronous filesystem and crypto work in request-serving paths.

## Environment Variables

Treat `process.env` as untrusted strings.

Requirements:

- Read environment variables in one configuration boundary.
- Validate required values at startup.
- Parse numbers and Booleans explicitly.
- Do not scatter environment access across business code.
- Do not log secret values.
- Use an `.env.example` only for safe placeholders.
- Do not require `.env` in production.

## Process Lifecycle

Handle:

- Startup validation
- `SIGTERM`
- `SIGINT` where appropriate
- Graceful shutdown
- In-flight work
- Owned server closing
- Database and queue clients
- Exit codes
- Unhandled failures

Do not use `process.exit()` before asynchronous cleanup completes unless the
process is irrecoverably unsafe.

Set `process.exitCode` when orderly shutdown can continue.

## Unhandled Errors

Treat these as defects:

- Unhandled promise rejections
- Uncaught exceptions
- EventEmitter `"error"` events without handling
- Stream errors
- Child-process errors

At the process boundary:

- Log safely.
- Begin controlled shutdown.
- Do not pretend the process is healthy after unknown state corruption.

Do not use global handlers as a substitute for local error handling.

## HTTP Servers

Define:

- Request timeout
- Header timeout
- Keep-alive behavior
- Maximum request size
- Graceful shutdown
- Proxy trust
- Connection limits
- Error handling

Do not accept unbounded bodies.

Do not trust forwarded headers from arbitrary clients.

## Outbound HTTP

Use a supported HTTP client or built-in `fetch`.

Requirements:

- Use `URL`.
- Apply timeout through `AbortSignal`.
- Validate target hosts for SSRF-sensitive flows.
- Bound response size.
- Handle redirects deliberately.
- Do not forward credentials across host changes.
- Propagate correlation safely.
- Retry only when operation semantics permit it.

## Streams

Use streams for large data.

Handle:

- Backpressure
- Errors
- Abort
- Cleanup
- Size limits
- Encoding

Prefer `pipeline` helpers.

Do not buffer unbounded content into memory.

## Filesystem

- Use `node:fs/promises`.
- Validate and normalize paths.
- Restrict user-controlled paths to approved roots.
- Handle symbolic links when boundaries matter.
- Use safe temporary directories.
- Clean up in `finally`.
- Avoid world-writable permissions.
- Do not execute uploaded or downloaded files without verification.

## Child Processes

- Prefer `spawn` or `execFile` with argument arrays.
- Avoid shell execution.
- Validate executable path and arguments.
- Do not include secrets in arguments.
- Bound output.
- Handle exit, error, timeout, and abort.
- Terminate owned child processes during shutdown.
- Do not use `exec` with untrusted strings.

## Worker Threads and Processes

Use worker threads for CPU-bound work when justified.

Use separate processes or external workers for isolation and durable ownership
when required.

Define:

- Concurrency
- Message schema
- Error behavior
- Shutdown
- Resource limits
- Restart behavior
- Observability

Do not use workers to hide blocking design without measurement.

## Timers

- Clear owned timers.
- Use unref only when process-lifetime behavior is understood.
- Avoid overlapping interval executions.
- Prefer recursive scheduled work when duration can exceed interval.
- Test time-sensitive behavior with controllable clocks.

## Node Permission Model

The Node permission model may provide defense in depth where supported.

Do not treat it as the sole security boundary.

Test required filesystem, network, and child-process access.

Keep Node patched because runtime security controls themselves can have defects.

## Packaging and Deployment

Document:

- Node version
- Package manager
- Lockfile
- Build output
- Runtime files
- Environment variables
- Ports
- Health checks
- Shutdown
- Persistent storage
- Native dependencies
- Container assumptions

Use production-only dependency installation for deployment artifacts where
appropriate.

## Guiding Rule

> Operate Node.js as a long-running production runtime with explicit limits, ownership, shutdown, and security boundaries.
