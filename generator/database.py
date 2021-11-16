import sqlite3


class Database:
    def get_connection(self):
        return sqlite3.connect("./db.sqlite")

    def add_card(self, card_title, card_text, card_link_text, card_link_url):
        con = self.get_connection()
        cur = con.cursor()

        create_table_query = "CREATE TABLE IF NOT EXISTS cards('card_title' VARCHAR," + \
                             " 'card_text' TEXT, 'card_link_text' VARCHAR, 'card_link_url' VARCHAR )"
        insert_data_query = f"INSERT INTO " + \
                            f"cards VALUES ({card_title}, {card_text}, {card_link_text}, {card_link_url})"
        try:
            cur.execute(create_table_query)
            cur.execute(insert_data_query)
            con.commit()
        except:
            print("an error has been occurred !")
