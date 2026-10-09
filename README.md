# Sensor Data Validation Framework

## Overview

A Python-based validation framework for ingesting and validating sensor readings stored in JSON. The project focuses on structural validation, duplicate ID detection, and value-boundary checks to identify potentially invalid sensor measurements.

## Features

* **JSON ingestion:** Load sensor readings from JSON files.
* **Structural validation:** Check for required fields and duplicate measurement IDs.
* **Value validation:** Validate temperature, exposure, and focus error against predefined thresholds.
* **Error reporting:** Identify measurements that fall outside acceptable ranges.
* **Test data:** Use varied sensor readings to test validation behavior across normal, boundary, and invalid cases.

## Purpose

The project demonstrates practical data validation, input handling, and automated quality checks for sensor data, with an emphasis on producing clear and actionable validation results.

## Technologies
**Python, PyTest, Bash, GitHub Actions, Docker**

