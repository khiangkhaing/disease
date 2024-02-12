from flask import Flask, render_template

app = Flask(__name__)

# Sample data for diseases
diseases = [
    {
        'name': 'Bacterial Leaf Blight',
        'description': 'Bacterial leaf blight is a common rice disease caused by the bacterium Xanthomonas oryzae. It typically affects rice plants during the growing season, causing characteristic lesions on the leaves. This disease can result in significant yield losses if not managed properly.',
        'image': 'disease1.jpg',
        
        'What it does': 'Bacterial leaf blight is a common rice disease caused by the bacterium Xanthomonas oryzae. It typically affects rice plants during the growing season, causing characteristic lesions on the leaves. This disease can result in significant yield losses if not managed properly.',
        'Why and where it occurs': 'Bacterial leaf blight occurs in regions with high humidity and warm temperatures, which are conducive to bacterial growth. It is prevalent in many rice-growing areas around the world.',
        
        'How to identify': 'Bacterial leaf blight can be identified by the presence of water-soaked lesions on the leaves, which later turn brown and elongated. Under favorable conditions, these lesions may coalesce, leading to extensive damage. Laboratory tests may be required for accurate diagnosis.',
        'How to manage': 'Bacterial leaf blight can be identified by the presence of water-soaked lesions on the leaves, which later turn brown and elongated. Under favorable conditions, these lesions may coalesce, leading to extensive damage. Laboratory tests may be required for accurate diagnosis.',
        'Fungicide': 'Bacterial leaf blight can be identified by the presence of water-soaked lesions on the leaves, which later turn brown and elongated. Under favorable conditions, these lesions may coalesce, leading to extensive damage. Laboratory tests may be required for accurate diagnosis.'
    },

    # Add more diseases as needed
]

@app.route('/')
def index():
    return render_template('index.html', diseases=diseases)

if __name__ == '__main__':
    app.run(debug=True)

