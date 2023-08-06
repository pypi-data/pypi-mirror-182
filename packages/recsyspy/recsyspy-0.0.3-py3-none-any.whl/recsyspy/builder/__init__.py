class BaseRecoBuilder:
    def __init__(self, debug: bool):
        self.debug = debug

    def run(self):
        print("Calculate recommendations...")

    def store_relations(self):
        print("Store results...")
