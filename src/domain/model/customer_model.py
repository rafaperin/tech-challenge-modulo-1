from dataclasses import dataclass


@dataclass
class Customer:
    cpf: str
    first_name: str
    last_name: str
    email: str
    phone: str

    @classmethod
    def create(cls, cpf: str, first_name: str, last_name: str, email: str, phone: str) -> "Customer":
        return cls(cpf, first_name, last_name, email, phone)

    def change_personal_data(self, new_first_name: str, new_last_name: str) -> None:
        self.first_name = new_first_name
        self.last_name = new_last_name

    def change_email(self, new_email: str) -> None:
        self.email = new_email

    def change_phone(self, new_phone: str) -> None:
        self.phone = new_phone


def customer_factory(cpf: str, first_name: str, last_name: str, email: str, phone: str) -> Customer:
    return Customer(
        cpf=cpf,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
    )
