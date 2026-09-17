from django.shortcuts import render

# Create your views here.

def catalog(request):
    products = [
        {
            "name": "Laptop",
            "price": 55000,
            "category": "Electronics",
            "description": "Powerful laptop for work and study.",
            "rating": 4.5,
            "in_stock": True,
        },
        {
            "name": "Smartphone",
            "price": 25000,
            "category": "Electronics",
            "description": "Modern smartphone with a high-quality camera.",
            "rating": 4.3,
            "in_stock": True,
        },
        {
            "name": "Headphones",
            "price": 3000,
            "category": "Accessories",
            "description": "Wireless headphones with clear sound.",
            "rating": 4.1,
            "in_stock": False,
        },
        {
            "name": "Keyboard",
            "price": 1500,
            "category": "Accessories",
            "description": "Comfortable keyboard for everyday use.",
            "rating": 4.0,
            "in_stock": True,
        },
        {
            "name": "Smart Watch",
            "price": 5000,
            "category": "Wearables",
            "description": "Smart watch with fitness tracking features.",
            "rating": 4.4,
            "in_stock": False,
        },
    ]

    return render(request, "products/catalog.html", {"products": products})