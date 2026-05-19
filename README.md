# Bosch eBike Connect for Home Assistant

<p align="center">
  <img src="images/logo.png" width="150">
</p>

Custom Home Assistant integration for Bosch eBike systems using the Bosch eBike Connect platform.

Supports older Bosch systems such as:

- Kiox (non 300/500)
- Bosch eBike Connect app
- Performance Line CX
- PowerTube batteries
- Bosch System 2 compatible bikes

## Features

Current functionality:

### Bike information

✅ Automatic Bosch device discovery  
✅ Home Assistant device registration  
✅ Bike metadata sensors

Available sensors:

- Bike Name
- Motor
- Display
- Battery model

### Last Ride statistics

✅ Ride history retrieval  
✅ Automatic ride segment aggregation  
✅ Dedicated Last Ride device

Available sensors:

- Last Ride Distance
- Last Ride Duration
- Last Ride Average Speed
- Last Ride Maximum Speed
- Last Ride Calories
- Last Ride Location

## Installation

### HACS

1. Open HACS
2. Go to Integrations
3. Open the three-dot menu
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
8. Add the integration via Devices & Services

## Configuration

Enter:

- Bosch eBike Connect email
- Bosch eBike Connect password

## Notes

This integration currently targets Bosch systems using the Bosch eBike Connect platform.

Not currently supported:

- Bosch Flow app systems
- Kiox 300
- Kiox 500
- Smart System devices

Some live bike telemetry appears unavailable through the Bosch Connect cloud API:

- Live battery percentage
- Cadence
- Real-time speed
- Current motor power

## Planned

Potential future features:

- Ride history entities
- Total distance statistics
- Ride maps (if GPS coordinates are available)
- Additional ride analytics
- Activity dashboards

## Disclaimer

This project is unofficial and is not affiliated with Bosch.

## Credits

Based on inspiration and reverse engineering work from:

- TA2k ioBroker Bosch eBike adapter
- Bosch eBike Connect platform