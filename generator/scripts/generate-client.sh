#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../" || exit

# Remove old generated code
rm -rf ../generated/

# Generated client
java -ea -server -Duser.timezone=UTC -jar "$(pwd)/../../openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar" generate -c ./openapi-generator-config.yml --skip-validate-spec

# Copy
cp -r ../generated/aries_cloudcontroller/ ..

black .

# Apply the patches required
cd ..

echo -e "\nApplying patch"
git apply --verbose generator/data/__init__.patch || {
    # git apply failed! Warn the user
    echo -e "$(tput setaf 1)\n\nFailed to apply patch. Client generation INCOMPLETE!\n\nPlease, ensure to fix this before proceeding.\nTake care when committing unpatched code.\n\n"
    exit 1
}
black .
