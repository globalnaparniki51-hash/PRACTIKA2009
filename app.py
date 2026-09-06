from flask import Flask, jsonify, request, render_template

# 1. Говорим Питону: "Вот наше приложение"
app = Flask(__name__)

# 2. Наш каталог воды (пока храним прямо здесь)
catalog = [
    {"id": 1, "name": "Байкальская глубина", "price_rub": 450, "image": "baykal.jpg"},
    {"id": 2, "name": "Архыз Vita", "price_rub": 120, "image": "arhiz.png",}
]

# 3. Страница нашего сайта "/"
@app.route('/')
def home():
    return "<h1>Магазин артезианской воды работает!</h1><p>Перейдите на /api/catalog</p>"





@app.route('/api/product/<int:id>')
def get_product(id):
    # Ищем продукт по id
    for p in catalog:
        if p['id'] == id:
            return render_template('product.html', product=p)
    
    # Если не нашли - возвращаем ошибку
    return jsonify({"error": "Product not found"}), 404


# 4. Адрес "/api/catalog" отдает список воды
@app.route('/api/catalog')
def get_catalog():
    return jsonify(catalog)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


if __name__ == '__main__':
    # Запускаем сервер
    app.run(debug=True)# Добавляем маршрут для страницы конкретного продукта
    