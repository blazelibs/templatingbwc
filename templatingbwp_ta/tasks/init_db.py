from blazeweb.tasks import attributes
from templatingbwp_ta.model.orm import Make

@attributes('base-data')
def action_30_base_data():
    pass

@attributes('+dev')
def action_40_developer_data():
    pass

@attributes('+test')
def action_40_test_data():
    pass
