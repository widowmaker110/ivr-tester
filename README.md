# AWS IVR Testing Client
## _Making IVR testing simple_


This is a sister project to [IVR Testing Server](https://github.com/widowmaker110/ivr-testing-server). Both are needed to make them work. 

Heavy inspiration taken from https://github.com/SketchingDev/ivr-tester

## Features

- Easy to use JSON inputs for unit tests
- Results logged in local JSON database created for you

## Installation

This project runs on a few stacks to perform its operations.

- [AWS](https://aws.amazon.com/) (Connect phone center)
- [Python](https://www.python.org/downloads/) (logic - built on 3.8)
- [ngrok](https://ngrok.com/) (local server for Twilio to ping during calls)
- [Twilio](https://www.twilio.com/) (programmatic phone handling)
- ✨Magic ✨

In this project's directory, install all the libraries to get this running

```sh
pip install -r requirements.txt
```

Run the sister project after configuring it so it performs an server logic.

I'm using [Pycharm](https://www.jetbrains.com/pycharm/) so I just run the project but if you're running CLI commands (in a new tab separate from ngrok):

```sh
python3 main.py
```

## Roadmap

- Ability to handle multiple test files at once
- Test code coverage

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
