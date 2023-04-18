#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#######################
# Garrett Collier
# SDEV 220
# M04 Lab
# 4/17/23
######################


# imports needed libraries
from flask
import Flask, jsonify, request

# assigns the app to an object
application = Flask(__name__)

# creates a list of two books
books = [
    {
        'id': 1,
        'book_name': 'Enlightenment Now!',
        'author': 'Steven Pinker',
        'publisher': 'Viking Press'
    },
    {
        'id': 2,
        'book_name': 'Factfulness',
        'author': 'Hans Rosling',
        'publisher': 'Flatiron Books'
    }
]

# Function that gathers a list of all books
# returns a JSON response that contains a list of all the books stored in the 'books' list
@application.route('/books', methods = ['GET'])
def get_books():
    return jsonify(books) 

# Function that retrieves a specific book by its id
# Takes id as an argument, finds the book assoc. by id, then returns a JSON response containing the book.
@application.route('/books/<int:id>', methods = ['GET'])
def get_book(id):
    book = [book for book in books if book['id'] == id]
    return jsonify(book)

# Function that adds a book to the list
@application.route('/books', methods = ['POST'])
def add_book():
    book = {
        'id': books[-1]['id'] + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(book)
    return jsonify(book)

# Function that updates a specific book in the list
@application.route('/books/<int:id>', methods = ['PUT'])
def update_book(id):
    book = [book for book in books if book['id'] == id]
    book[0]['book_name'] = request.json.get('book_name', book[0]['book_name'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['publisher'] = request.json.get('publisher', book[0]['publisher'])
    return jsonify(book[0])

# Function that deletes a book from the list
@application.route('/books/<int:id>', methods = ['DELETE'])
def delete_book(id):
    book = [book for book in books if book['id'] == id]
    books.remove(book[0])
    return jsonify({'result': 'Book has been deleted'})

if __name__ == '__main__':
    application.run(debug = True)

