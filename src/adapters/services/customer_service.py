import uuid

from kink import inject

from src.domain.model.customer.customer_schemas import (
    ChangeCustomerDTO,
    CreateCustomerDTO,
)
from src.domain.model.customer.customer_model import Customer, customer_factory
from src.domain.ports.repositories.customer_repository import ICustomerRepository
from src.domain.ports.services.customer_service import CustomerServiceInterface


@inject
class CustomerService(CustomerServiceInterface):
    def __init__(self, customer_repo: ICustomerRepository) -> None:
        self._customer_repo = customer_repo

    def get_by_id(self, customer_id: uuid.UUID):
        result = self._customer_repo.get_by_id(customer_id)
        customer = customer_factory(
            result.customer_id,
            result.cpf,
            result.first_name,
            result.last_name,
            result.email,
            result.phone,
        )
        return customer

    def get_by_cpf(self, cpf: str):
        result = self._customer_repo.get_by_cpf(cpf)
        customer = customer_factory(
            result.customer_id,
            result.cpf,
            result.first_name,
            result.last_name,
            result.email,
            result.phone,
        )
        return customer

    def get_all(self):
        result = self._customer_repo.get_all()
        customers = []
        for obj in result:
            customer = customer_factory(
                obj.customer_id,
                obj.cpf,
                obj.first_name,
                obj.last_name,
                obj.email,
                obj.phone,
            )
            customers.append(customer)
        return customers

    def create(self, input_dto: CreateCustomerDTO) -> Customer:
        customer = Customer.create(
            input_dto.cpf,
            input_dto.first_name,
            input_dto.last_name,
            input_dto.email,
            input_dto.phone,
        )
        self._customer_repo.create(customer)
        return customer

    def update(self, customer_id: uuid.UUID, input_dto: ChangeCustomerDTO) -> Customer:
        customer = self._customer_repo.get_by_id(customer_id)

        if input_dto.first_name:
            customer.change_first_name(input_dto.first_name)
        if input_dto.last_name:
            customer.change_last_name(input_dto.last_name)
        if input_dto.email:
            customer.change_email(input_dto.email)
        if input_dto.phone:
            customer.change_phone(input_dto.phone)

        updated_customer = self._customer_repo.update(customer_id, customer)
        return updated_customer

    def remove(self, customer_id: uuid.UUID) -> None:
        self._customer_repo.remove(customer_id)
