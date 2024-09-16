"""Configuration module for the application"""
import os
import json

# Load configuration from JSON file
with open('/etc/benefitshub_config.json') as config_file:
    config = json.load(config_file)

class Config:
    """Configuration class for the application"""
    # Secret key for Flask sessions and security    
    SECRET_KEY = config.get('SECRET_KEY')
    
    # Database URI for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    
    # Email configuration
    # SMTP server settings for Gmail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465  # Port for SSL
    MAIL_USE_SSL = True  # Use SSL for secure connection
    
    # Email credentials from config file
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')
