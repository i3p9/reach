# Reach: A WiFi Channel Analyzer

Reach automagically searches and figures out the best wifi channel for your network avoiding populated channels.

## Usage: 

First of all, enable the built in airport service on macOS. This command simply copies the `airport` binary into PATH,`usr/local/bin/`so that it can be called from terminal. 

```bash
sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport
```

Then, clone this repo and run

```bash
python3 main.py
```

Everything else should be self-explanatory.

## To-do

- Better findchannel algorithm (wip)
- Support for Windows and Linux



<img src="https://i.imgur.com/xSTmoPz.png" style="zoom:67%;" />