PYTHON_RUNTIME_TAG=chirichidi/scratch-pad

update:
	git reset --hard
	git pull

build: \
	install-python

install-python:
	docker build \
    		--tag ${PYTHON_RUNTIME_TAG} \
    		./env/docker