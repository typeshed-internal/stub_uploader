from typing import Any
from unittest.mock import Mock, call, patch

import pytest
from packaging.requirements import Requirement
from packaging.specifiers import Specifier

from stub_uploader.metadata import InvalidRequires, Metadata, verify_external_req


def response(data: dict[str, Any], status_code: int = 200) -> Mock:
    return Mock(status_code=status_code, json=Mock(return_value=data))


@pytest.fixture
def project_data() -> dict[str, Any]:
    return {
        "info": {"version": "2.0", "requires_dist": []},
        "releases": {
            "1.9": [{"yanked": False}],
            "1.10": [{"yanked": True}, {"yanked": False}],
            "2.0": [{"yanked": False}],
            "1.11rc1": [{"yanked": False}],
            "1.11": [{"yanked": True}],
            "1.12": [],
            "legacy-version": [{"yanked": False}],
        },
        "urls": [{"packagetype": "sdist", "filename": "example-2.0.tar.gz"}],
    }


@pytest.mark.parametrize("field", ["dependencies", "optional-dependencies"])
@pytest.mark.parametrize(
    "version_spec,expected_version",
    [
        ("1.*", "1.10"),
        ("~=1.9", "1.10"),
        ("1.9", "1.9"),
        ("1.11rc1", "1.11rc1"),
    ],
)
def test_supported_release_metadata(
    project_data: dict[str, Any], field: str, version_spec: str, expected_version: str
) -> None:
    metadata = Metadata("example", {"version": version_spec, field: ["numpy"]}, set())
    with patch(
        "stub_uploader.metadata.requests.get",
        side_effect=[
            response(project_data),
            response({"info": {"requires_dist": ["numpy"]}, "urls": []}),
        ],
    ) as get:
        dependencies = (
            metadata.dependencies
            if field == "dependencies"
            else metadata.optional_dependencies
        )
    assert [dep.name for dep in dependencies] == ["numpy"]
    assert get.call_args_list == [
        call("https://pypi.org/pypi/example/json"),
        call(f"https://pypi.org/pypi/example/{expected_version}/json"),
    ]


@pytest.mark.parametrize("version_spec", ["==3.*", "==1.11", "==1.12"])
def test_no_supported_release(project_data: dict[str, Any], version_spec: str) -> None:
    with patch(
        "stub_uploader.metadata.requests.get", return_value=response(project_data)
    ) as get:
        with pytest.raises(InvalidRequires, match="No published, non-yanked release"):
            verify_external_req(
                Requirement("numpy"), "example", Specifier(version_spec)
            )
    get.assert_called_once_with("https://pypi.org/pypi/example/json")


def test_dependency_must_be_in_selected_release(project_data: dict[str, Any]) -> None:
    project_data["info"]["requires_dist"] = ["numpy"]
    with patch(
        "stub_uploader.metadata.requests.get",
        side_effect=[
            response(project_data),
            response({"info": {"requires_dist": []}, "urls": []}),
        ],
    ) as get:
        with pytest.raises(
            InvalidRequires, match="to be listed in example's requires_dist"
        ):
            verify_external_req(Requirement("numpy"), "example", Specifier("==1.*"))
    assert get.call_args_list[-1] == call("https://pypi.org/pypi/example/1.10/json")


@pytest.mark.parametrize("dependency_groups", [False, True])
def test_sdist_metadata_uses_selected_release(
    project_data: dict[str, Any], dependency_groups: bool
) -> None:
    req = Requirement("numpy")
    sdist = {"packagetype": "sdist", "filename": "example-1.10.tar.gz"}
    with (
        patch(
            "stub_uploader.metadata.requests.get",
            side_effect=[
                response(project_data),
                response({"info": {"requires_dist": []}, "urls": [sdist]}),
            ],
        ),
        patch(
            "stub_uploader.metadata.extract_sdist_requires",
            return_value=iter([] if dependency_groups else [req]),
        ) as requires,
        patch(
            "stub_uploader.metadata.extract_sdist_pyproject_requires",
            return_value=iter([req]),
        ) as groups,
    ):
        verify_external_req(req, "example", Specifier("==1.*"))
    requires.assert_called_once_with(sdist, req)
    if dependency_groups:
        groups.assert_called_once_with(sdist, req)
    else:
        groups.assert_not_called()


@pytest.mark.parametrize("release_error", [False, True])
def test_pypi_error(project_data: dict[str, Any], release_error: bool) -> None:
    responses = [response({}, status_code=503)]
    if release_error:
        responses.insert(0, response(project_data))
    with patch("stub_uploader.metadata.requests.get", side_effect=responses):
        with pytest.raises(InvalidRequires, match="got 503"):
            verify_external_req(Requirement("numpy"), "example", Specifier("==1.*"))
