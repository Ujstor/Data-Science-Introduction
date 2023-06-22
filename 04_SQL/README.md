# DB Setup
Short steps for downloading, setting up, and importing the `classicmodels.db` file into MySQL:

1. Download the `classicmodels.db` file.

2. Install MySQL: Visit the official MySQL website (https://dev.mysql.com/downloads/) and download the appropriate version of MySQL for your operating system. Follow the instructions to install MySQL on your system. You may be prompted to set a root password for MySQL during the installation process. Make sure to remember this password, as you'll need it to import the `classicmodels.db` file.

3. Run the import command: Execute the following command to import the `classicmodels.db` :

   ```
   mysql -u root -p < classicmodels.db
   ```

   You may be prompted to enter the MySQL root password.

4.  Verify the imported data: Re-access the MySQL CLI using the `mysql -u root -p` command. Switch to the imported database using the following command:

    ```
    USE classicmodels;
    ```

    You can then run SQL queries to verify that the data from the `classicmodels.db` file has been successfully imported into the database.
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



<br><br>
- [SQL Tutorial for Beginners](https://www.youtube.com/watch?v=-fW2X7fh7Yg&t=10535s)
- [Relational Databases and SQL](https://jovian.com/aakashns/relational-databases-and-sql)
- [Aggregation and Joins with SQL](https://jovian.com/aakashns/advanced-sql-aggregation-and-joins)
