CREATE TABLE transactions (
  id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  date VARCHAR,
  customer_id VARCHAR,
  payment_method VARCHAR(50),
  delivery_status VARCHAR(50),
  duration VARCHAR,
  orders VARCHAR,
  amount VARCHAR
);

