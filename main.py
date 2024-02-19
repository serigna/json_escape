# import json

# def escape_json_special_characters(input_string):
#     escaped_chars = {
#         "\\": "\\\\",
#         "\b": "\\b",
#         "\f": "\\f",
#         "\n": "\\n",
#         "\r": "\\r",
#         "\t": "\\t",
#         "\"": "\\\"",
#         ",": ",\\n",
#         '{': '{\\n',
#         '}': '\\n}'
#     }
    
#     escaped_string = ""
#     for char in input_string:
#         if char in escaped_chars:
#             escaped_string += escaped_chars[char]
#         else:
#             escaped_string += char
#     return escaped_string


# js_example = { 
#     "isbn": "123-456-222",  
#  "author": 
#     {
#       "lastname": "Doe",
#       "firstname": "Jane"
#     },
# "editor": 
#     {
#       "lastname": "Smith",
#       "firstname": "Jane"
#     },
#   "title": "The Ultimate Database Study Guide",  
#   "category": ["Non-Fiction", "Technology"]
#  }

# test = escape_json_special_characters(json.dumps(js_example))

# print(test)



# # import json

# # # Define the JSON data
data = {
    "isbn": "123-456-222",
    "author": {
        "lastname": "Doe",
        "firstname": "Jane"
    },
    "editor": {
        "lastname": "Smith",
        "firstname": "Jane"
    },
    "title": "The Ultimate Database Study Guide",
    "category": ["Non-Fiction", "Technology"]
}

# # # Convert the dictionary to a JSON-formatted string with custom formatting
# # formatted_json = json.dumps(data, indent=2, separators=(", ", ": "), ensure_ascii=False)

# # # Replace double quotes with escaped double quotes
# # formatted_json = formatted_json.replace('"', '\\"')

# # # Manually add newline characters before each opening brace
# # formatted_json = formatted_json.replace('{', '{\\n')
# # # Manually add newline characters after each closing brace
# # formatted_json = formatted_json.replace('}', '\\n}')

# # print(formatted_json)



def escape_json_string(input_string, indent=2):
    # Replace special characters with their escaped versions
    escaped_string = input_string.replace('\\', '\\\\')
    escaped_string = escaped_string.replace('\b', '\\b')
    escaped_string = escaped_string.replace('\f', '\\f')
    escaped_string = escaped_string.replace('\n', '\\n')
    escaped_string = escaped_string.replace('\r', '\\r')
    escaped_string = escaped_string.replace('\t', '\\t')
    escaped_string = escaped_string.replace('"', '\\"')
    
    # Add new lines after each key-value pair
    lines = escaped_string.split(',')
    formatted_lines = [line.strip() for line in lines]  # Remove leading/trailing spaces
    
    # Check for list sequences and format them with new lines
    formatted_lines_with_lists = []
    for line in formatted_lines:
        if '[' in line and ']' in line:
            line = line.replace('[', '[\\n' + ' ' * indent).replace(']', '\\n' + ' ' * (indent - 2) + ']')
        formatted_lines_with_lists.append(line)
    
    formatted_string = ',\n'.join(formatted_lines_with_lists)  # Join lines with new lines
    return formatted_string

# Example usage:
input_json = '{ "name": "John", "age": 30, "city": "New York", "hobbies": ["Reading", "Gardening", "Cooking"] }'
# escaped_json = escape_json_string(input_json)
test = data.read()
print(repr(test.replace('"', '\\"').replace('\n', '\\n')))
