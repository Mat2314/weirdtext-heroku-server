#!/bin/bash

echo "Changing to local environment"
rm ../Dockerfile*
cp Dockerfile-local ..
mv ../Dockerfile-local ../Dockerfile
echo "Local environment ready"
echo "Run docker-compose up to start the server locally"
