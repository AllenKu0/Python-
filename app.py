import flask
import json
from ec2 import get_ec2_instance_detail
from models.models import EC2,engine
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm.session import Session

app = flask.Flask(__name__)

@app.route('/api/ec2', methods=['GET'])
def ec2():
    result = get_ec2_instance_detail()
    ec2_json_detail = json.loads(result)
    with Session(engine) as session:
        for ec2 in ec2_json_detail:
            session.execute(
                insert(EC2).values(
                    instance_Name = ec2['InstanceName'],
                    instance_family = ec2['InstanceFamily'],
                    instance_type = ec2['InstanceType'],
                    vCPU = ec2['vCPU'],
                    memory = ec2['Memory'],
                    network = ec2['Network'],
                    storage = ec2['Storage'],
                    on_demand_hourly_cost = ec2['OnDemandHourlyCost'],
                    current_generation = ec2['CurrentGeneration'],
                    potential_saving = ec2['Potential saving'],
                )
            )
        session.commit()
    return result

if __name__ == "__main__":
    app.run(debug=True, port=5000,host='0.0.0.0')