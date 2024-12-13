# TikTokBoost 🎵

<div align="center"><img src=https://i.pinimg.com/originals/f2/2b/cf/f22bcf30acbab8d3fdffaa10c7926d19.gif></div>

TikTokBoost is a Python-based tool that allows you to automate various TikTok growth tasks such as liking, following, sharing, and viewing. This project is highly inspired by the [xtekky-zefoy](https://github.com/xtekky/zefoy) repository.

>[!WARNING]
>on maintenance, this script is highly dependent on zefoy.com, so if there is an error from zefoy.com (ex: too many request) you cant do anything about that but wait until the feature is working properly, you can go directly to [zefoy](https://zefoy.com) to check it yourself before automate the process using this script.

## Update 11/2024

- **auto captcha** = user no longer need to input captcha manually like in demo video
- **fix Comments Hearts** = after input the url user need to input comments id, this is the video example of how to get it [video by plowside](https://youtu.be/AjRFf5jw9Vw)
- **add command line arguments** = you can directly write link, comment id and limit when runing the script
- **change default to headless** = change default selenium to headless, do "--show" to make browser visible

## Installation

1. Clone the repository:

```
git clone https://github.com/Ifarra/TikTokBoost.git
```

2. Navigate to the project directory:

```
cd TikTokBoost
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

## Usage

To run the TikTokBoost script, use the following command:

```
python main.py
```

you can use command line arguments for faster input

- `--url [str]`
- `--comment [str]`

```
# for url
python main.py --url https://www.tiktok.com/@gatowcbyrsc112/video/7401028246650752264

# for url and comment id
python main.py --url https://www.tiktok.com/@gatowcbyrsc112/video/7401028246650752264 --comment 7401038661750326023
```

you can also make the browser visible by using show option

```
python main.py --show
```

The script will guide you through the necessary steps to start automating your TikTok growth tasks.

## Interface

```
Modified by:
██╗███████╗ █████╗ ██████╗ ██████╗  █████╗
██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║█████╗  ███████║██████╔╝██████╔╝███████║
██║██╔══╝  ██╔══██║██╔══██╗██╔══██╗██╔══██║
██║██║     ██║  ██║██║  ██║██║  ██║██║  ██║
╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

 [-] Select your option below.

 [1] followers [OFFLINE]
 [2] hearts [OFFLINE]
 [3] comment_hearts [WORKS]
 [4] views [WORKS]
 [5] shares [OFFLINE]
 [6] favorites [WORKS]
 [7] Set Limit
```

> The availability of the feature depends on the third-party Zefoy.com

## Demo (old version)

https://github.com/user-attachments/assets/1747b5ef-9b62-45c0-b3dc-8b1dfcadf86f

## Disclaimer

This tool is for educational purposes only. Use it at your own risk, and make sure to comply with TikTok's terms of service.
