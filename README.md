# BenefitsHub Nigeria

BenefitsHub Nigeria is a web application that connects Nigerian citizens with government benefits and services. It serves as a centralized platform where government agencies can list available benefits, and citizens can easily discover, view, and apply for these benefits.

You can also make blog posts on any topic and share them with the world.


Features

- User registration and authentication for both citizens and government agencies
- Profile management for users
- Benefit listing and management for government agencies
- Search and filter functionality for benefits
- Application process for citizens to request benefits
- Admin dashboard for managing users and benefits

Technologies Used

- Python 3.8+
- Flask web framework
- SQLAlchemy ORM
- SQLite3 database
- HTML, CSS, JavaScript
- Bootstrap for responsive design

Installation

1. Clone the repository:
   ```
   git clone https://github.com/JuliusDgenius/alx-portfolio_project.git
   cd alx-portfolio_project
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the configuration:
   - Create a `config.json` file in the `/etc/` directory with the following structure:
     ```json
     {
       "SECRET_KEY": "your_secret_key",
       "SQLALCHEMY_DATABASE_URI": "postgresql://user:password@localhost/benefitshub",
       "EMAIL_USER": "your_email@gmail.com",
       "EMAIL_PASS": "your_email_password"
     }
     ```

5. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```
   python wsgi.py
   ```

Usage

1. Access the application at `https://benefitshub.juliusdgenius.tech/`
2. Register as a user or government agency
3. Log in to your account
4. Explore available benefits or create new benefit listings (for agencies)
5. Apply for benefits or manage applications (depending on user type)

Contributing

We welcome contributions to BenefitsHub Nigeria. Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Contact

Your Name - (https://twitter.com/@0xjulius_) - ibejulius1@gmail.com

Project Link: [https://github.com/JuliusDgenius/alx-portfolio/]

Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
