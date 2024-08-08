#pylint: disable=W0613,W0622
from .person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self,id: int, first_name: str, last_name: str, pet_name: str, pet_type: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

class MockPeopleRepository:
    def get_person(self, person_id: int):
        return MockPerson(
            id=1,
            first_name='John',
            last_name='Doe',
            pet_name='cao',
            pet_type='Dog'
        )


def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(1)
    
    expected_response = {
        "data": {
            "type": "person",
            "id": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "cao",
                "pet_type": "Dog"
            }
        }
    }
    
    assert response == expected_response