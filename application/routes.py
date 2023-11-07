#import app
from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return {'id':character.id, 'name':character.name, 'age':character.age, 'catch_phrase':character.catch_phrase}

@app.route('/')
def hello_world():
    return '<p>Hello world</p>'

@app.route('/characters', methods=['POST'])
def create_character():
   #retreive the body - equivalent of req.body in express
    data=request.json
    #now we need to craete a character

    character=FriendsCharacter(data['name'], data['age'], data['catch_phrase'])
    # add the character to the database
    db.session.add(character)
    #commit the changes
    db.session.commit()
    #return a response, send back a JSON response
    #jsonify-> turns a python object into a json response object
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

#GET route to retrieve all characters

@app.route('/characters')
def get_characters():
    #query the database
    characters=FriendsCharacter.query.all() #-> returns a list of all the characters, equiavlent of select * from characters
    #return a response
    #create a list of characters
    character_list=[]
    #loop through the characters
    for character in characters:
        #append each character to the output list
        character_list.append(format_character(character))
    return {'characters':character_list}

@app.route('/characters/<id>')
def get_character(id):
    #query the database -> in sql we do select * from characters where id=1
    character=FriendsCharacter.query.filter_by(id=id).first() #-> returns a list of all the characters, equiavlent of select * from characters
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

#now doing the delete
@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
    #query the database -> in sql we do select * from characters where id=1
    character=FriendsCharacter.query.filter_by(id=id).first()
    #delete the character
    db.session.delete(character)
    #commit the changes
    db.session.commit()
    return "character deleted"

#now doing the update
@app.route('/characters/<id>', methods=['PATCH'])
def update_character(id):
    #query the database -> in sql we do select * from characters where id=1
    character=FriendsCharacter.query.filter_by(id=id)
    data=request.json
    #update the character
    character.update(dict(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase']))

    #commit the changes
    db.session.commit()

    #retrieve the specific character from the filtering
    updatedCharacter = character.first()

    #return a json object of the updated character
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)



