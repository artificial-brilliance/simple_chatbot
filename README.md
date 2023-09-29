# A Simple Chatbot

This repo demonstrates how to create a simple chatbot using OpenAI's chat completion API.  It is inspired by a great article by [Simon Willison](https://til.simonwillison.net/llms/python-react-pattern).

## Usage

This repository was written using Python 3.11 and uses the [pdm](https://pdm.fming.dev) tool to handle dependencies.

To get started
1. Clone the repo:
   ```
     git clone git@github.com:artificial-brilliance/simple_chatbot.git
   ```
2. At the root of the repo, install necessary dependencies:
   ```
     pdm install
   ```
3. At the root of the repo, run the code with:
   ```
     pdm run start
   ```

## An Example Conversation

```
$ pdm run start
You are chatting with a helpful assistant.  To stop the conversation press Ctrl+C.
[You] Hi
[Assistant] Hello! How can I assist you today?
[You] Can I ask you a question
[Assistant] Of course! Feel free to ask me anything you'd like.
[You] What is a Corgi dog?
[Assistant] A Corgi is a type of dog breed that originated in Wales, United Kingdom. There are two main breeds of Corgis: the Pembroke Welsh Corgi and the Cardigan Welsh Corgi.

Pembroke Welsh Corgis are known for their short legs, long bodies, and pointy ears. They have a friendly and outgoing personality, and they are often described as intelligent and affectionate. They are also known for their distinctive "smiling" faces.

Cardigan Welsh Corgis, on the other hand, have a similar body shape but with a longer tail. They have rounded ears and are known for their intelligence, loyalty, and versatility. They are often described as being more reserved and cautious compared to Pembroke Welsh Corgis.

Both breeds are herding dogs and were traditionally used to help farmers in Wales with herding cattle and other livestock. Nowadays, Corgis are popular pets known for their playful nature, loyalty, and adorable appearance.
[You] Thanks.  How do you feel?
[Assistant] As an AI, I don't have feelings in the same way humans do. However, I'm here to assist you and provide information to the best of my abilities. Is there anything else I can help you with?
[You] That makes sense.
[Assistant] I'm glad it makes sense to you! If you have any more questions or need further assistance, feel free to ask. I'm here to help!
[You]
```