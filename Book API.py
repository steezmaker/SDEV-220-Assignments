from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data to simulate a database
books = []

class Book:
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(len(books) + 1, data['book_name'], data['author'], data['publisher'])
    books.append(new_book)
    return jsonify({'message': 'Book created successfully'}), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    books_data = []
    for book in books:
        books_data.append({'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher})
    return jsonify({'books': books_data})

# Get a single book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book.id == id), None)
    if book:
        return jsonify({'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher})
    return jsonify({'message': 'Book not found'}), 404

# Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book.id == id), None)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    data = request.get_json()
    book.book_name = data['book_name']
    book.author = data['author']
    book.publisher = data['publisher']
    return jsonify({'message': 'Book updated successfully'})

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book.id != id]
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
