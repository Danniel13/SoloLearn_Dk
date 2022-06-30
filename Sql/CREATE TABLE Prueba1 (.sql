CREATE TABLE Prueba1 (
  ID int IDENTITY,
  nombre VARCHAR(50),
  Correo VARCHAR(50),
  edad SMALLINT
)
INSERT INTO Prueba1 (nombre, correo, edad)
VALUES('Daniel', 'danielgz.m@hotmail.com',28)

SELECT * FROM Prueba1