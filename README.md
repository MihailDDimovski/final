# Project Overview and Setup Guide

This repository contains Ansible playbooks, Docker configurations, GitHub Actions workflows, and security tools integration for managing a Dockerized Flyway migration tool with an Oracle Database. Below is an overview of the setup and components involved in the project.

## Components

1. **Ansible Playbooks**: Used to automate the deployment and configuration of the Dockerized Flyway with an Oracle Database.

2. **Docker Configuration**: Dockerfiles and Docker Compose files for building and running the Docker containers required for Flyway and Oracle Database.

3. **GitHub Actions Workflows**: CI/CD workflows to automate the build, push, and deployment process of Docker images, along with security scanning using Trivy and Snyk.

4. **Security Tools Integration**: Integration of Trivy for vulnerability scanning of Docker images and TruffleHog for scanning code for secrets.

## Ansible Playbooks

The Ansible playbook `flyway_deploy.yml` automates the deployment of Flyway with an Oracle Database. It performs tasks like setting up a Docker network, pulling Docker images, starting containers, and running Flyway migration.

### Usage

```bash
ansible-playbook flyway_deploy.yml
```

## Docker Configuration

The `Dockerfile` and `docker-compose.yml` files in the `app` and `oracle_flyway` directories define the Docker configurations for building and running Flyway and Oracle Database containers.

## GitHub Actions Workflows

The `.github/workflows` directory contains GitHub Actions workflows for CI/CD and security scanning.

1. **Build-Push-Container-app**: Workflow for building and pushing the Flyway application Docker image to Docker Hub. It also includes Trivy vulnerability scanning.

2. **Build-Push-Container-oracle**: Workflow for building and pushing the Oracle Database Docker image to Docker Hub. It also includes Trivy vulnerability scanning.

3. **Truffle-HOG-Secret-Scan**: Workflow for scanning the codebase for secrets using TruffleHog.

4. **security-snyk**: Workflow for checking vulnerabilities using Snyk and generating SARIF reports.

5. **ansible**: Workflow for deploying the Flyway application and Oracle Database using Ansible. It includes steps to stop and remove any existing Docker containers.

## Contributing

Contributions to this project are welcome! Feel free to submit pull requests or open issues for any improvements, bug fixes, or new features.

## License

This project is licensed under the [MIT License](LICENSE).
