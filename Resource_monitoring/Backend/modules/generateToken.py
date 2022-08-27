import db_connection as dbc
import jwt
import timestampRM


def encodeToken(string_to_encode):
    data = {
        "string_to_encode":string_to_encode + (timestampRM.getTimestampForEncodedString("|"))
    } 
    encoded_data = jwt.encode(data, "secret", algorithm="HS256")
    return encoded_data

def decodeToken(encoded_data):  
    decoded_data = (jwt.decode(encoded_data, "secret", algorithms=["HS256"]))
    return decoded_data

