## 7.1.0.20260109 (2026-01-09)

[docker] Fix `Container.attach()` return type ([#15155](https://github.com/python/typeshed/pull/15155))

## 7.1.0.20251202 (2025-12-02)

Fix docker exec types ([#15097](https://github.com/python/typeshed/pull/15097))

[docker-py] Add fallback `exec_start` overload ([#15098](https://github.com/python/typeshed/pull/15098))

## 7.1.0.20251129 (2025-11-29)

[docker-py] Add some missing types ([#15084](https://github.com/python/typeshed/pull/15084))

## 7.1.0.20251127 (2025-11-27)

[docker-py] Fix the type of `Model` and `Collection` `client` attribute ([#15083](https://github.com/python/typeshed/pull/15083))

## 7.1.0.20251125 (2025-11-25)

[docker-py] Fix `Container.top()` return type ([#15067](https://github.com/python/typeshed/pull/15067))

[docker-py] Add `str` type to `named` parameter in `Image.save()` method ([#15068](https://github.com/python/typeshed/pull/15068))

[docker-py] Add some return types to `DockerClient` method ([#15069](https://github.com/python/typeshed/pull/15069))

## 7.1.0.20251009 (2025-10-09)

[docker] Fix some incomplete types ([#14817](https://github.com/python/typeshed/pull/14817))

## 7.1.0.20250916 (2025-09-16)

Fix docker mount source type ([#14726](https://github.com/python/typeshed/pull/14726))

The source of a mount can be None e.g. if the type is tmpfs.
The parse_mount_string also sets source=None in some cases

## 7.1.0.20250907 (2025-09-07)

[docker] Add default value for `detach` parameter of `ContainerCollection.create` ([#14666](https://github.com/python/typeshed/pull/14666))

## 7.1.0.20250822 (2025-08-22)

Add missing defaults to third-party stubs ([#14617](https://github.com/python/typeshed/pull/14617))

## 7.1.0.20250809 (2025-08-09)

Mark stub-only private symbols as `@type_check_only` in third-party stubs (#14545)

## 7.1.0.20250705 (2025-07-05)

[docker] load() accepts bytes streams (#14366)

## 7.1.0.20250523 (2025-05-23)

Expand type stubs for Docker container device read/write bps/iops (#14092)

## 7.1.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs (#14063)

## 7.1.0.20250503 (2025-05-03)

Improve `docker.types` (#13809)

Co-authored-by: Avasam <samuel.06@hotmail.com>

## 7.1.0.20250416 (2025-04-16)

Improve `docker.utils` (#13808)

## 7.1.0.20241229 (2024-12-29)

Fix missed type hints in docker containers.pyi (#13136)

Previously, `Container.exec_run` and `Container.get_archive` missed type hints on `cmd` and `path` arguments, respectively.
Added type hints based on docstring.

## 7.1.0.20240827 (2024-08-27)

[docker-py] Fix 'volumes' argument type hint for 'run' and 'create' functions in containers.pyi (#12594)

## 7.1.0.20240821 (2024-08-21)

chunk_size parameter of get_image accepts None (#12560)

## 7.1.0.20240806 (2024-08-06)

Bump mypy to 1.11.1 (#12463)

## 7.1.0.20240720 (2024-07-20)

[docker] Add restart_policy type annotation to Container model (#12366)

## 7.1.0.20240711 (2024-07-11)

[docker] Update ports type annotation (#12284)

## 7.1.0.20240703 (2024-07-03)

Specify stream type of Docker logs (#12214)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 7.1.0.20240629 (2024-06-29)

Allow users of docker run, create to not give name/version (#12234)

## 7.1.0.20240628 (2024-06-28)

Add kwarg types to Docker container run and create (#12216)

Add Container wait return type at Docker model layer (#12217)

Also, improve type for the API layer. Previously, the type accounted for a 404 response. However, in the 404 case, a `docker.errors.NotFound` exception is raised.

## 7.1.0.20240626 (2024-06-26)

Add more keyword argument types for Docker pull (#12210)

Add parameter types to docker.models.images.ImageCollection.build (#12196)

Introduce stubs-only module `docker._types`.

Add return types to docker container run (#12206)

## 7.1.0.20240625 (2024-06-25)

Add more specific types to Docker network inspect/get equivalent methods (#12188)

Add types for container and net_id parameters in docker/api/network (#12042)

Add parameter types to docker's NetworkCollection create (#12190)

Add more precise types in docker.types.containers (#12191)

## 7.1.0.20240624 (2024-06-24)

Use more specific types for Docker create_network (#12187)

## 7.1.0.20240621 (2024-06-21)

Add some types for Docker.api.network.NetworkApiMixing.create_network parameters (#12156)

See implementation at
https://github.com/docker/docker-py/blob/a3652028b1ead708bd9191efb286f909ba6c2a49/docker/api/network.py#L40

## 7.1.0.20240617 (2024-06-17)

[docker] Add a number of types to docker.models.containers.Container (#12077)

## 7.1.0.20240601 (2024-06-01)

[docker] Annotate Container.stop() (#12052)

Update docker to 7.1.x (#12068)

## 7.0.0.20240529 (2024-05-29)

Add types to docker.models.containers.Container.logs (#12044)

## 7.0.0.20240528 (2024-05-28)

Add keyword argument types to `docker.models.containers.Container.wait()` (#12037)

## 7.0.0.20240527 (2024-05-27)

Add return type for Docker Container wait (#12036)

## 7.0.0.20240524 (2024-05-24)

Add types to parameters for Docker Network.disconnect (#12007)

## 7.0.0.20240523 (2024-05-23)

Add types for Docker client from_env kwargs (#11989)

## 7.0.0.20240519 (2024-05-19)

Fix type of Docker BuildError.build_log (#11917)

In working this out I also had a go at changing the json_stream
functions used to create every BuildError in docker-py.

There are two `BuildError`s raised in docker-py, both in
https://github.com/docker/docker-py/blob/b6464dbed92b14b2c61d5ee49805fce041a3e083/docker/models/images.py#L304-L315

```python
result_stream, internal_stream = itertools.tee(json_stream(resp))
for chunk in internal_stream:
    if 'error' in chunk:
        raise BuildError(chunk['error'], result_stream)
    if 'stream' in chunk:
        match = re.search(
            r'(^Successfully built |sha256:)([0-9a-f]+)$',
            chunk['stream']
        )
        if match:
            image_id = match.group(2)
    last_event = chunk
if image_id:
    return (self.get(image_id), result_stream)
raise BuildError(last_event or 'Unknown', result_stream)
```

## 7.0.0.20240515 (2024-05-15)

Add a number of types to docker.models.containers (#11912)

## 7.0.0.20240513 (2024-05-13)

Add many types to docker.api.container (#11911)

Add types to all "container" parameters in docker.api.container (#11908)

Add remaining parameter types to docker.api.container logs (#11907)

Add return type to Docker Container.logs (#11888)

Add return type for Docker container start (#11905)

Fix "tail" parameter type for Docker container logs (#11906)

Allow Image type for docker container run image parameter (#11900)

## 7.0.0.20240511 (2024-05-11)

Add some types to Docker ContainerCollection parameters (#11857)

## 7.0.0.20240507 (2024-05-07)

Add return type to Docker Container.stop (#11869)

We can see at
https://github.com/docker/docker-py/blob/b6464dbed92b14b2c61d5ee49805fce041a3e083/docker/models/containers.py#L452
that this returns the return value of `self.client.api.stop`.

We can see at
https://github.com/docker/docker-py/blob/b6464dbed92b14b2c61d5ee49805fce041a3e083/docker/api/container.py#L1187
that this returns None.

Add return type to Docker Container.remove (#11868)

## 7.0.0.20240506 (2024-05-06)

Improve types in docker models (#11859)

## 7.0.0.20240503 (2024-05-03)

[docker-py] Add return type for building a Docker image (#11851)

## 7.0.0.20240501 (2024-05-01)

 Improve docker api types (#11846)

## 7.0.0.20240430 (2024-04-30)

Add types to docker/context (#11818)

## 7.0.0.20240424 (2024-04-24)

Fully type docker/api/build (#11789)

## 7.0.0.20240413 (2024-04-13)

Add docker-py stubs (#11749)

