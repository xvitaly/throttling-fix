#!/usr/bin/sh
set -e

echo 63BE270F-1C11-48FD-A6F7-3AF253FF3E2D > /sys/devices/platform/INT3400:00/uuids/current_uuid
echo enabled > /sys/class/thermal/thermal_zone1/mode
