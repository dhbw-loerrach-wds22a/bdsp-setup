# Database Setup Instructions
# See services repository for setup instructions

## Overview
This repository contains a script and configurations for setting up a MySQL database, along with  importing data into the database.

## Repository setup
Clone the repositories from [GitHub](https://github.com/dhbw-loerrach-wds22a)
1. [bdsp-setup](https://github.com/dhbw-loerrach-wds22a/bdsp-setup)
3. [bdsp-extract-pipe](https://github.com/dhbw-loerrach-wds22a/bdsp-extract-pipe)
4. [bdsp-services](https://github.com/dhbw-loerrach-wds22a/bdsp-services)

Layout of the repositories:

Project folder
  - bdsp-setup
  - bdsp-extract-pipe
  - bdsp-services

## Files Description
- `setup_mysql.py`: Script for setting up the MySQL database.
- `fake_data.py`: Script for creating dummy data.
- `check_dup.py`: Script that checks for duplicates.
- `requirements.txt`: Contains a list of Python packages required to run the scripts.

## Prerequisites
- Python 3.x installed.
- Access to theMySQL container. See repository "bdsp-services" for the docker containers needed to run this project.

## Installation
1. Clone the repository to your local machine.
2. Install the required Python packages:
```pip install -r requirements.txt```

## Adding the Customer Dataset
1. Download the Yelp dataset from the official [eCommerce behavoir data](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store/).
2. Place the individual files from the downloaded dataset in the `data` folder, which should be in the same directory as the scripts.


## Configuration
Before running the setup script:

- Ensure MySQL service is running.
- Update the script with the correct MySQL connection details and credentials.

## Running the Script
Run the setup scripts to configure the databases:
```python setup_mysql.py```


## Security Note
The setup scripts contain sensitive information such as server credentials. Ensure that these details are secured and not exposed in public repositories or unsecured files.

## Support
For any issues or questions, please open an issue in the repository or contact the repository maintainer.

