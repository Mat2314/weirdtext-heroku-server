# WeirdText Server
A web server which enables encoding and decoding weirdtext messages.
A running application testing server functionalities can be found here: https://weirdtext-client.herokuapp.com/

## Endpoints
The server runs by default on port 8000. 
Below there is a list of endpoints used in the web server.

Endpoint | Method | Payload | Returned value | Description |
---------|--------|---------|----------------|-------------|
/v1/encode/ | POST | message: string | ok: string, encoded_message: string, original_words: list | Endpoint is encoding given message. It returns encoded text and list of original words (necessary to decode the message). 
/v1/decode/ | POST | weirdtext: string, original_words: list | ok: string, decoded_message: string, error: string, error_type: string | Endpoint is decoding given message. It requires weirdtext as a message which was encoded and original_words as a list of words in their original form. If there's any unexpected error endpoint returns error message and error_type which more specifically describes what went wrong.

## Examples of usage
Running server example can be found here: https://weirdtext-server.herokuapp.com/ 

#### Encoding

Encode the message: `curl -X POST -H 'Content-Type: application/json' -d '{"message":"This is my message"}' https://weirdtext-server.herokuapp.com/v1/encode/`

Server returns the following response: `{"ok": "Successfully encoded the message", "encoded_message": "\n--weird--\nTihs is my msegase\n--weird--\n", "original_words": ["This", "is", "message", "my"]}`

#### Decoding

Now to decode this message let's run the following command: `curl -X POST -H 'Content-Type: application/json' -d '{"weirdtext":"\n--weird--\nTihs is my msegase\n--weird--\n","original_words":["This", "is", "message", "my"]}' https://weirdtext-server.herokuapp.com/v1/decode/`

It will return the following response: `{"ok": "Successfully decoded the message", "decoded_message": "This is my message"}`

#### Error handling

To test what's going to happen when the parameters will not be correct, simply run the command with wrong values. 
It can be either deleted magic separator `\n--weird--\n` or removed original words or other modification of weirdtext.

Example: `curl -X POST -H 'Content-Type: application/json' -d '{"weirdtext":"\n--weird--\nTihs is my msegase\n--weird--\n","original_words":["No", "way", "it", "will", "be", "corrrrrrrrrrect"]}' https://weirdtext-server.herokuapp.com/v1/decode/`

In return we'll get this response: `{"error": "Could not decode the message", "error_type": "Words length in both versions differ"}`
which basically means that length of original words array and length of the weirdtext message is different. 

## Running the application locally

To run the server locally download this repo and do the following steps:

- Go to `environments` directory
- Run script `./localenv.sh`
- Go back to root directory
- Run `docker-compose up` 
- The server should be listening on localhost on port 8000