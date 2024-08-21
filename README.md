
# Ubike_InTime_Search

Ubike InTime Search system

## Project Overview

The **Ubike InTime Search** system is designed to provide real-time information about Ubike stations, including the availability of bikes and parking spaces. This project is built using Flask for the backend and MSSQL as the database.

## Features

- Real-time search for Ubike stations.
- Availability status of bikes and parking spaces.
- Responsive web interface.
- Integration with MSSQL database for efficient data management.

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: MSSQL


## Installation

### Prerequisites

- Python 3.x
- MSSQL Server
- Flask
- MSSQL Python Driver (`pyodbc` or equivalent)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Ubike_InTime_Search.git
   cd Ubike_InTime_Search
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MSSQL Database**
   - Create a database in MSSQL Server.
   - Execute the provided SQL scripts (if any) to set up the required tables.

5. **Configuration**
   - Create a `.env` file or update the `config.py` file with your MSSQL database credentials.
   - Example `.env` file:
     ```
     DB_SERVER=your_server
     DB_NAME=your_database
     DB_USER=your_username
     DB_PASSWORD=your_password
     ```

6. **Run the Application**
   ```bash
   flask run
   ```

## Configuration

- **Database Configuration**: Ensure that your MSSQL server is running and accessible. Update the database connection strings in your configuration file.
- **Environment Variables**: Use a `.env` file or directly configure the environment variables in your system.

## Usage

1. **Accessing the Application**
   - The application can be accessed via a web browser at `http://localhost:5000`.

2. **Searching for Ubike Stations**
   - Use the search feature on the homepage to find real-time information about Ubike stations.



## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

- **Author**: Jack Chang
- **Email**: jkchang115@gmail.com

![image](https://github.com/user-attachments/assets/6b1d9c15-c0ef-49f5-b57c-3f556ad01144)

![image](https://github.com/user-attachments/assets/5ea431f2-45dc-48fa-9ace-599205a9c5dc)
