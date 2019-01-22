import json
import yaml
from kubernetes import client, config, watch
import os

if __name__ == "__main__":
    if 'KUBERNETES_PORT' in os.environ:
        config.load_incluster_config()
    else:
        config.load_kube_config()

    api_client = client.CoreV1Api()

    for event in watch.Watch().stream(api_client.list_pod_for_all_namespaces()):
        print("Event: %s %s %s" % (event['type'],event['object'].kind, event['object'].metadata.name))
