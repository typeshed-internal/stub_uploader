# Security Implication of the Typeshed Stub Uploader

Security for the stub uploader is of the highest importance. If the stub
uploader gets compromised, an attacker could upload manipulated stub
packages to gain full access to developer machines or even production hosts.
Considering the high trust, quick turnaround, and automated installation of
stub packages, this could have significant security implications.

## Maintainers

Only a small number of typeshed maintainers have commit rights for this
repository to minimize the attack vector in case of hacked accounts. This
is also the reason that this repository is part of a separate GitHub
organization and not the [python](https://github.com/python) or
[psf](https://github.com/psf) organizations, like typeshed is.

Typeshed maintainers without commit rights are still considered maintainers
of the stub uploader and are encouraged to manage issues and send and review
pull requests.

## Typeshed Data

To ensure that a compromised typeshed repository can't lead to compromised
stub packages, all typeshed data is verified by the stub uploader before
building packages. The stub uploader ensures that only stub and metadata
files are added to the stub packages. This also means that no code from the
typeshed repository must be executed while building packages, and no
modules must be imported.

## Dependencies

Another possible attack vector are dependencies of stub packages.
A compromised dependency can have a similar effect to when a stub package
gets compromised directly. Therefore, only certain dependencies are
allowed:

* Dependencies on other stub packages created by typeshed.
* Dependencies on packages the upstream package depends on – even recursively.
  Since it's likely that a stub package gets installed alongside the
  upstream package, this does not introduce an additional security liability.
* Dependencies that are explicitly allowlisted in the stub uploader. These
  dependencies are vetted to be from a trusted source.

## PyPI Uploads

Stub packages are uploaded to PyPI by the PyPI user
[typeshed_bot](https://pypi.org/user/typeshed_bot/) using an API token.
The packages are owned solely by that user, so that no other user can
upload new versions of the packages, in case an account gets compromised.
