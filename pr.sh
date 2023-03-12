#!/bin/bash

# Exit on error
set -e

# Get all the modules that were changed
# shellcheck disable=SC2162
while read line; do
  module_name=${line%%/*}
  echo $module_name
  if [[ ${MODULES} != *"${module_name}" ]]; then
    MODULES="${MODULES} ${module_name}"
  fi
done < <(git diff --name-only)
changed_modules=$MODULES

# Get a list of all available gradle tasks
AVAILABLE_TASKS=$(./gradlew tasks --all)

# Check if these modules have gradle tasks
build_commands=""
for module in $changed_modules
do
  if [[ $AVAILABLE_TASKS =~ $module":app:" ]]; then
    build_commands=${build_commands}" :"${module}":app:assembleDebug :"${module}":app:check"
  fi
done

# Build
echo "Building Pull Request with"
echo "command $build_commands"
eval "./gradlew clean ktlint ${build_commands}"
