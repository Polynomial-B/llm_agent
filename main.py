import os, argparse, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():

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

    for _ in range(20):
        # --------- RESPONSE ---------

        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],
                system_instruction=system_prompt),
        )

        if response.candidates:
            for c in response.candidates:
                messages.append(c.content)
        if not response.function_calls:
            print("Response:")
            print(response.text)
            return
    

        if args.verbose:
            print("User prompt: " + str(args.user_prompt))
            print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
            print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

        if response.function_calls:
            function_responses = []
            for f in response.function_calls:
                result_call_function = call_function(f, verbose=args.verbose)

                if not result_call_function.parts[0]:
                    raise Exception("Error: an error occurred")
                if result_call_function.parts[0].function_response == None:
                    raise Exception("Error: an error occurred")
                if result_call_function.parts[0].function_response.response == None:
                    raise Exception("Error: an error occurred")
                
                function_responses.append(result_call_function.parts[0])
                
                if args.verbose:
                    print(f"-> {result_call_function.parts[0].function_response.response}")

            messages.append(types.Content(role="user", parts=function_responses))
            
        if not response.function_calls:
            print("Response:")
            print(response.text)
            return
        
    print("Max iterations ended")
    sys.exit(1)


if __name__ == "__main__":
    main()
