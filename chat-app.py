import os
from dotenv import load_dotenv

# import namespaces
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Get configuration settings
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        print("Attempting to authenticate to Azure using DefaultAzureCredential...")
        print("(This uses az login credentials if available)\n")

        # Initialize the OpenAI client using DefaultAzureCredential
        # This will use 'az login' credentials if available
        credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
        token_provider = get_bearer_token_provider(
            credential, "https://ai.azure.com/.default"
        )

        openai_client = OpenAI(
            base_url=azure_openai_endpoint,
            api_key=token_provider
        )

        print("✅ Authentication successful!\n")

        # Track responses for conversation context
        last_response_id = None

        # Loop until the user wants to quit
        while True:
            input_text = input('\nEnter a prompt (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            # Get a response using Responses API with conversation tracking
            response = openai_client.responses.create(
                model=model_deployment,
                instructions="You are a helpful AI assistant that answers questions and provides information.",
                input=input_text,
                previous_response_id=last_response_id,
            )
            print("\nAssistant:", response.output_text)
            
            # Store the response ID for the next request
            last_response_id = response.id

    except Exception as ex:
        print(f"Error: {ex}")
        print("\nIf you see an authentication error, try running: az login")


if __name__ == '__main__':
    main()