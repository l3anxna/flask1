from flask import Flask, request

app = Flask(__name__)

@app.route('/sum_of_squares', methods=['GET'])
def sum_of_squares():
    # Get the numbers from the URL parameters
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except (TypeError, ValueError):
        return "Please provide two valid integers for x and y.", 400

    # Calculate the sum of squares
    result = x**2 + y**2

    # Create a formatted response
    response = f"{x}^2 + {y}^2 = {result}"

    # Return the response
    return response

if __name__ == '__main__':
    app.run(debug=True)
