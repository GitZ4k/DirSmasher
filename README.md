# DirSmasher
 Directory Brute Forcer is a user-friendly and simple Python tool for discovering hidden directories on a website by brute-forcing potential paths using a wordlist. It supports customizable status code filters, multi-threading for fast execution, and color-coded results for easy analysis.

**Installation and Usage**
To install the required libraries for the script, run the following command:
pip install -r requirements.txt

**Using the Script**

*Input Status Codes*: When prompted, enter the status codes you want the script to look for. You can input multiple status codes by separating them with either commas or spaces.

Examples:
200, 301, 404
or
200 301 404

*Input Wordlist Path*: When prompted, enter the path to the wordlist file. Make sure the wordlist file is located in the same directory as the script for convenience. For example, you can use the common.txt wordlist file that has been provided.

*Input Website URL*: Enter the target website URL for the brute-force scanning. The script will automatically ensure that the URL starts with https:// and ends with a /.

Example:
https://example.com
