
UPSTREAM_DIR=upstream

PYTHON_VERS=3.4.6
PYTHON_FILE=Python-$(PYTHON_VERS).tgz
PYTHON_SIG=$(PYTHON_FILE).asc
PYTHON_DIST=https://www.python.org/ftp/python/$(PYTHON_VERS)
PYTHON_FILE_URL=$(PYTHON_DIST)/$(PYTHON_FILE)
PYTHON_SIG_URL=$(PYTHON_DIST)/$(PYTHON_SIG)

.PHONY: all upstream spec setup rpm

all: upstream setup rpm

upstream: upstream/$(PYTHON_FILE) upstream/$(PYTHON_SIG)
	gpg --verify upstream/$(PYTHON_SIG)

upstream/$(PYTHON_FILE):
	-mkdir -p upstream
	curl -L -o $@ $(PYTHON_FILE_URL)

upstream/$(PYTHON_SIG):
	-mkdir -p upstream
	curl -L -o $@ $(PYTHON_SIG_URL)

setup:
	rpmdev-setuptree
	cp nlm-python.spec ~/rpmbuild/SPECS
	cp upstream/$(PYTHON_FILE) ~/rpmbuild/SOURCES

rpm:
	rpmbuild -bb ~/rpmbuild/SPECS/nlm-python.spec

clean:
	-rm -rf upstream

