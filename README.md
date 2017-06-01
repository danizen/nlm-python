# nlm-python

## Summary

A simple, non-opinionated spec file for Python 3+
My guys need a Python rpm that they can turn the crank on when they need to.

## How to build

1. Import the keys for the python builders:

```
gpg --recv-keys F73C700D
```

2. Download the Python code.

This is a wrapper of curl and gpg --verify:

```
make upstream
```

3. Setup your rpm directories

This is a wrapper around rpmdev-setup and some copies:

```
make setup
```

4. Build the rpms

This is a wrapper around rpmbuild:

```
make rpms
```

