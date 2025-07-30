# Firewall Login Page (Flask)

This is a simple Flask web app that mimics a firewall or network appliance login page. When users log in with `admin:admin`, a flag is displayed.

## Features
- Simple login form styled like a firewall appliance
- Shows a flag/message when logging in as admin
- Makefile for local run and GCP Cloud Run deployment

## Usage

### Local Development

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run locally:
   ```sh
   make local
   ```

### Deploy to Google Cloud Run

1. Set your GCP project ID in the Makefile (`PROJECT_ID`)
2. Build, push, and deploy:
   ```sh
   make all
   ```

## Default Admin Credentials
- **Username:** admin
- **Password:** admin

## Flag
- `FLAG{firewall_admin_access}`
