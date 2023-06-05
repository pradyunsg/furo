# A dockerfile to run our snapshot tests locally. This is to avoid issues with CI and local
# differing. In CI, we also run with the same base image.
# See https://playwright.dev/docs/test-snapshots.
#
# Note that we build the Sphinx docs outside of this Docker image; we only need to run the
# server inside Docker so that the docs are rendered the same locally and in CI.

# Keep this base image in sync with .githug/workflows/TODO.yml.
FROM mcr.microsoft.com/playwright:v1.34.0-jammy

WORKDIR /app

# Install our dependencies in CI mode so that we error if changes are necessary.
# Users should `npm install` locally if this is the case.
COPY package*.json ./
RUN npm ci

# Copy over only the folders needed for our tests.
COPY ../../playwright.config.js ./
COPY snapshot_tests/ snapshot_tests/
COPY ../../build/docs/ build/docs/

CMD [ "npm", "run", "_run-tests" ]
