# API Fetcher Program

This program fetches data from two APIs: GitHub and NASA. You can easily retrieve information from either API by providing your email and specifying which API you want to query.

When you query the NASA API, you'll receive the Astronomy Picture of the Day (APOD), which includes an image, along with a brief explanation of the content. 

If you choose to fetch data from the GitHub API, you will receive a summary of my GitHub portfolio. This summary includes titles, links to repositories, and the programming languages used in each project.

## Setup Instructions

1. **Create a `.env` File**:  
   Before running the program, create a `.env` file in the same directory as your `send.py` file. Add your email and app password to this file using the following format:

   ```plaintext
   EMAIL=your_email@gmail.com
   PASSWORD=your_app_password
If you are unsure how to create an app password for Gmail, please refer to this [Gmail App Passwords Guide](https://support.google.com/mail/answer/185833?hl=en).

## Running the Program

To run the program, open your terminal and use the following commands:

- To fetch data from GitHub:
  ```bash
  python main.py your_email github
- To fetch data from Nasa:
  ```bash
  python main.py your_email nasa

- To run the tests:
  ```bash
  pytest test

## Results
<img width="390" alt="nasa" src="https://github.com/user-attachments/assets/4c225065-b0a1-4d6e-a72c-840eb86d9d48">

<img width="384" alt="github" src="https://github.com/user-attachments/assets/6405cf2b-7aca-4941-b497-673f337b181a">
