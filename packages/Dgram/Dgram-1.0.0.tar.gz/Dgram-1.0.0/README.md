
[![PyPi Package Version](https://img.shields.io/pypi/v/dgram.svg)](https://pypi.python.org/pypi/dgram)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/dgram.svg)](https://pypi.python.org/pypi/dgram)
[![Documentation Status](https://readthedocs.org/projects/pytba/badge/?version=latest)](https://pytba.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/eternnoir/dgram.svg?branch=master)](https://travis-ci.org/eternnoir/dgram)
[![PyPi downloads](https://img.shields.io/pypi/dm/dgram.svg)](https://pypi.org/project/dgram/)
[![PyPi status](https://img.shields.io/pypi/status/dgram.svg?style=flat-square)](https://pypi.python.org/pypi/dgram)

# <p align="center">dgram

<p align="center">A simple, but extensible Python implementation for the <a href="https://core.telegram.org/bots/api">Telegram Bot API</a>.</p>
<p align="center">Both synchronous and asynchronous.</p>

## <p align="center">Supported Bot API version: <a href="https://core.telegram.org/bots/api#november-5-2022">6.3</a>!

<h2><a href='https://pytba.readthedocs.io/en/latest/index.html'>Official documentation</a></h2>
	
## Contents

  * [Getting started](#getting-started)
  * [Writing your first bot](#writing-your-first-bot)
    * [Prerequisites](#prerequisites)
    * [A simple echo bot](#a-simple-echo-bot)
  * [General API Documentation](#general-api-documentation)
    * [Types](#types)
    * [Methods](#methods)
    * [General use of the API](#general-use-of-the-api)
      * [Message handlers](#message-handlers)
      * [Edited Message handler](#edited-message-handler)
      * [Channel Post handler](#channel-post-handler)
      * [Edited Channel Post handler](#edited-channel-post-handler)
      * [Callback Query handlers](#callback-query-handler)
      * [Shipping Query Handler](#shipping-query-handler)
      * [Pre Checkout Query Handler](#pre-checkout-query-handler)
      * [Poll Handler](#poll-handler)
      * [Poll Answer Handler](#poll-answer-handler)
      * [My Chat Member Handler](#my-chat-member-handler)
      * [Chat Member Handler](#chat-member-handler)
      * [Chat Join request handler](#chat-join-request-handler)
    * [Inline Mode](#inline-mode)
      * [Inline handler](#inline-handler)
      * [Chosen Inline handler](#chosen-inline-handler)
      * [Answer Inline Query](#answer-inline-query)
    * [Additional API features](#additional-api-features)
      * [Middleware handlers](#middleware-handlers)
      * [Custom filters](#custom-filters)
      * [dgram](#dgram)
      * [Reply markup](#reply-markup)
  * [Advanced use of the API](#advanced-use-of-the-api)
    * [Using local Bot API Server](#using-local-bot-api-sever)
    * [Asynchronous dgram](#asynchronous-dgram)
    * [Sending large text messages](#sending-large-text-messages)
    * [Controlling the amount of Threads used by dgram](#controlling-the-amount-of-threads-used-by-dgram)
    * [The listener mechanism](#the-listener-mechanism)
    * [Using web hooks](#using-web-hooks)
    * [Logging](#logging)
    * [Proxy](#proxy)
    * [Testing](#testing)
  * [API conformance limitations](#api-conformance-limitations)
  * [Asyncdgram](#asyncdgram)
  * [F.A.Q.](#faq)
    * [How can I distinguish a User and a GroupChat in message.chat?](#how-can-i-distinguish-a-user-and-a-groupchat-in-messagechat)
    * [How can I handle reocurring ConnectionResetErrors?](#how-can-i-handle-reocurring-connectionreseterrors)
  * [The Telegram Chat Group](#the-telegram-chat-group)
  * [Telegram Channel](#telegram-channel)
  * [More examples](#more-examples)
  * [Code Template](#code-template)
  * [Bots using this library](#bots-using-this-library)

## Getting started

This API is tested with Python 3.7-3.11 and Pypy 3.
There are two ways to install the library:

* Installation using pip (a Python package manager):

```
$ pip install dgram
```
* Installation from source (requires git):

```
$ git clone https://github.com/DEV-Degram/dgram.git
$ cd dgram
$ python setup.py install
```
or:
```
$ pip install git+https://github.com/eternnoir/dgram.git
```
* Started Code:
```
import dgram

bot = dgram.dgram("YOUR_TOKEN_HERE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome, dear!")

bot.polling()
```


