# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Services": 200,
    "Cybersecurity": 225,
    "IT Support": 250
    }

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", "email": "john.smith@abccorp.com", "phone": "555-1234"}
customer2 = {"company_name": "XYZ Ltd", "contact_person": "Jane Doe", "email": "alice.johnson@xyzltd.com", "phone": "555-5678"}
customer3 = {"company_name": "Tech Solutions", "contact_person": "Bob Lee", "email": "bob.lee@techsolutions.com", "phone": "555-8765"}
customer4 = {"company_name": "Innovate Inc", "contact_person": "Clara Wu", "email": "clara.wu@innovate.com", "phone": "555-4321"}


# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4,
    }

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for cid, info in customers.items():
    print(f"Customer ID: {cid}")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print("-" * 30)

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)
c002_info = customers.get("C002")
c003_contact = customers.get("C003", {}).get("contact_person")
c999_info = customers.get("C999", "Customer C999 not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999 Info:", c999_info)


# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
customers["C001"]["phone"] = "555-9999"
customers["C002"]["industry"] = "Finance"

print("\n\nUpdating Customer Information:")
print("-" * 60)
print("C001 Updated:", customers["C001"])
print("C002 Updated:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
projects = {
    "C001": [
        {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000},
        {"name": "Data Migration", "service": "Cloud Services", "hours": 80, "budget": 16000}
    ],
    "C002": [
        {"name": "Financial Dashboard", "service": "Data Analysis", "hours": 100, "budget": 17500}
    ],
    "C003": [
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 90, "budget": 20250},
        {"name": "Server Setup", "service": "IT Support", "hours": 60, "budget": 7200}
    ],
    "C004": [
        {"name": "System Upgrade", "service": "IT Support", "hours": 50, "budget": 6000}
    ]
}

print("\n\nProject Information:")
print("-" * 60)
for cid, proj_list in projects.items():
    print(f"Customer {cid} Projects:")
    for proj in proj_list:
        print(f"  {proj}")
    print("-" * 30)
    
# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
for cid, proj_list in projects.items():
    for proj in proj_list:
        rate = services.get(proj["service"], 0)
        cost = rate * proj["hours"]
        print(f"{proj['name']} (Customer {cid}) - Cost: ${cost}")


# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
print("Customer IDs:", list(customers.keys()))
print("Customer Companies:", [info["company_name"] for info in customers.values()])
print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
service_counts = {}
for proj_list in projects.values():
    for proj in proj_list:
        service = proj["service"]
        service_counts[service] = service_counts.get(service, 0) + 1
        
print("\n\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)
all_hours = [proj["hours"] for plist in projects.values() for proj in plist]
all_budgets = [proj["budget"] for plist in projects.values() for proj in plist]

total_hours = sum(all_hours)
total_budget = sum(all_budgets)
avg_budget = total_budget / len(all_budgets) if all_budgets else 0
max_budget = max(all_budgets) if all_budgets else 0
min_budget = min(all_budgets) if all_budgets else 0

print("\n\nFinancial Summary:")
print("-" * 60)
print(f"Total Hours: {total_hours}")
print(f"Total Budget: ${total_budget}")
print(f"Average Budget: ${avg_budget}")
print(f"Max Budget: ${max_budget}")
print(f"Min Budget: ${min_budget}")

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
for cid, info in customers.items():
    cust_projects = projects.get(cid, [])
    total_cust_hours = sum(p["hours"] for p in cust_projects)
    total_cust_budget = sum(p["budget"] for p in cust_projects)
    print(f"{cid} - {info['company_name']}")
    print(f"  Contact: {info['contact_person']}, Email: {info['email']}, Phone: {info['phone']}")
    print(f"  Number of Projects: {len(cust_projects)}")
    print(f"  Total Hours: {total_cust_hours}, Total Budget: ${total_cust_budget}")
    print("-" * 30)

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

active_customers = {cid: info for cid, info in customers.items() if projects.get(cid)}
print("\n\nActive Customers (with projects):")
print("-" * 60)
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}
print("\n\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension
service_tiers = {
    s: "Premium" if rate >= 200 else "Standard" if 100 <= rate < 200 else "Basic"
    for s, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    return all(field in customer_dict for field in required_fields)

print("\n\nCustomer Validation:")
print("-" * 60)

for cid, info in customers.items():
    print(f"{cid}: Valid = {validate_customer(info)}")

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses
status_counts = {"active": 0, "completed": 0, "pending": 0}
# Add status to projects
for plist in projects.values():
    for proj in plist:
        proj["status"] = "active"  # Example: all active for demo
        status_counts[proj["status"]] += 1

print("\n\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys
def analyze_customer_budgets(projects_dict):
    result = {}
    for cid, plist in projects_dict.items():
        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count if count else 0
        result[cid] = {"total": total, "average": avg, "count": count}
    return result

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations
def recommend_services(customer_id, customers, projects, services):
    used_services = {p["service"] for p in projects.get(customer_id, [])}
    remaining_services = [s for s in services if s not in used_services]
    cust_projects = projects.get(customer_id, [])
    avg_budget = sum(p["budget"] for p in cust_projects)/len(cust_projects) if cust_projects else 0
    recommended = [s for s in remaining_services if services[s]*10 <= avg_budget]
    return recommended

print("\n\nService Recommendations:")
print("-" * 60)
for cid in customers:
    rec = recommend_services(cid, customers, projects, services)
    print(f"{cid}: Recommended Services: {rec}")