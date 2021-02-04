#!/bin/bash

echo "Changing to production environment"
rm ../Dockerfile*
cp Dockerfile-heroku ..
mv ../Dockerfile-heroku ../Dockerfile
echo "Production environment ready"
