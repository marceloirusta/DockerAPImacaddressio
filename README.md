
# Simple Coding Homework Assignment
The main approach to solve this assignment was by doing a python script inside a linux enviroment, setting this up
inside a Docker container.

The way this works is that the python file does a GET request to the macaddress.io API,
by providing a specific mac address in the request, and just take the Company Name from the
response and show that Company Name to the user, along with a google link which redirects
to the company page or any other link related to the company. (Feature supported by
Google's "I'm feeling Lucky").

Talking about security; from one side the mac address API has a security wall by 
requesting a user to get an API key, so from that perspective a user should not be able to
do any request from an idependent way. But, if somehow the user of this script manages to
see the content of the script, he would be able to see what's the API key being used at that moment.
So the way I proposed to deal with this situation is to have the API key being set at an OS level, by 
storing the key value as an environment variable in the OS. That way the script will only call to that variable
without having it as a plain text.




## Run Locally

Clone the project

```bash
  git clone https://github.com/marceloirusta/DockerAPImacaddressio.git
```

Go to the project directory

```bash
  cd <<ProjectDirectory>>
```

Build your docker image

```bash
  docker build -t python-img-mac .
```

Run the created image

```bash
  docker run -t -i python-img-mac
```

After this last command is run, the script will require you to input a mac address, you
can provide any mac address you want.

For example: 44:38:39:ff:ef:57

Expected Response:

You'll get a message with the company name associated with that mac addres and a link related to the actual company. You can click on it an it will redirect you either to the company page or a google confirmation page previous to your destination URL.


![alt text](https://files.slack.com/files-pri/T02LRKTL7-F048V8KSMA5/image.png?pub_secret=034bc5cb2f)

## Authors

- [@marceloirusta](https://www.github.com/marceloirusta)

