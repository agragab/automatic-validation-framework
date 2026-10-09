from dataclasses import dataclass

# # @dataclass
# class StructuralValidity:



@dataclass
class TestResult:
    test_result_id: int 
    temperature_test: dict
    exposure_test: dict
    focus_test: dict

    def __repr__(self):
        return f"Test Result: {self.test_result_id} \n {50*"-"} \n Temperature Test: {self.temperature_test} \n Exposure Test: {self.exposure_test} \n Focus Test: {self.exposure_test}"

