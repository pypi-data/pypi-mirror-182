from typing import Optional
from docker import DockerClient
from docker.models.containers import Container


def _is_valid_v4_container(c: Container) -> bool:
    valid_env = any("SENTRY_ENVIRONMENT" in e for e in c.attrs["Config"]["Env"])
    valid_tag = any("nodefluxio/visionaire4" in t for t in c.image.tags)
    return valid_env and valid_tag


def _is_valid_prom_container(c: Container, prom_addr: str) -> bool:
    split = prom_addr.split(":")
    port = "9090" if len(split) < 2 else split[-1]
    valid = any(port in p for p in c.attrs["NetworkSettings"]["Ports"])
    return valid


def find_v4_container(client: DockerClient, possible_name: str) -> Optional[Container]:
    containers = client.containers.list()
    result = [c for c in containers if c.name == possible_name]
    if len(result) > 0:
        return result[0]

    ## name not found, use container attributes
    result = [c for c in containers if _is_valid_v4_container(c)]
    if len(result) > 0:
        return result[0]
    return None


def find_prom_container(
    client: DockerClient, possible_name: str, prom_addr: str
) -> Optional[Container]:
    containers = client.containers.list()
    result = [c for c in containers if c.name == possible_name]
    if len(result) > 0:
        return result[0]

    ## name not found, use container attributes
    result = [c for c in containers if _is_valid_prom_container(c, prom_addr)]
    if len(result) > 0:
        return result[0]
    return None
