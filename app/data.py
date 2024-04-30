from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


# Load the environment variables
load_dotenv()


class Database:

    # Open the connection to the MongoDB Database
    database = MongoClient(getenv('DB_URL'), tlsCAFile=where())['Bandersnatch']

    # Open the monsters collection
    collection = database.get_collection('monsters')

    def seed(self, amount: int):
        '''
        Takes an amount and enter the "amount" rows into a MongoDB Database.

        Parameters:
        amount (int): An Integer
        '''
        # saves monster data in a variable "monster_list"
        monster_list = [Monster().to_dict() for _ in range(amount)]

        # inserts monster_list in the monsters collection
        self.collection.insert_many(monster_list)

    def reset(self):
        '''
        Resets all current data in the monsters collection
        within the connected MongoDB Database.
        '''
        # delete all documents in monsters collection
        self.collection.drop()

    def count(self) -> int:
        '''
        Returns the total amount of documents within the monsters
        collection in the connected MongoDB Database.
        '''
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        '''
        Collects all the documents in the connected MongoDB
        Database and converts/returns a Pandas DataFrame.
        '''
        return DataFrame(self.collection.find()).drop(columns='_id')

    def html_table(self) -> str:

        '''
        Returns all of the documents in the connected MongoDB
        Database monsters collection in the specified HTML Format.
        '''
        # store the graph data to insert
        # into the the html variable
        graph_html = ''

        # use dataframe method to grab
        # data from MongoDB and store in
        # a pandas dataframe object
        df = self.dataframe()

        for row in range(self.count()):
            # add the <tr> tag before adding data
            graph_html = graph_html + '<tr>\n'
            graph_html = graph_html + f'    <th>{row}</th>\n'

            for column in df:
                # add each columns data between a <td> and </td> tag
                graph_html = graph_html + '<td>' + \
                    str(df[column][row]) + '</td>\n'

            # end with a </tr> tag to close row
            graph_html = graph_html + '</tr>\n'

        html = f'''<table border="1" class="dataframe">\n
        <thead>\n
            <tr style="text-align: right;">\n
                <th></th>\n<th>Name</th>\n
                <th>Type</th>\n<th>Level</th>\n
                <th>Rarity</th>\n<th>Damage</th>\n
                <th>Health</th>\n<th>Energy</th>\n
                <th>Sanity</th>\n<th>Timestamp</th>\n
            </tr>\n
        </thead>\n
        <tbody>\n
            {graph_html}\n
        </tbody>\n
    </table>\n\n'''

        # return html
        return html
