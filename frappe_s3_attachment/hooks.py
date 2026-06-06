app_name = "frappe_s3_attachment"
app_title = "Frappe S3 Attachment"
app_publisher = "Frappe"
app_description = "Frappe app to make file upload to S3 through attach file option."
app_email = "ramesh.ravi@zerodha.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "frappe_s3_attachment",
# 		"logo": "/assets/frappe_s3_attachment/logo.png",
# 		"title": "Frappe S3 Attachment",
# 		"route": "/frappe_s3_attachment",
# 		"has_permission": "frappe_s3_attachment.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_s3_attachment/css/frappe_s3_attachment.css"
# app_include_js = "/assets/frappe_s3_attachment/js/frappe_s3_attachment.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_s3_attachment/css/frappe_s3_attachment.css"
# web_include_js = "/assets/frappe_s3_attachment/js/frappe_s3_attachment.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {
	"S3 Attachment Settings": [
		"frappe_s3_attachment/doctype/s3_attachment_settings/s3_attachment_settings.js"
	]
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "frappe_s3_attachment/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_s3_attachment.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "frappe_s3_attachment.utils.jinja_methods",
# 	"filters": "frappe_s3_attachment.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "frappe_s3_attachment.install.before_install"
# after_install = "frappe_s3_attachment.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "frappe_s3_attachment.uninstall.before_uninstall"
# after_uninstall = "frappe_s3_attachment.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "frappe_s3_attachment.utils.before_app_install"
# after_app_install = "frappe_s3_attachment.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "frappe_s3_attachment.utils.before_app_uninstall"
# after_app_uninstall = "frappe_s3_attachment.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_s3_attachment.notifications.get_notification_config"

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
# }
# }

doc_events = {
	"File": {
		"after_insert": "frappe_s3_attachment.controller.file_upload_to_s3",
		"on_trash": "frappe_s3_attachment.controller.delete_from_cloud",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_s3_attachment.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_s3_attachment.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_s3_attachment.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_s3_attachment.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_s3_attachment.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_s3_attachment.install.before_tests"


# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_s3_attachment.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_s3_attachment.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["frappe_s3_attachment.utils.before_request"]
# after_request = ["frappe_s3_attachment.utils.after_request"]

# Job Events
# ----------
# before_job = ["frappe_s3_attachment.utils.before_job"]
# after_job = ["frappe_s3_attachment.utils.after_job"]

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
# 	"frappe_s3_attachment.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []
