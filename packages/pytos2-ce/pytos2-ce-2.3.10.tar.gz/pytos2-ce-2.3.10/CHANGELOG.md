# Changelog
All notable changes to this project will be documented in this file

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [2.3.9] - 2022-10-26
### Added
- Additional test data and tests
- Tox configuration for testing
### Changed
- BUGFIX: Fix duplicate target issue for Fortimanager when using multiple policies
- BUGFIX: Handle miissing singleServiceDTO.class_name for some Aur object results
- BUGFIX: Correct model for bindable objects
- BUGFIX: Correct issue with policies when device is ASA
## [2.3.8] - 2022-08-03
### API Changes
- Adds `AnyNetworkObject` mapping for SecureChange network objects.

## [2.3.7] - 2022-08-03
### API Changes
- Adds `HostNetworkObjectWithInterfaces` mapping for SecureChange network objects.

## [2.3.6] - 2022-08-03
### Fixes
- Fixes mismapped `Instruction.sources` and `Instruction.destinations`

## [2.3.5] - 2022-08-02
### API Changes
- Adds an `AnyService` mapping for service objects in `SlimRule`.
- Adds `comment`, `version_id`, `referenced`, `type_on_device`, `negate`, and `match_for_any` to `ServiceObject`

## [2.3.4] - 2022-08-02
### API Changes
- Adds a CloneServerPolicyRequest mapping to pytos2.securechange.fields
- Changes mapping type for `ServerDecommissionRequest.servers` from `IPObject` to `Object`

## [2.3.3] - 2022-08-01
### Fixes
- Changes mapping type for `ServerDecommissionRequest.servers` from `IPObject` to `Object`
- Updates cache when user not found in Scw.get_user(...)
- Handles "localuser" XSI type properly.
### API Changes
- Re-type several fields in SCWParty and SCWUser.
- Adds update_cache: bool to Scw.get_user(...)

## [2.3.2] - 2022-07-29
### Fixes
- Moves instruction mappings around.

## [2.3.1] - 2022-07-12
### Fixes
- Combines designer.Rule and rule.SlimRule
### API Changes
- Deprecates `SlimRule.source_networks` in favor of `SlimRule.source_objects`
- Deprecates `SlimRule.destination_networks` in favor of `SlimRule.destination_objects`
- Deprecates `SlimRule.destination_services` in favor of `SlimRule.services`
- Deprecates `designer.Rule`

## [2.3.0] - 2022-07-08
### Fixes
- Adds missing fields to SlimRule mapping
### API Changes
- Adds `TicketHistory` mappings

## [2.3.0] - 2022-08-11
### Added
- Added license
- Documentation updates
### Changed
- BUGFIX: Desginer/Verifier syntax error.

## [2.2.1] - 2021-12-23
- First public release!
