#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

ENSURO_REPO_PATH=../ensuro

current_ref() {
    # from https://stackoverflow.com/a/18660163
    git -C "${ENSURO_REPO_PATH}" symbolic-ref -q --short HEAD || git  -C "${ENSURO_REPO_PATH}" describe --tags --exact-match
}

if [ -z "${1:-}" ]; then
    echo "ERROR: Usage $0 <version>" >&2
    exit 10
fi

if [ "$(current_ref)" != "$1" ]; then
    echo "ERROR: ${ENSURO_REPO_PATH} must be checked out at '$1' and is instead at '$(current_ref)'" >&2
    exit 11
fi

# TODO: remove, debug only
set -x

# Build the contracts (in a subshell for easier cwd management)
(
    cd "${ENSURO_REPO_PATH}"
    npm ci
    npx hardhat compile
)

# Copy compiled contracts over to this repo
for x in $(find "${ENSURO_REPO_PATH}/artifacts/contracts/" -maxdepth 2 -name "*.json" -not -name "*.dbg.json"); do
    cp $x src/ensuro/contracts/ ;
done

for x in $(find "${ENSURO_REPO_PATH}/artifacts/contracts/interfaces/" -maxdepth 2 -name "*.json" -not -name "*.dbg.json"); do
    cp $x src/ensuro/contracts/ ;
done

for x in ERC1967Proxy.json IERC20Metadata.json IERC20.json IERC721.json ; do
    cp $(find "${ENSURO_REPO_PATH}/artifacts/@openzeppelin/" -name $x) src/ensuro/contracts/$x ;
done

# Copy python code over
cp "${ENSURO_REPO_PATH}/prototype/ensuro.py" src/ensuro/prototype.py
cp "${ENSURO_REPO_PATH}/prototype/wrappers.py" src/ensuro/wrappers.py
cp "${ENSURO_REPO_PATH}/prototype/utils.py" src/ensuro/utils.py


echo "Release prepared. Commit, create a tag and run the build"
