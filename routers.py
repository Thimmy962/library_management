# database_router.py

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Point all read operations for the second app to 'secondary'."""
        if model._meta.app_label == 'dashboard_analytics':
            return 'secondary'
        return 'default'

    def db_for_write(self, model, **hints):
        """Point all write operations for the second app to 'secondary'."""
        if model._meta.app_label == 'dashboard_analytics':
            return 'secondary'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations only within the same database."""
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that migrations only affect the intended database."""
        if app_label == 'dashboard_analytics':
            return db == 'secondary'
        return db == 'default'
