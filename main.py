import json
import webbrowser
import openai

# getting config
with open('config.json', 'r') as f:
    data = json.load(f)

# Set up the OpenAI API client with your API key
openai.api_key = data.get("openai_key", "")

def generate_image(prompt, size):
    response = openai.Image.create(prompt=prompt, n=1, size=size)
    image_url = response['data'][0]['url']
    return image_url

if __name__ == "__main__":
    # choosing size for output
    sizes = ['256x256', '512x512', '1024x1024']
    choice = int(input("Choose a size for output images\n0) For 256x256\n1) For 512x512\n2) For 1024x1024\n> "))
    if choice not in {0, 1, 2}:
        print("Invalid choice for size")
        exit(1)
    size = sizes[choice]

    # generating images and opening them in new tabs
    while True:
        prompt = input("Enter a prompt ('exit' to quit) > ")
        if prompt == 'exit':
            exit(0)
        image_url = generate_image(prompt, size)
        webbrowser.open_new_tab(image_url)
