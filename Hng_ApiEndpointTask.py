from flask import Flask, jsonify, request, flask-cors




app = Flask(__name__)

#modify endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')#get number parameter from ur
    if number is None:
        return jsonify({"error": "Number pararmeter is required"}), 400

    try:
        number =  int(number_str)
    except:
        return  jsonify({"error":"invalid interger , please provide a valid onez"}), 400


    is_prime(n) = False
    is_perfect(n) = False
    is_armstrong(n) =
    digit_sum(n) =
    get_fun_fact(n)


    return jsonify





if __name__ = '__main__':
    app.run(debug=True)

