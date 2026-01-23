import json

class Governor:
    def __init__(self):
        self.manifest = self._load_manifest()

    def _load_manifest(self):
        try:
            with open("canon_manifest.json", "r") as f:
                data = json.load(f)
                return data if data.get("status") == "CANONICAL" else None
        except FileNotFoundError:
            return None

    def validate_existence(self, action):
        if not self.manifest:
            return False
        # The ontological triad: intent, trace, liability
        requirements = ["intent", "trace", "liability"]
        return all(k in action for k in requirements)

    def execute(self, action):
        if self.validate_existence(action):
            return "EXISTENCE_CONFIRMED"
        return "SYSTEM_INACTIVE: ONTOLOGY_NOT_FOUND"

if __name__ == "__main__":
    gov = Governor()
    # Test action to trigger the output in terminal
    test_action = {"intent": "X", "trace": "Y", "liability": "Z"}
    
    # This line generates the text in the Linux terminal
    print(gov.execute(test_action))
