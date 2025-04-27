from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "بوت الأنمي شغال!", 200

@app.route('/anime', methods=['POST'])
def get_anime():
    data = request.get_json()
    anime_name = data.get('name', 'Naruto')  # مثال لو لم يرسل اسم

    # مبدئياً بيانات ثابتة للتجربة
    response = {
        'title': anime_name,
        'story': 'هذه قصة أنمي رائعة!',
        'rating': '8.5',
        'image_url': 'https://example.com/anime.jpg',
        'characters': ['شخصية 1', 'شخصية 2', 'شخصية 3']
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)