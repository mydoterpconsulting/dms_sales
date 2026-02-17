app_name = "dms_sales"
app_title = "Mydot DMS Sales"
app_publisher = "Mydot Consulting"
app_description = "Sales and Service management for automotive dealerships"
app_email = "amirul.zulkefli@mydotconsulting.com"
app_license = "mit"

# Apps
# ------------------

required_apps = ["erpnext"]

# Fixtures
# --------
# Automatically install these doctypes/records

fixtures = [
	# Custom Fields
	{
		"dt": "Custom Field",
		"filters": [
			[
				"name",
				"in",
				[
					# Workflow state fields
					"VSO-workflow_state",
					"Car Details And Checklist-workflow_state",
					"Car Stock Request-workflow_state",
					"SA Commission Claim Form-workflow_state",
					# WooCommerce integration
					"Address-woocommerce_id",
					"Address-woocommerce_email",
					"Address-tax_category",
					"Address-is_your_company_address",
					"Customer-woocommerce_id",
					"Customer-woocommerce_email",
					"Item-woocommerce_id",
					"Sales Order-woocommerce_id",
					# HR & Payroll
					"Company-custom_outlet_code",
					"Company-hr_settings_section",
					"Company-default_expense_claim_payable_account",
					"Company-default_employee_advance_account",
					"Company-column_break_10",
					"Company-default_payroll_payable_account",
					"Company-hr_and_payroll_tab",
					"Department-section_break_4",
					"Department-payroll_cost_center",
					"Department-column_break_9",
					"Department-leave_block_list",
					"Department-approvers",
					"Department-shift_request_approver",
					"Department-leave_approvers",
					"Department-expense_approvers",
					"Designation-appraisal_template",
					"Designation-required_skills_section",
					"Designation-skills",
					"Employee-employment_type",
					"Employee-grade",
					"Employee-job_applicant",
					"Employee-default_shift",
					"Employee-approvers_section",
					"Employee-expense_approver",
					"Employee-leave_approver",
					"Employee-column_break_45",
					"Employee-shift_request_approver",
					"Employee-salary_cb",
					"Employee-payroll_cost_center",
					"Employee-health_insurance_section",
					"Employee-health_insurance_provider",
					"Employee-health_insurance_no",
					# Other
					"Contact-is_billing_contact",
					"Print Settings-compact_item_print",
					"Print Settings-print_uom_after_quantity",
					"Print Settings-print_taxes_with_zero_amount",
					"Project-total_expense_claim",
					"Task-total_expense_claim",
					"Terms and Conditions-hr",
					"Timesheet-salary_slip",
				]
			]
		]
	},
	# Master Data - Malaysian States
	"state.json",
	# Master Data - Insurance Companies
	"insurance_company.json",
	# Master Data - Car Color Types
	"car_color_type.json",
	# Master Data - Car Models (Perodua vehicles)
	"car_model.json",
	# Workspaces
	{
		"dt": "Workspace",
		"filters": [
			[
				"name",
				"in",
				[
					"SA Manager",
					"SA",
					"Tutorial",
					"SA Admin",
					"HR DC Auto"
				]
			]
		]
	},
]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "dms_sales",
# 		"logo": "/assets/dms_sales/logo.png",
# 		"title": "Mydot DMS Sales",
# 		"route": "/dms_sales",
# 		"has_permission": "dms_sales.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dms_sales/css/dms_sales.css"
# app_include_js = "/assets/dms_sales/js/dms_sales.js"

# include js, css files in header of web template
# web_include_css = "/assets/dms_sales/css/dms_sales.css"
# web_include_js = "/assets/dms_sales/js/dms_sales.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dms_sales/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "dms_sales/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "dms_sales.utils.jinja_methods",
# 	"filters": "dms_sales.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dms_sales.install.before_install"
after_install = "dms_sales.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dms_sales.uninstall.before_uninstall"
# after_uninstall = "dms_sales.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "dms_sales.utils.before_app_install"
# after_app_install = "dms_sales.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "dms_sales.utils.before_app_uninstall"
# after_app_uninstall = "dms_sales.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dms_sales.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dms_sales.tasks.all"
# 	],
# 	"daily": [
# 		"dms_sales.tasks.daily"
# 	],
# 	"hourly": [
# 		"dms_sales.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dms_sales.tasks.weekly"
# 	],
# 	"monthly": [
# 		"dms_sales.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "dms_sales.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dms_sales.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dms_sales.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["dms_sales.utils.before_request"]
# after_request = ["dms_sales.utils.after_request"]

# Job Events
# ----------
# before_job = ["dms_sales.utils.before_job"]
# after_job = ["dms_sales.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"dms_sales.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

