# myaibot
Hi, I am myaibot, a chatbot built using the OpenAI GPT-3 model.

## Introduction
myaibot is a chatbot that uses the OpenAI GPT-3 model to generate responses to user input. It is designed to be simple to use, with a single function `myaibot` that takes an input string and prints the bot's response.

## Installation
To use myaibot, you will need to install the required dependencies:

```
pip install myaibot
```
You will also need to set your OpenAI API key as an environment variable.

## Usage
To set up your OpenAI API key, you will need to sign up for an OpenAI account and obtain an API key. 
Here is a step-by-step guide:
1. Go to the OpenAI website (https://openai.com/) and click on the "Sign Up" button in the top right corner.
2. Follow the prompts to create a new OpenAI account. You will need to provide your email address, name, and password.
3. Once your account has been created, go to the "API Keys" page in your account settings. This can be accessed by clicking on your profile icon in the top right corner and selecting "Settings" from the dropdown menu.

4. Click on the "Create New Key" button to create a new API key.

5. Copy the API key to your clipboard.

6. Set the API key as an environment variable. You can do this by adding the following line to your shell configuration file (such as ~/.bashrc or ~/.bash_profile):
```
export OPENAI_API_KEY="your-api-key"
```
Replace your-api-key with the API key that you copied in step 5.

7. Reload your shell configuration file by running the following command:
```
source ~/.bashrc #or source ~/.zshrc or source ~/.bash_profile
```
depending on which file you edited in step 6.
Your OpenAI API key is now set up and ready to use. You can use it in your Python code by accessing the os.environ["OPENAI_API_KEY"] variable.

### To use myaibot, simply call the myaibot function with the input string as an argument:

```
import myaibot
```
myaibot.myaibot("Hello, how are you today?")
This will print the bot's response to the user's input.

You can also pass the --debug flag to enable debug output:
```
python -m myaibot --input "Hello, how are you today?" --debug
```
## Credits
myaibot was developed by Hamid Ali Syed.

## License
myaibot is released under the MIT License. See the LICENSE file for more details.