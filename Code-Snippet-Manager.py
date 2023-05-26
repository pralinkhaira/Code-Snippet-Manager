import json

class CodeSnippetManager:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.snippets = []
        self.load_snippets()

    def load_snippets(self):
        try:
            with open(self.storage_file, 'r') as file:
                self.snippets = json.load(file)
        except FileNotFoundError:
            self.snippets = []

    def save_snippets(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.snippets, file)

    def add_snippet(self, title, code, language):
        snippet = {
            'title': title,
            'code': code,
            'language': language
        }
        self.snippets.append(snippet)
        self.save_snippets()

    def delete_snippet(self, index):
        if index >= 0 and index < len(self.snippets):
            del self.snippets[index]
            self.save_snippets()

    def search_snippets(self, keyword):
        results = []
        for snippet in self.snippets:
            if keyword.lower() in snippet['title'].lower() or keyword.lower() in snippet['code'].lower():
                results.append(snippet)
        return results

    def display_snippets(self):
        for index, snippet in enumerate(self.snippets):
            print(f"{index + 1}. {snippet['title']}")
            print(f"Language: {snippet['language']}")
            print(f"Code:\n{snippet['code']}\n")

# Example usage:
snippet_manager = CodeSnippetManager("snippets.json")

# Add a code snippet
snippet_manager.add_snippet("Hello World", "print('Hello, World!')", "Python")

# Add another code snippet
snippet_manager.add_snippet("Square a Number", "def square(n):\n    return n ** 2", "Python")

# Display all snippets
snippet_manager.display_snippets()

# Search for snippets containing the keyword 'square'
search_results = snippet_manager.search_snippets("square")
for snippet in search_results:
    print(f"Title: {snippet['title']}")
    print(f"Language: {snippet['language']}")
    print(f"Code:\n{snippet['code']}\n")

# Delete the first snippet
snippet_manager.delete_snippet(0)

# Display the updated list of snippets
snippet_manager.display_snippets()
