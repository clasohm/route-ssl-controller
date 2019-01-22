from kubernetes import client, config, watch

if __name__ == "__main__":
    config.load_incluster_config()
    api_client = client.CoreV1Api()

    for event in watch.Watch().stream(api_client.list_cluster_custom_object('route.openshift.io', 'v1', 'routes')):
        print("Event: %s %s %s" % (event['type'],event['object'].kind, event['object'].metadata.name))
