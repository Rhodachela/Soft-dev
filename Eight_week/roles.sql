CREATE ROLE StudentAdmin;
GRANT SELECT, INSERT, UPDATE, DELETE ON Students TO StudentAdmin;
CREATE USER "Admin_user" IDENTIFIED BY "Password123";
GRANT StudentAdmin to "Admin_user";