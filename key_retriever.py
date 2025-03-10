# key location ./api_key.txt
def load_api_key(filename="api_key.txt"):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create it with your API key.")
        return None