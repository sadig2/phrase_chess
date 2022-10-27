# Create and activate environment
        python3 -m venv env
        source env/bin/activate
# Install packages
        pip install -r requirements
# To run function test 
        python3 tests.py
# To start api run 
        python3 main.py
# Payload format to send by post request

                {
        "n":2,
        "chess_pieces":"bishop"
        }



