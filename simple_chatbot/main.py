import os
from typing import cast, Any, Optional

import openai

# Read the OpenAI API token form the OPENAI_API_KEY environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

class ChatBot(object):
    """A simple chatbot that is able to have a conversation with a human
    by recording the conversation between the chatbot and the human.
    """

    def __init__(self, system_prompt: Optional[str]):
        # If a system prompt is specified, then it should be the first
        # message in the context.  The "system" role is used to specify
        # system messages.  These messages are helpful in to instruct
        # the model on how it should behavior or give it background
        # information relevant to the conversation.
        self.messages = [] if system_prompt is None else [{
            "role": "system",
            "content": system_prompt,
        }]

    def process(self, message: str):
        """Processes a message from the user, returning the chatbot's response.

        Parameters
        -----------
        message: the message from the user

        Returns
        -------
        The chatbot's response to the user.
        """

        # Add the user's message to the context (i.e. the conversation)
        self.messages.append({"role": "user", "content": message})
        # Ask the model to complete the conversation.  That is, the
        # messages up to this point represent the conversation
        # where the last message in the list is the most recent
        # message (i.e. the message the user just made).
        completion = openai.ChatCompletion.create(
            # The model GPT-3.5-turbo is used because it works really
            # well and has a nice price point
            model="gpt-3.5-turbo",
            # The messages are essentially the conversation at this point.
            # (i.e. the context).  Each entry in the conversation is marked
            # as being from the user or the assistant via the "role" field.
            messages=self.messages,
            # The temperature is used to essentially tell the API how
            # creative the model can be.  A value of 1 means it can be
            # really creative.  That is, the same input to the model can
            # have very different completions.  A value of 0, on the other
            # hand, means the same input to the model with always return
            # roughly the same completion (but note that the completions
            # won't necessary be exactly the same).
            #
            # A value of zero is useful for testing code understanding the
            # model because is reduces one degree of a freedom (the creativity
            # of the model) which helps in understanding how the model
            # responds to different inputs.
            temperature=0)
        # The completion of the messages is what the model thinks should
        # be the next part of the conversation.  As such, make sure
        # to add the response to the list of messages (which records the
        # conversation) making sure to specify the "assistant" role, which
        # instructs the ChatCompletion API that the message came from the
        # assistant.
        #
        # Specifically of all of the choices that the model returns for
        # possible completions for the conversation, we always just use
        # the first choice.
        #
        # Note: The cast to Any is needed because the type of completion
        #       is "Unknown".
        result = cast(Any, completion).choices[0].message.content
        # Update the conversation to include the assistant's response making
        # sure to specify the response is from the assistant.
        self.messages.append({"role": "assistant", "content": result})
        # The completion of the conversation up to this point is the chatbot's
        # response.
        return result

def main():
    print("You are chatting with a helpful assistant.  To stop the conversation press Ctrl+C.")
    chatbot = ChatBot("You are a helpful assistant.")
    while True:
        message = input("[You] ")
        response = chatbot.process(message)
        print(f"[Assistant] {response}")

main()
