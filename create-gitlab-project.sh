#!/bin/sh

curl -d '{"name":"demo-project"}' -H "Content-Type: application/json" -X POST http://localhost:8080/projects