from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

dic = {0: 'glioma', 1: 'meningioma', 2: 'notumor', 3: 'pituitary'}

model = load_model('C:\\Users\\doug\\PycharmProjects\\brain_tumor_app\\brain_tumor_model.h5')

model.make_predict_function()


def predict_label(img_path):
    i = image.image_utils.load_img(img_path, target_size=(224, 224))
    i = image.image_utils.img_to_array(i) / 255.0
    i = i.reshape(-1, 224, 224, 3)
    p = model.predict(i)
    return dic[p.argmax()]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return "A Brain Tumor Classifier Application"


@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "static/" + img.filename
        img.save(img_path)

        p = predict_label(img_path)

    return render_template("index.html", prediction=p, img_path=img_path)


if __name__ == '__main__':
    app.run(debug=True)
