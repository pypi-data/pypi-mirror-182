from swt.nlp.basis import base_processing, text_processing

def test_text_processing_default_setting():
    tp = text_processing()
    assert len(tp._preprocesses)  == 1
    assert len(tp._postprocesses) == 0


def test_text_processing_custom_setting():
    # no preprocesses
    tp = text_processing(preprocesses=[])
    assert len(tp._preprocesses)  == 0
    assert len(tp._postprocesses) == 0

    # stacked preprocess
    tp = text_processing(preprocesses=[lambda t: t.lower(), lambda t: t.strip()])
    assert len(tp._preprocesses)  == 2
    assert len(tp._postprocesses) == 0
