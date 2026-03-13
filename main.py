import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("Error getting API Key")

# ---------- CLIENT ----------
client = genai.Client(api_key=api_key)

# --------- ARGPARSE ---------
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# ------- MESSAGES LIST ------
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# --------- RESPONSE ---------
response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions],
        system_instruction=system_prompt, max_output_tokens=200), # ! MAX TOKEN LIMIT ADDED
)
if args.verbose:
    print("User prompt: " + str(args.user_prompt))
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

if response.function_calls:
    for f in response.function_calls:
        print(f"Calling function: {f.name}({f.args})")
else:
    print(response.text)

def main():
    pass

if __name__ == "__main__":
    main()
