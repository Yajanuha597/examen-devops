CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio NUMERIC(10,2),
    stock INTEGER
);

INSERT INTO productos (nombre, precio, stock)
VALUES
('Laptop', 850.50, 10),
('Mouse', 15.00, 50),
('Teclado', 25.00, 30),
('Monitor', 180.00, 15),
('Impresora', 220.00, 8);