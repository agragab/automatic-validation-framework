import new_validate as d

d.clear_json()
d.set_m_id(0, 101)
d.set_timestamp(0, "Youm el khamees elly gy")
d.set_temperature(0, 60)
d.set_exposure(0, 20)
d.set_focus_error(0, 12)
d.run_temperature_validation()


