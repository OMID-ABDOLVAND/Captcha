# Django CAPTCHA Service with API Key Authentication

This project is a Django-based CAPTCHA service that uses API key authentication to generate and validate CAPTCHAs. The service provides a secure and customizable solution for adding CAPTCHA protection to web applications.

## Features

- **API Key Authentication:** Secure the CAPTCHA endpoints using API key authentication.
- **CAPTCHA Generation:** Dynamically generate CAPTCHA images and text.
- **CAPTCHA Validation:** Validate user input against the generated CAPTCHA.
- **Customizable CAPTCHA Options:** Configure CAPTCHA text, images, noise, and more.

## Why Use This Project?

This CAPTCHA service provides a simple and secure way to prevent automated bots from accessing or abusing your web application. By using API key authentication, the service ensures that only authorized clients can access the CAPTCHA endpoints, adding an additional layer of security. It's particularly useful in scenarios where:

- You want to add CAPTCHA protection to forms, such as login, signup, or contact forms.
- You need to ensure that only real users (not bots) are interacting with your application.
- You require a customizable CAPTCHA solution that can be integrated into different applications.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- Django Rest Framework (DRF)
- `Pillow` library for image processing

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

### Endpoints

- **Generate CAPTCHA:**  
  `GET /generate/`  
  Requires API key authentication and returns a CAPTCHA image and ID.

- **Validate CAPTCHA:**  
  `POST /validate/`  
  Requires API key authentication and validates the CAPTCHA response.

### API Key Authentication

To access the endpoints, you need to authenticate using an API key. API keys are associated with users in the system.

1. **Create a User:** Register or create a user via the Django admin panel.
2. **Generate API Key:** The API key is automatically generated when the user is created. Use this key in the request headers.

### Example Request

```http
GET /generate/
Headers:
  API-Key: your_api_key_here
```

### Example Response
```json
{
  "captcha_id": "abcd1234efgh5678",
  "image": "base64_encoded_image_string"
}
```

### Models
1. **APIKey** :
Stores the API key associated with each user.

2. **Captcha**:
Stores the CAPTCHA text, image (Base64 encoded), and metadata like IP address.

## Decoding the CAPTCHA Image

The CAPTCHA image is returned as a Base64-encoded string. To use it in a real project, you need to decode it into an image format that can be rendered in a web browser.

### Example: Decoding in JavaScript

You can decode and display the image using JavaScript in your web application as follows:

```javascript
// Assume you have the base64 image string from the API response
const base64Image = "base64_encoded_image_string";

// Create an image element
const imgElement = document.createElement('img');
imgElement.src = `data:image/png;base64,${base64Image}`;

// Append the image to the desired location in your document
document.getElementById('captcha-container').appendChild(imgElement);
```

**Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements.**