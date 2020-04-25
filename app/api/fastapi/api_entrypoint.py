from application import Application
# import of tasks to allow celery find them
app_instance = Application()

fast_api_app = app_instance.interface.app
