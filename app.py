from flask import Flask, request, jsonify

app = Flask(__name__)

# This is the custom function you want to run
def my_hosted_function(name):
    return f"Hello, {name}! Your function executed successfully on the server."

@app.route('/run-function', methods=['POST'])
def run_logic():
    # 1. Get data from the request (JSON format)
    data = request.get_json()
    
    # 2. Extract a variable (e.g., a name)
    user_name = data.get("name", "Guest")
    
    # 3. Call your Python function
    result = my_hosted_function(user_name)
    
    # 4. Return the result as JSON
    return jsonify({
        "status": "success",
        "output": result
    })

if __name__ == '__main__':
    # Set debug=True to see errors clearly during development
    app.run(host='0.0.0.0', port=5000, debug=True)