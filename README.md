# Bosch eBike Connect for Home Assistant

Custom Home Assistant integration for older Bosch eBike systems using the Bosch eBike Connect platform.

Supports Bosch System 2 devices such as:

- Kiox (non 300/500)
- Bosch eBike Connect app
- Performance Line CX
- PowerTube batteries
- Other Bosch Connect compatible systems

## Features

Current functionality:

✅ Login using Bosch eBike Connect account  
✅ Automatic device discovery  
✅ Home Assistant device registration  
✅ Bike information sensors:

- Bike name
- Motor
- Display
- Battery model

## Planned

Potential future features:

- Trip history
- Last ride statistics
- Distance tracking
- Average speed
- Elevation gain
- Ride summaries
- Additional metadata sensors

## Installation

### HACS

1. Open HACS
2. Go to Integrations
3. Click the three dots in the top-right corner
4. Select "Custom repositories"
5. Add:

```
https://github.com/injectx/bosch-ebike-connect-ha
```

Category:

```
Integration
```

6. Install Bosch eBike Connect
7. Restart Home Assistant
8. Add the integration from Devices & Services

## Configuration

Enter:

- Bosch eBike Connect email
- Bosch eBike Connect password

## Notes

This integration is intended for older Bosch systems using the Bosch eBike Connect app.

It does not currently support Bosch Flow based systems.

Some live values such as battery percentage, cadence and real-time bike telemetry may not be exposed through the Bosch Connect cloud API.

## Disclaimer

This project is unofficial and is not affiliated with Bosch.

## Credits

Based on reverse engineering and inspiration from:

- TA2k ioBroker Bosch eBike adapter
- Bosch eBike Connect platform