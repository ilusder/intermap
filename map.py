from flask import Flask
import folium
from folium import Marker, FeatureGroup, LayerControl


app = Flask(__name__)

m = folium.Map(location=[32.80, 35.0311],
               zoom_start=10,
               tiles='CartoDB positron')



feature_group = FeatureGroup(name="North")
feature_group2 = FeatureGroup(name="Center")


mark1 = Marker(location=[32.851740, 35.066356], popup="Qiryat Yam", color='crimson').add_to(feature_group)

mark2 = Marker(location=[32.4340, 34.9197], popup="Hadera", color='red').add_to(feature_group2)

feature_group.add_to(m)
feature_group2.add_to(m)

LayerControl().add_to(m)


@app.route('/map')
def show_map():
    return m._repr_html_()


m.save('index.html')
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
