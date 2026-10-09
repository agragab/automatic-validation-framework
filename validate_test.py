import validate

def test_validate_temperature_within_bounds():

    Readings = [{
        "m_id": "101",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "20",
        "exposure": "2",
        "focus_error": "0"
    },
    {
        "m_id": "102",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "21",
        "exposure": "2",
        "focus_error": "0"
    }
    ]

    assert validate.validate_temperature(Readings) == {
        "test": "Temperature",
        "result": False,
        "out_of_bounds": [],
        "in_bounds": ["101","102"],
        "reading": []
    }

def test_validate_temperature_outside_bounds():

    Readings = [{
        "m_id": "101",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "19",
        "exposure": "2",
        "focus_error": "0"
    },
    {
        "m_id": "102",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "18",
        "exposure": "2",
        "focus_error": "0"
    }
    ]

    assert validate.validate_temperature(Readings) == {
        "test": "Temperature",
        "result": True,
        "out_of_bounds": ["101","102"],
        "in_bounds": [],
        "reading": ["19","18"]
    }

def test_validate_exposure_within_bounds():

    Readings = [{
        "m_id": "101",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "20",
        "exposure": "2",
        "focus_error": "0"
    },
    {
        "m_id": "102",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "21",
        "exposure": "3",
        "focus_error": "0"
    }
    ]

    assert validate.validate_exposure(Readings) == {
        "test": "Exposure",
        "result": False,
        "out_of_bounds": [],
        "in_bounds": ["101","102"],
        "reading": []
    }

def test_validate_exposure_outside_bounds():

    Readings = [{
        "m_id": "101",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "20",
        "exposure": "6",
        "focus_error": "0"
    },
    {
        "m_id": "102",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "21",
        "exposure": "1",
        "focus_error": "0"
    }
    ]

    assert validate.validate_exposure(Readings) == {
        "test": "Exposure",
        "result": True,
        "out_of_bounds": ["101","102"],
        "in_bounds": [],
        "reading": ["6","1"]
    }

def test_validate_focus_within_bounds():

    Readings = [{
        "m_id": "101",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "20",
        "exposure": "2",
        "focus_error": "16"
    },
    {
        "m_id": "102",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "21",
        "exposure": "2",
        "focus_error": "52"
    }
    ]

    assert validate.validate_focus(Readings) == {
        "test": "Focus",
        "result": False,
        "out_of_bounds": [],
        "in_bounds": ["101","102"],
        "reading": []
    }

def test_validate_focus_outside_bounds():

    Readings = [{
        "m_id": "101",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "20",
        "exposure": "2",
        "focus_error": "60"
    },
    {
        "m_id": "102",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "21",
        "exposure": "2",
        "focus_error": "100"
    }
    ]

    assert validate.validate_focus(Readings) == {
        "test": "Focus",
        "result": True,
        "out_of_bounds": ["101","102"],
        "in_bounds": [],
        "reading": ["60","100"]
    }