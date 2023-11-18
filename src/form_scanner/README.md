# Web Scraping Project

## Overview
This project is a Python-based web scraping tool designed to extract specific information from a list of URLs. The script scrapes data like the title of forms, the institution owning the form, alternate language URLs, and more. The results are saved in both JSON and CSV formats.

## Features
- Scrape web pages for specific information within forms.
- Handles various HTML structures and web page layouts.
- Outputs data in both JSON and CSV formats for easy analysis.
- Includes progress tracking for large sets of URLs.

## Prerequisites
Before you run the script, ensure you have the following installed:
- Python 3
- `requests`
- `beautifulsoup4`
- `tqdm`

You can install the required Python libraries using:

```bash
pip install requests beautifulsoup4 tqdm
```

## Installation
1. Clone the repository or download the script to your local machine.
2. Ensure you have the required libraries installed (see Prerequisites).

## Usage
1. Place your list of URLs in a text file (e.g., `forms.txt`).
2. Run the script from your command line:

```bash
python main.py
```

3. Check the output files (`scraped_data.json` and `scraped_data.csv`) for the results.

## Testing
To run the tests, execute the following command:

```bash
python -m unittest
```

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your updates.

## License
Unless otherwise noted, computer program source code of the Alpha Canada.ca is
covered under Crown Copyright, Government of Canada, and is distributed under the MIT License.

The Canada wordmark and related graphics associated with this distribution are protected under
trademark law and copyright law. No permission is granted to use them outside the parameters
of the Government of Canada's corporate identity program. For more information, see
https://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp

Copyright title to all 3rd party software distributed with the Web Experience Toolkit (WET) is
held by the respective copyright holders as noted in those files. Users are asked to read the
3rd Party Licenses referenced with those assets.


MIT License

Copyright (c) 2014 Government of Canada

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.