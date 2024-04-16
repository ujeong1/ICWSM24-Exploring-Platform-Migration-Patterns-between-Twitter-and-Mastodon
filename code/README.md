# User Profile Crawler Documentation

This repository hosts scripts designed for crawling user profiles, utilizing IDs found in the 'data' directory. It includes scripts tailored for different platforms, including Mastodon and Twitter. These scripts enable users to retrieve profiles from specified instances or platforms, subject to authentication and access requirements.

## Prerequisites

Before running any scripts, ensure you have installed all necessary dependencies by running: `pip install -r requirements.txt`


## Specific Requirements

- **Mastodon**: To use `crawl_mastodon_user_profiles.py`, you must have an account on the Mastodon instance you wish to access. You need to provide different accounts according to the instance you access as this script relies on authenticated API endpoints for data retrieval.
- **Twitter**: Due to Twitter's transition to a priced model for API access, a token from the Twitter API is required for crawling user profiles. Ensure you have obtained and configured your API token before attempting to crawl Twitter user profiles.

