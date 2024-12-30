class SidecarGenerator:

    otelSidecarDefinition = {
        "name": "otel",
        "image": "otel/opentelemetry-collector-contrib"
    }

    def __init__(self):
        pass

    def addOtelSidecar(self, json):
        return self._addSidecar(json, self.otelSidecarDefinition)

    def _addSidecar(self, json, sidecar):
        json['containerDefinitions'].append(sidecar)
        return json
