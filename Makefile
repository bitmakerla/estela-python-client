GENERATOR_IMAGE=openapitools/openapi-generator-cli:latest
GENERATOR_NAME=python
SPEC_URL=https://raw.githubusercontent.com/bitmakerla/estela/main/estela-api/docs/api.yaml
GIT_HOST=github.com
GIT_REPO_ID=estela-python-client
GIT_USER_ID=bitmakerla
PACKAGE_NAME=estela_client

.PHONY: update
update:
	docker run --rm -v ${PWD}:/local $(GENERATOR_IMAGE) generate \
			--input-spec $(SPEC_URL) \
			--generator-name $(GENERATOR_NAME) \
			--output /local/ \
			--git-host $(GIT_HOST) \
			--git-repo-id $(GIT_REPO_ID) \
			--git-user-id $(GIT_USER_ID) \
			--minimal-update \
			--additional-properties packageName=$(PACKAGE_NAME)
