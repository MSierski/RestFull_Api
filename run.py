from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Music(Resource):
    def get(self):
        return {
        'Song1':
            {
                'Wykonawca': 'Royal Republic',
                'Tytul' : 'Good to be bad',
                'Czas' : '2:47',
                'Format' : 'MP3'
            },
        'Song2':
            {
                'Wykonawca': 'Keith Power, Alan Doyle',
                'Tytul' : 'Sleeping in the Cold Below',
                'Czas' : '3:31',
                'Format' : 'MP3'
            },
        'Song3':
            {
                'Wykonawca': 'STRLGHT',
                'Tytul' : 'Flames',
                'Czas' : '3:05',
                'Format' : 'MP3'
            },
        'Song4':
            {
                'Wykonawca': 'Joshua James',
                'Tytul' : 'Battle Hymn of the Republic',
                'Czas' : '4:05',
                'Format' : 'MP3'
            },
         }

api.add_resource(Music, '/')

if __name__ == '__main__':
    app.run(debug=True)
