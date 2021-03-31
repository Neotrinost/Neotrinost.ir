# Neotrinost.ir

- programmer : Amirhossein Mohammadi

---

**Create User**

```mysql
CREATE USER 'neotrinost'@'localhost' IDENTIFIED BY 'neotrinost';
GRANT ALL PRIVILEGES ON *.* TO 'neotrinost'@'localhost';
FLUSH PRIVILEGES;
```

**Create Database and Table**

```mysql
CREATE DATABASE neotrinost;
USE neotrinost;
CREATE TABLE admin (usrname TEXT, passwd TEXT);
INSERT INTO admin VALUES ('usernamesample', 'passwordsample');
```

**Fandogh Commands**

```
fandogh login
fandogh imaga publish
fandogh service deploy
```
