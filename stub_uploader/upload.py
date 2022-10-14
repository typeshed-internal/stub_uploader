from __future__ import annotations

import os
import subprocess

from stub_uploader import build_wheel
from stub_uploader.get_version import determine_incremented_version
from stub_uploader.update_changelog import update_changelog
from stub_uploader.metadata import (
    read_metadata,
    recursive_verify,
    sort_by_dependency,
    uploaded_packages,
)


def upload(
    typeshed_dir: str,
    distributions: list[str],
    commit: str | None = None,
    *,
    dry_run: bool = False,
) -> None:
    to_upload = sort_by_dependency(typeshed_dir, distributions)
    print("Building and uploading stubs for:", ", ".join(distributions))
    print()
    for distribution in to_upload:
        print(f"Building stubs for {distribution}... ", end="")
        metadata = read_metadata(typeshed_dir, distribution)
        recursive_verify(metadata, typeshed_dir)

        version = determine_incremented_version(metadata)
        if commit:
            update_changelog(
                typeshed_dir, commit, distribution, version, dry_run=dry_run
            )

        temp_dir = build_wheel.main(typeshed_dir, distribution, version)
        print(f"ok, version {version}")

        print(f"Uploading stubs for {distribution}... ", end="")
        if dry_run:
            print(f"skipped")
        else:
            subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")], check=True)
            uploaded_packages.add(distribution)
            print(f"ok")
        print()
