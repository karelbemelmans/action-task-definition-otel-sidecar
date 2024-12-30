class SidecarGenerator:

    def __init__(self, container_name=None, image=None):
        self.otelSidecarDefinition = {
            "name": container_name,
            "image": image
        }

        pass

    def addOtelSidecar(self, json):
        return self._addSidecar(json, self.otelSidecarDefinition)

    def _addSidecar(self, json, sidecar):
        json['containerDefinitions'].append(sidecar)
        return json
