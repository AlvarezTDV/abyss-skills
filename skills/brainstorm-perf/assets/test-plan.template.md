# Performance plan — {{ID}}

Idea: [{{title}}]({{idea_path}})
Run: {{run_identifier}}
Execution: pending authorization

## Hypothesis
{{Specific suspected effect, origin of suspicion, flow and user-relevant problem criterion.}}

## Design
- Scenarios and volumes: {{representative_workloads}}
- Data source and characterization: {{safe_reference_not_raw_records}}
- Isolation controls: {{verified_or_missing_controls}}
- Metrics, repetitions and noise handling: {{method}}
- Tools and versions: {{available_tools_or_missing}}
- Time, memory, request and cost limits: {{bounds_and_stop_conditions}}
- Differences from the real environment: {{limitations}}

## Access and consent
- Original files/data: no modifications; {{baseline_integrity_checks}}.
- Services/destinations: {{none_or_exact_authorized_environment}}.
- Operations and credential/session method: {{scope_without_secret_values}}.
- Temporary writes: {{none_or_separately_authorized_test_environment_scope}}.
- Possible effects, costs and residuals: {{disclosure}}.
- User authorization: {{pending_or_exact_confirmed_scope_and_date}}.

## Reproduction
1. {{approved_preparation}}
2. {{approved_measurement_commands_no_secrets}}
3. {{post_execution_integrity_checks}}

## Cleanup plan
{{Owned_resources_only, verification_operations, retained_sanitized_evidence, sensitive_copy_disposal_and_known_or_uncertain_residuals.}}
