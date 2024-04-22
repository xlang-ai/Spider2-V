import os
import logging
from contextlib import contextmanager
import pytest
from unittest.mock import patch, Mock
from airflow.models import DagBag

dag_bag = DagBag(dag_folder='/home/user/projects/task_today/dags')

@contextmanager
def suppress_logging(namespace):
    logger = logging.getLogger(namespace)
    old_value = logger.disabled
    logger.disabled = True
    try:
        yield
    finally:
        logger.disabled = old_value


def get_import_errors():
    """
    Generate a tuple for import errors in the dag bag
    """
    with suppress_logging("airflow"):
        dag_bag = DagBag(include_examples=False)

        def strip_path_prefix(path):
            return os.path.relpath(path, os.environ.get("AIRFLOW_HOME"))

        # prepend "(None,None)" to ensure that a test object is always created even if it's a no op.
        return [(None, None)] + [
            (strip_path_prefix(k), v.strip()) for k, v in dag_bag.import_errors.items()
        ]


def get_dags():
    """
    Generate a tuple of dag_id, <DAG objects> in the DagBag
    """
    with suppress_logging("airflow"):
        dag_bag = DagBag(include_examples=False)

    def strip_path_prefix(path):
        return os.path.relpath(path, os.environ.get("AIRFLOW_HOME"))

    return [(k, v, strip_path_prefix(v.fileloc)) for k, v in dag_bag.dags.items()]


@pytest.mark.parametrize(
    "rel_path,rv", get_import_errors(), ids=[x[0] for x in get_import_errors()]
)

def test_file_imports(rel_path, rv):
    """Test for import errors on a file"""
    if rel_path and rv:
        raise Exception(f"{rel_path} failed to import with message \n {rv}")

def test_dag_schedule_interval():
    """Verify that the DAG's schedule interval is set to daily."""
    dag = dag_bag.get_dag('activity_suggestion_dag')
    assert dag.schedule_interval == '@daily', "DAG schedule interval is not set to daily."

def test_task_workflow_order():
    """Ensure that tasks in the DAG follow the correct execution order."""
    dag = dag_bag.get_dag('activity_suggestion_dag')
    task_ids = [task.task_id for task in dag.tasks]

    expected_order = ['fetch_activity', 'log_activity', 'analyze_activity']
    assert task_ids == expected_order, f"Tasks are not in the expected order: {expected_order}"
