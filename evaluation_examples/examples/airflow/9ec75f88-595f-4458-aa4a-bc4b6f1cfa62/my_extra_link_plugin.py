from airflow.plugins_manager import AirflowPlugin
from airflow.models.baseoperator import BaseOperatorLink
from airflow.providers.http.operators.http import SimpleHttpOperator

class WTTRWeatherLink(BaseOperatorLink):
    name = "WTTRWeather"

    operators = [SimpleHttpOperator]

    def get_link(self, operator, *, ti_key=None):
        return "https://wttr.in/HongKong"

class HTTPDocsLink(BaseOperatorLink):
    name = "HTTP file"

    operators = [SimpleHttpOperator]

    def get_link(self, operator, *, ti_key=None):
        return "https://developer.mozilla.org/en-US/docs/Web/HTTP"

class AirflowExtraLinkPlugin(AirflowPlugin):
    name = "extra_link_plugin"
    operator_extra_links = [
        WTTRWeatherLink(),
        HTTPDocsLink(),
    ]

