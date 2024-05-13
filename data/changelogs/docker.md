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

