import unittest
import MySQLdb

class TestDatabaseFunctionality(unittest.TestCase):
    def setUp(self):
        # Connect to the test database
        self.conn = MySQLdb.connect(
            user='hbnb_test',
            password='hbnb_test_pwd',
            host='localhost',
            database='hbnb_test_db'
        )
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Rollback any changes and close the database connection
        self.conn.rollback()
        self.cursor.close()
        self.conn.close()

    def test_create_state(self):
        # Get the initial number of records in the states table
        initial_count = self._get_states_count()

        # Execute the action: create a new state
        self._create_state("California")

        # Get the number of records in the states table again
        final_count = self._get_states_count()

        # Validate the action
        self.assertEqual(final_count, initial_count + 1, "New state was not created")

    def _get_states_count(self):
        # Helper function to get the number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

    def _create_state(self, state_name):
        # Helper function to create a state in the database
        try:
            self.cursor.execute("INSERT INTO states (name) VALUES (%s)", (state_name,))
            self.conn.commit()
        except MySQLdb.Error as e:
            # Handle database errors gracefully
            self.fail(f"Failed to create state: {e}")

if __name__ == '__main__':
    unittest.main()

