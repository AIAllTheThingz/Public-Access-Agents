---
id: TF-CODE-001
status: baseline
title: Terraform and OpenTofu Coding Standard
---

# Terraform and OpenTofu Coding Standard

- Format all HCL with the declared engine.
- Use descriptive resource, variable, local, module, and output names.
- Keep configuration deterministic and avoid dependence on unstable ordering.
- Define variable types, descriptions, validation, sensitivity, and safe defaults.
- Mark sensitive outputs appropriately and expose only required values.
- Avoid provisioners when provider-native or image-based approaches exist.
- Use `for_each` or `count` deliberately and preserve stable resource addressing.
- Keep environment values outside reusable modules.
- Do not reformat or refactor unrelated infrastructure.
