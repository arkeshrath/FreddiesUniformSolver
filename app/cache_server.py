from flask import Flask, request, jsonify
import cachetools
import hashlib

app = Flask(__name__)

# Initialize cache
cache = cachetools.TTLCache(maxsize=100, ttl=3000)

@app.route('/cache/<key>', methods=['GET'])
def get_cache(key):
    """Retrieve value from cache."""
    value = cache.get(key)
    if value is None:
        return jsonify({'error': 'Key not found'}), 404
    return jsonify({'key': key, 'value': value})

@app.route('/cache/<key>', methods=['POST'])
def set_cache(key):
    """Set value in cache."""
    value = request.json.get('value')
    if value is None:
        return jsonify({'error': 'No value provided'}), 400
    cache[key] = value
    return jsonify({'key': key, 'value': value}), 201

@app.route('/cache/<key>', methods=['DELETE'])
def delete_cache(key):
    """Delete value from cache."""
    if key in cache:
        del cache[key]
        return jsonify({'message': 'Key deleted'}), 200
    return jsonify({'error': 'Key not found'}), 404

if __name__ == '__main__':
    app.run(port=5001)