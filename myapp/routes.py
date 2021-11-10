from myapp import myobj
from myapp import db
from myapp.models import cities
from myapp.forms import TopCities
from flask import render_template, flash, redirect

@myobj.route("/", methods = ['GET', 'POST'])
def addCity():
    name = 'Yinglin'
    title = 'Top Cities'
    form = TopCities()
    db.create_all()

    if form.validate_on_submit():
        flash (f'[{form.city_name.data}] [ranked {form.city_rank.data}] [Visited = {form.is_visited.data}] is added!')
        city_name = form.city_name.data
        city_rank = form.city_rank.data
        is_visited = form.is_visited.data
        city = cities(city_name = city_name, city_rank = city_rank, is_visited = is_visited)
        db.session.add(city)
        db.session.commit()
    top_cities = cities.query.order_by(cities.city_rank).all()
    return render_template('home.html', name = name, title = title, form = form, top_cities = top_cities)