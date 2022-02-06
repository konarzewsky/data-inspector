from dotenv import dotenv_values
import os

# development: get variables from .env file
config = dotenv_values(".env")

# production: get variables with os package
if len(config) == 0:
    config = {
        'LINKEDIN_LOGO_URL': os.getenv('LINKEDIN_LOGO_URL'),
        'LINKEDIN_PROFILE_URL': os.getenv('LINKEDIN_PROFILE_URL'),
        'GITHUB_LOGO_URL': os.getenv('GITHUB_LOGO_URL'),
        'GITHUB_PROFILE_URL': os.getenv('GITHUB_PROFILE_URL'),
        'MAPBOX_ACCESS_TOKEN': os.getenv('MAPBOX_ACCESS_TOKEN'),
    }
