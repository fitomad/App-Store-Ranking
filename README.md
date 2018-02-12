# App-Store-Ranking
Obtain your app ranking in realtime inside App Store and Mac App Store for every country

![License MIT](https://img.shields.io/github/license/mashape/apistatus.svg) ![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg) ![macOS 10.13](https://img.shields.io/badge/macOS-10.13-orange.svg) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-1.20-red.svg)

![Terminal](https://github.com/fitomad/App-Store-Ranking/blob/master/Images/terminal.png)

## Usage

This repository contains two scripts, one for App Store (iosr.py) and the other one for Mac App Store (macr.py)

You can obtain command information by typing command listed below in your Terminal or Command Prompt:

```bash
python iosr.py --help

# or

python macr.py --help
```

To obtain a list with all possible values for all script parameters run this command in Terminal or Command Prompt:

```bash
python iosr.py

#or

python macr.py
```

### App Store Ranking. Parameters

To obtain an application ranking inside the App Store you have to type this command in Terminal or Command Prompt

```bash
python iosr.py -appid 361309726 -stores top -category 6007 -platform iphone
```

This returns the ranking for **Pages** app `(-appid 361309726)` in the **Top 10 countries by revenue** `(-stores top)` inside the **Productivity category** `(-category 6007)` for **iPhone** devices `(-platform iphone)`

Available stores sets are `world` for all countries where Apple has an App Store available and `top` for the ten countries with more revenues.

Platforms availables are `iphone` for iPhone only devices, `ipad` for iPad only devices and `appleTV` for Apple TV only devices.

To figure out the code related to yout app category type `python iosr.py` in your command line to get a list with all possible values.

### Mac App Store Ranking. Parameters

Request Mac App Store rankings is similar to App Store Ranking procedure. Type this command in Terminal or Command Prompt

```bash
python macr.py -appid 424389933 -category 12020 -stores world
```

This returns the **Final Cut Pro** application `(-appid 424389933)` ranking inside the **Video category** `(-category 12020)` in **all Mac App Store countries** `(-stores world)`

Available stores sets are `world` for all countries where Apple has a Mac App Store available and `top` for the ten countries with more revenues.

To figure out the code related to yout app category type `python macr.py` in your command line to get a list with all possible values.


## Contact

Comments and suggestions are welcome. Find me on twitter at [@fitomad](https://twitter.com/fitomad)
