# FastAPI Product Search API

This is a simple FastAPI-based project to search and paginate products stored in a MySQL database. The API allows clients to query product names and retrieve product details such as price, image, quantity, and rating.

##  Setup Instructions

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Setup `.env` file.

3. Run the API Server:

    ```bash
    uvicorn main:app --reload
    ```

## API Usage

### Search Products

**GET** `/search?query=amul&page=1&page_size=5`

**Query Parameters:**

- `query` (required): Search term (min 1 character)
- `page`: Page number (default: 1)
- `page_size`: Results per page (default: 10)

### Example Response:

```json
[
  {
    "product name": "Amul Chocolate Ice Cream",
    "price": "120.00",
    "image": "amul_choco.jpg",
    "quantity": "500 ml",
    "rating": "4.4"
  },
  ...
]
```

### Setup Database
```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    quantity VARCHAR(100),
    image VARCHAR(255),
    rating DECIMAL(3, 2)
);

INSERT INTO products (name, price, quantity, image, rating) VALUES
("Amul Chocolate Ice Cream", 120.00, "500 ml", "amul_choco.jpg", 4.4),
("Kwality Walls Butterscotch", 99.00, "700 ml", "kwality_butterscotch.jpg", 4.2),
("Vadilal Vanilla Ice Cream", 110.00, "1 L", "vadilal_vanilla.jpg", 4.1),
("Amul Strawberry Magic", 85.00, "500 ml", "amul_strawberry.jpg", 4.3),
("Naturals Tender Coconut", 180.00, "500 ml", "naturals_coconut.jpg", 4.6),
("Havmor Kesar Pista", 130.00, "700 ml", "havmor_kesar.jpg", 4.5),
("Kwality Walls Choco Brownie", 150.00, "750 ml", "kwality_brownie.jpg", 4.4),
("Vadilal Rajbhog", 160.00, "1 L", "vadilal_rajbhog.jpg", 4.2),
("Amul Mango Dolly", 30.00, "1 piece", "amul_mango_dolly.jpg", 4.0),
("Cornetto Choco Cone", 45.00, "1 cone", "cornetto_choco.jpg", 4.3);
```