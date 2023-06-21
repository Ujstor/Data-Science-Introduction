# DB Setup
Short steps for downloading, setting up, and importing the `classicmodels.db` file into MySQL:

1. Download the `classicmodels.db` file.

2. Install MySQL: Visit the official MySQL website (https://dev.mysql.com/downloads/) and download the appropriate version of MySQL for your operating system.

3. Launch the MySQL server: Start the MySQL server using the installed MySQL software. The process for starting the server may vary depending on your operating system.

4. Access the MySQL command-line interface: Open a terminal or command prompt and access the MySQL command-line interface (CLI) by typing the following command and pressing Enter:

   ```
   mysql -u root -p
   ```

   You may be prompted to enter the MySQL root password that you set during the installation process.

5. Create a new database: Once you're in the MySQL CLI, create a new database to import the `classicmodels.db` file into. You can use the following command to create a new database:

   ```
   CREATE DATABASE database_name;
   ```

   Replace `database_name` with your desired name for the database.

6. Exit the MySQL CLI: After creating the database, exit the MySQL CLI by typing `exit` and pressing Enter.

7. Run the import command: Execute the following command to import the `classicmodels.db` file into the previously created database:

   ```
   mysql -u root -p database_name < classicmodels.db
   ```

   Replace `database_name` with the name of the database you created earlier. You may be prompted to enter the MySQL root password.

8.  Verify the imported data: Re-access the MySQL CLI using the `mysql -u root -p` command. Switch to the imported database using the following command:

    ```
    USE database_name;
    ```

    Replace `database_name` with the name of your imported database. You can then run SQL queries to verify that the data from the `classicmodels.db` file has been successfully imported into the database.
<br><br>

## Entity Relationship (ER) Diagram
![ERDaigram](https://i.imgur.com/AlEBoFL.png)
<br><br>

##  Query Tools
[DBeaver Community](https://dbeaver.io/) is a free, open-source, and cross-platform universal database tool that provides a user-friendly interface for managing and working with various databases. It supports a wide range of database systems, including MySQL, PostgreSQL, Oracle, SQL Server, SQLite, and more.
<br><br>
![DBeaver](https://i.imgur.com/lhpLeER.png)

or directly in Jupiter Notebook using %sql and %%sql Jupyter magics
The ipython-sql library provides magic commands to write raw SQL queries in Jupyter notebooks and retrieve results. It uses SQLAlchemy under the hood.

```python
pip install sqlalchemy PyMySQL
pip install ipython-sql

%load_ext sql

from getpass import getpass
password = getpass()

conn_str = "mysql+pymysql://root:{}@localhost:3306/ClassicModels".format(password)

%sql {conn_str}
```
```python
%sql SELECT officeCode, city, phone FROM offices;
```
```python
%%sql

SELECT YEAR(paymentDate) as `year`, 
    MONTH(paymentDate) as `month`, 
    ROUND(SUM(amount), 2) as `totalPayments`
    FROM payments 
    GROUP BY `year`, `month` 
    ORDER BY `year`, `month`;
```




[SQL Tutorial for Beginners](https://www.youtube.com/watch?v=-fW2X7fh7Yg&t=10535s)
