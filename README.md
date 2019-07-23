# About [![Copr build status](https://copr.fedorainfracloud.org/coprs/xvitaly/ecrepo/package/throttling-fix/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xvitaly/ecrepo/package/throttling-fix/)

Fixes throttling issues on supported laptops by explicitly setting correct power scheme.

Use with extremely caution! Incorrect usage can destroy your system.

# Supported laptops

  * Lenovo ThinkPad T480 series;
  * Lenovo ThinkPad T580 series.

# Installation

## Installation on T480 and T580

1. Enable COPR repository:
```
sudo dnf copr enable xvitaly/ecrepo
```

2. Enable systemd unit:
```
sudo systemctl enable --now throttling-fix-t480.service
```

3. Reboot.
