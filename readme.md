# AWS test python integration

## Setup RDS 

Go to aws.com => creaete free account

Create RDS DB using "Easy create" option

Config:

* mysql
* free tier
* id: database-1
* username admin
* autogenerate password
* use all default settings
* auto gen password = master password created during the database creation and will be displayed in the credential details. This is the only time you will be able to view this password.

Once db is setup, goto "modify" and make it publicly available

Goto the security group for the DB and change the inbound rule to accept all trafiic

