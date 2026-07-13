---
id: SCHEMA-EXT-001
title: Schema Extension Policy
version: 0.2.0
status: baseline
---

# Schema Extension Policy

## Default rule

Top-level schema objects remain closed with `additionalProperties: false`.

Custom fields must be placed under the optional `extensions` object.

## Extension keys

Use namespaced keys such as:

```json
{
  "extensions": {
    "example.org.ticketId": "CHG-1234",
    "example.org.ownerTeam": "platform-engineering"
  }
}
```

Do not use vague keys such as `custom`, `misc`, or `extraData`.

## Prohibited extensions

Extensions must not:

- redefine a standard field
- weaken a required control
- hide validation failure
- contain secrets or unrestricted sensitive data
- impersonate approval or evidence
- change the meaning of the standard status, risk, or result fields
- create an undocumented second contract

## Promoting an extension

Promote an extension to a standard property only when:

- multiple consumers need it
- ownership and meaning are stable
- compatibility is analyzed
- examples and migration guidance exist
- a schema version decision is recorded
