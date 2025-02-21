# TELEGRAM ISLAMIC LECTURE DOWNLOADER

## Plans:
- If i could figure out a way to access telegram files outside the package I am using, I plan on developing a basic website.
- Enhancing the script's user-friendliness, making it more interactive and intuitive for users to use.

### Note: You must join the telegram channel you want to download from, before you can download from it using the script.

| Channel Name                              | Link                                                 |
| ---------------------------------------- |------------------------------------------------------|
| Shaykh Dr. Luqman Idris Sekoni Lectures  | [Join](https://t.me/joinchat/VR0OTMQuzCNJDnJ0)       |
| At-Tasfiyah wat-Tarbiya                  | [Join](https://t.me/abunaasir)                       |
| Dr. Sharafuddeen Raji Lectures            | [Join](https://t.me/joinchat/AAAAAFBqo6yHZp1920H73g) |
| 🇳🇬AMUBIEYA ONLINE OFFICIAL CHANNEL©     | [Join](https://t.me/shiekhamubieyalectures)          |

1. **CLONE** the repository on your device
```bash
git clone https://github.com/Afeez1131/telegram_lecture_downloader.git
```

2. **CD** into the directory and create a new virtual environment
```bash
cd telegram_lecture_downloader
python -m venv venv
```

3. **Activate** the virtual environment
```bash
source venv/Scripts/activate
```

4. **Install** the requirements
```bash
pip install -r requirements.txt
```

5. Create a `.env` file, and set values like below; which can be obtained from [https://my.telegram.org/apps](https://my.telegram.org/apps)!
```bash
API_ID=YOUR_TELEGRAM_API_ID
API_HASH=YOUR_TELEGRAM_API_HASH
```

6. Run the following command to get the details of channels you are a member of:
```bash
python get_channels.py
```
If prompted for your Phone number, enter your telegram phone number, then a code would be sent to it, which you would prompted to provide next.

You should have a similar response to:
```bash
You are subscribed to the following channels:
Channel  channel_name has ID -channel_id and title is: channel title
Channel  channel_name has ID -channel_id and title is: channel title
Channel  channel_name has ID -channel_id and title is: channel title
```

7. Open the `main.py` file, replace the `CHANNEL_NAME` value with any channel name you want to download from.

8. Run the `main.py` file using
```bash
python main.py
```

9. If everything is right, a folder should be created with the name of the channel, and you should see the progress of the files getting downloaded in real-time as below;
```bash
    $ python main.py                                                          
Al_Fiqhu_fil_Islam_247_Dr_Sharafuddeen_Gbadebo_Raji_01_Mar_2024.amr: 54.3MB [00:07, 8.09MB/s]                      
File downloaded: Dr. Sharafuddeen Raji Lectures\Al_Fiqhu_fil_Islam_247_Dr_Sharafuddeen_Gbadebo_Raji_01_Mar_2024.amr
Jumu'ah_Khutbah_Wife's_Responsibilities_ep_2_Dr_Sharafuddeen_Raaji.amr: 78.6MB [00:14, 5.66MB/s]                      
File downloaded: Dr. Sharafuddeen Raji Lectures\Jumu'ah_Khutbah_Wife's_Responsibilities_ep_2_Dr_Sharafuddeen_Raaji.amr
Al_Fiqhu_fil_Islam_246_Dr_Sharafuddeen_Gbadebo_Raji_23_Feb_2024.amr: 50.7MB [00:10, 5.07MB/s]                         
File downloaded: Dr. Sharafuddeen Raji Lectures\Al_Fiqhu_fil_Islam_246_Dr_Sharafuddeen_Gbadebo_Raji_23_Feb_2024.amr

```

10. **Contributing and Contact**:

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub: [telegram_lecture_downloader](https://github.com/Afeez1131/telegram_lecture_downloader)

For any further assistance or inquiries, you can contact me at [lawalafeez052@gmail.com](mailto:lawalafeez052@gmail.com).

```
