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


    #initialising
    is_prime_result = is_prime(number)
    is_armstrong = is_armstrong(number)
    parity_result = check_parity(number)
    digit_sum = sum(int(digit) for digit  in  str(number))

    #step 4: Compute is_prime
    if number > 1:
        is_prime = all(number % i != 0 for i in range(2, int(number**0.5) + 1))
        return  number;

    # step 5: compute is_perfect
    if number > 0:
        divisors_sum = sum(i for in range(1, number) if number  % i == 0)
        is_perfect =  (divisors_sum  == number )

    #step 6 compute Properties
    if number > 0:
        #check for armstrong number (example logic)
        num_str = str(number)
        num_digits = len(num_str)
        armstrong_sum = sum(int(digit)  ** num_digits  for digit in num_str)
        if armstrong_sum ==  number:
            properties.append("armstrong")


    #check if  the number is even or odd
    properties.append("even" if number % 2 == 0 else "odd")



    properties = []
    if is_armstrong_result:
        properties.append("armstrong")
    properties.append(parity_append)


    fun_fact = fetch_fun_fact(number) #assuming you implement this


    response = {
        "number": number,
        "is_prime": is_prime_result,
        "is_perfect": False,
        "properties": properties,
        "digit_sum" : digit_sum,
        "fun_fact" : fun_fact
    }
    return jsonify(response), 200

def fetch_fun_fact(n):
    #Here you'd call the numebers API to get a fun fact
    return f"{n} is a fun number!"



if __name__ = '__main__':
    app.run(debug=True)

