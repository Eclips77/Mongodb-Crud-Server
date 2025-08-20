from flask import Flask, request, jsonify
from services.dal import SoldierDAL
from services.solider_entity import Soldier

app = Flask(__name__)
soldier_dal = SoldierDAL()

@app.route('/soldiers', methods=['POST'])
def create_soldier():
    """Create new soldier"""
    try:
        data = request.get_json()
        
        if not data.get('first_name') or not data.get('last_name'):
            return jsonify({"error": "First name and last name are required"}), 400
        
        soldier = Soldier(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            phone_number=data.get('phone_number'),
            rank=data.get('rank')
        )
        
        soldier_id = soldier_dal.create(soldier)
        return jsonify({"message": "Soldier created successfully", "id": soldier_id}), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/soldiers/<soldier_id>', methods=['GET'])
def get_soldier(soldier_id):
    """Get soldier by ID"""
    try:
        soldier = soldier_dal.get_by_id(soldier_id)
        if soldier:
            return jsonify(soldier.to_dict()), 200
        return jsonify({"error": "Soldier not found"}), 404
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/soldiers', methods=['GET'])
def get_all_soldiers():
    """Get all soldiers"""
    try:
        soldiers = soldier_dal.get_all()
        return jsonify([soldier.to_dict() for soldier in soldiers]), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/soldiers/<soldier_id>', methods=['PUT'])
def update_soldier(soldier_id):
    """Update soldier"""
    try:
        data = request.get_json()
        
        existing_soldier = soldier_dal.get_by_id(soldier_id)
        if not existing_soldier:
            return jsonify({"error": "Soldier not found"}), 404
        
        success = soldier_dal.update(soldier_id, data)
        if success:
            return jsonify({"message": "Soldier updated successfully"}), 200
        return jsonify({"error": "Failed to update soldier"}), 400
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/soldiers/<soldier_id>', methods=['DELETE'])
def delete_soldier(soldier_id):
    """Delete soldier"""
    try:
        success = soldier_dal.delete(soldier_id)
        if success:
            return jsonify({"message": "Soldier deleted successfully"}), 200
        return jsonify({"error": "Soldier not found"}), 404
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "OK", "message": "Server is running"}), 200

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
