# Duplicate File Removal Automation Script

This Python script is designed to remove duplicate files from a specified directory based on their checksums. It also creates a log file to maintain the names of the deleted duplicate files and sends an email notification with statistics about the operation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Command Line Options](#command-line-options)

## Introduction

When dealing with large datasets or directories, it's common to have duplicate files that take up unnecessary space. This script provides an automated solution to find and remove duplicate files based on their checksums.

## Features

- Accepts input through the command line or configuration file.
- Logs messages in a log file instead of the console.
- Organizes tasks into separate functions for better maintainability.
- Performs validations before taking any actions.
- Utilizes user-defined modules to store functionality.
- Provides email notifications with statistics about the operation.

## Usage

To use this script, follow the instructions below:
Run the script using the following command-line options:
bash
Copy code
python DuplicateFileRemoval.py [directory_path] [log_interval] [receiver_email]
[directory_path]: Absolute path of the directory containing potential duplicate files.
[log_interval]: The interval (in minutes) for log file naming based on date and time.
[receiver_email]: Email address of the recipient for the log file.
Follow the on-screen prompts for email credentials and confirmation.

## Command Line Options

DuplicateFileRemoval.py: Name of the Python automation script.
[directory_path]: Absolute path of the directory that may contain duplicate files.
[log_interval]: The interval (in minutes) for log file naming based on date and time.
[receiver_email]: Email ID of the receiver for the log file.