#!/bin/bash

# Intro message
echo "Data Collector Script"
echo "---------------------"
echo "This script captures system data using ps aux, netstat, and vmstat commands."
echo "The captured data is saved to files for analysis using the Python script 'anomaly_detection.py'."

# Set default timer (1 hour)
TIMER=3600

# Ask user for custom timer (optional)
echo "Enter custom capture duration (seconds) or press Enter for default (1 hour):"
read CUSTOM_TIMER
if [ -n "$CUSTOM_TIMER" ]; then
  TIMER=$CUSTOM_TIMER
fi

# Set output file names
PS_OUTPUT="ps_aux_data.txt"
NETSTAT_OUTPUT="netstat_data.txt"
VMSTAT_OUTPUT="vmstat_data.txt"

# Inform user about data capture
echo "Starting data capture for $TIMER seconds..."
echo "Capturing ps aux data..."
ps aux > $PS_OUTPUT &
echo " Done!"

echo "Capturing netstat data..."
netstat -anp > $NETSTAT_OUTPUT &
echo " Done!"

echo "Capturing vmstat data..."
vm_stat -c $TIMER > $VMSTAT_OUTPUT &
echo " Done!"

# Wait for the timer to expire
echo "Waiting for $TIMER seconds..."
sleep $TIMER

# Inform user about data capture completion
echo "Data capture complete!"
echo "Output files: $PS_OUTPUT, $NETSTAT_OUTPUT, $VMSTAT_OUTPUT"

# Error handling
if [ $? -ne 0 ]; then
  echo "Error occurred during data capture. Please check output files for errors."
fi