# Bosch eBike Connect for Home Assistant 🚴

Custom Home Assistant integration for legacy Bosch eBike systems using **Bosch eBike Connect**, including support for older systems such as:

- Kiox (legacy, non 300/500)
- Bosch System 2
- Older Bosch eBike Connect devices

## Current status

⚠️ Early development / experimental

This project started as an attempt to bring support for legacy Bosch eBike Connect devices into Home Assistant. The newer Bosch Smart System already has integrations available, but older Kiox and Bosch eBike Connect systems are often left unsupported.

Current progress:

- [x] Home Assistant custom component structure
- [x] HACS support
- [ ] Bosch eBike Connect authentication
- [ ] Device discovery
- [ ] Sensor entities
- [ ] Configuration flow
- [ ] Diagnostics

## Planned sensors

Examples of sensors planned:

- Battery percentage 🔋
- Estimated range
- Odometer / total distance
- Speed
- Cadence
- Power
- Assistance level
- Torque
- Ride statistics

## Installation

### HACS (Custom Repository)

1. Open HACS
2. Open Custom repositories
3. Add:

```text
https://github.com/injectx/bosch-ebike-connect-ha
```

Type:

```text
Integration
```

4. Install
5. Restart Home Assistant

## Disclaimer

This project is unofficial and not affiliated with Bosch.

Bosch may change their APIs at any time which can affect functionality.

## Contributions

Pull requests, testing and feedback are welcome.