# main.py

from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Tenant, MaintenanceRequest
from config import Config
from datetime import datetime
import os

# Initialize Flask app and configuration
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Ensure the 'uploads' directory exists for file storage
os.makedirs('uploads', exist_ok=True)


# Home Page
@app.route('/')
def home():
    return render_template('home.html')


# Tenant Dashboard
@app.route('/tenant')
def tenant_dashboard():
    return render_template('tenant/dashboard.html')


# Route for Tenant to Submit Maintenance Request
@app.route('/tenant/submit_request', methods=['GET', 'POST'])
def submit_request():
    if request.method == 'POST':
        # Capture form data
        tenant_id = request.form['tenant_id']
        apartment_number = request.form['apartment_number']
        problem_area = request.form['problem_area']
        description = request.form['description']

        # Optional photo upload handling
        photo = None
        if 'photo' in request.files and request.files['photo'].filename != '':
            photo_file = request.files['photo']
            photo_path = os.path.join('uploads', photo_file.filename)
            photo_file.save(photo_path)
            photo = photo_path

        # Create and save the maintenance request
        new_request = MaintenanceRequest(
            tenant_id=tenant_id,
            apartment_number=apartment_number,
            problem_area=problem_area,
            description=description,
            date_time=datetime.utcnow(),
            photo=photo,
            status='pending'
        )
        db.session.add(new_request)
        try:
            db.session.commit()
            flash("Your maintenance request has been successfully submitted!", "success")
            return redirect(url_for('submit_request_success'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred while submitting the request: {str(e)}", "error")

    return render_template('tenant/submit_request.html')


# Confirmation page after request submission
@app.route('/tenant/submit_request_success')
def submit_request_success():
    return render_template('tenant/request_success.html')


# Staff Dashboard
@app.route('/staff')
def staff_dashboard():
    return render_template('staff/dashboard.html')


# Route for Staff to Browse and Filter Maintenance Requests
@app.route('/staff/browse_requests', methods=['GET'])
def browse_requests():
    # Filtering parameters
    apartment_number = request.args.get('apartment_number')
    problem_area = request.args.get('problem_area')
    status = request.args.get('status')

    # Query with applied filters
    query = MaintenanceRequest.query
    if apartment_number:
        query = query.filter_by(apartment_number=apartment_number)
    if problem_area:
        query = query.filter_by(problem_area=problem_area)
    if status:
        query = query.filter_by(status=status)

    maintenance_requests = query.all()
    return render_template('staff/browse_requests.html', maintenance_requests=maintenance_requests)


# Route for Staff to Update Request Status
@app.route('/staff/update_status/<int:request_id>', methods=['POST'])
def update_request_status(request_id):
    request_to_update = MaintenanceRequest.query.get(request_id)
    if request_to_update and request_to_update.status == 'pending':
        request_to_update.status = 'completed'
        db.session.commit()
        flash("Request status updated successfully!", "success")
    else:
        flash("Request status could not be updated.", "error")
    return redirect(url_for('browse_requests'))


# Manager Dashboard
@app.route('/manager')
def manager_dashboard():
    return render_template('manager/dashboard.html')


# Route for Manager to Add Tenant
@app.route('/manager/add_tenant', methods=['POST'])
def add_tenant():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    apartment_number = request.form['apartment_number']
    check_in_date = datetime.utcnow()

    new_tenant = Tenant(name=name, phone=phone, email=email, apartment_number=apartment_number,
                        check_in_date=check_in_date)
    db.session.add(new_tenant)
    db.session.commit()
    flash("Tenant added successfully!", "success")
    return redirect(url_for('manager_dashboard'))


# Route for Manager to Move Tenant
@app.route('/manager/move_tenant', methods=['POST'])
def move_tenant():
    tenant_id = request.form['tenant_id']
    new_apartment_number = request.form['new_apartment_number']
    tenant = Tenant.query.get(tenant_id)
    if tenant:
        tenant.apartment_number = new_apartment_number
        db.session.commit()
        flash("Tenant moved successfully!", "success")
    else:
        flash("Error: Tenant not found.", "error")
    return redirect(url_for('manager_dashboard'))


# Route for Manager to Delete Tenant
@app.route('/manager/delete_tenant', methods=['POST'])
def delete_tenant():
    tenant_id = request.form['tenant_id']
    tenant = Tenant.query.get(tenant_id)
    if tenant:
        db.session.delete(tenant)
        db.session.commit()
        flash("Tenant deleted successfully!", "success")
    else:
        flash("Error: Tenant not found.", "error")
    return redirect(url_for('manager_dashboard'))


# Route for Manager to View and Manage Tenants
@app.route('/manager/manage_tenants')
def manage_tenants():
    tenants = Tenant.query.all()
    return render_template('manager/manage_tenants.html', tenants=tenants)


if __name__ == '__main__':
    app.run(debug=True)
