# Simple IaC example for CI using gitlab

## Requirements
 - docker
 - docker-compose  
 - git  
 - python

## Instalation & Configuration
1. Exec command `docker-compose up`
2. Access gitlab on your favourite browser -> `localhost:8080`
3. Create a new project
4. Get runner access token (your new project > settings > CI/CD > Runners > Section "Set up a specific Runner manually")
5. Edit file `gitlab-runner-register.sh` and replace variable value `registration_token` with you token
6. Run file `gitlab-runner-register.sh`
7. Push his code to you local gitlab -> `localhost:8080`
