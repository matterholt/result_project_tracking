from ..pkg.pre_process.result_template_process import detail_column


def test_detail_column():
    detail = ["model_name","V00R00"]
    assert detail_column(detail) == "V00R00"