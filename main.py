from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.get_json()
    

    if not data or 'array' not in data:
        return jsonify({'error': 'Missing array in request'}), 400
    arr = data['array']
    if not isinstance(arr, list) or not all(isinstance(x, (int, float)) for x in arr):
        return jsonify({'error': 'Array must be a list of numbers'}), 400
   
    steps = bubble_sort(arr)
    return jsonify({'steps': steps})

def bubble_sort(arr):
    steps = []
    n = len(arr)
    arr_copy = arr.copy() 
    
    for i in range(n - 1):
        swapped_in_pass = False
        for j in range(0, n - i - 1):
            compared_indices = [j, j + 1]
            swapped_indices = []

            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped_indices = [j, j + 1]
                swapped_in_pass = True

            step_info = {
                'array': arr_copy.copy(),
                'compared': compared_indices,
                'swapped': swapped_indices,
                'sorted': list(range(n - i, n)) 
            }
            steps.append(step_info)
        
        if not swapped_in_pass:
            break

    steps.append({
        'array': arr_copy.copy(),
        'compared': [],
        'swapped': [],
        'sorted': list(range(n))
    })
    return steps

if __name__ == '__main__':
    app.run(debug=True)