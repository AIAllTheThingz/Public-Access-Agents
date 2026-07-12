# Web Front-End Standard

## Purpose

This standard governs browser-based JavaScript and TypeScript applications,
independent of a specific UI framework.

## Browser Support

Declare supported browsers.

Do not add legacy transpilation or polyfills without an explicit support
requirement.

Use a maintained browserslist or equivalent policy where tooling requires it.

Do not claim compatibility without browser testing.

## Component Design

Components should:

- Have one clear responsibility.
- Keep rendering separate from data access where practical.
- Accept explicit inputs.
- Emit explicit events or callbacks.
- Avoid hidden global state.
- Keep side effects controlled.
- Handle loading, empty, error, and success states.
- Preserve accessibility.

Do not create a universal component abstraction before real reuse exists.

## State

Use the smallest state scope that works:

- Local component state
- Shared feature state
- URL state
- Server cache
- Persistent browser storage

Do not place all state in a global store by default.

Do not duplicate server state unnecessarily.

Document persistence and invalidation.

## DOM Safety

- Prefer text APIs and framework escaping.
- Do not use `innerHTML` or equivalent unsafe HTML injection with untrusted data.
- Sanitize trusted-rich-text inputs with a maintained sanitizer.
- Avoid inline event-handler strings.
- Use Content Security Policy compatible patterns.

## Accessibility

Meet applicable accessibility requirements.

At minimum:

- Semantic HTML
- Keyboard operation
- Visible focus
- Labels
- Error association
- Appropriate ARIA only when native semantics are insufficient
- Sufficient contrast
- Reduced-motion support where animation exists
- Screen-reader testing for critical flows

Do not treat automated accessibility checks as complete coverage.

## Forms

- Use semantic controls.
- Validate on server and client.
- Preserve entered values after recoverable errors.
- Provide clear errors.
- Do not disable paste in credential fields.
- Use correct autocomplete attributes.
- Prevent accidental duplicate submission.
- Handle slow networks and retries.

Client validation is a usability feature, not a trust boundary.

## Networking

- Use an API client boundary.
- Apply cancellation to obsolete requests.
- Handle timeout.
- Handle offline and retry states.
- Avoid duplicate requests.
- Do not expose secrets to browser code.
- Avoid storing sensitive tokens in unsafe browser storage.
- Protect against cross-origin data leakage.

## Authentication

Browser code may reflect authentication state but must not be the sole
authorization control.

Use secure cookie or token patterns appropriate to the architecture.

Protect against:

- XSS token theft
- CSRF
- Open redirects
- Clickjacking
- Session fixation
- Cross-tab state confusion

## Routing and URL State

Use URLs for shareable navigation state where appropriate.

Validate route parameters.

Do not place secrets in URLs.

Handle unknown routes.

Preserve back and forward navigation.

## Performance

Measure before claiming improvement.

Consider:

- Bundle size
- Code splitting
- Lazy loading
- Image loading
- Rendering frequency
- Network waterfalls
- Cache policy
- Hydration
- Long tasks
- Memory leaks

Do not optimize by destroying readability without evidence.

## Browser Storage

Treat localStorage, sessionStorage, IndexedDB, and cookies as untrusted
persistence.

- Validate values on read.
- Version stored schemas.
- Do not store secrets unnecessarily.
- Handle quota and privacy modes.
- Define retention.
- Clear obsolete state.
- Avoid cross-user leakage on shared devices.

## Service Workers

Use service workers only with a defined offline, caching, or update requirement.

Document:

- Cache versioning
- Update behavior
- Offline behavior
- Data sensitivity
- Rollback
- Storage cleanup

Incorrect service-worker caching can preserve broken applications with
impressive persistence.

## Error Handling

Provide safe user-facing errors.

Capture diagnostic context without personal data or secrets.

Use error boundaries or equivalent framework mechanisms for critical UI areas.

Do not expose stack traces to users.

## Testing

Test:

- User-visible behavior
- Keyboard access
- Validation
- Loading and error states
- Authentication transitions
- Routing
- Responsive behavior
- Browser compatibility
- XSS-sensitive rendering
- Critical accessibility flows

Prefer tests through user-observable behavior over component internals.

## Guiding Rule

> Browser code must remain accessible, secure, resilient to slow or failed networks, and subordinate to server-side trust boundaries.
