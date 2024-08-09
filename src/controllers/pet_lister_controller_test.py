from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id=1, pet_name='Rex', type='dog'),
            PetsTable(id=2, pet_name='Mia', type='cat')
        ]
        

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()
        
    expected_response = {
        'data': {
            "type": "pets",
            "count": 2,
            "attributes": [
                { "name": "Rex", "id": 1 },
                { "name": "Mia", "id": 2 }
            ]
        }
    }
        
    assert response == expected_response