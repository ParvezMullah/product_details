from sqlalchemy.orm import Session, defer
from app.db.database import Base


def get_or_create(session: Session, model: Base, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance, False
    else:
        kwargs |= defaults or {}
        instance = model(**kwargs)
        try:
            session.add(instance)
            session.commit()
        except Exception:
            # The actual exception depends on the specific database
            # so we catch all exceptions. This is similar to the
            # official documentation:
            # https://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance, False
        else:
            return instance, True


def filter_helper(db: Session, model: Base, **filter_kwargs):
    # To add all the given fields in the filter.
    query = db.query(model)
    for attr, value in filter_kwargs.items():
        query = query.filter(getattr(model, attr) == value)
    query.filter(getattr(model, 'is_active') == True)
    return query


def get_filtered_objects(db: Session, model: Base, **filter_kwargs):
    # To return multiple objects.
    query = filter_helper(db, model, **filter_kwargs)
    results = query.all()
    return results


def get_filtered_object(db: Session, model: Base, **filter_kwargs):
    # To return single objects.
    query = filter_helper(db, model, **filter_kwargs)
    result = query.first()
    return result


def defer_fields(query, defer_field_names: list):
    # this wont be fetched untill accessed.
    for field_name in defer_field_names:
        query = query.options(defer(field_name))
    return query

