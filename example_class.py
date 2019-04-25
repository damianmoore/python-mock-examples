class ExampleClass:
    def __init__(self):
        self.results = []

    def fetch_results(self):
        # Would be doing an expensive operation like calling an API
        self.results.append('original value')

    def get_results(self):
        return self.results
