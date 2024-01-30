CI/CD Pipeline for Oracle Database and Flask App
Overview
This GitHub Actions workflow automates the deployment process for an Oracle Database and a Flask app. The workflow consists of three jobs:

Build-Push-Container:

Builds and pushes the Flask app container to Docker Hub.
security:

Runs Snyk to check for vulnerabilities in the code.
ansible:

Runs an Ansible playbook using a self-hosted runner to set up an Oracle Database, execute SQL scripts, and deploy a Flask app container.
Workflow Steps
Build-Push-Container Job:
Build and Push Flask App Container:
The job checks out the code, logs in to Docker Hub, sets up Docker Buildx, and builds/pushes the Flask app container to Docker Hub. Docker Hub credentials are securely stored in GitHub Secrets.
Security Job:
Run Snyk for Vulnerability Scanning:
The job checks out the code and runs Snyk to identify and report vulnerabilities. The Snyk token is securely stored in GitHub Secrets.
Ansible Job:
Run Ansible Playbook:
The job runs an Ansible playbook using a self-hosted runner.
The Ansible playbook performs the following tasks:
Starts an Oracle Database container using a pushed image.
Waits for the Oracle Database container to be ready.
Copies an SQL script to the Oracle Database container.
Executes the SQL script on the Oracle Database.
Pulls another Docker image from Docker Hub.
Tags the pulled image.
Starts a Flask app container using the tagged image.
Configuration
GitHub Secrets:
Make sure to set up the following secrets in the GitHub repository:

DOCKERHUB_USERNAME: Your Docker Hub username.
DOCKER_PASSWORD: Your Docker Hub password.
SNYK_TOKEN: Your Snyk API token for vulnerability scanning.
PASS: Ansible vault password.
PIPEDREAM_ENDPOINT: Pipedream webhook endpoint for Docker Hub pushes.
Ansible Vault Password File:
Ensure that the Ansible vault password is securely stored at /home/misho/pass_vault and referenced in the Ansible playbook.

Execution
The workflow is triggered automatically on pushes to the master branch and closed pull requests. Additionally, you can manually trigger the workflow using the GitHub Actions UI.
