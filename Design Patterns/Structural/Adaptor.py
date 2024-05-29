# Adapter method helps in making incompatible objects adaptable to each other. The main purpose is to create a bridge
# between two incompatible interfaces. Using this pattern, we can integrate the classes that could not be integrated
# due to interface incompatibility.


from abc import ABC, abstractmethod
import uuid

class StripApi:

    def create_payment(self, amount):
        print(f"Payment of {amount} is created")

    def check_status(self, payment_id):
        print(f"Payment status of {payment_id} is checked")


class PayPalApi:

    def make_payment(self, amount):
        print(f"Payment of {amount} is made")

    def get_status(self, payment_id):
        print(f"Payment status of {payment_id} is checked")


class PaymentProvider(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass

    @abstractmethod
    def get_status(self, payment_id):
        pass


class StripApiAdapter(PaymentProvider):

    def __init__(self):
        self.strip_api = StripApi()

    def make_payment(self, amount):
        self.strip_api.create_payment(amount)

    def get_status(self, payment_id):
        self.strip_api.check_status(payment_id)


class PayPalApiAdapter(PaymentProvider):

    def __init__(self):
        self.paypal_api = PayPalApi()

    def make_payment(self, amount):
        self.paypal_api.make_payment(amount)

    def get_status(self, payment_id):
        self.paypal_api.get_status(payment_id)


class PaymentProcessor:

    def __init__(self, payment_provider):
        self.payment_provider = payment_provider

    def process_payment(self, amount):
        self.payment_provider.make_payment(amount)
        return uuid.uuid4()

    def check_payment_status(self, payment_id):
        self.payment_provider.get_status(payment_id)


def get_payment_provider_from_user():
    payment_type = str(input("Enter payment type (1 for Strip, 2 for PayPal): "))
    if payment_type == '1':
        return StripApiAdapter()
    elif payment_type == '2':
        return PayPalApiAdapter()
    else:
        raise ValueError("Invalid payment type")


if __name__ == '__main__':
    payment_provider = get_payment_provider_from_user()
    payment_processor = PaymentProcessor(payment_provider)
    payment_id = payment_processor.process_payment(1999)
    print(f"Payment ID: {payment_id}")
    payment_processor.check_payment_status(payment_id)
