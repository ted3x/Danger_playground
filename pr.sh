#!/bin/bash

# Get the list of modified modules in the Pull Request
MODIFIED_MODULES=$(git diff --name-only HEAD^..HEAD | grep "/src/" | cut -d'/' -f2 | uniq)

# Run the lint task for each modified module
for MODULE in ${MODIFIED_MODULES}; do
  echo "Running lint for module: ${MODULE}"
  ./gradlew ${MODULE}:lint
done
