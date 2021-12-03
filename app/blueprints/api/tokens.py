from flask import jsonify, request, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user
from app import db
from app.blueprints.api import bp as api
from .auth import basic_auth, token_auth
from app.blueprints.api.models import Collection
import requests, json


@api.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()
    db.session.commit()
    return jsonify({'token': token})


@api.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return jsonify({'message': "User's token has been revoked"}), 204


@api.route('/collections')
def collection():
    context = {
        'collections': Collection.query.order_by(Collection.date_created.desc()).all()
    }
    return render_template('collections.html', **context)


@api.route('/add_collection', methods=['POST'])
def add_collection():
    status = request.form.get('collection_status')
    # params = {
    #     'api_key': 'aee9a2ab736fd2d1e79bc52275b98ab4',
    # }
    # r = requests.get(f'https://gateway.marvel.com:443/v1/public/characters?name={status}&apikey={params["api_key"]}', params=params)
    
    f = open('./app/heroes.json')
    data = json.load(f)

    print(data)
    
    # r = requests.get('./marvel/app/heroes.json')
    
    # print(data.json())
    # new_hero = data.json()[f'{status}']
    if status:
        c = Collection(name=status, owner=current_user.get_id())
    params = {
        'api_key': 'aee9a2ab736fd2d1e79bc52275b98ab4',
    }
    r = request.get('https://gateway.marvel.com:443/v1/public/characters?name=' +
                     'status' + '&apikey=' + 'api_key', params=params)
    new_hero = Collection()
    if status:
        c = Collection(name=status, user_id=current_user.get_id())
        db.session.add(c)
        db.session.commit()
        flash('You have successfully added a new superhero.', 'success')
    else:
        flash('You cannot post nothing', 'warning')
    return redirect(url_for('api.collection'))


    return redirect(url_for('api.collect'))
