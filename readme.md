# BI Inventory

## Overview

This application presents business intelligence metadata and inventories to users.

## Grabbing this application

Just execute the follwing command to grab the application.

```bash
$ git clone https://github.com/atindale/bi-inventory.git
```

## Creating the database

This application currently needs these tables:

* documents
* tables
* elements
* reports
* cubes
* cube_structure

Create them in MySQL with the following DDL.

```SQL
CREATE TABLE `columns` (
  `column_key` int(11) NOT NULL AUTO_INCREMENT,
  `table_name` varchar(45) DEFAULT NULL,
  `column_name` varchar(45) DEFAULT NULL,
  `column_format` varchar(45) DEFAULT NULL,
  `column_length` varchar(45) DEFAULT NULL,
  `column_label` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`column_key`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
CREATE TABLE `cubes` (
  `cube_key` int(11) NOT NULL AUTO_INCREMENT,
  `business_unit` varchar(45) NOT NULL,
  `cube_name` varchar(45) NOT NULL,
  `cube_description` varchar(200) DEFAULT NULL,
  `cube_source` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cube_key`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
CREATE TABLE `cube_structure` (
  `cube_structure_key` int(11) NOT NULL AUTO_INCREMENT,
  `cube_name` varchar(45) DEFAULT NULL,
  `structure_type` varchar(45) DEFAULT NULL,
  `structure_name` varchar(45) DEFAULT NULL,
  `structure_parts` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cube_structure_key`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
CREATE TABLE `documents` (
  `document_key` int(11) NOT NULL AUTO_INCREMENT,
  `document_type` varchar(45) DEFAULT NULL,
  `document_name` varchar(100) DEFAULT NULL,
  `document_filename` varchar(100) DEFAULT NULL,
  `document_description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`document_key`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
CREATE TABLE `elements` (
  `element_key` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` varchar(45) DEFAULT NULL,
  `element_name` varchar(45) DEFAULT NULL,
  `element_description` varchar(200) DEFAULT NULL,
  `element_notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`element_key`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
CREATE TABLE `glossary` (
  `glossary_key` int(11) NOT NULL AUTO_INCREMENT,
  `glossary_term` varchar(100) DEFAULT NULL,
  `glossary_term_description` varchar(200) DEFAULT NULL,
  `glossary_owner` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`glossary_key`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
CREATE TABLE `reports` (
  `report_key` int(11) NOT NULL AUTO_INCREMENT,
  `business_unit` varchar(45) DEFAULT NULL,
  `report_id` varchar(45) DEFAULT NULL,
  `report_name` varchar(45) DEFAULT NULL,
  `report_description` varchar(100) DEFAULT NULL,
  `report_owner` varchar(45) DEFAULT NULL,
  `report_source` varchar(45) DEFAULT NULL,
  `report_source_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`report_key`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
CREATE TABLE `tables` (
  `table_key` int(11) NOT NULL AUTO_INCREMENT,
  `table_name` varchar(45) DEFAULT NULL,
  `table_description` varchar(45) DEFAULT NULL,
  `update_frequency` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`table_key`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
```

Obviously create your own database and database user beforehand

```SQL
$ mysql
mysql> create database warehouse_inventory
mysql> create user 'newuser'@'localhost' identified by 'password';
mysql> grant all privileges on *.* to 'newuser'@'localhost';
````

## Configuring your database connection

Simply create a config.py file from config.py.example and update the parameters therein.

## Running this application

You can run this application by:

```bash

$ cd app
$ python runserver.py
```
